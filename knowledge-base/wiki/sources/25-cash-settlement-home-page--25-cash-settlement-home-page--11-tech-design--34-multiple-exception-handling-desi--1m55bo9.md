---
type: source
title: Multiple Exception Handling Design
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exception-handling, NSTP, SSI, Camunda, maker-checker, design-draft]
related: [multiple-cashflow-exception-handling, partial-success-exception-resolution, exception-operation-level, cashflow-versioned-exception-orchestration, cash-settlement-exception-handling, adhoc-ssi-maker-checker-workflow, adhoc-ssi-exception-lifecycle, ratan, rule-service, lifecycle-service, ssi-stamping-service, ratanone-stamping-service, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---

# Multiple Exception Handling Design

## Summary

This design proposes handling all business exceptions for a cashflow together from the Cashflow Blotter cashflow-detail view. The scope includes SSI exceptions, pending affirmation, back-value exceptions, netting-related NSTP exceptions, and other settlement exceptions.

The proposed workflow uses Camunda to coordinate maker and checker tasks, while domain services execute individual exception-fixing actions. Exception state remains independent from cashflow state, and each action is correlated using the cashflow identity and business, cashflow, and minor versions.

The document is a detailed design draft rather than an authoritative implementation contract. Its strongest requirements are cashflow-scoped exception handling, maker/checker segregation, partial success, adhoc SSI support, payment-regeneration prevention, and version-aware orchestration. Concurrency, idempotency, transaction boundaries, endpoint normalization, and several action semantics remain unresolved.

## Operating model

- All business exceptions are displayed together in the cashflow details page.
- The maker has one overall action: `Submit`.
- The checker has two overall actions: `Approve` and `Reject`.
- Approval across multiple cashflows is not allowed.
- If some exception actions succeed and another fails, successful actions must not be repeated. The cashflow remains `WAITING / Pending_Operator`, and the next maker session shows only the unresolved exception.
- A separate requirement is needed for marking a cashflow as failed.

The proposed exception scope includes:

- SSI exceptions
- Pending affirmation
- Back-value exceptions
- NSTP exceptions

## Business rules

The source records the following proposed rules and scope constraints:

- A cashflow above USD 100 Mio may remain STP if no other exceptions exist.
- A settlement manual touch on a cashflow above USD 100 Mio creates an NSTP requirement for the ringfenced checker.
- A confirmation manual touch does not count as Settlement NSTP.
- Currency-specific mandatory requirements, such as RUB requirements, may still be STP after confirmation matching.
- An unnetted gross-client cashflow is non-STP.
- The user who performs an unnetting action must not accept the resulting exception.
- Moving netting-client cashflows from Gross to Net requires a checker exception, but this is not applicable to China Day 1 because FX deals are directly booked and settled in RAZOR.
- Missing cover flag and mandatory currency information are SI-input validations rather than separate exceptions.
- A payment must not be regenerated from a cashflow after a payment has already been sent. Manual resending is handled through AMH.
- MT199/299 recall messages should be available on an adhoc basis using predefined templates for the Nostro Agent, Beneficiary Agent, or Beneficiary.
- Auto-identification of the TPP beneficiary from Beneficiary and Counterparty information is included for China Day 1.

## Exception state model

The source proposes the following Java structures:

```java
public class CommonException {
    private String exceptionId;
    private CommonExceptionStatus commonExceptionStatus; // PENDING_OPERATOR  PENDING_VERIFICATION
}

public enum CommonExceptionStatus {
    PENDING_OPERATOR,
    PENDING_VERIFICATION,
    CLOSED
}
```

The intended lifecycle is:

```text
PENDING_OPERATOR → PENDING_VERIFICATION → CLOSED
                         ↓
                   PENDING_OPERATOR
```

A maker submission moves an exception from `PENDING_OPERATOR` to `PENDING_VERIFICATION`. A checker approval closes the exception. A checker rejection returns it to `PENDING_OPERATOR`.

The source uses several serialized variants, including `PENDING_OPERATOR`, `Pending_Operator`, `Pending Operator`, `PENDING_VERIFICATION`, and `Pending_Verification`. A canonical representation still needs to be selected.

## Generic platform exception

The proposed generic exception model is:

```java
public class PlatformException {
    private String originalExceptionId;
    private String businessFlow;
    private String sourceSystem;
    private String exceptionCode;
    private RatanExceptionType exceptionType;
    private String description;
    private List<Action> actions;
    private Map<String, String> metaData;
    private String entityId;
    private int entityVersion;
    private String entityType;
    private String trackingId;
    private Instant exceptionTime;
    private String status; //Pending Operator/Pending Verification/Closed
} 
class Action {

    private String actionName;
    private String apiUrl;
    private String apiMethod;
    private String actionType;

}
enum RatanExceptionType {
    TECHNICAL,
    BUSINESS,
    TECHNICAL_VISIBLE;
}
```

The action model allows the UI to render action-specific API details and attach an optional `requestBody`, such as SSI details, to an exception action.

## Camunda and domain-service contract

The source describes the Camunda request structure as follows:

```java
public class CamundaApiRequest<T> implements Serializable, Cloneable {
    private static final long serialVersionUID = 1L;
    private String trackingId;
    private String message;
    private Map<String, Object> metadata;
    private List<?> metadataList = Lists.newArrayList();  //This is for Exception Information
}
```

Domain services return exception statuses through `metadataList`:

```java
List<CommonException> commonExceptionList = Lists.newArrayList();
CommonException e1 = new CommonException();
e1.setExceptionId("e001");
e1.setCommonExceptionStatus(CommonExceptionStatus.PENDING_VERIFICATION);
commonExceptionList.add(e1);
response.setMetadataList(commonExceptionList);
response.setCamundaResponseCode(CamundaResponseCode.SUCCESS);
return response;
```

A representative SCBML update is:

```text
call http://localhost:8991/ratan/ssi/maker, POST   API type: POST
Request parameter: CamundaApiRequest

{
    "trackingId":"xxxx",
    "message":"<SCBML1/>",
    "metadata":{
        "cashflowId":"009381505007",
        "businessVersion":"0",
        "cashflowVersion":"0",
        "minorVersion":"4",
        "exceptionId":"xxxxxx",
        "exceptionStatus":"Pending_Verification",
        "requestBody": "{xxxxxxxxxxxxxxxx}" //Nullable
    }
}

Response: CamundaApiResposne

{
    "trackingId":"xxxx",
    "camundaResponseCode":"SUCCESS",
    "description":"xxxxxx",
    "message":"<SCBML2/>",
    "metadata":{
        "cashflowId":"009381505007",
        "businessVersion":"0",
        "cashflowVersion":"0",
        "minorVersion":"5",
        "exceptionId":"xxxxxx",
        "exceptionStatus":"CLOSED"
    }
}
```

The source alternates between `CamundaApiRequest`, `CamundaApiResponse`, and the misspelled `CamundaApiRespose`. The exact canonical class and response contract require confirmation.

## Maker and checker task API

The proposed endpoints are:

```text
maker api url   : /v1/camunda/task/{buisnessType}/maker

checker api url : /v1/camunda/task/{businessType}/checker

businessType: nstpssi
```

The request body is:

```json
{
    "cashflowId": "009381505007",
    "businessVersion": "0",
    "cashflowVersion": "0",
    "minorVersion": "3",
    "action": "Submit",
    "exceptions": [
        {
            "id": "ratan-10007",
            "exceptionCode": "exception-code-001",
            "sourceSystem": "SSI Service",
            "exceptionType": "BUSINESS",
            "exceptionCategory": "MissingVostro",
            "businessFlow": "SETTLEMENT",
            "description": "Missing Vostro",
            "actions": [
                {
                    "actionName": "Submit",
                    "actionType": "Rest",
                    "apiUrl": "http://localhost:8991/ratan/camunda/cashflow/ssi/maker",
                    "apiMethod": "POST",
                    "requestBody": "{BIC:xxx}"
                }
            ],
            "metaData": null,
            "entityId": "000012345678",
            "entityVersion": "0-0-2",
            "entityType": "Cashflow",
            "trackingId": "000012345678-001",
            "status": "Pending Operator"
        },
        {
            "id": "ratan-10007",
            "exceptionCode": "exception-code-001",
            "sourceSystem": "SSI Service",
            "exceptionType": "BUSINESS",
            "exceptionCategory": "MissingVostro",
            "businessFlow": "SETTLEMENT",
            "description": "Missing Vostro",
            "actions": [
                {
                    "actionName": "Submit",
                    "actionType": "Rest",
                    "apiUrl": "http://localhost:8991/ratan/camunda/cashflow/service2",
                    "apiMethod": "POST"
                }
            ],
            "metaData": null,
            "entityId": "000012345678",
            "entityVersion": "0-0-2",
            "entityType": "Cashflow",
            "trackingId": "000012345678-001",
            "status": "Pending Operator"
        }
    ]
}
```

The documented response outcomes are:

| HTTP code | Message | Reason |
|---|---|---|
| 200 | `Success` | Task completed successfully |
| 500 | `Maker/Checker task can not be found` | Task completed, or no matching `cashflowId` and version exists |
| 500 | `Maker/Checker task still uncompleted` | Exceptions remain unresolved |
| 500 | `Fix exception failed during executing following api: xxxxx` | An exception-fixing API failed |

Using HTTP 500 for business-state outcomes is provisional and should be reviewed against structured application error codes and possible `409 Conflict` semantics.

## Adhoc SSI

When stamping is good, the SSI service may create a closed dummy exception with:

- Exception code: `Adhoc SSI`
- Exception category: `SSI`
- Status: `Closed`
- Maker action: `Submit`
- Checker action: `Reject`

The dummy exception is proposed when there is no SSI exception or only a secondary SSI or not-match exception. It allows the UI to expose SSI editing from a cashflow that would otherwise have no active SSI exception.

The proposed transitions are:

```text
CLOSED
  -- maker Submit --> PENDING_VERIFICATION
  -- checker Reject --> PENDING_OPERATOR
  -- checker Approve --> CLOSED
```

The UI should enable SSI editing when the dummy exception exists and the cashflow is either:

- `WAITING / Pending_Operator`, or
- `READY`

The source contains inconsistent action tables for the closed dummy exception, particularly around the checker `Reject` action and whether `Submit` or `Approve` is exposed at each stage. These semantics are provisional.

## Example cashflow progression

The principal happy-path example progresses through these versions:

| Cashflow version | Status | Sub-status | Comment |
|---:|---|---|---|
| 2 | `WAITING` | `Pending_Operator` | Initial exception state |
| 3 | `WAITING` | `Pending_Verification` | Maker fixes completed |
| 4 | `WAITING` | `Pending_Verification` | SSI stamped |
| 5 | `WAITING` | `Pending_Verification` | Payment date updated |
| 6 | `WAITING` | `Pending_Verification` | Manual affirmation |
| 7 | `READY` | `NA` | All exceptions closed |
| 8 | `RELEASED` | `NA` | Payment released |
| 9 | `SETTLED` | `NA` | Settlement completed |

Exception statuses and cashflow status are therefore related but not identical. The source does not formalize the derivation rule for cashflow-level status when individual exception actions close at different versions.

## Rule Service

The proposed rule attributes are:

```text
ruleType
businessFlow
rule
reason
exceptionCode
exceptionCategory
operationLevel
```

Operation-level values are:

| Value | Meaning |
|---:|---|
| 1 | Checker only |
| 2 | Maker/checker |
| 3 | Maker only |

Rule statuses include:

```text
ADD_PENDING
ADD_CONFIRMED
ADD_CANCELLED
DEL_PENDING
DEL_CONFIRMED
```

The source lists APIs for rule creation, confirmation, cancellation, deletion, history queries, rule-type queries, special NSTP rules, suppression rules, NSTP checks, and exception submit/approve/reject operations. Several copied URLs contain malformed or duplicated path fragments and should not be treated as canonical endpoint definitions.

## Database structures

No complete DDL is supplied. The source provides the following column-level structures.

### `exception`

| Column | Type | Nullable | Sample | Unique |
|---|---|---|---|---|
| `exception_id` | `Text` | Mandatory | `1` | Yes |
| `cashflow__cashflow_id` | `Text` | Mandatory | `003690235910` | |
| `cashflow__cashflow_business_version` | `Text` | Mandatory | `0` | |
| `cashflow__cashflow_version` | `Text` | Mandatory | `0` | |
| `cashflow__cashflow_minor_version` | `Text` | Nullable | `2` | |
| `status` | `Text` | Mandatory | `Pending_Operator Pending_Verification` | |
| `reason` | `Jsonb` | Nullable | | |
| `ratan_label` | `Text` | Nullable | | |
| `created_at` | `Timestamp` | Mandatory | | |
| `updated_at` | `Timestamp` | Mandatory | | |

### `rules`

| Column | Type | Nullable | Sample |
|---|---|---|---|
| `...` | | | |
| `exception_code` | `Text` | Mandatory | `Unaffirmed Cashflow` |
| `operation_level` | `Number` | Mandatory | `1(Checker only) 2 (M/C) 3 (Maker only)` |

The source does not specify complete primary-key, foreign-key, index, or composite uniqueness definitions beyond the uniqueness note for `exception_id`.

## Migration assessment

The source gives planning estimates, not delivery commitments:

| Service | Proposed change points | Estimation |
|---|---|---:|
| Strategic Query Service Exception platform | GraphQL exception-list query and data entitlement for EG, BCS, and CN | 4 |
| Strategic SSI Stamping Service | Differentiate BCS and CN cashflows, close exceptions on stamping, and migrate trade stamping | 16 |
| Cashflow Service | Status machine, FMCODE stamping, exception closure on new versions, and impacted-cashflow status query | 16 |
| BAU Exception Blotter | Strategic Query Service client-data query, CN SSI form inheritance, and possible future exception queries | 8 |
| BAU Camunda | Exception closure, FMCODE stamping, query-failure interface exception, and exception-publishing changes | 8 |
| Test and bug fix | Testing and defect correction | 8 |

## Open questions and limitations

The source leaves unresolved:

- Whether exception actions execute sequentially or in parallel.
- How partial commits, retries, idempotency, and downstream timeouts are handled.
- How stale cashflow versions are rejected.
- Which service owns the authoritative cashflow status transition.
- Whether a checker can reject one exception or must reject the entire maker submission.
- What a checker `Reject` means for a closed `Adhoc SSI` dummy exception.
- How exception counts include already-closed exceptions.
- What authorization and entitlement rules apply to EG, BCS, and CN.
- Whether marking a cashflow as failed belongs in this workflow.
- How the incomplete process-flow and transaction sections should be implemented.

This draft should be reconciled with [[queries/what-is-the-canonical-cash-settlement-exception-state-machine]], [[concepts/adhoc-ssi-maker-checker-workflow]], and [[concepts/cash-settlement-exception-handling]] before being used as an implementation authority.
---
type: source
title: Source: Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [cash-settlement, ratan, suspended-status, rule-service, camunda, fx-replication]
related: [ratan-suspended-cashflow-rule-filtering, fail-open-rule-service-evaluation, rule-semantic-compilation-risk, ratan-rule-service, camunda, ratan-cashflow-lifecycle-service, ratanone-settlement-orchestration-service, how-is-ratan-suspended-rule-conjunction-evaluated, what-is-the-ratan-suspended-rule-service-api-contract, how-are-fail-open-suspended-cashflows-reconciled]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# SUSPENDED RULE FILTER in Ratan Tech Design

This design makes handling of inbound cashflows with source status `SUSPENDED` configurable through Ratan Rule Service. It applies to messages from SCBML and Uber.

The implemented option places the check in the Camunda workflow, in `1_1_Cash_Settlement_Inbound.bpmn`, after group-message processing. A matching cashflow is persisted as suspended, stops downstream processing, emits no `GroupReadyEvent`, and produces no STP publication. A non-match continues through the normal path.

## Implemented scope

| Component | Change |
|---|---|
| `ratan-cash-settlement-orchestration` | Add an FX-replication rule-check module and a `RATAN_SUSPENDED` status-update module to the BPMN workflow. |
| lifecycle-service | Add `Ratan_Suspend`, `RATAN_SUSPENDED`, and withdrawal-to-cancellation handling. |
| `ratan-rule-service` | Add a suspension-rule REST endpoint. |
| Rule-engine database | Insert one LIVE `RATAN_SUSPENDED` rule. |

The alternative group-service-layer design was not selected. It would have checked before `savePending()` or offset persistence, reducing processing overhead but placing a remote call inside transaction-sensitive inbound handlers.

## Rule-service endpoint

```text
POST /v1/ratanSuspendedRule/check
```

The source does not specify request and response schemas, authentication, retry behavior, timeout values, response codes, or the criterion by which `matchedRules` represents an overall rule match.

## Lifecycle extension

```java
// ValidationRequestV2.java
public enum RuleType {
    TRADE_VALIDATION,
    RATAN_SUSPENDED
}
```

```java
@Configuration
public class RatanSuspendedTransactionList extends CashflowStatusTransactionList {
    @Override
    public void initCashflowStatusTransactionList() {
        this.setCashflowStatusTransaction(new ArrayList<>(Arrays.asList(
            CashflowStatusTransaction.builder()
                .previousStatus(CashflowStatus.RatanSuspended)
                .action(CashflowEnumAction.Withdrawal)
                .allowBusinessVersionUpgrade(true)
                .nextStatus(CashflowStatus.Cancelled)
                .build()
        )));
    }
}
```

The design also specifies:

```java
CashflowEnumAction.Ratan_Suspend
CashflowEnumMainStatus.RATAN_SUSPENDED
public static CashflowStatus RatanSuspended =
    new CashflowStatus(
        CashflowEnumMainStatus.RATAN_SUSPENDED,
        CashflowEnumSubStatus.NA,
        CashflowEnumSubStatusType.NA);
```

Only the `RATAN_SUSPENDED` to `Cancelled` transition through `Withdrawal` is shown. Entry, reinstatement, amendment, replay, and post-rule-change re-evaluation semantics are not defined.

## LIVE FX replication rule

The migration creates rule `7444684846945615873333` in `ratanone_rule_service.ratan_rule_engine`.

```sql
INSERT INTO ratanone_rule_service.ratan_rule_engine
(id, business_flow, rule_type, user_rule, running_rule, status, reason, "comment", need_dry_run, reference_rule_id, created_at, updated_at, created_by, updated_by, "version", meta_data)
VALUES(
'7444684846945615873333',
'STRATEGIC_SETTLEMENT',
'RATAN_SUSPENDED',
'Data_Flow__Source_Stack_Flow_Name == "FMRPSTELLA"
&& Entity__Booking_Entity_SCI_FMID != §Entity__Counterparty_SCI_FMID
&& Instrument_Common__ISDA_Taxonomy in ("ForeignExchange:Spot", "ForeignExchange:Forward", "ForeignExchange:Swap")
&& Is_Duplicate_Booking != true
&& (Cashflow__Payment_Type == null || !(Cashflow__Payment_Type matches "(?i).*fee.*"))',
'See source document for the complete generated Drools running_rule, containing rule IDs 7444684846945615873333-0 through 7444684846945615873333-14.',
'LIVE',
'FX Replication Rule for Global Rates',
'',
false,
'7444553081115459584',
'2026-03-31 09:59:43.067',
'2026-03-31 10:00:45.936',
'1376592',
'1376592',
2,
'{"autoClose":true}'
);
```

The full rule additionally contains counterparty and booking-entity FMID exclusions, booking-entity-specific exceptions, contract-typology and parent-position conditions, and a defined counterparty FMID allowlist. It targets `FMRPSTELLA` FX Spot, Forward, and Swap cashflows while excluding duplicate bookings and fee payment types.

> [!WARNING]
> The `user_rule` is a conjunction, but the generated Drools `running_rule` records each clause as an independent rule in `matchedRuleSet`. The endpoint's aggregation semantics must be confirmed before relying on the filter. See [[how-is-ratan-suspended-rule-conjunction-evaluated]].

The `§` character in `Entity__Booking_Entity_SCI_FMID != §Entity__Counterparty_SCI_FMID` should also be validated against the persisted rule and parser syntax.

## Failure handling

Rule-service timeout, unavailability, and unexpected errors are explicitly fail-open: the caller logs the condition, returns `false`, and continues normal processing. An empty `matchedRules` result is also treated as not suspended.

This is an availability-over-strict-filtering policy. Eligible cashflows can therefore proceed to downstream handling during a rule-service failure unless a separate reconciliation control exists.

## Verification reported

The source reports screenshot-based PASS results for:

- A cashflow that matches the suspension rule and is filtered as `RATAN_SUSPENDED`.
- A cashflow that does not match and is processed normally.

It does not demonstrate SCBML and Uber independently, persistence values, suppression of `GroupReadyEvent`, suppression of all STP outputs, error-path behavior, lifecycle cancellation, or retry and duplicate-delivery behavior.
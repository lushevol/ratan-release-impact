---
type: source
title: Cash Settlement Lifecycle Status Machine
authors: []
year: 2023
url: ""
venue: Internal functional requirements
tags: [cash-settlement, ratan, lifecycle, state-machine, functional-requirements]
related: [ratan-cashflow-lifecycle-state-machine, cashflow-lifecycle-versioning, ratan-external-and-internal-lifecycle-requests, fmo, what-is-the-authoritative-ratan-lifecycle-transition-matrix, what-is-the-canonical-unhold-and-suppression-reject-behavior, what-are-the-canonical-ratan-lifecycle-enum-values]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# Cash Settlement Lifecycle Status Machine

This internal functional-requirements document specifies the intended RATAN cashflow lifecycle, including transition rules, lifecycle request versioning, API interfaces, and event payloads. It is design evidence, not confirmation that each transition or endpoint is implemented, deployed, or currently supported.

The specification positions [[ratan]] as the lifecycle-management component for cashflows received from [[murex-2-11]], [[razor]], [[stella]], and TDS3/TDSS3. RATAN is intended to write lifecycle status back to STELLA/TDS3 and to receive settlement acknowledgements from [[amh]] or [[scpay]].

## Lifecycle statuses

| Status | Source-defined purpose |
| --- | --- |
| `PROJECTED` | Initialized and published after upstream new, amendment, cancellation, or trade-related events. |
| `QUEUED` | Temporary processing status, normally entered through scheduled VD-5 materialization. |
| `WAITING` | Workflow or user-operation state pending netting, another leg, exceptions, suppression approval, reversal/rebook, or review. |
| `HOLD` | Manual prevention of automatic STP. |
| `READY` | Eligible for STP at the release cutoff. |
| `CANCELLED` | Cancelled before downstream release. |
| `RELEASED` | Published to FMSGW for SWIFT or to Razor in the legacy flow. |
| `SETTLED` | Acknowledged by AMH/SCPAY or settled directly. |
| `NOSTRO_MATCHED` | TLM reconciliation result; explicitly described as out of scope at the time of writing. |
| `CASHFLOW_SUPPRESSED` | Ineligible for settlement and accounting. |
| `SWIFT_SUPPRESSED` | Eligible for accounting but excluded from SWIFT generation. |
| `NETTED` | Component cashflow after scheduled or manual netting. |
| `DEAD` | Resultant cashflow after un-netting or certain upstream amendments/cancellations. |
| `FAILED` | Not valid for settlement but potentially eligible for reinstatement and accounting. |
| `UTILIZED` | Fully utilized with zero remaining amount. |
| `PARTIALLY_UTILIZED` | Partially utilized with nonzero remaining amount. |
| `PASTDUE` | Not utilized by VD end of day. |
| `SPLIT` | Parent cashflow after manual or automatic splitting. |
| `ERROR` | Used for withdrawal attempts on utilized cashflows. |

The lifecycle state index consists of a main status, a sub-status, and a sub-status type. In particular, `WAITING` represents a family of workflows rather than a single uniform condition. See [[ratan-cashflow-lifecycle-state-machine]].

## Selected transition records

| Source status | Source sub-status | Source sub-status type | Action | Target status | Target sub-status | Target sub-status type |
| --- | --- | --- | --- | --- | --- | --- |
| `NA` | `NA` | `NA` | `New` | `PROJECTED` | `NA` | `NA` |
| `PROJECTED` | `NA` | `NA` | `Materialize` | `QUEUED` | `NA` | `NA` |
| `PROJECTED` | `NA` | `NA` | `Withdrawal` | `CANCELLED` | `NA` | `NA` |
| `QUEUED` | `NA` | `NA` | `IsNettingEligible` | `WAITING` | `Pending Operator` | `Pending Netting` |
| `QUEUED` | `NA` | `NA` | `WaitingAnotherLeg` | `WAITING` | `NA` | `Pending Another Leg` |
| `QUEUED` | `NA` | `NA` | `IsNstpChecker` | `WAITING` | `Pending Verification` | `Pending Exception` |
| `QUEUED` | `NA` | `NA` | `ValidateDirect` | `READY` | `NA` | `NA` |
| `QUEUED` | `NA` | `NA` | `SwiftSuppress` | `SWIFT_SUPPRESSED` | `NA` | `NA` |
| `QUEUED` | `NA` | `NA` | `Suppress` | `CASHFLOW_SUPPRESSED` | `NA` | `NA` |
| `WAITING` | `Pending Verification` | `Pending Exception` | `Approve` | `READY` | `NA` | `NA` |
| `WAITING` | `Pending Verification` | `Cashflow Suppression` | `Approve` | `CASHFLOW_SUPPRESSED` | `NA` | `NA` |
| `WAITING` | `Pending Verification` | `Undo Cashflow Suppression` | `Approve` | `QUEUED` | `NA` | `NA` |
| `WAITING` | `Pending Verification` | `Swift Suppression` | `Approve` | `SWIFT_SUPPRESSED` | `NA` | `NA` |
| `WAITING` | `Pending Verification` | `Undo Swift Suppression` | `Approve` | `QUEUED` | `NA` | `NA` |
| `READY` | `NA` | `NA` | `Release` | `RELEASED` | `NA` | `NA` |
| `READY` | `NA` | `NA` | `SettleDirect` | `SETTLED` | `NA` | `NA` |
| `RELEASED` | `NA` | `NA` | `Settle` | `SETTLED` | `NA` | `NA` |
| `SETTLED` | `NA` | `NA` | `NostroMatch` | `NOSTRO_MATCHED` | `NA` | `NA` |
| `FAILED` | `NA` | `NA` | `ReInstate` | `QUEUED` | `NA` | `NA` |
| `NETTED` | `NA` | `NA` | `UnNet` | `QUEUED` | `NA` | `NA` |
| `SPLIT` | `NA` | `NA` | `UnSplit` | `QUEUED` | `NA` | `NA` |
| `QUEUED` | `ALL` | `ALL` | `UnSplit` | `DEAD` | `NA` | `NA` |
| `WAITING` | `ALL` | `ALL` | `UnSplit` | `DEAD` | `NA` | `NA` |

## Versioning and requests

The document defines three lifecycle versions:

1. **Business Version** changes when a trade action affects a cashflow, including booking, amendment, and cancellation.
2. **Cashflow Version** changes when Business Version changes or when STELLA changes the cashflow status.
3. **Minor Version** increments for every lifecycle action, including upstream events and RATAN STP or manual actions.

External requests from STELLA or Murex are intended for STP only. They are admitted for `PROJECTED` cashflows on `New`, `Amendment`, and `Withdrawal`; and for `RELEASED`, `SETTLED`, and `NETTED` cashflows on `Withdrawal` or `Withdrawal & New`. They carry cashflow ID, Business Version, Cashflow Version, and action.

Internal RATAN requests cover STP and manual actions such as stamping. They do not change Business Version or Cashflow Version and carry cashflow ID, Minor Version, and action. See [[cashflow-lifecycle-versioning]] and [[ratan-external-and-internal-lifecycle-requests]].

## API interfaces

The source documents these lifecycle routes. Internal hosts, Basic-auth credentials, and dated environment details have been intentionally omitted because they are sensitive and may be obsolete.

```text
POST /api/v1/ratan/lifecycle/update/status
POST /api/v1/ratan/lifecycle/update/status/batch/transactional
POST /api/v1/ratan/lifecycle/update/status/batch
POST /api/v1/ratan/cashflow/query
POST /api/v1/ratan/cashflow/auto/materialization
POST /api/v1/ratan/cashflow/user/status/update
POST /api/v1/ratan/lifecycle/hold
POST /api/v1/ratan/lifecycle/unhold
POST /v1/camunda/task/fail
POST /v1/camunda/task/reinstate
POST /v1/ratan/lifecycle/suppress/maker
POST /v1/ratan/lifecycle/suppress/checker

LifecycleService.statusUpdate
```

The documented lifecycle request structure is:

```json
{
  "cashflowId": "002690235964",
  "businessVersion": "0",
  "cashflowVersion": "0",
  "minorVersion": "0",
  "ratanAction": "New",
  "updater": "System",
  "nstpReason": "",
  "bodyEventRowKey": "",
  "valueDate": "",
  "eventType": "New",
  "message": "SCBML",
  "swiftPaymentDate": "2023-02-28",
  "comment": "Affirmed by somebody",
  "affirmationDetails": {
    "affirmedBy": "Geoffrey",
    "phone_email": "geoffrey@[sc.com](http://sc.com)"
  }
}
```

The documented status response structure is:

```json
{
  "cashflowId": "002690235964",
  "businessVersion": "0",
  "cashflowVersion": "0",
  "action": "Materialize",
  "updater": "1481696",
  "previousCashflowIndex": {
    "minorVersion": "0",
    "cashflowStatus": {
      "cashflowEnumMainStatus": "PROJECTED",
      "cashflowEnumSubStatus": "NA",
      "cashflowEnumSubStatusType": "NA"
    }
  },
  "nextCashflowIndex": {
    "minorVersion": "1",
    "cashflowStatus": {
      "cashflowEnumMainStatus": "QUEUED",
      "cashflowEnumSubStatus": "NA",
      "cashflowEnumSubStatusType": "NA"
    }
  },
  "cashflowStatusResponseCode": "SUCCESS",
  "reason": null
}
```

## Lifecycle events

```json
{
  "messageId": "7ba714be17e84277ab4bcec9819a8d53",
  "aggregateId": "003690235969",
  "aggregateType": "Cashflow",
  "type": "CashflowCreationEvent",
  "payload": {
    "cashflow": {
      "cashflowId": "003690235969",
      "cashflowBusinessVersion": "0",
      "cashflowVersion": "0",
      "cashflowMinorVersion": "0",
      "cashflowStatus": "PROJECTED",
      "cashflowSubStatus": "NA",
      "cashflowSubStatusType": "NA",
      "cashflowSubStatusUpdater": "STELLA",
      "cashflowRowData": "<SCBML>message</SCBML>"
    }
  },
  "version": 71203,
  "revision": 2,
  "timestamp": 1667285771640,
  "metadata": {
    "traceId": "c-74c9c36cf4f3439ba27f8571b4d168cb"
  },
  "status": "PUBLISHED"
}
```

```json
{
  "messageId": "db04fabc25d54dc1bdb2ac814d2fd7f3",
  "aggregateId": "003690235969",
  "aggregateType": "Cashflow",
  "type": "CashflowStatusUpdateEvent",
  "payload": {
    "cashflow": {
      "cashflowId": "003690235969",
      "cashflowBusinessVersion": "0",
      "cashflowVersion": "0",
      "cashflowMinorVersion": "1",
      "cashflowStatus": "QUEUED",
      "cashflowSubStatus": "NA",
      "cashflowSubStatusType": "NA",
      "cashflowSubStatusUpdater": "1481696"
    }
  },
  "version": 71204,
  "revision": 3,
  "timestamp": 1667285931167,
  "metadata": {
    "traceId": "ab64121631183f77"
  },
  "status": "PUBLISHED"
}
```

## Caveats

Several transition rows are incomplete or inconsistent. `UnHold` from `HOLD / Pending Verification` has no target status. Four maker/checker suppression rejection rows also specify `NA` as every target-state field. The matrix contains the malformed label `Pending Netting 4 Withdrawal`, uses inconsistent forms such as `PARTIALLY-UTILIZED` and `PARTIALLY_UTILIZED`, and refers to both TDS3 and TDSS3.

`NOSTRO_MATCHED` has transition rows but is described as out of scope. Struck-through `SPLIT` transitions should not be treated as active behavior without a later approved source. These issues are tracked in [[what-is-the-authoritative-ratan-lifecycle-transition-matrix]], [[what-is-the-canonical-unhold-and-suppression-reject-behavior]], and [[what-are-the-canonical-ratan-lifecycle-enum-values]].
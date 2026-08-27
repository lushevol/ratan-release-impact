---
type: source
title: Settlement Method Update
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, FX, RATAN, settlement-method, cashflow-blotter]
related: [ratan, cashflow-blotter, settlement-method-update, util-to-gross-settlement-update, gross-to-util-settlement-update, trade-level-cashflow-selection-expansion, cashflow-status-lifecycle, reversal-and-correction-cashflow-processing, accounting-feed-reconciliation, trade-cashflow-reference-linkage, what-is-the-authoritative-settlement-method-update-contract, what-is-the-authoritative-ratan-utilization-static-data-and-fmid-eligibility-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# Settlement Method Update

## Summary

This functional requirement describes a user-triggered **Settlement Method Update** action in the [[cashflow-blotter]]. The action changes eligible FX cashflows between `UTIL` and `GROSS` settlement, reinstates them for the target settlement path, and applies direction-specific amount, status, accounting, and settlement-means rules.

[[ratan]] is the backend platform involved in settlement-method stamping, utilization eligibility checks, and processing. The requirement distinguishes cashflow-level execution from trade-level selection expansion and success/failure reporting.

## UTIL-to-Gross behavior

An eligible cashflow has:

```text
Settlement method = 'UTIL'
cashflow status IN (WAITING, READY, PASTDUE)
```

The action:

1. Sets the settlement method to Gross.
2. Reinstates the cashflow for Gross settlement.
3. Sets the remaining amount to `0`.
4. Removes the `PASTDUE` cashflow sub-status.
5. For a `PASTDUE` cashflow, post-settles as Gross, generates a reversed accounting entry, and sends that entry out.
6. Operates at cashflow level.
7. Requires no special NSTP rule for this scenario.

The reversed accounting behavior is limited to the `PASTDUE` UTIL-to-Gross case described here.

## Gross-to-UTIL behavior

The stated eligibility condition is:

```text
Settlement method IN ('GROSS', "")
cashflow status IN (WAITING, READY + NA + NA)
data_source_system != Ratan
ISDA_Taxonomy IN (
  'ForeignExchange:Forward',
  'ForeignExchange:Spot',
  'ForeignExchange:Swap'
)
event reason != 'reversal'
```

The action:

1. Sets the settlement method to UTIL.
2. Reinstates the cashflow for Util settlement.
3. Updates the payment amount to the remaining amount.
4. Post-settles as Util.
5. Stamps settlement means according to client static-data setup.

The source does not define the meaning of `READY + NA + NA`, the semantics of a blank settlement method, or behavior when the required static data is missing.

## Settlement-method stamping

For settlement-method stamping, the source requires the ISDA taxonomy to be one of:

```text
'ForeignExchange:Forward'
'ForeignExchange:Spot'
'ForeignExchange:Swap'
```

The backend then checks utilization static data for eligible entities identified by FMID. The requirement does not specify the static-data schema, lookup precedence, eligible-entity values, or fallback behavior.

## Cashflow Blotter interaction

When a user selects only one cashflow in the [[cashflow-blotter]], the system automatically displays or selects all cashflows under the same trade.

Additional UI behavior includes:

- Ordering results by trade ID.
- Filtering out cashflows with status `+ERROR`.
- Limiting bulk update to 100 trades/cashflows.
- Warning when the selected cashflow count differs from the frontend feedback cashflow count.
- Warning that all cashflows under trades such as `T01` and `T02` were automatically selected.

The source states that success and failure responses are reported at trade level, but it does not define partial-failure, atomicity, retry, idempotency, or per-cashflow diagnostic behavior.

## Structured requirement data

### UTIL-to-Gross rule

| Field | Requirement |
|---|---|
| Input settlement method | `UTIL` |
| Eligible cashflow statuses | `WAITING`, `READY`, `PASTDUE` |
| Target settlement method | Gross |
| Reinstatement | Required |
| Remaining amount | Set to `0` |
| `PASTDUE` sub-status | Removed |
| PASTDUE accounting | Reversed accounting entry generated and sent |
| Processing level | Cashflow |
| Special NSTP rule | Not required |

### Gross-to-UTIL rule

| Field | Requirement |
|---|---|
| Input settlement method | `GROSS` or blank (`""`) |
| Eligible cashflow status | `WAITING, READY + NA + NA` |
| Data source system | Must not equal `Ratan` |
| ISDA Taxonomy | `ForeignExchange:Forward`, `ForeignExchange:Spot`, or `ForeignExchange:Swap` |
| Event reason | Must not equal `reversal` |
| Target settlement method | `UTIL` |
| Reinstatement | Required |
| Payment amount | Set to remaining amount |
| Settlement processing | Post-settle as Util |
| Settlement means | Stamped from client static data |

### UI and bulk behavior

| Field | Requirement |
|---|---|
| Selection expansion | Selecting one cashflow automatically selects/displays all cashflows under the same trade |
| Ordering | By trade ID |
| Filtering | Filter out cashflows with status `+ERROR` |
| Bulk limit | 100 trades/cashflows |
| Count warning | Warn when selected count differs from frontend feedback count |
| Success/failure response | Trade level |

## Evidence limitations

The document specifies intended behavior but does not provide a version, owner, acceptance criteria, API contract, data model, error codes, or detailed processing semantics. The open issues are tracked in [[what-is-the-authoritative-settlement-method-update-contract]] and [[what-is-the-authoritative-ratan-utilization-static-data-and-fmid-eligibility-rule]].
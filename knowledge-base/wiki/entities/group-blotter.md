---
type: entity
title: Group Blotter
created: 2026-08-23
updated: 2026-08-23
tags: ["cash-settlement", "user-interface", "group-blotter", "operations", "operational-ui", "manual-stp", "trade", "cashflow", "application-interface", "exception-monitoring", "grouped-cashflows"]
related: ["bulk-manual-stp-group-blotter", "group-blotter-cashflow-state-lifecycle", "settlement-ops", "cashflow-migration", "cash-settlement-home-page", "ratan", "bulk-manual-stp-for-group-blotter", "group-major-version-completion-rules", "group-blotter-eco-fields", "cashflow-record", "trade-record", "grouped-cashflow-monitoring", "group-pending-monitoring", "group-pending-validation-monitoring", "cashflow-blotter-functional-scope"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Grouping Blotter Monitoring.md"]
---
# Group Blotter

## Role and operational context

The Group Blotter is an operational interface in the [[cash-settlement-home-page]] domain. The Grouping Blotter Monitoring source describes it as an operational worklist opened from non-zero **Group Pending** or **Group Pending Validation** counters on the [[cash-settlement-home-page]].

It presents grouped cashflows for investigation and supports status-based filtering and manual recovery actions. The bulk manual STP requirement describes the Group Blotter as the entry point from which Operations selects cashflow messages and invokes bulk manual delivery for both single-group and multi-group manual STP.

The bulk manual STP test matrix describes the Group Blotter as the grouped operational selection context. It presents group-major-version records and their underlying cashflows as selectable items, including both broad selection of a group version and targeted selection of individual pending cashflows.

## Monitoring and investigation behavior

According to the Grouping Blotter Monitoring source, the Group Blotter:

- Opens with `Status = PENDING` for Group Pending monitoring.
- Opens with cashflows in `Pending Trade Validation` for Group Pending Validation monitoring.
- Allows users to retrieve underlying payments using the original trade ID.
- Exposes the `Pending Reason`, including a missing payment ID where applicable.
- Supports manual pushing of cashflows to the Cashflow Blotter when a Murex and RATAN trade-ID mismatch prevents automatic synchronization.

## Bulk manual delivery

For a bulk manual-delivery request, the Group Blotter supplies selected cashflows to the processing flow.

For multi-group selections, the bulk manual STP sources specify that cashflows are:

1. Grouped by trade for precheck.
2. Ordered by `trade_group_majorVersion`.
3. Processed through the original group-message logic.

Successful processing is expected to route cashflows to the Cashflow Blotter and record `bookingSystemEvent='ManualDeliver'`.

## 2026 eco-fields scope

The 2026 Group Blotter requirements identify twelve fields split between cashflow and trade records. The complete inventory is documented in [[group-blotter-eco-fields]].

### Cashflow record

| Logical model field | Source comment |
| --- | --- |
| `Entity.Booking_Entity_SCI_FMID` | |
| `Entity.Counterparty_SCI_FMID` | |
| `Cashflow.Pay_Receive_Indicator` | |
| `Cashflow.Payment_Amount` | |
| `Cashflow.Payment_Currency` | |
| `Cashflow.Payment_Date` | |
| `Settlement_Method` | SCBML and Uber release-specific sourcing |
| `Portfolio.Booking_Entity_Trade_Portfolio_Name` | To be released with RFI |

### Trade record

| Field | Classification |
| --- | --- |
| `LIEN_Monitoring` | Eco field |
| `Contract_Typology` | Special field |
| `Linked_Package_Id` | Special field |
| `Swap_Agent_Id` | Special field |

## Release caveats

For `Settlement_Method`, the 2026 source states that:

- The SCBML version takes the value from the production `Cashflow Record`.
- The Uber version takes the value from the `Cashflow Record` in the TB release.

See [[scbml]] for the specific SCBML relationship.

`Portfolio.Booking_Entity_Trade_Portfolio_Name` is marked as to be released with RFI. The source does not confirm whether that release occurred.

## Operational boundary and not established

The Grouping Blotter Monitoring source characterizes the Group Blotter as an investigation and recovery interface. It does not, by itself, define the authoritative grouping key, status derivation rules, validation contract, or controls for manual-action approval.

The 2026 field inventory does not establish whether the listed fields are displayed, filterable, sortable, searchable, mandatory, or used for Group Blotter processing. It also does not define trade-to-cashflow join keys, data types, permissible values, ownership, or validation criteria.

The fields should not be treated as STP, netting, lien, or swap-agent workflow rules without additional evidence.

The bulk manual STP requirement does not identify the underlying application platform. Its behavior should therefore be treated as specific to that Group Blotter requirement and not generalized to all settlement interfaces.

The bulk manual STP test-matrix source does not define the Group Blotter's implementation, user permissions, or system of record. It also does not establish that the Group Blotter is explicitly part of [[ratan]]; the RATAN association is limited to surrounding business context.
---
type: source
title: OPS Allowed Actions Post Pending Release
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, RATAN, operations, duplicate-payment, release-control, netting]
related: [ratan, fmo-settlements, cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, cash-settlement-release-cutoff-controls, is-ratan-release-status-validation-atomic-with-downstream-dispatch, what-idempotency-controls-protect-ratan-ready-state-retries, were-ratan-release-time-controls-deployed-and-validated-by-their-2026-dates]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release"
venue: "Internal technical design"
---
# OPS Allowed Actions Post Pending Release

## Incident summary

On 13 Jan 2026, RATAN processed both a CNH 1,989,276,383 gross payment (equivalent USD 285m) and a CNH 95,857,685 net payment (equivalent USD 13m) for a Forward Precious Metal trade. The client had requested ad-hoc net settlement, which FMO Settlements had agreed.

The source attributes the event to a short concurrent-processing window: automatic currency release began after the RATAN release time of 11:00:34 AM GMT while an Operations user performed ad-hoc netting on the same `READY` gross cashflow. The source specifies a 55-second overlap. The gross payment was recalled and returned on 14 Jan 2026.

The root-cause statement identifies an undocumented RATAN behavior: the application did not block ad-hoc netting while the gross cashflow was being released. This is documented as an inadequate software configuration or missing system function.

## Proposed controls

Two controls are described, but the source does not provide deployment evidence, test results, or production-validation records.

1. **Timing control:** prevent Operations from performing netting or splitting in the final ten minutes before the release cutoff. The stated target date is 2026-01-17.
2. **Status check:** permit only `READY` payments to be sent downstream; release must stop when a payment changes to another status. The stated target date is 2026-01-31.

The source uses both past-tense language about controls being put in place and future-oriented target dates. The actual deployment chronology and effectiveness therefore remain unresolved.

## Allowed actions from `READY`

| | Source Cashflow Status | Action | Target Cashflow Status | Business Case | Risk On Duplication | Control |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | READY | Maker Submit | WAITING | Adhoc SSI stamping - Maker resubmit SI | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 2 | READY | Checker Reject | WAITING | SSI Adjustment - Checker Reject to Maker | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 3 | READY | Early Release | READY | OPS manual release payment | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 4 | READY | Un Net | DEAD | OPS Unnet resultant payment | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 5 | READY | UnSplit | DEAD | OPS Un Split payment | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 6 | READY | Hold | HOLD | OPS Hold the payment from auto releasing | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 7 | READY | Manual Swift Suppress | WAITING | Maker submit swift suppression to checker | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 8 | READY | Manual Fail | WAITING | Maker submit manual fail to checker | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 9 | READY | Full Utilize | UTILIZED | Either OPS manually process FX Full Utilization from FXU or by auto utilization process | , Status Machine Control, No Payment generated | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 10 | READY | Partial Utilize | PARTIALLY_UTILIZED | OPS manually process FX Partial Utilization from FXU | , Status Machine Control, No Payment generated | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 11 | READY | Net | NETTED | OPS net the payment | by Jan 2026, Strategic fix done | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 12 | READY | Split | SPLIT | OPS split the payment | by Jan 2026, Strategic fix done | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 13 | READY | Manual Suppress | WAITING | Maker submit cashflow suppression to checker | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 14 | READY | Resend To Razor | READY | Post release job, OPS manual retry when Razor did not receive the cashflow on edge exceptional case | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |
| 15 | READY | Regenerate Swift | READY | Post release job, OPS manual retry when Swift Service did not receive the cashflow on edge exceptional case | , Status Machine Control | Applied hard block that allow only READY payments sending to downstream, as explained by [Section 5](https://confluence.global.standardchartered.com/display/DSP/OPS+Allowed+Actions+Post+Pending+Release#OPSAllowedActionsPostPendingRelease-DiagramForTheControl) |

## Design implications

The stated `READY`-only rule is an intended business invariant, not evidence that checking eligibility, updating status, creating an outgoing instruction, and dispatching it are atomic. In particular, `Early Release`, `Resend To Razor`, and `Regenerate Swift` retain `READY` status and require separate idempotency and delivery-state safeguards.

See [[cashflow-release-and-netting-race-condition]], [[release-time-cashflow-status-gating]], and [[cash-settlement-release-cutoff-controls]]. The `READY` transitions complement the lifecycle context in [[ratan-cashflow-lifecycle-service]].
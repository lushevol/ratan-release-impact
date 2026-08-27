---
type: source
title: 2025 Cash Settlement Tranche 1 RATAN Runbook
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, release-runbook, RATAN-ONE, FMRP-China, CPT]
related: [2025-cash-settlement-tranche-1, murex, control-m, nds-auto-netting, cashflow-monitoring, cashflow-reconciliation, cashflow-accounting-release, what-flag-does-nds-auto-netting-require, how-should-swap-agent-and-rfr-be-validated]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2025 Release Plan/2025 Cash Settlement Tranche 1 Ratan Runbook.md"]
---

# 2025 Cash Settlement Tranche 1 RATAN Runbook

## Summary

This operational runbook describes the planned release sequence for the 2025 Cash Settlement Tranche 1 under the [[FMRP China Cash Settlement]] process and [[RATAN ONE]] release plan. It covers preparation, controlled CPT cashflow testing, monitoring, cancellation, whole-data publication, reconciliation, operations processing, and accounting release.

The document is a plan rather than an execution record. It does not establish that any scheduled activity completed successfully, nor does it provide acceptance thresholds, reconciliation results, incidents, or measured performance.

## Planned sequence

1. **Preparation**
   - Apr 21: Rule update by data operations, assigned to [[Lina Feng]].
   - Apr 25: [[Control M]] job release, assigned to [[Jie Cai]].
   - Apr 26 at 9 AM: Change release by `Dev`.

2. **Controlled tranche testing**
   - Apr 28 at 11 AM: [[Murex]] starts pushing tranche 1 CPT cashflows using `1 USD/0.01 XAU`.
   - After the push completes, monitoring begins. The source table lists 12 PM for this checkpoint.
   - Apr 28 at 19 PM: [[Murex]] cancels the CPT cashflow.
   - Apr 29 and Apr 30: The source instructs the team to repeat the same behavior as steps 4–6, without restating the exact times, quantities, or actions.

3. **Whole-data publication and reconciliation**
   - May 10 at 9 AM: The whole dataset is published.
   - After publication, reconciliation is assigned to [[Yang Chen]] and [[Lina Feng]].

4. **Operations and accounting processing**
   - May 16: Operations users process cashflows.
   - May 17: The runbook calls for accounting release handling for `SWIFT_SUPP` and `READY` cashflows, bulk unsuppress-to-reject processing for `SWIFT_SUPP`, manual early release of `READY` cashflows, and a CPT configuration update.

## Monitoring and reconciliation checklist

The same seven-point checklist is specified after the controlled tranche push and after whole-data publication:

1. Cashflow numbers.
2. Cashflow status.
3. Whether the rules are working.
4. Whether [[NDS Auto Netting]] is pending another flag.
5. Whether the commodity flag is present.
6. Whether the pending fixing flag is present.
7. `Swap Agent` and `RFR` status or behavior.

The runbook does not define expected values, tolerances, acceptance thresholds, or the precise meaning of the pending-flag and `Swap Agent`/`RFR` checks.

## Structured schedule

The source schedule is preserved below.

| | Date | Time | Action | Action On |
| --- | --- | --- | --- | --- |
| 1 | Apr 21st | | Rule update by data ops | @Lina Feng |
| 2 | Apr 25th | | Control M job release | @Jie Cai |
| 3 | Apr 26th | 9 AM | Change Release | Dev |
| 4 | Apr 28th | 11 AM | Murex start to push tranche1 CPT cashflow (1 USD/0.01 XAU) | Murex |
| 5 | | 12 PM | Once done pushing, start monitor, check point: 1. Cashflow Numbers 2. Cashflow Status 3. Rule are working 4. NDS Auto Netting are pending another flag 5. Have commodity flag 6. Have pending fixing flag 7. Swap Agent/RFR? | @Lina Feng |
| 6 | | 19 PM | Murex cancel CPT cashflow | |
| 7 | Apr 29th | | Same Behavior as step 4-6 | |
| 8 | Apr 30th | | Same Behavior as step 4-6 | |
| 9 | May 10th | 9 AM | Start to publish whole data | |
| 10 | | | Once done pushing, start recon, check point: 1. Cashflow Numbers 2. Cashflow Status 3. Rule are working 4. NDS Auto Netting are pending another flag 5. Have commodity flag 6. Have pending fixing flag 7. Swap Agent/RFR? | @Yang Chen @Lina Feng |
| 11 | May 16th | | Ops user process cashflow | |
| 12 | May 17th | | 1. Release SWIFT_SUPP/READY cashflow for accounting 1. User bulk unsuppress->reject for SWIFT_SUPP 2. User manual early release READY cashflow 2. Update CPT config | |
| 13 | | | | |
| 14 | | | | |

## Ownership and controls

Named ownership is provided for the rule update, Control M job release, monitoring, and reconciliation. Ownership is not specified for whole-data publication, Murex cancellation, operations processing, the May 17 accounting actions, or authorization of manual early release.

No rollback procedure, incident process, escalation path, or approval sequence is included for the rule update, change release, or CPT configuration update.

## Open implementation questions

- Are all dates intended to be in 2025, and which time zone applies?
- Does “same behavior” on Apr 29 and Apr 30 include the same quantity, monitoring time, and cancellation time?
- What exact flag is required for the `NDS Auto Netting` pending state?
- What are the expected values for the commodity and pending fixing flags?
- What does the `Swap Agent`/`RFR` check validate?
- What are the acceptance thresholds for counts, statuses, rules, and reconciliation differences?
- What is the order and dependency between unsuppress-to-reject, manual early release, and CPT configuration update?
- Who owns and authorizes the May 16–17 operations and accounting actions?

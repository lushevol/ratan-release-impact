---
type: source
title: "Inter-Entity Netting — UAT"
authors: [test user]
year: 2026
url: "https://uklvadapp1342.uk.dev.net:8453/?show_normal_login=y"
venue: FMO Post Trade Portal
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, settlement-day-2, inter-entity-netting, auto-netting, UAT]
related: [inter-entity-netting, pending-auto-netting-state, netting-resultant-cashflow, netting-un-net-lifecycle, netting-resultant-cashflow-lifecycle, netting-eligibility-rules, auto-netting-datetime-calculation, irs-resultant-cashflow-netting, nostro-static-validation, released-resultant-amendment-handling, clearing-resultant-swift-suppression, settlement-suppression-exceptions, fmo-post-trade-portal, ratan, lms, irs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting - UAT.md"]
---

# Inter-Entity Netting — UAT

## Source context

This document records user-acceptance testing for inter-entity cashflow netting in [[entities/ratan]], using the fmo post trade portal test environment. The tester is identified as `test user`. The Day 1 entity scope was recorded as **to be confirmed**.

The embedded evidence covers April–May 2026. Several scenarios were initially affected by temporary environment or queued-status issues and passed after reinstatement and retest. LMS confirmations were added for selected scenarios by Nivi on 2026-04-27.

## Core findings

The UAT supports the following observed behavior:

- Non-USD cashflows, USD cashflows above USD 100,000, and cashflows for out-of-scope entities do not meet the tested inter-entity netting conditions.
- Eligible cashflows enter `Pending auto netting` before successful matching and transition to `NETTED`.
- Exact FMID matching, backend static mapping, and BIC-based conditions can produce netting resultants.
- When the counterpart is missing or suppressed by a cashflow suppression or SWIFT suppression rule, the eligible cashflow eventually settles as gross.
- Cashflows arriving after the netting date/time can be handled by a later netting cycle. The test expectation was a subsequent run after 30 minutes.
- Withdrawal and amendment behavior depends on whether one or both resulting payments have been released.
- Disabling the inter-entity rule sends pending, not-yet-netted cashflows as gross but does not affect existing netted components or resultants.
- IRS aggregation resultants can be moved to `DEAD` and their component cashflows re-netted into new inter-entity resultants.
- Manual one-sided un-netting is technically supported but is explicitly not expected in normal BAU operations.

These findings are consolidated in [[concepts/inter-entity-netting]].

## Test environment and evidence qualifications

The test environment was:

`https://uklvadapp1342.uk.dev.net:8453/?show_normal_login=y`

Initial failures or anomalous statuses were recorded in Scenarios 6, 10, and 11. The source attributes these to a temporary environment issue or queued cashflows; the flows were reinstated and the retests passed. These cases should therefore be treated as final retest passes with an environment caveat, rather than as uninterrupted successful executions.

Scenario 8 passed after a missing nostro static was corrected. This separates netting creation from resultant release: the matching and netting succeeded, but the net parent could not initially be released.

Scenario 13 is marked passed in the evidence, but the document also states that the case became invalid after a withdrawal-event-handling feature was added. Its result must not be treated as confirmation of current canonical behavior.

LMS status is not populated for every scenario. Application status evidence and LMS receipt confirmation are therefore not interchangeable.

## Scenario evidence

| Scenario | Test area | Test data or resultant identifiers | Recorded outcome |
|---:|---|---|---|
| 1 | Non-USD cashflow exclusion | `M00426072128` | Passed; EUR cashflow was not eligible for netting. |
| 2 | Amount above USD 100,000 exclusion | `M00326072128` | Passed; USD 120k cashflow was not eligible. |
| 3 | Out-of-scope entity exclusion | `M00626072128` | Passed; cashflow booked for SCB NY was not eligible. |
| 4 | Missing counterpart; gross fallback | `M00126090160`, `M00226090160` | Passed; only the China-side cashflow was received, so it was not netted. |
| 5 | Counterpart affected by cashflow suppression | `M00326090220`, `M00426090220`, `M00526090160`, `M00626090160` | Passed; CN cashflows did not net because the opposite HK cashflows were suppressed. |
| 6 | Counterpart affected by SWIFT suppression | `M00226376328`, `M00226376330`, `M00326376328`, `M00326376330` | Initial queued-status issue; passed after environment remediation and retest. |
| 7 | Exact FMID matching | `M00226378919`, `M00126378919`, `M00226378886`, `M00126378886` → `N00000148207`, `N00000148206` | Passed; components entered `Pending auto netting` and then became `NETTED`. |
| 8 | Backend static mapping with non-exact FMIDs | `007754385448`, `008754385448`, `M00126314449`, `M00226314449` → `N00000148211`, `N00000148210` | Passed after nostro static correction; initial resultant release was blocked by missing nostro static. |
| 9 | BIC-based matching | `M00226389175`, `M00226389177`, `M00126389177`, `M00126389175` → `N00000148705`, `N00000148704` | Passed after the rule was updated with a BIC condition. |
| 10 | Eligible cashflow without a counterpart; gross fallback | `M00126376330`, `M00126376328` | Initial queued-status issue; passed after retest and was received as gross. |
| 11 | Late arrival and subsequent 30-minute cycle | Batch 1 → `N00000148212`, `N00000148213`; Batch 2 → `N00000156552`, `N00000156553` | Initial queued-status failure; passed after reinstatement and retest. |
| 12 | Withdrawal while pending | `M00126330470` | Passed; pending cashflow was cancelled after withdrawal. |
| 13 | Obsolete withdrawal-after-netting case | `M00326330476`, `M00226330476`, `M00126330476`, `M00326330478`, `M00226330478`, `M00126330478` → `N00000148247` | Recorded as passed, but explicitly declared invalid after a feature change. |
| 14 | IRS aggregation interaction | `N00000148696`–`N00000148699` → `N00000148700`, `N00000148701` | Passed; IRS aggregation resultants moved to `DEAD` and components were re-netted. |
| 15 | Withdrawal after netting, before either release | `N00000150578`, `N00000150579` → `N00000150580`, `N00000150581` | Passed; resultants were un-netted, the withdrawn component cancelled, and remaining components were rebuilt. |
| 16 | Withdrawal after one resultant was released | `N00000150582`, `N00000150583` | Passed; existing resultants were not changed and the affected component remained in a waiting state. |
| 17 | Withdrawal after both resultants were released | `N00000150590`, `N00000150591` | Passed; released resultants remained unchanged. |
| 18 | Disablement rollback for pending flows | `M00946677889`, `M00925677888` | Passed; pending cashflows settled as gross after rule disablement. |
| 19 | Disablement after netting | `M00825677888`, `M00815677888`, `M00816677889`, `M00826677889` → `N00000150599`, `N00000150600` | Passed; existing components and resultants were unaffected. |
| 20 | Amendment before payment release | `N00000150669`, `N00000150670`; withdrawal `M00B75714459`; replacement `M00A26128057` | Passed; original net parent moved to `DEAD` and a new netting pair was generated. |
| 21 | Amendment after one-side release | `N00000150667`, `N00000150668`; withdrawal `M00A75714459`; replacement `M00A16128057` | Passed; existing completed netting was unaffected and the cancelled flow remained waiting. |
| 22 | Amendment after both-side release | `N00000150646`, `N00000150647` | Passed; released resultants were unaffected. |
| 23 | Manual un-net of one resultant | `N00000150671`, `N00000150674` | Passed as an exception test; un-net components were reprocessed while untouched components remained `Netted`. Not BAU behavior. |
| 24 | Manual un-net of both resultants | `N00000150675`, `N00000150676` → `N00000150677`, `N00000150678` | Passed; resultants moved to `DEAD`, and a later cycle generated new net cashflows. |
| 25 | Withdrawal followed by one-sided manual un-net | `N00000150679`, `N00000150680` | Passed as an exception test; the withdrawn component and corresponding net flow moved to `DEAD`, with remaining components reprocessed or sent gross. Not BAU behavior. |

## Lifecycle interpretation

The evidence indicates a release-state boundary:

- Before netting, withdrawal directly cancels a pending cashflow.
- After netting but before release, withdrawal or amendment can invalidate the existing resultants, return components to processing, and generate replacement netting.
- After one or both sides are released, existing resultants are preserved. The affected component may remain in `WAITING` or another waiting-type state rather than changing the completed payment.
- Manual un-netting is an operational exception and should not be used as the definition of the normal automatic lifecycle.

See [[concepts/netting-un-net-lifecycle]] and [[concepts/released-resultant-amendment-handling]].

## Open questions

- What is the confirmed Day 1 entity scope?
- Is the USD 100,000 threshold inclusive, and does the same threshold apply across all supported currencies and products?
- What timeout or job criterion changes an unmatched pending cashflow to gross?
- Is the 30-minute interval globally configured or specific to this environment?
- What precedence applies when FMID, backend static, and BIC matching mechanisms are simultaneously available?
- Who owns production disablement and rollback of the inter-entity netting rule?
- Does the LMS evidence represent formal UAT sign-off or only operational receipt confirmation?

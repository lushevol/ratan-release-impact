---
type: source
title: "CHG1047654 RATAN BAU Release — 15 August 2026"
authors: []
year: 2026
url: ""
venue: "BPMS Existing Flow/Feature Operational Readiness Questionnaire"
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, bau-release, change-management, pre-cab, operational-readiness, auto-netting]
related: [chg1047654, data-archival-backup-table-retirement, migrated-data-amendment-validation, what-was-the-single-auto-netting-issue-fixed-in-story-15576808, how-is-backup-history-table-removal-recoverable-in-story-14766494, where-is-chg1047654-uvt-regression-and-uat-evidence]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_15_CHG1047654_Ratan BAU Release - 15th Aug.md"]
---
# CHG1047654 RATAN BAU Release — 15 August 2026

This source is a Pre-CAB operational-readiness questionnaire for the RATAN BAU release identified as [[chg1047654]], scheduled for 15 August 2026. It records planned scope and governance attestations; it does not establish that deployment completed successfully or that post-release verification passed.

## Release scope

| ADO Story | Source description | Change category |
|---|---|---|
| 14766494 | `[Archival & Retrieval] production business live phase 1- drop backup history table` | Data archival and backup-history-table removal |
| 15506023 | `Enhancement for non-eco amend check for migrated data` | Migrated-data amendment validation enhancement |
| 15576808 | `Fix single auto netting issue` | Auto-netting defect fix |

The three changes are bundled in one release record, but the source does not show that they affect the same component, workflow, repository, or service.

## Operational readiness record

| Checklist area | Recorded response |
|---|---|
| Implementation plan / manual-step attestation | `All ADO pipelines` |
| UVT plan | Blank |
| Rollback plan | `All ADO pipelines` |
| Change scheduling | `15/08/2026` |
| PSS resource booking window | `16:00~18:00` |
| Safe Change attestation | `SAFE` |
| OLA / SLA / ASRM / DOI updates | `NA` |
| PSS Core Function / Interface Confluence updates | `NA` |
| Monitoring changes | `NA` |
| Functional test evidence | Attached image: `attachments/image-2026-8-12_9-29-36.png` |
| Regression test evidence | Blank |
| Performance test evidence | Blank |
| UAT sign-off | Blank |
| DR test evidence | Blank |

## Interpretation and limitations

The stated implementation and rollback mechanism is “All ADO pipelines,” without named pipelines, versioned deployment artefacts, release gates, rollback triggers, or validation procedures.

The `SAFE` Safe Change Dashboard status indicates a recorded governance outcome. The source says CRP Meeting approval is required when the dashboard result is Non-Compliant; it therefore implies that this additional approval was not required. No dashboard snapshot, approval record, booking confirmation, or deployment outcome is included.

The functional-test attachment is present in the source, but its contents are unavailable in the supplied text. UVT, regression, performance, UAT, and DR evidence are blank rather than marked `NA` or linked elsewhere. This is a documentation gap, not evidence that such testing did not occur.

[[data-archival-backup-table-retirement]] is the highest recoverability concern in the listed scope because the source identifies a backup-history-table removal while providing no table name, retention requirements, restoration method, dependency analysis, or restoration-test evidence.

Story 15576808 is described only as a “single auto netting issue” fix. It may be adjacent to [[single-cashflow-auto-netting-exception]], but the source does not establish that it implements that specific exception behavior.
---
type: source
title: SFX Supporting
authors: []
year: 2024
url: ""
venue: Internal operational support notes
created: 2026-08-23
updated: 2026-08-23
tags: [sfx, lifecycle-testing, disaster-recovery, migration-cycle-2, nstp]
related: [sfx, ratan, lms, razor, tds3, migration-weekend-lifecycle-event-control, cashflow-migration-readiness, was-the-sfx-migration-weekend-nstp-hold-approved-deployed-and-removed, how-should-sfx-past-value-date-events-reconcile-between-ratan-and-lms, what-is-the-approved-sfx-dr-test-treatment-for-future-cashflows-in-ssi-exception, was-razor-acknowledgement-without-status-accepted-for-sfx-lifecycle-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md"]
---
# SFX Supporting

Internal SFX operational support notes covering migration-cycle-2 lifecycle testing, planned disaster-recovery (DR) preparation, and migration-weekend event-handling expectations. The document contains observations and proposed test outcomes, with several items explicitly awaiting confirmation; it does not establish approved production policy.

## Scope and evidence status

The notes include entries dated 9 November 2023 and 11 January 2024. They refer to email attachments and a screenshot that are not included in the imported content. Consequently, statements about replies, confirmations, and test outcomes are limited to what the notes record.

## Migration-cycle-2 lifecycle-test limitation

During migration cycle 2, [[tds3]] reportedly sent only the last version of historical data to [[ratan]]. This was identified as non-production-like behavior. Only the rebook event was received and processed by RATAN.

This limits validation of a complete historical lifecycle sequence, including any preceding versions and withdrawal behavior. See [[cashflow-migration-readiness]].

## Operational testing observations

Operations support requested test scenarios from Karthik. One test cashflow was acknowledged by [[razor]] without a further reported status. Karthik was asked to confirm whether that outcome was acceptable or whether the cashflow needed to be rebooked for testing. The source does not record a final answer.

A separate lifecycle check examined cashflows received by RATAN and sent to Razor after Operations processing. Based on a list shared by the upstream system, some cashflows were pending manual Operations processing while others had already been sent to [[lms]] and Razor. The outcome of the reported response is not included.

## Planned DR activity

On 11 January 2024, the notes recorded a planned DR data cut on 23 February and an expected March load date, still to be confirmed. This is planning information only and does not evidence execution or final approval.

## Proposed migration-weekend approach

The proposed approach, pending confirmation from Dinesh and Karthik, was:

- LMS would ignore migration-weekend events with past value dates, assuming cashflows whose payment date preceded migration had settled.
- Because partial STP was enabled in the BCS flow, an NSTP rule was proposed to hold all unaffirmed cashflows during the migration weekend and be removed afterward.
- A withdrawal ACU for a past-value-date cashflow would be received and held in the RATAN NSTP queue; a future cashflow would be directly cancelled in RATAN.
- A withdrawal ACU would be sent to LMS when the relevant cashflow had previously been sent to LMS.
- A rebook DBU would be received and held in the RATAN NSTP queue. Operations would ignore past-value-date rebooks and process future cashflows through BAU.
- The required treatment of future cashflows held in an SSI exception remained unresolved.

These are expected DR test results rather than verified system behavior. The control and reconciliation gaps are tracked in [[migration-weekend-lifecycle-event-control]] and its linked queries.
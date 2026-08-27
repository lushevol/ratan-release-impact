---
type: concept
title: Migration-Weekend Lifecycle Event Control
created: 2026-08-23
updated: 2026-08-23
tags: [migration, disaster-recovery, lifecycle-events, nstp, operations-control, partial-stp]
related: [sfx, ratan, lms, razor, tds3, cashflow-migration-readiness, fmrp-trade-attribute-cashflow-nstp, was-the-sfx-migration-weekend-nstp-hold-approved-deployed-and-removed, how-should-sfx-past-value-date-events-reconcile-between-ratan-and-lms, what-is-the-approved-sfx-dr-test-treatment-for-future-cashflows-in-ssi-exception]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md"]
---
# Migration-Weekend Lifecycle Event Control

Migration-weekend lifecycle event control is a temporary operational-control pattern intended to prevent unintended settlement processing while migration or DR activity is underway.

## SFX DR test proposal

In the SFX support notes, the proposed control pattern combines:

- segmentation of events by past versus future value date;
- temporary holding of unaffirmed cashflows in NSTP to mitigate partial-STP risk;
- explicit routing of withdrawals to LMS where the original cashflow had already been routed there;
- manual Operations treatment of held rebook events; and
- removal of the temporary NSTP rule after the migration window.

The source presents this as a proposed DR approach with outstanding confirmations, not as an approved or deployed control.

## Control risks

A past-value-date suppression rule relies on the assumption that all pre-migration payments have settled. That assumption requires evidence and reconciliation controls.

The proposed behavior also creates a potential split-state condition: [[lms]] may ignore past-value-date events while [[ratan]] holds related events in NSTP. A defined ownership model, exception process, and reconciliation output are needed to demonstrate that valid corrections are not lost.

Partial STP in the BCS flow was identified as a risk, but the notes do not establish whether the temporary NSTP control was approved, enabled, tested, or removed.

## Test coverage

A representative DR test should cover ACU withdrawals and DBU rebooks across:

- past and future value dates;
- cashflows previously routed to LMS and those not routed there;
- NSTP-held and automatically processed states;
- Operations handling decisions; and
- SSI-exception cases.

The SFX migration-cycle-2 data set was not sufficient to validate the full lifecycle sequence because [[tds3]] reportedly supplied only final historical versions. See [[cashflow-migration-readiness]].
---
type: query
title: How Should SFX Past-Value-Date Events Reconcile Between RATAN and LMS?
created: 2026-08-23
updated: 2026-08-23
tags: [sfx, reconciliation, past-value-date, ratan, lms, disaster-recovery]
related: [sfx, ratan, lms, migration-weekend-lifecycle-event-control, cashflow-migration-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/SFX Supporting.md"]
---
# How Should SFX Past-Value-Date Events Reconcile Between RATAN and LMS?

The proposed SFX DR approach says that [[lms]] would ignore migration-weekend events with past value dates, based on the assumption that pre-migration payments had settled. At the same time, [[ratan]] was expected to hold certain past-value-date ACU withdrawal and DBU rebook events in NSTP.

The source does not define how the systems reconcile these different treatments or how Operations confirms that an unsettled historical cashflow, valid withdrawal, or downstream correction has not been lost.

## Evidence needed

- Confirmation of the settlement-status assumption for pre-migration payments.
- An event correlation key and reconciliation report spanning RATAN and LMS.
- Ownership for reviewing held, ignored, rejected, and already-routed events.
- Exception handling for historical cashflows found not to be settled.
- Acceptance criteria for DR-test reconciliation completion.
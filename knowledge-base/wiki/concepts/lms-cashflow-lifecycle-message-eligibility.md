---
type: concept
title: LMS Cashflow Lifecycle Message Eligibility
tags: [lms, cashflow, lifecycle-events, message-eligibility, settlement]
related: [lms, manual-entity-lms-reference-data-feed, cashflow-suppression-rule, why-do-released-nos-cashflows-have-different-lms-send-outcomes, what-is-the-lms-outcome-for-swift-suppressed-withdrawal-before-release]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Self testing.md"]
---
# LMS Cashflow Lifecycle Message Eligibility

LMS cashflow lifecycle message eligibility is the decision area governing whether a cashflow lifecycle event, such as release or withdrawal, creates an outbound message to [[lms]].

Eligibility may depend on lifecycle sequence, settlement means, product or cashflow classification, counterparty or account configuration, static data, and suppression state. It must not be reduced to a settlement-means-only rule without corroborating specification or configuration evidence.

## UAT2 evidence

The [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--r2mefv]] record provides limited self-test evidence:

- A release and a withdrawal for `M00202510132` have separately named send-to-LMS XML artifacts.
- A released `OVER` sample, `M00202510124`, is explicitly recorded as not sent to LMS.
- Released NOS samples have mixed recorded outcomes: several appear in the send-to-LMS test set, whereas `M00202510128` is explicitly marked not sent.
- A SWIFT-suppressed withdrawal-before-release scenario was tested, but its resulting LMS behavior is not stated in readable text.

## Evidence boundary

Outbound artifact creation is not equivalent to confirmed LMS ingestion, acknowledgement, reconciliation, or business completion. The record does not define the authoritative eligibility contract or the semantics of `NOS`, `OVER`, `CURR|OPT|SMP`, `CURR|FXD|FXD`, `XSW`, or `FXD`.

This concept is distinct from [[manual-entity-lms-reference-data-feed]], which addresses reference-data feed and reconciliation rather than lifecycle-event message generation.
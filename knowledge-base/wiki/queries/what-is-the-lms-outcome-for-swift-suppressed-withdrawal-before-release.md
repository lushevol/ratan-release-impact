---
type: query
title: What Is the LMS Outcome for SWIFT-Suppressed Withdrawal Before Release?
tags: [lms, swift, withdrawal, suppression, uat2]
related: [lms, lms-cashflow-lifecycle-message-eligibility, cashflow-suppression-rule, what-is-the-authoritative-difference-between-swift-and-cashflow-suppression]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Self testing.md"]
---
# What Is the LMS Outcome for SWIFT-Suppressed Withdrawal Before Release?

## Evidence

The UAT2 record lists `M00202510136 swift suppressed withdrawal before released` and references the artifacts:

- `lms_message_202510261211.csv`
- `lms_message_202510261203.csv`

The readable source does not state whether LMS received a withdrawal event, no event, a cancellation-like event, or another outcome.

## Information needed

- Contents and timestamps of both LMS CSV artifacts.
- Lifecycle-event timeline for `M00202510136`.
- The authoritative distinction between SWIFT suppression and cashflow suppression.
- LMS outbound logs, acknowledgement records, and any retry or idempotency evidence.
- The applicable specification or configured rule for withdrawal before release.

## Decision impact

The outcome determines whether message generation follows cashflow state transitions independently of SWIFT delivery suppression.
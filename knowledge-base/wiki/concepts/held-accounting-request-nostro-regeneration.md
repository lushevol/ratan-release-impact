---
type: concept
title: Held Accounting Request Nostro Regeneration
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, nostro, request-regeneration, hold, delayed-send, data-freshness]
related: [ratan-cash-settlement-accounting-service, nostro-notification-and-refresh, settlement-accounting, should-historical-cashflows-refresh-nostro-identifiers, what-is-the-atomicity-and-cutoff-contract-for-nostro-refresh-before-accounting-send]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/[Accounting Enhancement] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"] Prepare Nstro Account Info before Sent.md"]
---
# Held Accounting Request Nostro Regeneration

Held accounting request Nostro regeneration is the requirement to refresh the Nostro-dependent portion of an accounting request for applicable tasks awaiting delayed downstream dispatch.

## Requirement

If accounting information was generated while a task was in `HOLD`, and the associated Nostro account is refreshed before the scheduled send, the Nostro-related partial request information must be regenerated before the task is sent downstream.

The purpose is to prevent an accounting request prepared against an old Nostro from being dispatched after refreshed Nostro data is available.

## Scope

The confirmed requirement concerns outbound accounting-request preparation. It does not by itself require:

- updating persisted cashflow Nostro identifiers;
- creating a new cashflow version;
- re-stamping SWIFT or SSI information;
- applying RFI, dedicated-Nostro, or portfolio-based selection rules.

These domains require separate evidence and contracts.

## Unspecified operational contract

The source does not define which tasks are “applicable,” how a Nostro refresh is identified, whether regeneration is event-driven or send-time-driven, or how dispatch races and retries are handled. These questions are tracked in [[what-is-the-atomicity-and-cutoff-contract-for-nostro-refresh-before-accounting-send]].

The source also leaves unanswered whether netted, released, and withdrawn cashflows follow this rule; see [[does-nostro-refresh-regenerate-accounting-requests-for-netted-released-and-withdrawn-cashflows]].
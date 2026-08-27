---
type: concept
title: Double-Blind Exception Verification
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, exception-management, maker-checker, verification, scbml]
related: [nstp-exception-operation-levels, nstp-exception-metadata, ratan-cashflow-lifecycle-service, what-exactly-is-double-blind-verification-for-affirmation-and-back-value-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
---
# Double-Blind Exception Verification

Double-blind verification is a stated approval control for NSTP **Affirmation** and **Back Value** exceptions. These exception types require additional user input. On checker approval, Rule Service performs verification, and the exception can close only when that verification passes.

## Scope

The source limits this behavior to Affirmation and Back Value exceptions. Successful approval makes the user input effective on the SCBML message. The special-rule integration matrix identifies [[ratan-cashflow-lifecycle-service]] as the exception-fix integration for both rule types.

This source does not state that double-blind verification applies to GSAM Client, Corp Client, High Value Payment, or Bad Business Day exceptions.

## Missing control definition

The source does not define:

- the inputs supplied by the maker and checker;
- what makes the verification independent or “double-blind”;
- comparison and matching rules;
- handling when verification fails;
- retries, rejection, and rework behavior; or
- the mechanism used to update the SCBML message.

These required details are tracked in [[what-exactly-is-double-blind-verification-for-affirmation-and-back-value-exceptions]].
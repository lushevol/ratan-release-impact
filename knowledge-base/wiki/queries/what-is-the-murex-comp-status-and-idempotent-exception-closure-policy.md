---
type: query
title: What Is the Murex COMP Status and Idempotent Exception Closure Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, comp, idempotency, replay, cashflow-exception]
related: [murex-211, ratan, solace, murex-comp-confirmation-exception-resolution, murex-ratan-cashflow-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# What Is the Murex COMP Status and Idempotent Exception Closure Policy?

The source requires closure of `Pending Confirmation/Affirmation` when a matching Murex trade has `Source_System_Validation_Status = COMP`, with STP promotion only when no other exception remains.

Clarify:

- The authoritative semantic definition of `COMP`.
- Whether `COMP` is final and whether it can regress.
- Idempotency behavior for duplicate trade messages.
- Handling of `/replay` messages and out-of-order delivery.
- Matching behavior when no cashflow or multiple cashflows match the trade ID.
- Audit, retry, error handling, and reconciliation requirements.
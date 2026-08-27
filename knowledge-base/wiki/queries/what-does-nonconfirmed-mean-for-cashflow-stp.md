---
type: query
title: What Does NONCONFIRMED Mean for Cashflow STP?
created: 2026-08-24
updated: 2026-08-24
tags: [nonconfirmed, trade-confirmation, cashflow-stp, stella]
related: [trade-confirmation-driven-cashflow-stp, cdu, stella, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# What Does NONCONFIRMED Mean for Cashflow STP?

The requirement states that Stella statuses `AFFIRMED`, `CONFIRMED`, and `NONCONFIRMED` can close `Pending Confirmation/Affirmation`.

It does not define whether `NONCONFIRMED` means a final negative confirmation result, a non-applicable confirmation outcome, or another state. It also does not state the resulting cashflow disposition after exception closure.

Resolve whether `NONCONFIRMED` may close the exception and whether the resulting cashflow is STP, NSTP with another exception, rejected, suppressed, or otherwise held.
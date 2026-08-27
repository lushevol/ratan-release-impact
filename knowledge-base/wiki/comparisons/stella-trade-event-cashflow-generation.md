---
type: comparison
title: Stella Trade Event Cashflow Generation
created: 2026-08-23
updated: 2026-08-23
tags: [stella, cashflow, trade-events, lifecycle, deprecated]
related: [stella, ratan, cdu, cashflow-amendment-supersession, trade-economic-versus-non-economic-update, trade-confirmation-driven-cashflow-stp, cashflow-partial-update, what-is-the-authoritative-stella-cdu-cashflow-version-correlation-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Deprecated - Stella Market events & cashflow generation.md"]
---
# Stella Trade Event Cashflow Generation

> **Historical comparison only.** The underlying requirement is deprecated.

## Event comparison

| Trade business event and action | Cashflow behavior stated by source | Evidence quality |
| --- | --- | --- |
| Trade — Book | `New` cashflow event | Strong; repeated detailed examples |
| Trade — Economic update | `New → Amendment` or `New ( Cashflow Partial update)` | Strong for amendment examples; partial-update semantics unspecified |
| Trade — Non-economic update | No cashflow event specified in examples | Moderate; absence of listed output is not a formal invariant |
| Trade — Cancel | `New → Withdrawal`, or `New → Amendment → Withdrawal` | Strong; repeated examples |
| Amendment — Economic book | `New → Amendment` or partial update | Moderate; mapping table only |
| Amendment — Non-economic book | `New` | Moderate; mapping table only |
| Amendment — Economic update | Repeated amendments or a new cashflow | Moderate; mapping table only |
| Amendment — Cancel | `New → Amendment → Withdrawal` or `New → Withdrawal` | Moderate; mapping table only |
| Withdrawal — Book | `New → Withdrawal` or `New → Amendment → Withdrawal` | Moderate; mapping table and one detailed scenario |
| Withdrawal — Undo / Revive | Withdrawal followed by amendment | Moderate; mapping table only |
| Termination | `Withdrawal/New` | Weak; no detailed scenario |
| Partial Termination | `Amendment/New/Withdrawal` | Weak; no detailed scenario |
| Close Out, Expiry, Novation, Allocation | No cashflow behavior recorded | Insufficient |

## Confirmation behavior

For detailed Trade and Amendment scenarios, generated cashflows initially progress as NSTP:

```text
PROJECTED->QUEUED->PENDING
```

After a CDU-related confirmation, the document reports STP promotion and settlement:

```text
PENDING->VALIDATED->RELEASED->SETTLED
```

This is evidence for [[trade-confirmation-driven-cashflow-stp]] in the Stella-to-Ratan flow. It does not define the exact event-correlation algorithm or establish that the rule applies to other products.

## Replacement behavior after a confirmed amendment

The detailed confirmed-trade scenario records the following chain:

```text
Trade Book: New cashflows, version 0, NSTP
Trade confirmation: existing version-0 cashflows become STP and settle
Amendment Book: Withdrawal cashflows, version 1, plus replacement New cashflows, version 0
Amendment confirmation: replacement cashflows become STP and settle
```

This supports [[stella-cashflow-amendment-supersession]]: an amendment to a confirmed trade creates a replacement cashflow generation, rather than changing the already-settled cashflow in place.

## Immediate cancellation

For a booked trade that is cancelled before downstream transmission, the source says the `New` and `Withdrawal` events remain in [[ratan]] and are not sent to [[razor]]. Their observed cancellation path is:

```text
PROJECTED->CANCELLED
```

“Discarded” is ambiguous in the source and must not be read as proof of physical deletion.
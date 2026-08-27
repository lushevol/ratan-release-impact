---
type: query
title: What Is the Complete Nostro and Vostro Impact Matrix?
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, nostro, vostro, notifications, re-stamping, open-question]
related: [ssi-change-notification-re-stamping, ssi-stamping-and-best-match, ssi-stamping-reference-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# What Is the Complete Nostro and Vostro Impact Matrix?

The source defines a useful but incomplete mapping between SSI change events, exception categories, and impacted-cashflow algorithms.

## Open points

The vostro matrix leaves blank cells for `missing vostro`, `mismatch`, and several UPDATE and DELETE transitions. It is unclear whether these cells mean no impact, not applicable, or behavior that has not yet been implemented.

The authoritative matrix should also specify:

- Event idempotency and duplicate notification handling.
- Behavior after a re-stamp fails again.
- Whether `AUTO_CLOSED` is the only terminal maker-checker state.
- The exact semantics of global versus non-global vostro conditions.
- Whether selection by business condition and selection by persisted SSI ID can overlap safely.
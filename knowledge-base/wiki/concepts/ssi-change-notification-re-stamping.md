---
type: concept
title: SSI Change Notification Re-Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, notifications, re-stamping, nostro, vostro, eventual-consistency]
related: [ssi-stamping-and-best-match, ssi-stamping-reference-data, eventual-consistency-for-cashflow-exceptions-and-swift-status, cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# SSI Change Notification Re-Stamping

SSI change notification re-stamping is an event-driven recovery mechanism for cashflows whose SSI stamping failed or whose existing settlement instruction may be affected by a nostro or vostro change.

## Selection controls

Impact computation uses:

- Active records in `cashflow_stamping_legacy_exception`.
- Matching party, currency, CFI-code, SSI-ID, and payment-date conditions.
- A recency filter of `updated_at >= current_date - 6`.
- `EXCEPT` clauses to remove records already associated with stamped nostro data or records with non-`AUTO_CLOSED` maker-checker requests.

The six-day window and the meaning of `AUTO_CLOSED` as the sole closed state require confirmation against the operational contract.

## Nostro changes

Nostro events use three algorithms:

- **NA1:** Finds active exception cashflows by party, currency, and event date range.
- **NA2:** Finds recently updated cashflows stamped for a party and currency.
- **NA3:** Finds recently updated cashflows associated with a particular `nostroStaticId` and within the event date range.

The source maps nostro events as follows:

| Type | INSERT | UPDATE | DELETE |
| --- | --- | --- | --- |
| missing nostro | NA1 | NA1 | No impact |
| good stamped | NA2 | NA3 | NA3 |

## Vostro changes

Vostro notifications use either:

- `getImpactCashflowIdsByCondition`, for active exceptions matching business conditions.
- `getImpactCashflowIdsBySsiId`, for active exceptions associated with a specific stamped-vostro SSI ID.

The published matrix is incomplete, especially for `missing vostro`. Blank cells must not be interpreted as “no impact” without confirmation.

## Operational safeguards

Automatic re-stamping is designed not to overwrite manual or ad-hoc SSI work. Existing stamped nostro records and pending maker-checker requests are excluded in the relevant queries. See [[ad-hoc-ssi-stamping-exclusion]].

This design is a concrete example of eventual recovery after reference-data changes, but it does not prove that every selected cashflow will re-stamp successfully.
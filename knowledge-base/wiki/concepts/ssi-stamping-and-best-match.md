---
type: concept
title: SSI Stamping and Best Match
created: 2026-08-24
updated: 2026-08-24
tags: [SSI, stamping, best-match, cash-settlement]
related: [ssi-stamping-reference-data, cashflow, cdups, scbml, ssi-change-notification-re-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md"]
---
# SSI Stamping and Best Match

SSI stamping matches a trade or cashflow to settlement instructions and applies the selected SSI. The design states that candidate vostro and nostro records are queried and evaluated using best-match logic.

## Success criterion

Stamping succeeds only when exactly one unique vostro or nostro is found. A missing candidate or multiple candidates is therefore an exception condition rather than a reason to select an arbitrary record.

The source does not provide the detailed ranking or tie-breaking rules used by best-match logic. The uniqueness requirement should therefore be treated as authoritative for the outcome, but not as a complete specification of candidate ranking.

## Separate APIs with shared matching logic

Trade and cashflow stamping share matching logic, but remain separate APIs because:

- Their response formats differ.
- Trade-stamping inputs must be parsed from SCBML.
- XPath locations vary by trade type.
- The cashflow and trade APIs expose different integration boundaries.

[[cdups]] invokes trade stamping and receives enriched [[scbml]]. [[camunda]] triggers cashflow stamping.

## Failure behavior

Cashflow stamping failures generate SSI exceptions and place the cashflow into NSTP. The source does not define equivalent failure handling for trade stamping.

The implementation is described in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1j9svpi]].
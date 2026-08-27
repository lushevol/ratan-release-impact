---
type: concept
title: Vostro and Nostro SSI Matching
created: 2026-08-23
updated: 2026-08-23
tags: [vostro, nostro, settlement-instructions, ssi-stamping, matching]
related: [ssi-stamping-service, ssi-stamping, nostro-account-scope, scbml-trade-enrichment-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# Vostro and Nostro SSI Matching

Vostro and Nostro SSI matching resolves settlement-instruction records for the counterparty and the bank's own settlement account during [[concepts/ssi-stamping]].

## Vostro matching

Vostro lookup uses the counterparty FMID, branch FM code, currency, CFI code, settlement method, settlement type, debit/credit, and SSI status.

The design specifies these defaults or pending values:

- CFI code: `*F****`.
- Settlement method: `cash`.
- Settlement type: `cash`.
- SSI status: one of `"Active"`, `"New"`, or `"Update"`, currently described as hard-coded.
- Branch FM code: obtained from SSI Stamping query logic.

Vostro outcomes include unique, missing, and multiple matches.

## Nostro matching

Nostro lookup uses the legal-entity FMID and payment currency. Settlement means and settlement account are obtained from the Vostro result. The default Nostro is specified as `Currency + MAIN`.

Nostro outcomes include unique, missing, multiple, and default matches.

## Outcome semantics

For SCB Pay / sell currency, unique Vostro plus unique Nostro enriches both parties. Missing or multiple Vostro may result in blank Vostro with either default or blank Nostro. Unique Vostro with missing or multiple Nostro enriches the counterparty while setting the SCB account to `To Be Advise`.

For SCB Receive / buy currency, only Nostro matching is evaluated. A unique Nostro enriches the SCB account; missing or multiple Nostro results in `To Be Advise`.

The source's statement that `Credit` means `SCB (Payer)` and `Debit` means `SCB (receiver)` is preserved as a service rule, but requires domain validation.
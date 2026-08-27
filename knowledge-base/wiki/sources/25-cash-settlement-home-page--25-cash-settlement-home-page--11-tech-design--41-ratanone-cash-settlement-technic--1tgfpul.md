---
type: source
title: Cashflow Lifecycle Stamping Logic
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, lifecycle-service, technical-design, stamping]
related: [cashflow-lifecycle-stamping, cashflow-precheck-validation, lifecycle-service, bpsi, data-persistence-node, cashflow-unnetting, withdrawal-new-cashflow-and-razor-release-check, lien-stamping-and-re-stamping, pending-fixing-flag-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# Cashflow Lifecycle Stamping Logic

## Summary

This technical-design document proposes moving cashflow attribute stamping out of the Data Persistence Node and into a separate reusable API and lifecycle action within Lifecycle Service. The proposal responds to the expansion of requirements from Day 1 China support to H2 UK/DE and planned UK 2025 attributes.

The document describes current precheck, enrichment, validation, withdrawal, and new-cashflow processing. It does not establish that the proposed API or lifecycle action was approved or implemented.

## Attribute scope

| Phase | Cashflow attribute | Mandatory |
| --- | --- | --- |
| Day 1 for CN | Booking entity FMCODE | Yes |
| Day 1 for CN | Counterparty FMCODE | Yes |
| Day 1 for CN | Client Type | No |
| Day 1 for CN | Reversal / Rebook | No |
| H2 for UK/DE | Client domicile country | No |
| H2 for UK/DE | Client BIC | No |
| For UK 2025 | LIEN AMOUNT | No |
| For UK 2025 | Pending Fixing Flag | No |

Only booking entity FMCODE and counterparty FMCODE are explicitly mandatory in this source. The later attributes, including `LIEN AMOUNT` and `Pending Fixing Flag`, are explicitly non-mandatory.

## Proposed design

The proposed model has three stated goals:

1. Simplify the logic and responsibility of the Data Persistence Node.
2. Move stamping logic to a separate API within Lifecycle Service.
3. Make cashflow attribute stamping a reusable lifecycle action for other workflow paths, including reinstate.

This is an architectural proposal rather than an implementation confirmation. The source does not define an API signature, state transition contract, authorization model, rollback behavior, or migration plan.

## Precheck and enrichment

The documented precheck logic is:

1. Convert to `StellaInfo`; the source questions whether this remains necessary.
2. Convert to `RatanStellaMessageEvent`.
   - Convert to `StellaInfo` again; the rationale is questioned.
   - Publish a common Event; the continued need is questioned.
   - Round the settlement amount.
   - Format `settlementDate` as `yyyy-MM-dd`.
   - Enrich legal entities `party1` and `party2` with `FMCODE`, `FMTYPE`, `DOMICILECOUNTRY`, and `ADDRLINE`.
   - Format the Withdrawal settlement date if present; the source states that this XPath is not in use and has been removed.
   - Enrich event reason.
   - Enrich the beneficiary `bic` flag.
3. Validate the input.

The historical or removed Withdrawal XPath is:

```text
/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow[scb:header/scb:event='Withdrawal']/scb:payment/conf:paymentDate/conf:unadjustedDate
```

## Validation rules

The source lists these validation checks:

1. Amount is a number.
2. Value-date format is valid.
3. Amount is greater than zero.
4. Entity FMID exists.
5. CFI code exists.
6. Currency exists.
7. Counterparty FMID exists.
8. Entity FMID exists — marked as a duplicate.
9. Cashflow length is 12.

The document does not define error codes, lookup authorities, whether validation is sequential or aggregated, or the meaning of “cashflow length is 12.” The repeated entity FMID check should be treated as an editorial issue until confirmed.

## Withdrawal processing

The documented Withdrawal path is:

1. If status is `SUSPENDED` or `SUSPENDED_MATURED`, return `FAIL`.
2. Query whether the cashflow ID exists. The source states that a nonexistent cashflow should not bypass holding disable and data persistence, but does not precisely define the resulting control flow.
3. If the cashflow exists with status `NETTED` or `SPLIT`, and its resultant cashflow is not post released, return `FILTERED` to the workflow so that unnetting occurs first.
4. If unnetting is not required, disable the holding queue.
5. Persist `RatanStellaMessageEvent`.
6. Construct SCBML from the current message and event.
7. Build the lifecycle request.
8. Run lifecycle processing.

The meanings of `FAIL`, `FILTERED`, “post released,” and the holding-queue behavior for nonexistent cashflows are not defined in this source.

## New-cashflow processing

The documented New path is:

1. If the cashflow is not `PROJECTED`, return `FAIL`.
2. Persist `RatanStellaMessageEvent`.
3. Construct SCBML from the current message and event.
4. Build the lifecycle request.
5. Run lifecycle processing.

## Open design concerns

The source explicitly questions the continued need for:

- The initial conversion to `StellaInfo`.
- The second conversion to `StellaInfo` after creating `RatanStellaMessageEvent`.
- Publication of a common Event.
- The old Withdrawal settlement-date formatting operation.

These are unresolved design questions, not confirmed defects. Removing any conversion or publication step could affect persistence, SCBML construction, or downstream consumers.

## Related wiki material

- [[cashflow-lifecycle-stamping]] describes the proposed reusable enrichment responsibility.
- [[cashflow-precheck-validation]] captures normalization and validation concerns.
- [[entities/lifecycle-service]] is the proposed owner of the API and lifecycle action.
- [[concepts/cashflow-unnetting]] covers the stated Withdrawal prerequisite for `NETTED` and `SPLIT` cashflows.
- [[concepts/lien-stamping-and-re-stamping]] and [[concepts/pending-fixing-flag-processing]] provide domain context for planned attributes.

---
type: source
title: Compatibility Design for Multiple Entities in SSI Stamping
authors: []
year: 2024
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/3733407"
venue: Azure DevOps
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, SSI-stamping, cash-settlement, multi-entity, Nostro]
related: [ratan, tds3, fmrp, ssi-stamping-service, group-management-service, scbml, ssi-plus, ssi-stamping, ccy-pair-based-nostro-selection, multi-entity-cash-settlement-compatibility, group-ready-ccy-pair-enrichment, primary-nostro-fallback, group-enrichment-versus-tds3-lookup-for-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Compatibility Design for Multiple Entities in SSI Stamping

## Summary

This design proposal addresses onboarding Egypt, Saudi Arabia, and Nepal entities to the [[ratan]] strategic cashflow settlement flow. It proposes making `CCY Pair` available to SSI stamping so the process can select the expected Nostro account for eligible local-currency cashflows.

The document is a design proposal rather than evidence of an approved architecture or implemented production behavior. It does not provide implementation evidence, test results, an approved option, or a completed flow chart.

## Scope

The proposed logic must:

- Support Saudi Arabia, Nepal, and Egypt booking entities.
- Support local-currency processing for those entities.
- Select the expected Nostro account using currency-pair information.
- Allow further entities to be added through configuration rather than a hard-coded redesign.
- Avoid database changes in both Group management service and cash settlement SSI stamping service.

## Source Attribute Mapping

| Concepts | Attribute | Source | Meaning | Value | Xpath |
|---|---|---|---|---|---|
| — | CCY Pair | SCBML | Currency pair, new xpath added by Ratan | eg. EGOUSD | TBD |
| — | Entity Fm Id | SCBML | Booking eneity fm id, existing xpath | SA: 400991880 NP: 400007847 EG: 401036553 | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party1']/conf:partyId[@partyIdScheme='http://www.sc.com/coding-scheme/partyId/FMID']` |
| — | Product Taxonomy | SCBML | Product type | `ForeignExchange:Forward` `ForeignExchange:Swap` `ForeignExchange:Spot` | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:productId[@productIdScheme="http://www.fpml.org/coding-scheme/product-taxonomy"]` |
| — | Settlement_Instruction. Account.SCB_Nostro_Account_Type | SSI+ | Settlement means | FXBRREC | `/scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflowSSI/scb:settlementInstruction[scb:partyReference/@href='party2']/scb:settlementMeans/scb:settlementAccountNo` |
| — | Currency_Pair | TDS3 | Trade field: Instrument_Common.Currency_Pair | eg. EGOUSD | — |

## Proposed Enrichment Rule

`CCY Pair` should be enriched by the Group management service after a group is ready only when all of the following conditions hold:

```text
Enrich CCY Pair if:
  booking_entity_fm_id IN (
    400991880,  -- Saudi Arabia
    400007847,  -- Nepal
    401036553   -- Egypt
  )
  AND product_taxonomy IN (
    ForeignExchange:Forward,
    ForeignExchange:Swap,
    ForeignExchange:Spot
  )
  AND grouped_cashflows contain exactly two payment currencies

Otherwise:
  do not enrich CCY Pair
```

The source does not define the final configuration mechanism or the authoritative XPath for `CCY Pair`.

## Proposed SSI Stamping Behavior

For a single Vostro result, if settlement means is `FXBRREC` and `CCY Pair` exists, SSI stamping should query Nostro using `CCY Pair`. Otherwise, the existing CN logic should be followed.

For missing or multiple Vostro results, if `CCY Pair` exists, the proposal is to query primary Nostro using `CCY Pair`. Otherwise, the existing CN logic should be followed.

The fallback when a pair-specific query returns no Nostro is unresolved.

## Implementation Options

### Option 1: Group management enrichment

The Group management service enriches `CCY Pair` before SSI stamping. SSI stamping extracts the value from SCBML, avoiding a runtime [[tds3]] lookup.

This option requires changes to both Group management service and SSI stamping service. It may have better runtime performance, but incomplete manually delivered groups may not receive the enrichment.

### Option 2: TDS3 lookup

The SSI stamping service queries [[tds3]] for `Currency_Pair` instead of waiting for another leg or relying on Group management enrichment.

This option changes only one service, but the additional TDS3 lookup is expected to degrade performance.

## Exceptions and Open Questions

The proposal leaves unresolved:

- Whether a pair-specific Nostro lookup should fall back to a lookup without `CCY Pair`.
- Whether primary Nostro queries should use `CCY Pair`.
- The final `CCY Pair` XPath and SCBML contract.
- Ownership of the enrichment rule and its configuration.
- Handling of incomplete groups.
- The exception and replay contract for missing or invalid `CCY Pair`.
- The authoritative Nostro static-data schema.
- The performance threshold for accepting the TDS3 lookup option.

No database change is expected for either affected service.

## Evidence Assessment

The document provides moderate requirements evidence but low operational and implementation evidence. Option 1 and Option 2 remain alternatives; neither is recorded as approved. The proposal should therefore be used as a design input and not as a statement of current RATAN production behavior.
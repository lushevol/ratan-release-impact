---
type: concept
title: Murex Payment MxML-to-SCBML Transformation
created: 2026-08-24
updated: 2026-08-24
tags: [mxml, mxpayml, scbml, transformation, cashflow, cn-settlement]
related: [murex-211, murex-2-11, ratan, mxpayml, scbml-cashflow-payload, murex-party-fmid-enrichment, murex-payment-pay-receive-derivation, cashflow-business-and-message-versioning, payment-date-versus-value-date]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - MxML mapping to SCBML.md"]
---
# Murex Payment MxML-to-SCBML Transformation

## Definition

This concept describes the proposed conversion of Murex 2.11 Payment MxML cashflow messages into SCBML cashflow payloads for CN settlement.

The intended flow is:

**Murex Payment MxML → enrichment and derivation → RATAN MLS transformation → SCBML cashflow payload**

## Direct mappings

The draft maps:

- `transactionID` to the SCBML trade identifier.
- `flowID` to `cashflowId`, left-padded with zeroes to 12 characters.
- `flowAmount` to payment amount.
- `currency` to payment currency.
- `systemDate` to event date.
- `releaseDate` to the unadjusted payment date.
- `type` to settlement method, with the example `cash` becoming `Cash`.
- `portfolio` to booking-entity trade portfolio name.
- `entityFMID` and `counterpartyFMID` to SCBML party identifiers.

## Enrichment and derivation

The transformation requires data outside the base payment message:

- `TRN_HDR_DBF` for trade confirmation status.
- `ENTITY_DBF` and `COUNTERP_DBF` for booking-entity party identifiers.
- `COUNTERP_DBF` for counterparty party identifiers.
- TDS3 for trade and trader information.
- RATAN MLS for payer/receiver assignment and likely product classification.

## Design risks

The source is not an authoritative runtime contract. Missing samples prevent validation of XML namespaces, XPath expressions, cardinality, and actual values.

The mapping also hard-codes `cashflowVersion=0`, `businessVersion=0`, and report event type `New`, despite lifecycle descriptions that imply version progression and multiple business events.

Product classification is provisional, and the treatment of amendment, withdrawal, and reversal cashflows remains incomplete.
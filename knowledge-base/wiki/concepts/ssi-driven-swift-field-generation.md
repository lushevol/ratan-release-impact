---
type: concept
title: SSI-Driven SWIFT Field Generation
created: 2026-08-23
updated: 2026-08-23
tags: [swift, ssi, static-data, bic, field-mapping]
related: [ratan-swift-message-generation, settlement-integration-static-data-readiness, static-data-readiness, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# SSI-Driven SWIFT Field Generation

SSI-driven SWIFT field generation is the dependency of RATAN message composition on settlement instructions, accounts, entity static data, and cashflow attributes.

## Required inputs

The requirement derives fields from `Cashflow`, `Settlement_Instruction`, `Settlement_Instruction.Account`, entity FMID/BIC records, SCI data, original SWIFT content for withdrawals, and precious-metals strategy/static lookup tables.

Key dependencies include:

- Booking-entity FMID, BIC, branch code, and local currency.
- Correspondent, intermediary, beneficiary bank, beneficiary, and ordering-customer account data.
- SSI ID, settlement method, and `Swift_Routing_Code_Block`.
- Counterparty LEI for qualifying high-value INR payments.
- Precious-metals allocation, availability location, type, quality, and unit values.

## Formatting behavior

The source specifies BIC normalization using `A` in sender BIC location codes and `X` in receiver BIC location codes. It overrides payment date with `Settlement_Instruction.Value_Date` when supplied, renders dates as `YYMMDD`, and replaces decimal points with commas without day-1 rounding.

USD, GBP, EUR, and INR routing rules add or normalize prefixes such as `//FW`, `//SC`, `//RT`, and `//` based on settlement method, SSI availability, and routing-code block.

## Control implication

Because missing fields, static-data inconsistencies, and pseudocode defects can alter payment instructions, the static-data mappings require explicit ownership, validation, and version control. See [[are-the-fmrp-swift-static-data-mappings-validated-and-owned]].
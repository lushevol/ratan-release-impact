---
type: concept
title: SSI Data Quality for SWIFT Generation
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, static-data, swift, data-quality, settlement-instructions]
related: [ssi-plus, fmswg, amh, fmswg-swift-message-validation, static-data-readiness, settlement-integration-static-data-readiness, entity-onboarding-static-data-controls, what-is-the-resolution-status-of-ssi-id-43262410]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# SSI Data Quality for SWIFT Generation

SSI data quality for SWIFT generation is the correctness, completeness, and serializability of standing settlement-instruction data used to construct outbound SWIFT fields.

## Relevant quality dimensions

The documented incidents show that readiness must include:

- valid BIC values, including Vostro and party-routing data;
- available beneficiary account details where mandatory for the message and currency;
- correctly populated custodian-account attributes, including `Has_Cash_Custodian_Account`;
- field-compatible formatting of account, address, and party data, including separators in free-format fields.

## Production consequences

Deficient data resulted in AMH rejections for invalid BICs (`T28008`) and malformed MT202 field `57D` content (`T31`). In one case, Operations used Oscar as a manual fallback while the BIC was corrected in Vostro static data.

A static-data correction, a request for a suppression rule, and a verified preventative validation control are distinct outcomes. The record does not confirm completion of the SSI ID `43262410` correction in ES; see [[what-is-the-resolution-status-of-ssi-id-43262410]].
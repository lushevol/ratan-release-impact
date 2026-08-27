---
type: entity
title: FMSWG
created: 2026-08-23
updated: 2026-08-23
tags: [swift, message-generation, payment-processing, validation]
related: [amh, ssi-plus, fmswg-swift-message-validation, ssi-data-quality-for-swift-generation, swift-network]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# FMSWG

FMSWG is the component identified in the source as generating SWIFT payment and settlement messages from cashflow and static-data inputs.

## Production evidence

The incident register documents that FMSWG:

- raised an error when an MT103 MXN message lacked the mandatory beneficiary account in field `59`;
- did not stop the dummy BIC `SUPPRESSXXX` in MT604 field `87A`;
- generated messages whose validity depended on SSI+ and Vostro static data.

AMH rejected the resulting invalid BIC in the MT604 case with `T28008`. The source does not confirm whether FMSWG was subsequently changed or whether validation covers every applicable SWIFT message type and party field.

## Related controls

[[fmswg-swift-message-validation]] distinguishes preventative FMSWG validation from downstream [[AMH]] rejection. SSI-derived message content is addressed in [[ssi-data-quality-for-swift-generation]].
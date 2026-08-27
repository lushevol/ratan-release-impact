---
type: concept
title: MT604 and MT605 HAU Message Customization
created: 2026-08-23
updated: 2026-08-23
tags: [MT604, MT605, SWIFT, HAU, RATAN, SSI-plus]
related: [ratan, hau, hkcs, ssi-driven-swift-and-mx-field-population, canonical-hau-hkcs-bic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# MT604 and MT605 HAU Message Customization

## Scope

The HKCS requirement calls for RATAN changes affecting MT604 / MT605 messages for the HAU gold flow.

## Required Message Handling

- Use the receiver BIC stated in the requirement, subject to resolution of the conflicting BIC recorded elsewhere.
- Update RATAN mapping to capture Field 26C for the HAU equivalent.
- Set Field 23 to `TRANSFER`.
- Configure SSI+ so Field 72 begins with `/ACC/SCRTRF`.
- Append subsequent SSI+ values from line 2 onward using `//`.

The source sample contains:

```text
:[26C:/HONGKONG/UNALLGOLD995+]
:30:260520
:20:SCBHKSCTS20MAY
:21:SCBHKSCTS20MAY
:23:TRANSFER
:32F:FOZ100,00
:87A:UBSWHKH0XXX
:88A:UBSWHKH0XXX
:[72:/ACC/SCRTRF]
```

## MT692 Boundary

Vivek Aggarwal is asked to advise on possible MT692 changes, but the source does not specify any MT692 field change, applicability rule, or approval. MT692 must therefore remain an open assessment item.

## Evidence Boundary

The source provides requirements, a sample, and a confirmation for Field 23. It does not provide RATAN configuration evidence or message-validation results.
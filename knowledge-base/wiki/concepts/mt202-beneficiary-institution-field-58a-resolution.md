---
type: concept
title: MT202 Beneficiary Institution Field 58a Resolution
created: 2026-08-24
updated: 2026-08-24
tags: [swift, mt202, field-58a, beneficiary-institution, vostro-ssi]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostr--1jab0vj, cms-dependent-swift-message-generation, murex-2-11, ratanone-swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
---
# MT202 Beneficiary Institution Field 58a Resolution

MT202 field 58a is resolved from either the default counterparty or an explicit Beneficiary(58), depending on whether Beneficiary(58) is populated. The source states that field 58 applies only to MT202.

## Selection precedence

1. If Beneficiary(58) is not populated, use counterparty (`ctp`) BIC and long name.
2. If Beneficiary(58) is populated, use that beneficiary's BIC and long name.

## Option selection and line formatting

For either selected party:

- If BIC is blank and Beneficiary A/C is blank, render option `58D` with the party long name.
- If BIC is blank and Beneficiary A/C is populated, render `58D` with Beneficiary A/C on line 1 and the long name on line 2.
- If BIC is populated and Beneficiary A/C is blank, render option `58A` with the BIC.
- If BIC is populated and Beneficiary A/C is populated, render `58A` with Beneficiary A/C on line 1 and the BIC on line 2.

The source says that red-highlighted inputs originate in the Murex GUI, but the referenced screenshot highlights are unavailable as machine-readable evidence. This rule therefore describes functional input provenance only, not confirmed implementation ownership.
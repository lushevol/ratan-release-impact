---
type: query
title: When Is HAU Commodity Flag Treatment Effective?
created: 2026-08-24
updated: 2026-08-24
tags: [hau, commodity, murex-211, ratan, cashflow-enrichment, release-management]
related: [murex-ratan-cashflow-enrichment-flags, precious-metal-currency-classification, murex-ratan-cashflow-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# When Is HAU Commodity Flag Treatment Effective?

Version 2.7 of the DOI is dated 2026-08-03 and states that HAU must be classified as bullion and sent with commodity flag `Y`. This is later than the original H2 2024 framing.

Confirmation is required for:

- whether 2026-08-03 is the correct version date;
- the deployment environment and production effective date of the HAU rule;
- the exact Murex configuration or code change that implements it;
- regression coverage distinguishing HAU from excluded `XAF`, `XOF`, and `XOH`.
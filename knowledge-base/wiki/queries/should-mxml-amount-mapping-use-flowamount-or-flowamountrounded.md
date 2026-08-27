---
type: query
title: Should MxML Amount Mapping Use flowAmount or flowAmountRounded?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, mxml, scbml, cashflow, amount, rounding]
related: [mxml-to-scbml-conversion, murex-to-ratan-cashflow-interface, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# Should MxML Amount Mapping Use flowAmount or flowAmountRounded?

The source conflicts on the payment amount mapping:

- the MxML field reference and mandatory-field list identify `/MxPayML/flowAmountRounded`;
- the detailed conversion rule replaces that path with `/MxPayML/flowAmount`.

The authoritative decision must specify the intended precision, rounding owner, currency-specific scale, downstream settlement and accounting impact, and whether the choice applies to all entities and products.
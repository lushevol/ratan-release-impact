---
type: query
title: Which SCBML XPaths and Settlement Instruction Fields Are Authoritative for 54A, 56A, and 57A?
created: 2026-08-23
updated: 2026-08-23
tags: [scbml, xpath, swift, 54a, 56a, 57a]
related: [scbml-ssi-field-mapping, cover-payment-and-mt103-serial-routing, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# Which SCBML XPaths and Settlement Instruction Fields Are Authoritative for 54A, 56A, and 57A?

The source’s 54A, 56A, and 57A mapping contains field names and XPath expressions that appear malformed, incomplete, or internally inconsistent. Examples include `Settlement_Instruction.ccount.Cash_Custodian_Agent_City`, `Settlement_Instruction.Account..Cash_Local_Agent_Account_Name`, `removeFirstSlas(...)`, and incomplete routing paths.

A validated SCBML schema, logical-model catalogue, and approved mapping specification are required before these mappings can be implemented.
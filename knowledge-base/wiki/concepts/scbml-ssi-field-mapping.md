---
type: concept
title: SCBML SSI Field Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [scbml, ssi, mapping, swift, enrichment]
related: [scbml, ratan-ssi-stamping, cover-payment-and-mt103-serial-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# SCBML SSI Field Mapping

SCBML SSI field mapping is the transformation of selected SSI data into RATAN logical-model fields and SCBML destinations.

The source covers settlement means and account, beneficiary and ordering-customer information, remittance and sender-to-receiver lines, POP Dubai, and routing data for 54A, 56A, and 57A. It also specifies input validation and length restrictions for many GUI fields.

The documented mapping is not yet authoritative implementation material: it includes malformed names, incomplete paths, inconsistent references, and semantically questionable mappings such as country values to city fields. Mapping owners must validate field existence and XPath syntax before development.
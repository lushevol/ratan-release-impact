---
type: query
title: What Are the NID and ND Parent Typology Validation Rules?
tags: [nid, ndirs, parent-trade, mxml, scbml, validation]
related: [nd-parent-trade-metadata, nstp-and-ndirs-rule-routing, ratan-mxg-cashflow-adaptor, scbml, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--30-nds-cashflow-processing-design--yw8sda]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Are the NID and ND Parent Typology Validation Rules?

The design requires NID to be mapped from MXML into SCBML and uses the existence of NID plus `NDIRS` versus non-`NDIRS` typology in rule routing. It does not define validation or provenance semantics.

## Questions to Resolve

- What MXML field and XPath are authoritative for NID?
- Does “NID exists” mean non-null, non-empty, syntactically valid, or successfully persisted?
- How are absent, blank, malformed, or conflicting NID values handled?
- What is the authoritative source for `ND_Parent_Trade_Id` and `ND_Parent_Typology`?
- Are values backfilled for existing cashflows?
- Are these internal fields available to events, APIs, GraphQL, or dynamic-query mappings?
---
type: entity
title: FMRP_H2_ENTITY_DBF
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, fmrp, static-data, entity-eligibility]
related: [fmrp, murex-211, fmrp-payment-eligibility-and-suppression, what-is-the-authoritative-fmrp-entity-eligibility-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# FMRP_H2_ENTITY_DBF

`FMRP_H2_ENTITY_DBF` is the Murex 2.11 static-data table identified by the DOI as storing `M_LABEL` values for entities in scope for Ratan cashflow processing.

The source requires a change ticket for amendments. It does not establish whether every listed row is active, pending, historical, or an alias, and it does not define `M_EBBS` as an eligibility flag despite the table containing both `Y` and `NA` values.

See [[what-is-the-authoritative-fmrp-entity-eligibility-configuration]] for unresolved configuration status, duplicate labels, and alias handling.
---
type: concept
title: Cashflow Stamping Domain Ownership
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, stamping, domain-boundaries, standardization-service, reinstatement]
related: [ssi-stamping-reference-data, cashflow-lifecycle-state-machine-restructuring, cash-settlement-2-0-technical-debt-remediation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement 2.0 Technical Design.md"]
---
# Cashflow Stamping Domain Ownership

A proposed service-boundary change under which Standardization Service becomes the default owner of cashflow stamping.

The proposal states that Standardization Service should stamp all required attributes using surrounding systems. When a cashflow is reinstated, lifecycle-service should call Standardization Service only for the specific attributes requiring stamping.

This is broader than [[ssi-stamping-reference-data]], which concerns SSI reference data. The source does not define the stamped-field inventory, data provenance, conflict resolution, freshness requirements, versioning, fallback behavior, or the canonical owner of the resulting cashflow record. Accordingly, this page records intended ownership rather than an established production contract.
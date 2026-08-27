---
type: query
title: What Is the Authoritative Korea COMP Message Contract and STP Eligibility Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, comp, stp, scbml, mxml, integration-contract]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--86qvyy, korea-direct-comp-driven-stp, murex-korea, mxml, scbml, tds3, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md"]
---
# What Is the Authoritative Korea COMP Message Contract and STP Eligibility Rule?

The source states that Murex Korea sends `COMP` directly to RATAN because TDS3 cannot provide it for Korea cashflows. However, it does not establish a schema-valid, operationally complete interface or define the conditions under which RATAN advances STP.

## Questions to Resolve

- What are the canonical SCBML schema paths, namespaces, and URI attribute values for this message?
- What sender, channel, routing, authentication, and acknowledgment arrangements apply?
- Is `COMP` alone sufficient for STP, or is it combined with cashflow state, static-data checks, settlement eligibility, or other controls?
- Which booking entities and product taxonomies are in scope beyond the illustrative `SCFB_SEOUL` and `CURR|OPT|ASN` values?
- Are package-child trades processed independently, or is package-level completion required?
- What duplicate-message, replay, ordering, audit, and failure-recovery controls apply?

The preserved mapping in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--86qvyy]] should be validated against a canonical SCBML XSD and production-like payloads before implementation.
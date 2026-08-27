---
type: query
title: What Is the Complete LIEN Escalation and Settlement Control After Murex Detection?
created: 2026-08-24
updated: 2026-08-24
tags: [lien, murex-211, ratan, settlement-control, operational-risk]
related: [murex-ratan-lien-control-gap, murex-ratan-cashflow-reconciliation, murex-211, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# What Is the Complete LIEN Escalation and Settlement Control After Murex Detection?

The DOI confirms that LIEN is not transmitted to Ratan and supplies a Murex query to identify candidate cashflows. It does not define how the detection result becomes a settlement control.

Required clarification:

- Who owns execution and review of the LIEN query, and at what frequency?
- What action must Operations take for each detected payment?
- Can Ratan place a hold, reverse processing, or otherwise prevent release after notification?
- What evidence proves that a LIEN-affected cashflow was resolved before settlement?
- How are exceptions escalated across Murex PSS, Ratan PSS, and Settlement Ops?
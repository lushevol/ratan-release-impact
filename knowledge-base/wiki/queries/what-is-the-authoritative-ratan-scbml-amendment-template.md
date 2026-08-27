---
type: query
title: What Is the Authoritative Ratan SCBML Amendment Template?
created: 2026-08-23
updated: 2026-08-23
tags: [query, ratan, scbml, amendment, cashflow]
related: [scbml, cashflowinfo, ratan-scbml-template-rendering, cashflow-amendment-supersession, cashflow-lifecycle-supersession-and-audit-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# What Is the Authoritative Ratan SCBML Amendment Template?

## Question

Does Amendment use a distinct SCBML template, reuse the New template with changed event and version values, or follow another message contract?

## Evidence

The source states that common templates cover New, Amendment, and Withdrawal events, but only New and Withdrawal XML are supplied. No Amendment-specific event value, element-population rule, version transition, or supersession behavior is documented.

## Resolution needed

Identify the authoritative Amendment template and confirm:

- The SCBML business event and process event.
- The relationship between the amended and superseded cashflows.
- Required version and minor-version values.
- Whether post-settlement amendment flags are dynamic.
- Required differences from New and Withdrawal payloads.

This question is directly connected to [[cashflow-amendment-supersession]].

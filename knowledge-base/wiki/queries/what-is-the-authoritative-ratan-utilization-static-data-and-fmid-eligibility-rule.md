---
type: query
title: What Is the Authoritative RATAN Utilization Static Data and FMID Eligibility Rule?
tags: [open-question, RATAN, UTIL, FMID, static-data, settlement-means]
related: [ratan, gross-to-util-settlement-update, settlement-method-update]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# What Is the Authoritative RATAN Utilization Static Data and FMID Eligibility Rule?

The Gross-to-UTIL flow requires backend utilization-static-data checks for eligible entities identified by FMID. The source does not provide the authoritative configuration contract.

## Questions

- What is the FMID lookup key and how is it mapped to an entity?
- Which static-data records make an entity eligible for UTIL settlement?
- Which settlement-means values can be stamped?
- What is the precedence when multiple client static-data records match?
- What happens when FMID data or utilization static data is missing, expired, or contradictory?
- Is settlement means stamped before or after post-settlement processing?
- Is the same static-data rule used for all FX Forward, Spot, and Swap products?

The product-taxonomy restriction is explicit in the source, but the eligibility and configuration details require confirmation before implementation or operational reconciliation.
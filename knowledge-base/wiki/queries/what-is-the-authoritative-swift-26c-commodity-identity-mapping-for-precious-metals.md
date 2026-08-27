---
type: query
title: What Is the Authoritative Swift 26C Commodity-Identity Mapping for Precious Metals?
created: 2026-08-24
updated: 2026-08-24
tags: [swift, precious-metals, field-26c, uber, mapping]
related: [swift-service, precious-metals-cashflow-identification, what-controls-make-swift-generation-safe-without-a-distributed-lock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# What Is the Authoritative Swift 26C Commodity-Identity Mapping for Precious Metals?

Story 14449450 requires Swift Field 26C / commodity identity support for precious metals, but the source's Swift Service section contains no implementation detail.

## Questions to resolve

- Which Swift message types and business flows require Field 26C?
- Which UBER fields populate the commodity identity?
- What formatting, truncation, character-set, and validation rules apply?
- What precedence applies when `Custodian_SCI_FMID`, `Custodian_Name`, `Delivery_Location`, and `Settlement_Method` conflict or are absent?
- Is Field 26C generated only for classified precious-metals cashflows?
- What fallback, rejection, audit, and regression-test behavior is required?

This question concerns field-content mapping. It does not establish or replace concurrency controls described by [[what-controls-make-swift-generation-safe-without-a-distributed-lock]].
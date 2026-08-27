---
type: query
title: What Is the Authoritative NID Grouping Key for NDS Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [nds, nid, auto-netting, ratan, data-model]
related: [nds-netting, ratan-netting-rule-check, ratan]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# What Is the Authoritative NID Grouping Key for NDS Netting?

The source states that NDS Non-Deliverable Interest Rate Swap cashflows must be auto-netted based on `NID`, but does not define the identifier.

## Questions to resolve

- What does `NID` represent and what is its canonical format?
- Which upstream system provides it and which RATAN field persists it?
- Is it the sole netting grouping key or one condition among additional eligibility criteria?
- How are missing, changed, reversed, or unmatched NID values handled?

Resolution requires authoritative data-model, interface, or production configuration evidence.
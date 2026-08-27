---
type: query
title: What Is the Authoritative Cross-Border Debit Message Format Selection Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [cross-border-debit, swift, iso-20022, mt202, mt103, pacs-009]
related: [cross-border-debit-message-mapping, cross-border-debit-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# What Is the Authoritative Cross-Border Debit Message Format Selection Rule?

The UAT source shows receive-side FIN MT202 messages, USD pay-side MT103/MT202 cover messages, and EUR/GBP pay-side CBPR+ `pacs.009.001.08` messages.

It does not determine whether format selection is controlled by direction, currency, booking entity, corridor, BIC routing, SWIFT migration state, or configurable channel rules.

## Evidence Needed

- An approved message-selection specification or interface contract.
- Configuration showing the applicable FIN and MX routing conditions.
- Test evidence for the same direction and currency across alternative corridors or booking entities.
- Confirmation whether `pacs.009.001.08` replaces, supplements, or represents the normal MT103/MT202 mapping.
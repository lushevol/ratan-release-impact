---
type: query
title: What Does Vostro SI Field 57 Control in Cross-Border Debit Routing?
created: 2026-08-23
updated: 2026-08-23
tags: [vostro, ssi, field-57, swift, routing, cross-border-debit]
related: [vostro-field-57-routing-derivation, cross-border-debit-settlement, ssi-swift-field-enrichment]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# What Does Vostro SI Field 57 Control in Cross-Border Debit Routing?

The UAT source repeatedly states that receive-side “Tag 1 and Tag 2” are selected from Vostro SI field 57, but it does not define the referred fields or the transformation rule.

## Questions

- Which FIN header blocks, BICs, or internal routing attributes are meant by “Tag 1 and Tag 2”?
- Is field 57 used only for receive-side `CROSSDEBIT` MT202 messages?
- What precedence applies when Vostro field 57 conflicts with Nostro 53B/BIC data?
- Are BIC normalization and branch-code derivation performed before message construction?

An authoritative SSI-to-message mapping and relevant configuration precedence are required.
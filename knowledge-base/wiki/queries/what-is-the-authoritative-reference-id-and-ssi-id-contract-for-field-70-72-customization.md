---
type: query
title: What Is the Authoritative Reference ID and SSI ID Contract for Field 70/72 Customization?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, reference-id, swift, field-70, field-72, maker-checker, open-question]
related: [field-70-72-customization-and-reference-id, ssi-selection-provenance-and-ad-hoc-classification, fmo-post-trade-portal, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1rgkk4g]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/SSI selection not treat as adhoc SSI - UAT.md"]
---
# What Is the Authoritative Reference ID and SSI ID Contract for Field 70/72 Customization?

The UAT states that, after the Reference ID change, field-70/72 customization should clear SSI ID and populate Reference ID. However, all formal result columns are blank and scenarios 3, 6, 9, 12, 16, 17, and 18 require retesting.

## Questions to resolve

- Is Reference ID substitution implemented and deployed for all field-70/72 customization flows?
- Which identifier appears to makers and checkers when there was no initially auto-stamped SSI?
- In the auto-stamped case, does Reference ID deliberately identify the original stamped SSI rather than a maker-selected SSI?
- What audit relationship connects displayed settlement details, field-70/72 edits, original auto-stamped SSI, and a subsequently selected SSI?
- Does reverting a field-70/72 value preserve Reference ID and the customization marker in persisted data as well as in the UI?

Resolution requires completed UAT results and the authoritative UI, API, or persistence specification.
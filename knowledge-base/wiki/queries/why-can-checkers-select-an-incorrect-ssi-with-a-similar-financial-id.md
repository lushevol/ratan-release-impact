---
type: query
title: Why Can Checkers Select an Incorrect SSI with a Similar Financial ID?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, financial-id, checker, validation, ui, data-quality, open-question]
related: [fmo-post-trade-portal, ssi-selection-provenance-and-ad-hoc-classification, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1rgkk4g]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/SSI selection not treat as adhoc SSI - UAT.md"]
---
# Why Can Checkers Select an Incorrect SSI with a Similar Financial ID?

Scenario 3 reports that a checker selected SSI ID `00021922` instead of `40150418` because both records had similar Financial IDs.

## Questions to resolve

- Which attributes are used to search, rank, and identify available SSI records?
- Is Financial ID intended to be unique, or must users distinguish records with additional attributes?
- Should the selection UI prominently expose SSI ID and other disambiguating details?
- Did the scenario represent a test-data ambiguity, user error, or a product defect?
- Should approval validate that the checker-selected SSI matches the intended or previously stamped SSI when fields 70/72 are customized?

This issue affects operational correctness and the auditability of SSI provenance.
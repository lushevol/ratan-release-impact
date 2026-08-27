---
type: query
title: What Is the Authoritative Inter-Entity Netting Eligibility Rule?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, eligibility, business-rules, open-question]
related: [inter-entity-netting, netting-eligibility-rules, auto-netting-datetime-calculation, nostro-static-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting - UAT.md"]
---

# What Is the Authoritative Inter-Entity Netting Eligibility Rule?

The UAT demonstrates that non-USD cashflows, USD cashflows above USD 100,000, and cashflows for an out-of-scope entity were excluded from the tested inter-entity netting scenarios. It also demonstrates matching through exact FMID, backend static mapping, and BIC-based conditions.

The authoritative production rule remains unresolved. The following points require confirmation:

- Whether the USD 100,000 threshold is inclusive or exclusive.
- Whether the threshold and currency restriction apply to every supported product.
- The confirmed entity scope.
- The precedence between FMID matching, backend static mapping, and BIC conditions.
- Whether a missing [[concepts/nostro-static-validation]] blocks only release or also affects netting eligibility.
- The timeout or processing criterion that converts an unmatched `Pending auto netting` cashflow to gross.

The evidence and limitations are summarized in [[concepts/inter-entity-netting]] and the related sources/26-auto-netting-page-md-files--165-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-se--30xx67.

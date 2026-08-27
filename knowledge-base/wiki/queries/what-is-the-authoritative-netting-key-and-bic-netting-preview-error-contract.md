---
type: query
title: What Is the Authoritative Netting Key and BIC Netting Preview Error Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, eligibility, validation, user-interface]
related: [netting-key-eligibility, beneficiary-bic-netting, bic-net-eligibility-flag]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/03 Beneficiary BIC Netting.md"]
---
# What Is the Authoritative Netting Key and BIC Netting Preview Error Contract?

The source identifies different Booking Entity, Currency, and Value Date as incompatible netting-key values. It expects the popup `Cashflow Netting Preview Can not Netting` and notes that no UI warning like CCIL is present.

## Questions

- Are Booking Entity, Currency, and Value Date the complete set of netting-key dimensions?
- Is Counterparty BIC part of the netting key, a manual-rule condition, or both?
- Are settlement method, payment direction, amount sign, legal entity, and value-date calendar eligibility dimensions?
- Is the preview popup blocking, and what is its canonical wording and error code?
- Does the UI identify incompatible cashflows or fields, and how does its behaviour differ from CCIL?

Until clarified, [[netting-key-eligibility]] records only the three explicit source-backed incompatibilities.
---
type: concept
title: Nostro Static-Data Governance
tags: [nostro, static-data, governance, swift, ssi, reconciliation]
related: [nostro-static-data, ssi-plus, static-data-readiness, swift-message-reconciliation, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# Nostro Static-Data Governance

Nostro static-data governance covers the maintenance, ownership, effective dating, and validation of Nostro accounts, agent BICs, routing prefixes, and related SWIFT field values.

The review assigns several differences to Nostro-file or SSI+ activity rather than RATAN code. Examples include 886 MT202 field 57A/58A line-one differences, 951 MT210 field 52A line-one differences, and 844 MT202 field 72 line-one differences.

## Required control evidence

A complete remediation record should identify the affected static-data record, owner, effective date, before-and-after values, replay result, and approval. “Nostro file updated” or “SSI data needs to be checked” does not establish that the generated messages were corrected in production.

This governance distinction is central to [[concepts/swift-message-reconciliation]] and [[concepts/static-data-readiness]].
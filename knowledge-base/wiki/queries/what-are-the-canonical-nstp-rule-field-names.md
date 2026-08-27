---
type: query
title: What Are the Canonical NSTP Rule Field Names?
created: 2026-08-23
updated: 2026-08-23
tags: [nstp, data-model, field-names, open-question]
related: [nstp-rule-routing, murex-2-11, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data.md"]
---
# What Are the Canonical NSTP Rule Field Names?

The requirement uses both `Data_Flow.Data_Source_System` and `Cashflow.Data_Flow__Data_Source_System` in NSTP expressions. It is unclear whether these are two distinct model fields, an export-format difference, or an error.

The same source contains NSTP rows with blank conditions, including Bad Business Day, High Value Payment, GSAM Client, Pending Affirmation, Corporate Client, and Back Value Date. Those rows may represent system-defined predicates or incomplete configuration exports.

## Required Resolution

Confirm the canonical field names, expression grammar, and representation of system-defined conditions before implementing or validating these rules.
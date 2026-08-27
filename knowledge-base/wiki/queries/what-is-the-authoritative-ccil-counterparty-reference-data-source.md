---
type: query
title: What Is the Authoritative CCIL Counterparty Reference-Data Source?
created: 2026-08-24
updated: 2026-08-24
tags: [CCIL, reference-data, static-data, MXG]
related: [ccil-cashflow-identification, murex-adaptor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# What Is the Authoritative CCIL Counterparty Reference-Data Source?

The design is unclear about the authoritative source for CCIL counterparty qualification. A proposed new static-data table is struck through, while the Murex adaptor is still expected to query a static data database in MXG.

Questions to resolve:

- What system owns the CCIL counterparty list?
- What is the schema and refresh process?
- What does “if hint” mean in the lookup instruction?
- Is counterparty `400021949` a permanent exception or a temporary rule?
- What should happen when the lookup is unavailable, stale, or ambiguous?

This query should be resolved before implementation because the lookup directly controls settlement-method tagging and downstream netting eligibility.
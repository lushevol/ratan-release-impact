---
type: query
title: What Is the Authoritative Murex Batch File Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [murex, ratan, batch-files, interface-contract, cashflows]
related: [murex, ratan, murex-batch-cashflow-ingestion, what-is-the-canonical-cash-settlement-exception-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Murex batch processing.md"]
---
# What Is the Authoritative Murex Batch File Contract?

The available design states a two-hourly snapshot-and-base-file pattern and a complete file after upload, but it does not define a consumable file contract.

## Questions to Resolve

- What is the exact filename convention, including the encoded cashflow count used for `BatchCountReconError`?
- What file format, encoding, required fields, delimiters, and validation rules apply?
- What are the respective contents and precedence rules for snapshot and base files?
- Is a complete file mandatory before RATAN reads either file, and does one complete file cover both files?
- What file-set identifier, business date, sequence number, and time zone apply?
- Is `SNTR` the only accepted status, and what does that status mean?
- Is 45,000 a hard producer limit, a RATAN acceptance limit, or an expected maximum?
- How should RATAN handle missing, late, duplicate, out-of-order, or partially uploaded files?

The source is insufficient to resolve these questions. Any confirmed contract should update [[murex-batch-cashflow-ingestion]] and inform the exception state machine tracked by [[what-is-the-canonical-cash-settlement-exception-state-machine]].
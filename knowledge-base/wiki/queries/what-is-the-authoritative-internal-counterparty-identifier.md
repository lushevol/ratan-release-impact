---
type: query
title: What Is the Authoritative Internal Counterparty Identifier?
tags: [cash-settlement, reference-data, internal-counterparty, Murex, STP]
related: [internal-counterparty-exception-bypass, inter-entity-cashflow-stp, murex-2-11]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# What Is the Authoritative Internal Counterparty Identifier?

The requirement depends on an internal-counterparty identifier, but does not name its field, data source, or governing system.

## Questions

- What is the exact identifier or reference-data attribute?
- Which system owns and maintains it?
- What values indicate that a counterparty is internal?
- How is the identifier propagated through Murex, RATAN, and downstream settlement processing?
- What is the lifecycle and approval process for changes?
- How are missing, stale, ambiguous, or conflicting values handled?
- Does eligibility require both the identifier and an MX cashflow classification?

An authoritative answer is required before the bypass mechanism can be implemented or tested safely.
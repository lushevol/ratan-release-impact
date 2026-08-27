---
type: query
title: What Is the Canonical Murex Stack Flow and LMS Source Value?
created: 2026-08-24
updated: 2026-08-24
tags: [Murex, FMRP, LMS, RATAN, data-contract, open-question]
related: [source-stack-flow-name-propagation, lms-source-value-proposals, murex-211, murex-ratan-cashflow-message-contract, lms, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# What Is the Canonical Murex Stack Flow and LMS Source Value?

## Question

Is the canonical Murex stack-flow and LMS source value `FMRPMUREX`, `MUREX`, `FMRP`, or another value?

## Evidence

The current-process table shows a null Murex stack value and `FMRP` as the LMS source. Proposal 1 introduces `FMRPMUREX`, and its integration tests expect new and withdrawal LMS messages with source value `FMRPMUREX`.

However, the Proposal 1 table contains `FMRPSTELLA FMRPMUREX` in the LMS source column without a delimiter or selection rule. Proposal 2 uses `MUREX` as the stack value and retains `FMRP` as the LMS source, but Proposal 2 was rejected.

## Required Resolution

Confirm:

- The exact stack-flow value.
- The exact LMS source value.
- Whether `FMRPSTELLA FMRPMUREX` is a documentation error or an allowed value set.
- Whether the value applies identically to direct, withdrawal, and netting-resultant messages.
- Whether `MUREX` is obsolete, rejected, or still accepted as a legacy value.

Until resolved, test evidence supports `FMRPMUREX` as the expected canonical LMS value, but the specification remains internally ambiguous.
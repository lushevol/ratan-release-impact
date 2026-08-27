---
type: query
title: What Is COMP Status and How Does It Drive STP in the Korea Migration?
created: 2026-08-23
updated: 2026-08-23
tags: [comp, stp, korea, migration, open-question]
related: [comp-status-driven-stp, korea-cash-settlement-migration, trade-validation-gated-group-processing, trade-validation-group-advancement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md"]
---
# What Is COMP Status and How Does It Drive STP in the Korea Migration?

## Question

What does `COMP` represent, which system is authoritative for it, and how does it drive STP in the Korea Murex-to-RATAN migration?

## Required Evidence

Review the linked **COMP status to drive STP process** design and determine:

- The status definition and lifecycle.
- The assigning and consuming systems.
- The processing level: trade, cashflow, group, or major version.
- Withdrawal and exception behavior.
- Precedence relative to `is_trade_validated`, cashflow state, group completion, and manual STP.
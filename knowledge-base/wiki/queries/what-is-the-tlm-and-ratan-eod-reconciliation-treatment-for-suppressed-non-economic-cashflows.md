---
type: query
title: What Is the TLM and Ratan EOD Reconciliation Treatment for Suppressed Non-Economic Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [tlm, reconciliation, ratan-eod, cashflows, amendments]
related: [cashflow-lineage-and-operational-visibility, how-should-projected-original-cashflows-be-represented-after-non-economic-amendment, tlm, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# What Is the TLM and Ratan EOD Reconciliation Treatment for Suppressed Non-Economic Cashflows?

The functional requirement states that status treatment for suppressed replacement cashflows must be confirmed for Ratan EOD and [[tlm]] reconciliation with Karthik and Feye.

Although the document reports no accounting or reconciliation impact following discussion with Aspire and TLM, that statement is not final while this status requirement remains open.

## Questions

- Which cashflow versions are included in Ratan EOD reconciliation feeds and controls?
- Are suppressed replacements represented as absent, linked, or status-bearing records?
- How are source-system Settled replacements reconciled to original operational cashflows?
- What exceptions identify failed or delayed status propagation to Stella?
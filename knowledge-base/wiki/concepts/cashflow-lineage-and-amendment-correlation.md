---
type: concept
title: Cashflow Lineage and Amendment Correlation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, lineage, amendment, withdrawal, trade-ID, Auto DVP]
related: [auto-dvp-ebbs, dvp-exception-lifecycle, ratan, murex, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# Cashflow Lineage and Amendment Correlation

Cashflow lineage and amendment correlation describe how Ratan associates withdrawn or amended cashflows with an existing Receive/Pay DVP relationship.

## Amendment behavior specified by the UAT cases

The apparent rule is:

```text
Trade ID unchanged:
    replacement cashflow retains the original DVP relationship
    and may inherit Auto DVP treatment.

Trade ID changed:
    replacement cashflow is treated as a new relationship
    and does not inherit automatic DVP closure.
```

For an unchanged Pay trade ID, the original Pay cashflow becomes `Cancelled`, the replacement remains `Waiting`, and its DVP exception auto-closes after the Receive-side RTA notification.

For an unchanged Receive trade ID, the original Receive cashflow becomes `Cancelled`, the replacement settles, and the linked Pay-side DVP exception auto-closes.

When the trade ID changes, the replacement Pay cashflow retains its DVP exception. A replacement Receive cashflow can settle, but the original Pay-side exception remains open.

## Withdrawal behavior

The withdrawal scenarios describe the original Receive or Pay cashflow first reaching `Settled`, followed by a withdrawal version returning to `Waiting`. The linked Pay-side exception remains open. The source does not clarify whether the withdrawal version is the same record, a child/version record, or a newly generated cashflow.

## Implementation gap

The source does not identify the authoritative lineage fields or matching algorithm beyond trade ID continuity and the existing Murex/Stella linkage keys.
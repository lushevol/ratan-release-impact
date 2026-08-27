---
type: concept
title: CCIL Cashflow Identification
created: 2026-08-24
updated: 2026-08-24
tags: [CCIL, cashflow-classification, Murex, settlement-method]
related: [ccil, murex-adaptor, ccil-netting, settlement-method-driven-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# CCIL Cashflow Identification

CCIL cashflow identification is the proposed rule-based classification of incoming cashflows that qualify for CCIL netting.

## Classification Predicate

The source specifies all of the following conditions:

```text
ccy=INO
family=IRS
group=IRD
fmid==4
and (counterparty in static data list or counterparty is 400021949)
```

The Murex adaptor is expected to query the static data database in MXG for the counterparty condition. If the lookup produces the required indication, the adaptor sets the settlement method to `CCIL` using the `scbextn:settlementMethod` extension.

## Boundaries

This predicate is a design requirement, not validated implementation evidence. The source does not establish whether `INO` is the intended currency code, whether counterparty `400021949` is permanent, or what happens when reference data is unavailable, stale, or ambiguous.
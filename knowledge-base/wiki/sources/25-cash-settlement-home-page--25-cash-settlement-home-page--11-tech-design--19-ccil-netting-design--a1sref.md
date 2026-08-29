---
type: source
title: CCIL Netting Design
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Tech Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, CCIL, netting, technical-design]
related: [ccil, ccil-cashflow-identification, ccil-netting, settlement-method-driven-netting, cash-settlement-platform, ratanone-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md"]
---
# CCIL Netting Design

## Summary

This technical design proposes changes across the Murex adaptor, rule service, netting service, and frontend to support CCIL-specific cashflow identification and netting. It is a design-level requirements document; it does not establish implementation status, production deployment, test results, or approval.

The design separates CCIL netting from normal cash netting through a settlement-method classification. Qualifying incoming cashflows receive the `CCIL` settlement-method value, are marked for straight-through processing and netting eligibility, and are handled through a dedicated CCIL netting controller and preview flow. The resultant cashflow is changed from `CCIL` to `CASH`.

## Structured Requirements

The source table is preserved below, including its original field names, values, wording, and struck-through content.

```markdown
| Module | Function | Description |
| --- | --- | --- |
| ~~static data service ~~ | ~~new static data table~~ | ~~refer to [CCIL Netting - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/CCIL+Netting)~~ |
| murex adaptor | identify the CCIL cashflow | - identify CCIL( **ccy=INO & family=IRS & group =IRD & fmid==4 and (counterparty in static data list or counterparty is ****400021949** )) - query static data DB in mxg, if hint, then set tag <scbextn:settlementMethod settlementMethodScheme="http://www.sc.com/coding-scheme/settlementMethod">CCIL</scbextn:settlementMethod> |
| rule service | add new NSTP rule for settlement method | - Settlement_Method = "CCIL" - if matched then Waiting+IsNettingEligible |
| netting service | netting review netting | - netting review change. allow different counterparties for (settlemenet method =CCIL) - netting change. netting resultant cashflow settlement method change to CASH Principle: 1. New controller for CCIL netting and preview 2. Reuse on the service layer for netting function without building new netting logic |
| frontend | add new logic model for Settlement_Method | - filter add settlement method value, drop-down (CASH / CCIL Netting) - identify normal netting and & CCIL netting - for CCIL netting, settlement method = CCIL & with the same entity/value date/currency and status is waiting+pending netting - normal netting can not be netted with CCIL netting cashflow |
```

## Proposed Processing Flow

1. The Murex adaptor evaluates the currency, product family, group, FMID, and counterparty conditions.
2. A qualifying cashflow is tagged with settlement method `CCIL`.
3. The rule service matches `Settlement_Method = "CCIL"` and applies `Waiting+IsNettingEligible`.
4. The frontend exposes separate `CASH` and `CCIL Netting` filtering and selection paths.
5. CCIL netting review permits different counterparties, subject to the same entity, value date, currency, and status constraints described by the design.
6. The netting service creates a resultant cashflow with settlement method `CASH`.

## Important Boundaries and Unresolved Points

- The source uses `ccy=INO`; the authoritative currency code is not confirmed.
- The meaning of “if hint” is undefined.
- The source refers both to a static-data table, which is struck through, and to a static data database in MXG.
- `Waiting+IsNettingEligible` and `waiting+pending netting` may refer to different fields or states.
- The design does not specify whether backend validation independently prevents mixing normal and CCIL netting.
- Cross-counterparty netting controls, audit requirements, and provenance retention are not defined.
- The proposal recommends reusing existing service-layer netting logic rather than creating a second netting engine, but it does not identify the extension points or APIs.

## Related Wiki Pages

- [[ccil]]
- [[ccil-cashflow-identification]]
- [[ccil-netting]]
- [[settlement-method-driven-netting]]
- cash settlement platform
- ratanone rule service
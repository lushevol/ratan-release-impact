---
type: concept
title: Inter-Entity Auto-Netting
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, inter-entity, ratan, settlement, usd]
related: [inter-entity-cashflow-pre-match, counterparty-mapping-static, auto-netting-rule-check, netting-resultant-cashflow, netting-un-net-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Inter-Entity Auto-Netting

Inter-entity auto-netting is the proposed ratan one process for reducing nostro charges by netting qualifying SCB internal-entity cashflows that would otherwise settle gross.

It is a controlled bilateral rule, not generic netting of all internal flows. Phase 1 is limited to USD, configured booking-entity/counterparty relationships, new cashflow events, non-LOANIQ source trades, and USD-equivalent amounts at or below 100,000.

## Processing model

A cashflow first passes the configured eligibility rule and then the [[inter-entity-cashflow-pre-match]] checks. Matching pairs produce linked, opposite-direction netting resultants under a new netting type. The resultant payment type is `Inter Entity Netting`.

The resultant netting key is:

```text
booking entity FMID + VD + Currency + Counterparty mapped value
```

Unmatched cashflows, or cashflows without a counterpart available for netting, proceed as gross flows.

## Scope constraints

- IRS aggregation resultants are in scope.
- The USD-equivalent field is calculated after VD-5 materialization and refreshed on reinstate.
- LOANIQ-sourced trades are excluded.
- Precious-metal currencies are not covered in Phase 1.
- `SCB CN CHO*CHO` ↔ `SCB HONGKON*HKG` is identified as the initial-enable pair, although the broader rule lists additional relationships.

Correctness depends on [[counterparty-mapping-static]], particularly where different FMIDs represent the same internal entity.
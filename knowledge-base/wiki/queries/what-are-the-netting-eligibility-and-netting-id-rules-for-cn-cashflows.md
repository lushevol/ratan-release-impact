---
type: query
title: What Are the Netting Eligibility and Netting ID Rules for CN Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, netting, netting-id, cn, open-question]
related: [cashflow-netting-and-un-netting-state-transitions, ratan, stella, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--26-cn-settlement-demo-se--10ylmrb]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md"]
---
# What Are the Netting Eligibility and Netting ID Rules for CN Cashflows?

Sprint 17 expects cashflows from Murex 2.11 spot trades and mocked Stella spot cashflows to be netted from the RATAN Cashflow Blotter. Components and resultant must share a Netting ID, and the resultant amount must equal the sum of component amounts.

The document does not state why the mixed-source cashflows are eligible to belong to one netting set.

## Questions to Resolve

- Which currency, value date, counterparty, account, SSI, entity, and direction conditions govern eligibility?
- Are component amounts summed algebraically, and what signed-amount convention applies?
- How is a Netting ID generated, made unique, retained, and associated with a resultant?
- Are netting and un-netting atomic operations?
- How are partial failures, concurrent changes, amendments, and withdrawals handled after netting?

## Evidence Needed

Obtain the RATAN netting design, Netting ID data model, operational procedure, and execution evidence for the netting and un-netting cases in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--26-cn-settlement-demo-se--10ylmrb]].
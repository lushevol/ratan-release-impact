---
type: query
title: What Is the Authoritative Meaning and Lifecycle of Cashflow Splitting ID?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, split, correlation, data-model, open-question]
related: [cashflow-splitting-id-correlation, cashflow-split-and-unsplit, cashflow-withdrawal-and-new, what-is-the-authoritative-post-split-withdrawal-amendment-and-netting-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Split design -delete.md"]
---
# What Is the Authoritative Meaning and Lifecycle of Cashflow Splitting ID?

A deprecated migration proposes `cashflow__splitting_id` on `cash_netting_service.t_cashflow`, uniquely constrained with `cashflow__cashflow_id`. The document does not define the field’s business meaning or lifecycle.

## Questions

- Does `cashflow__splitting_id` identify a split operation, parent cashflow, component group, or another business correlation key?
- Does the default empty string (`''`) formally mean “unsplit”? Is it also permitted for legacy records or records whose split identity is unknown?
- Which events populate, retain, replace, or clear this value: split, unsplit, amendment, withdrawal, reversal, and netting?
- Is the composite unique index on `(cashflow__cashflow_id, cashflow__splitting_id)` deployed and still authoritative?
- What is the intended relationship between this field and current [[cashflow-split-and-unsplit]] and post-split lifecycle processing?

## Available evidence

[[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--20-sp--n5cwwm]] provides only the proposed schema migration. Its split, unsplit, and withdrawal sections are empty, so it cannot resolve these questions.
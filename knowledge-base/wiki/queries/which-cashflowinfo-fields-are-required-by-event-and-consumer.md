---
type: query
title: Which CashFlowInfo Fields Are Required by Event and Consumer?
created: 2026-08-23
updated: 2026-08-23
tags: [query, cashflowinfo, scbml, data-contract, settlement]
related: [cashflowinfo, scbml, ratan-scbml-template-rendering, cashflow-detail-field-projection, cashflow-accounting-stamping, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/SCBML Template.md"]
---
# Which CashFlowInfo Fields Are Required by Event and Consumer?

## Question

Which `CashFlowInfo` attributes are mandatory, optional, or prohibited for each event and downstream consumer?

## Evidence

The bean mapping covers cashflow lifecycle, payment, data-flow, entity, instrument, portfolio, settlement-instruction, and trade domains. The supplied templates populate only subsets of those fields. New and Withdrawal also differ in their element coverage, while several values are hard-coded.

## Resolution needed

Produce an authoritative matrix for New, Amendment, and Withdrawal covering:

- Required bean properties.
- Required XML elements.
- Hard-coded versus dynamic values.
- Null and empty-value behavior.
- Consumer-specific requirements for settlement instructions, parties, EBBS, GL, SWIFT, audit, and Trade Lake data.
- Schema and business validation rules.

Until resolved, the complete `CashFlowInfo` mapping should be treated as an available projection contract rather than a guarantee that every event populates every field.

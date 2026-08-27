---
type: query
title: Which SWIFT Message Fields Are Stamped for SCB Receive Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [scb, receive-cashflow, swift, message-mapping, open-question]
related: [scb-receive-cashflow-swift-stamping, outbound-property-propagation-to-swift-mt-mx, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--v8owqc]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Swift process.md"]
---
# Which SWIFT Message Fields Are Stamped for SCB Receive Cashflows?

The unavailable source body does not identify any SWIFT message type, MT/MX variant, tag, field, account identifier, or value-propagation rule.

## Evidence needed

Retrieve `Swift process.md`, including diagrams, tables, examples, and appendices, to determine:

- the applicable SWIFT message types;
- fields or tags populated from receive-cashflow data;
- source-of-truth services and data attributes;
- validation, fallback, refresh, and override rules; and
- expected behavior for exceptions or suppression.

This question should not be resolved by applying rules from [[outbound-property-propagation-to-swift-mt-mx]] unless the source explicitly establishes that relationship.
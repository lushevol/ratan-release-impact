---
type: query
title: What Authorization and Masking Controls Govern cashflowsNew SSI Fields?
created: 2026-08-24
updated: 2026-08-24
tags: [security, authorization, masking, settlement-instructions, graphql]
related: [cashflowsnew, cash-settlement-query-service-graphql-read-model, cashflow-standing-settlement-instructions, trade-standing-settlement-instructions, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# What Authorization and Masking Controls Govern cashflowsNew SSI Fields?

## Question

What authorization, field-level entitlement, masking, audit, retention, and minimum-necessary-projection controls apply when `cashflowsNew` requests settlement-instruction data?

## Evidence

The documented projection includes account numbers, BICs, beneficiary and intermediary details, addresses, correspondent and ordering-customer data, remittance information, and sender-to-receiver information. All sample `Settlement_Instruction` values are null, so the source does not demonstrate populated-data behavior.

## Required Resolution

Confirm:

- Which user roles and service identities may request SSI and account fields.
- Whether individual sensitive fields are masked, omitted, or available only through separate scopes.
- Whether access is logged and audited.
- Whether clients must use approved field-selection templates.
- Which retention, export, and downstream handling requirements apply.
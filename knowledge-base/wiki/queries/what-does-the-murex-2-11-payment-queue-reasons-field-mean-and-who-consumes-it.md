---
type: query
title: What Does the Murex 2.11 Payment Queue Reasons Field Mean and Who Consumes It?
tags: [murex, payment-queue, reasons-field, cn-settlement, open-question]
related: [cn-settlement, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--32-cn-settlement-ops-week--o3lm83]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/Open Items.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Does the Murex 2.11 Payment Queue Reasons Field Mean and Who Consumes It?

## Question

What does the `Reasons` field in Murex 2.11 payment queues represent, which values can it contain, and which downstream systems or operational processes consume it?

## Evidence

The tracker records an Open action for Yi Li to check the `Reasons` field from Murex 2.11 payment queues. It supplies no field definition, example values, interface schema, or downstream consumer information.

## Needed to resolve

- Murex 2.11 field definition, data type, and permitted values.
- Conditions under which Murex populates the field.
- Whether the value affects CN Settlement eligibility, routing, exception management, or status.
- Interface mappings and downstream consumers.
- Treatment of absent, multiple, or unrecognized reasons.

## Related pages

- [[cn-settlement]]
- [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--32-cn-settlement-ops-week--o3lm83]]
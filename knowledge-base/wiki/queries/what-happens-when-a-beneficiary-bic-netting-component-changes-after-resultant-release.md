---
type: query
title: What Happens When a Beneficiary BIC Netting Component Changes After Resultant Release?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, beneficiary-bic, un-netting, release, cashflow-lifecycle]
related: [beneficiary-bic-netting, netting-resultant-attribute-inheritance, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md"]
---
# What Happens When a Beneficiary BIC Netting Component Changes After Resultant Release?

## Question

What reversal, exception, accounting, payment, and audit process applies when a Beneficiary BIC netting component is amended or withdrawn after its resultant has been released?

## Evidence

The stated requirement is limited to automatic un-netting where a component is amended or withdrawn and the resultant has **not** been released.

No behavior is specified for a released resultant.

## Required decision outputs

- Authoritative definition of “released”.
- Whether post-release amendment or withdrawal is blocked, exception-routed, or processed.
- Reversal and accounting requirements.
- Payment and messaging implications.
- Component and resultant status restoration rules.
- Lineage, versioning, and audit requirements.
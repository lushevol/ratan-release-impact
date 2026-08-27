---
type: comparison
title: Beneficiary BIC Netting Versus Bilateral Manual Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, operational-controls, segregation]
related: [beneficiary-bic-netting, paystp-net, ratan, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# Beneficiary BIC Netting Versus Bilateral Manual Netting

The requirement distinguishes Beneficiary BIC netting from bilateral manual netting and assigns BIC netting higher priority.

| Dimension | Beneficiary BIC netting | Bilateral manual netting |
|---|---|---|
| Primary grouping basis | Beneficiary BIC plus settlement and classification attributes | Bilateral or counterparty-specific manual grouping |
| Initiating interface | Ratan Cashflow Blotter with `Ben BIC Netting` action | Existing bilateral manual-netting workflow |
| Eligibility control | BIC-net flag, `Pending Netting`, entity, Beneficiary BIC, value date, currency, and potentially expanded classification fields | Not defined in this source |
| Decision authority | Operations user | Manual operations process |
| Priority | Higher priority | Lower priority than BIC netting |
| Result | New netting resultant cashflow | Not defined in this source |
| Conflict risk | Cashflows may otherwise be selected in multiple queues | Could compete with BIC-netting selection |

## Required segregation

The source identifies a BAU risk in which users manually net cashflows through both bilateral and BIC-based queues. This can cause mismatched settlement amounts, suppression of cashflows, and manual payment through OSCAR.

The target design therefore needs technical enforcement, not only a procedural priority statement. Possible mechanisms include eligibility exclusion, queue reservation, selection locks, or concurrency checks, but the source does not choose among them.
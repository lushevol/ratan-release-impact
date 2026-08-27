---
type: concept
title: BIC-Net Eligibility Flag
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, eligibility, BIC]
related: [beneficiary-bic-netting, paystp-net, sci, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting.md"]
---
# BIC-Net Eligibility Flag

The BIC-net eligibility flag identifies whether a cashflow may participate in Beneficiary BIC netting.

## Field mapping

The source defines the following logical and physical representations:

```text
BIC_NET flag Logical Model: Entity.Counterparty_SCI_BIC_Net_Flag
BIC_NET flag Physical Model: /scb:SCBML/scb:payload/scb:cashflowPayload/scb:party[@id='party2']/conf:bicNetFlag
```

The eligible value is:

```text
BIC_Net = 'Y'
```

The Beneficiary BIC is the BIC obtained from [[entities/sci]] where `mediumUsage='MXR'`.

## State transition

When a cashflow satisfies the eligibility conditions, it should be updated to:

```text
Cashflow.Cashflow_Sub_State_Type = Pending Netting
```

During execution, Ratan must validate both:

```text
BIC_Net == 'Y'
Cashflow.Cashflow_Sub_State_Type == 'Pending Netting'
```

This creates a distinction between eligibility classification and execution-time validation.

## Eligibility context

The source specifies `Entity = LONDON`. It also shows `Payment Date >= Today` struck through, so the final role of payment date is unresolved.
---
type: concept
title: Cashflow Netting and Auto Un-Netting
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, netting, un-netting, Ratan, resultant-cashflow]
related: [ratan, fmrp-cashflow-responsibility-split, cashflow-lifecycle-state-model, cashflow-version-concurrency-control, cashflow-suppression-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# Cashflow Netting and Auto Un-Netting

The target design moves netting from Stella to Ratan.

## Netting flow

Ratan identifies component cashflows, assigns a common `Netting ID`, changes component statuses to `Netted`, and creates a resultant cashflow. For the representative example:

```text
C101 (100) + C102 (200) = C103 (300)
Netting ID: N001
```

The component cashflows are reported to Stella as `Netted`. The Ratan-owned resultant cashflow proceeds through `Queued`, `Pending`, `Validated`, `Released`, and `Settled`.

## Auto un-netting

When an amendment affects a netted cashflow, Ratan is expected to reverse the netting relationship. The illustrative flow includes:

- Withdrawal of the resultant cashflow.
- Suppression or withdrawal of an affected component.
- Re-queuing of remaining or replacement cashflows.
- Reprocessing of netting after the amendment.

The source identifies a concurrency risk where a netting submission can be rejected after Stella advances a cashflow version. It asks whether netting can be transactional and automatically reversed but does not provide a final atomicity or retry contract.
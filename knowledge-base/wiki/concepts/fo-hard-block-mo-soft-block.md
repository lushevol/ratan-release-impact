---
type: concept
title: FO Hard Block and MO Soft Block
created: 2026-08-24
updated: 2026-08-24
tags: [front-office, middle-office, trade-events, controls, payment-release]
related: [cashflow-event-control, released-settled-amendment-control, nstp-rule-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# FO Hard Block and MO Soft Block

The CN Drop 2 UAT scenarios repeatedly specify different controls for Front Office (FO) and Middle Office (MO) after payment release:

- FO should receive a hard block.
- MO should receive a soft block.

This expectation is applied to post-release amendments and cancellations or withdrawals across single, BTB3/5/7, inter-entity, and intra-entity scenarios. It is also tested for novation after payment release.

## Evidence Boundary

The source does not specify which component enforces the controls, whether a MO soft block can be overridden, or whether the distinction applies outside the listed UAT scenarios. These details remain implementation and policy questions. The expected behavior should therefore be kept separate from confirmed production behavior.

The control boundary is related to [[concepts/cashflow-event-control]] and [[concepts/released-settled-amendment-control]].
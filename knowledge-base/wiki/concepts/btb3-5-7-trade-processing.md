---
type: concept
title: BTB3/5/7 Trade Processing
created: 2026-08-24
updated: 2026-08-24
tags: [btb3, btb5, btb7, multi-leg-trades, trade-events, settlement]
related: [cashflow-event-control, fo-hard-block-mo-soft-block, cashflow-netting-and-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# BTB3/5/7 Trade Processing

BTB3/5/7 scenarios cover package or multi-leg trade structures in booking, backdated booking, amendment, cancellation or withdrawal, and settlement processing.

The source identifies package-level and leg-level trade references, including BTB package IDs. It also tests these structures across different payment-release states and relationship classifications such as inter-entity and intra-entity trading.

## Control Relevance

Post-release amendments and cancellations for BTB3/5/7 trades are expected to apply the FO hard-block and MO soft-block distinction. The catalogue also examines how multi-leg structures interact with netting and rebook behavior.

The source does not define a canonical BTB package data model or prove that all package scenarios were executed successfully.
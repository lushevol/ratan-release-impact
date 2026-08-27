---
type: stakeholder
title: Operations
created: 2026-08-24
updated: 2026-08-24
tags: [operations, cashflow, exception-management, ratan]
related: [ratan, non-economic-cashflow-amendment-handling, trade-validation-cashflow-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/UAT test cases - Murex 2.11 booking.md"]
---
# Operations

Operations is the exception-processing role identified in the UAT scenarios. In non-economic and complex amendment sequences, Operations manually pushes selected cashflows from RATAN’s Group Blotter to the Cashflow Blotter when validation does not release them automatically.

Scenarios 11–13 show this intervention for predecessor or reversal payments while the latest replacement payment may be released automatically. The source does not define the required operator, approval model, audit evidence, service-level target, or whether manual processing is intended as a permanent production control.
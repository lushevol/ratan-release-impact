---
type: concept
title: Straight-Through Processing
created: 2026-08-22
updated: 2026-08-22
tags: [stp, automation, cash-settlement, warnings, controls, exceptions]
related: [cash-settlement, ratan, 51358-ratan-cash-settlement-group-management-service, cash-settlement-re-platforming, settlement-suppression, standard-settlement-instructions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# Straight-Through Processing

Straight-through processing, or STP, is automated transaction processing without routine manual intervention, as stated in the existing version. The newly generated version describes STP more conditionally: processing proceeds without manual intervention when required data and controls are satisfied.

## Backlog Requirements

The 2025 FMRP backlog contains both STP-enabling and STP-breaking requirements:

- **ADO 6473045** proposes consuming Confirmation Match status for Cashflow STP on the near leg of an FX Swap.
- **ADO 6473009** proposes STP for SCB counterparty cashflows.
- **ADO 6473025** proposes breaking STP for settlement using Blade Comments, subject to BLADE prioritization.

These backlog requirements show, according to the newly generated version, that STP is conditional rather than universally preferred. The backlog seeks automation where control inputs support it and deliberate intervention where specified comments or exceptions require review.

The source does not define the complete STP eligibility rules, the exact meaning of Blade Comments, or the manual workflow triggered when STP is broken.

## Warning Behavior in CHG1016055

[[chg1016055]] changes specified manual-STP cases from a technical warning to a soft warning for New and Amendment scenarios.

The behavior spans [[51358-ratan-cash-settlement-group-management-service]] and the `51358-mfe-cashflow-blotter` frontend. PIT includes a check for Business Event, Business Version, and soft-warning behavior, but its textual result is not populated.

A soft warning is non-blocking, so this change may affect operator workflow and risk signaling. The source states the behavior but does not document alternatives, rationale, or formal decision ownership.
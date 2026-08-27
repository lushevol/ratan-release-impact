---
type: entity
title: Opics
created: 2026-08-22
updated: 2026-08-23
tags: [payment-operations, legacy-system, cash-settlement, payments, manual-split, derivatives, cn-settlement]
related: [mx211-cash-settlement-decommission, payment-release-exception-orchestration, payment-and-cashflow-suppression-governance, murex-2-11, murex-2-11-cn-derivative-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Opics

## Operational use

The Settlement Touchpoints source describes Opics as a current operational channel for manual payments when an agent bank is not configured in MX2.11. It also associates Opics with manual GLTE postings used to clear breaks in commodity, CDS premium, and insufficient-funds workflows.

That source proposes moving selected manual-payment capability to [[ratan]], but does not establish that Opics can be retired or identify the approved transition scope.

## Manual splitting of derivative payments

The CN Settlement Ops session identifies Opics as the system used for manual splitting of Murex 2.11 derivative payments when requested by a client.

According to the session notes, these manual splits do not retain a linkage between the original payment and the split payments. This differs from the Razor auto-split reference behavior, in which parent-payment linkage is carried in SWIFT Field 72.
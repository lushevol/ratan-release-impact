---
type: entity
title: FMSRE
created: 2026-08-22
updated: 2026-08-23
tags: ["swift", "settlement-operations", "exception-status", "payment-release", "reversal", "cash-settlement", "mx211", "message-processing", "fmrp", "integration", "fmsre", "operations", "monitoring", "cashflow", "netting", "downstream-system", "cashflow-release"]
related: ["fm-swift-gateway", "scpay", "ratan-cashflow-blotter", "settlement-message-routing", "fmswift-gateway", "pending-reversal-acknowledgement", "ratan-one", "ratan-swift-message-generation", "swift-status-lifecycle-and-reconciliation", "fmswiftgateway", "scstar", "razor", "ratan", "cashflow-netting-and-un-netting-state-transitions", "cashflow-withdrawal-and-new", "cashflow-lifecycle-state-model"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# FMSRE

FMSRE is a downstream, SWIFT-related component referenced in cash-settlement workflows. The FMRP SWIFT-generation requirement identifies it as the message-processing component for MX-related acknowledgement and status handling. A deprecated Cashflow Events Control Draft 1 also references FMSRE as an operational monitoring context.

The Ratan and Stella cashflow integration source describes FMSRE as the downstream system to which Ratan sends generated Swift messages when a cashflow reaches `Released`. That source places FMSRE at the `Validated → Released` boundary. It does not define an interface contract, acknowledgement behavior, or ownership of the subsequent `Released → Settled` transition.

## Role in FMRP SWIFT generation

According to the FMRP SWIFT-generation requirement:

- RATAN-generated MX messages are sent to FMSRE after MX generation.
- FMSRE technical ACK maps to `Pending FMSRE Disp`.
- FMSRE business ACK maps to `Pending Manual Rel`.
- FMSRE business NACK maps to `FMSRE Error`.
- Razor-generated MT messages for LOANIQ, Egypt, Nepal, and Saudi Arabia are queried from FMSRE using tag 20.

These message-processing and acknowledgement mappings are defined by the FMRP SWIFT-generation source. The Ratan and Stella cashflow integration source separately describes the cashflow boundary at which Ratan sends generated Swift messages; it does not establish the acknowledgement behavior or interface contract.

## Manual-settlement eligibility

According to the FMRP Manual Settle eligibility rule, a `RELEASED` cashflow may be manually settled when its SWIFT status is `Check in FMSRE`, `FMSRE Deleted`, `FMSRE Error`, or `Pending FMSRE Disp`, among other listed error and dispatch statuses.

The Functional Requirement source describing manual-settlement eligibility does not define FMSRE ownership, interfaces, or remediation behavior.

## Operational caveat

`FMSRE Deleted` and `Manual Delete` map the RATAN cashflow to `SETTLED`, while the FMRP SWIFT-generation source expects payment to be completed manually through Oscar or AMH. Mapping a cashflow to `SETTLED` therefore does not demonstrate downstream payment completion.

The integration source likewise does not assign FMSRE ownership of the `Released → Settled` transition.

## MX2.11 decommission workflow

According to the MX2.11 Decomm Cash Settlement Business Workflow, FMSRE is the planned Day 1 payment and reversal processing path for workflow cases previously associated with FMSWIFT Gateway.

The `Pending in FMSWIFT Gateway` exception is expected to use FMSRE for Day 1. The workflow leaves open whether RATAN will initiate release or delete actions directly, or whether users will perform those actions in FMSRE.

The MX2.11 workflow source does not establish FMSRE ownership, interface behavior, or production enablement.

## Deprecated operational monitoring guidance

According to the deprecated Cashflow Events Control Draft 1, when a netting resultant such as `N101` is outside Ratan during withdrawal processing, Operations should check the resultant status in FMSRE. The draft further lists manual release and `MT192`/`MT202` actions as possible operational steps.

These actions are historical design guidance, not confirmed current requirements. The draft does not define FMSRE ownership, status semantics, integration behavior, or the conditions that make a cashflow “out of Ratan.”

## Source boundaries and limitations

The sources describe different aspects of FMSRE and do not establish a single complete interface or ownership model:

- The Ratan and Stella cashflow integration source places FMSRE at the `Validated → Released` boundary, where Ratan sends generated Swift messages to FMSRE, but does not define an interface contract, acknowledgement behavior, or ownership of the `Released → Settled` transition.
- The FMRP SWIFT-generation source defines message-processing, acknowledgement, status, and manual-payment expectations, but does not establish FMSRE ownership of those processes.
- The Functional Requirement source describing manual-settlement eligibility does not define FMSRE ownership, interfaces, or remediation behavior.
- The MX2.11 workflow source does not establish FMSRE ownership, interface behavior, or production enablement.
- The deprecated Cashflow Events Control Draft 1 provides historical operational guidance and does not define FMSRE ownership, status semantics, integration behavior, or the conditions that make a cashflow “out of Ratan.”

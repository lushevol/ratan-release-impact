---
type: entity
title: AMH
created: 2026-08-22
updated: 2026-08-23
tags: ["payment-handling", "manual-operations", "suppression", "payment-operations", "failed-settlement", "rma", "cash-settlement", "payment-hub", "integration", "swift", "settlement", "messaging", "validation", "production", "exception-processing", "downstream-system", "settlement-messages", "fmsgw", "payment-messaging", "message-processing", "amh", "manual-processing", "mt192", "ndf", "withdrawals"]
related: ["swift-versus-cashflow-suppression", "ratan-cashflow-blotter", "cashflow-fail-and-reinstatement", "cashflow-suppression-vs-payment-suppression", "ratan", "mx211-cash-settlement-decommission", "payment-release-exception-orchestration", "fmswiftgateway", "enisis", "scpay", "swift-status-lifecycle-and-reconciliation", "fmswg", "ssi-plus", "fmswg-swift-message-validation", "swift-network", "oscar", "cashflow-suppression", "fmsgw", "fmsgw-inbound-message-routing", "ratan-fmsgw-amh-settlement-message-routing", "scb-kenya-b", "fmsgw-manual-validation-queues", "zambia-scb-zambia-lus-gbs", "manual-entity-settlement-enablement", "ndf", "cashflow-suppression-rules", "ratan-cashflow-acknowledgement-and-release-processing"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/Settlement Touchpoints.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/004 KENYA SCB KENYA B NBO(GBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control/CN Drop 2 UAT - Settlements Scenarios - 2024.md"]
---
# AMH

AMH is referenced as an operational and payment system for settlement, payment remediation, manual-payment processing, and RMA-related exceptions. The FMRP SWIFT-generation requirement specifically names AMH as the downstream payment hub. Separately, the production incident register names AMH as a downstream messaging and validation component.

A separate CN Drop 2 UAT source identifies AMH as the tool used for manual drafting of `MT192` messages in an NDF withdrawal scenario. That source does not define AMH ownership, architecture, or broader processing responsibilities.

## Settlement-message forwarding in UAT evidence

The manual-entity UAT sources describe settlement messages being forwarded to AMH by [[fmsgw]]. These sources cover different test scopes and confirm outbound routing at the stated scope; they do not, in general, establish AMH-side processing or end-to-end settlement completion.

### Bahrain SCB UAT

The Bahrain SCB UAT source identifies AMH as the downstream recipient of settlement messages forwarded by [[fmsgw]]. Its scenarios state that the following are sent to AMH:

- `MT103/202COV`
- `MT202`
- `MT192/292`
- Approved high-value payment messages

This source confirms expected forwarding at a high level but does not include AMH-side processing records.

### Qatar SCB Doha UAT

The Qatar SCB Doha UAT source records successful forwarding to AMH of settlement messages originating from [[ratan]]. The recorded cases include:

- `MT103`
- `MT202COV`
- `MT202`
- `MT192`
- `MT292`
- Approved high-value `MT103` and `MT202` cases

This source provides no details about AMH processing, acceptance criteria, failure responses, or delivery-confirmation semantics.

### Kenya / SCB Kenya B / NBO (GBS) UAT

The Kenya UAT source documents AMH as the downstream message-processing destination in the tested Kenya / SCB Kenya B / NBO (GBS) flows.

For the tested configuration, [[fmsgw]] forwarded standard inbound settlement messages to AMH. High-value messages were forwarded only after approval in the High Value Payment Queue. Cancel-trade scenarios also state that `MT202` or `MT103` messages were sent to AMH.

The Kenya UAT source does not define AMH's full name, interface contract, acceptance criteria, or behavior after receipt.

### Zambia / SCB Zambia LUS (GBS) UAT

The Zambia manual-entity UAT source identifies AMH as the downstream recipient of settlement messages sent by [[fmsgw]].

The source records [[fmsgw]] sending the following to AMH:

- `MT103/202COV`
- `MT202`
- `MT192/292`
- Approved high-value `MT103`/`MT202` messages

This source does not define AMH's expansion, ownership, processing behavior, message-acceptance criteria, or confirmation contract. The recorded evidence therefore confirms [[fmsgw]]'s intended outbound routing only, not end-to-end processing within AMH.

## Manual drafting for NDF withdrawals

The CN Drop 2 UAT settlement-scenarios source identifies AMH as the tool for manually drafting `MT192` messages in an NDF withdrawal scenario.

Following an amended NDF cashflow sequence, the scenario requires manual drafting of the `N1` and `C1` messages after `C2` withdrawal is `SWIFT_SUPPRESSED` for accounting generation.

## Payment remediation and manual-payment processing

The Cashflow Blotter functional-requirement source names AMH / [[oscar]] as an external handling route when a payment becomes required after the value date and a prior SWIFT suppression cannot be reversed in the FMRP Cashflow Blotter.

The NSTP workflow source assigns post-value-date payment remediation for incorrectly reversed Payment Suppression cases to AMH or [[oscar]].

The Cashflow Swift Suppression requirement likewise names AMH as an external handling path, together with [[oscar]], when payment is required after value date for a Payment Suppression case.

The FMRP SWIFT-generation requirement also names AMH as a manual-payment channel after some FMSGW or FMSRE deletion and termination outcomes.

The Settlement Touchpoints source notes that payments may be stuck in AMH.

## FMRP SWIFT-generation status handling

In the FMSGW and ENISIS mappings described by the FMRP SWIFT-generation requirement:

- An AMH ACK is intended to move a RATAN cashflow to `SETTLED`.
- An AMH NACK leaves the cashflow `RELEASED` with `AMH Error`.

Because AMH is also named as a manual-payment channel in some deletion and termination outcomes, the FMRP SWIFT-generation source states that an AMH-related status does not by itself provide a single, unambiguous meaning of payment completion.

## RMA-related exceptions and validation

The NSTP workflow source identifies AMH as the source of RMA data for the No RMA exception. Following RMA setup or amendment, users may manually update settlement instructions.

The Settlement Touchpoints source proposes an AMH integration to support RMA-status checks.

## Recorded message-validation outcomes

The production incident register records the following AMH rejection outcomes:

- MT605 field `87A` containing invalid BIC `BLICGB2LXXX` was rejected with error `T28008`.
- MT604 field `87A` containing placeholder BIC `SUPPRESSXXX` was rejected with error `T28008`.
- MT202 field `57D` containing malformed separator or delimiter content was rejected with error `T31`.

These examples demonstrate downstream detection of specific invalid message content. They do not define AMH's complete validation rule set or prove that upstream [[FMSWG]] validation is comprehensive.

## Interfaces, ownership, and unresolved scope

The UAT sources provide routing evidence but leave AMH's detailed responsibilities and interfaces unresolved:

- The Bahrain UAT source does not define the expansion of the AMH acronym, its processing responsibilities, its interface, or its response contract.
- The Qatar UAT source records forwarding outcomes but does not define AMH processing, acceptance criteria, failure responses, or delivery-confirmation semantics.
- The Kenya UAT source does not define AMH's full name, interface contract, acceptance criteria, or behavior after receipt.
- The Zambia UAT source does not define AMH's expansion, ownership, processing behavior, message-acceptance criteria, or confirmation contract.
- The CN Drop 2 UAT settlement-scenarios source does not define AMH ownership, architecture, or broader processing responsibilities.
- The Cashflow Swift Suppression requirement does not define AMH's expansion, ownership, interfaces, or the division of responsibilities between AMH and [[oscar]].
- Neither the Cashflow Blotter functional-requirement source nor the NSTP workflow source defines AMH's processing interface or operational ownership boundary in detail.

The Settlement Touchpoints source identifies the following as unresolved:

- API prioritization
- The support model
- Remediation actions
- The boundary between AMH, SSI+, and [[ratan]]
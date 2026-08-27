---
type: entity
title: SCPAY
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
tags: ["scpay", "ssi", "validation", "egypt", "malaysia", "payment-processing", "swift", "settlement", "integration", "transaction-banking", "fx-utilization", "payment-instruction", "downstream-system", "uat"]
related: ["ssi-stamping", "standard-settlement-instructions", "fmswiftgateway", "amh", "swift-status-lifecycle-and-reconciliation", "fxu", "ratan", "utilization-request-idempotency", "scpay-settlement-routing", "why-were-nigeria-cases-30-and-31-settled-but-not-received-in-amh", "what-was-the-final-outcome-of-bahrain-case-24-in-scpay"]
updated: 2026-08-23
---
# SCPAY

## Role in SSI validation

According to the 2024 changes source, SCPAY is the market or system context for SSI validation in the SG/IN/MY/CN Day 2 scope.

The source calls for SCPAY market SSI validation for Egypt and Malaysia. It also requires maintaining a hard-coded booking-entities list.

This requirement is distinct from the unresolved Omgeo Alert SSI item and should not be treated as evidence that SCPAY is the authoritative SSI provider.

## Role in FMRP SWIFT generation

According to the FMRP SWIFT-generation source, SCPAY is a downstream payment-processing system named in the FMSGW route of the FMRP SWIFT-generation requirement.

The high-level cashflow/SWIFT event mapping refers to `SCPAY Processed` as a settled UI outcome, while the detailed FMSGW mapping uses `Released by AMH` for the downstream ACK state. The source does not establish whether these labels represent the same business event or different processing stages.

See [[are-scpay-scstar-and-amh-statuses-equivalent-across-swift-integration-routes]].

## Role in FX utilization processing

According to the FXU–RATAN analysis source, SCPAY, also written ScPay, is the Transaction Banking system from which Operations retrieve deals and apply client payment instructions before utilization is submitted through [[fxu]] to [[ratan]].

The proposed request lineage uses SCPAY as the maker ID, with an empty checker ID. Example accounting records use source payment references such as `SCPAY001` through `SCPAY004`.

The source does not define the authoritative identity, authorization, or request-correlation contract between SCPAY, FXU, and RATAN.

## Manual-entity UAT routing

According to the manual-entity UAT testing source, SCPAY is a downstream payment-processing destination for in-country or self-routed manual-entity UAT messages.

The source records Bahrain case 24 as routed to SCPAY but pending. Nigeria cases 32–33 were routed to SCPAY and subsequently requested for reinitiation. Neither set of observations establishes terminal downstream completion.

See [[scpay-settlement-routing]].
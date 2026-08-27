---
type: entity
title: Oscar
created: 2026-08-22
updated: 2026-08-25
tags: [manual-operations, payment-handling, settlement-accounting, payment-operations, accounting, failed-settlement, suppression, manual-settlement, recall, operational-tool, cash-settlement, payment, manual-payment, exception-handling, settlement, duplicate-prevention, oscar, manual-booking, operations, payment-processing, manual-fallback, ratan, murex-kr]
related: [swift-versus-cashflow-suppression, ratan-cashflow-blotter, cashflow-suppression-vs-payment-suppression, cashflow-fail-and-reinstatement, ratan, cn-trade-migration, early-settled-cashflow-migration-handling, settlement-ops, beneficiary-bic-netting, murex-211, murex-ratan-cashflow-reconciliation, razor, cashflow-reinstatement-and-replay, cash-settlement-exception-handling, ratan-murex-kr-mt-to-mx-interface, ratan-operational-resilience-plans, enisis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md", "Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Beneficiary BIC Netting/Beneficiary BIC Netting Demo.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md", "RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# OSCAR

OSCAR is also styled as Oscar. Across the cited sources, it is described as an external handling route, operations system, and operational/accounting system for manual payment, post-value-date settlement remediation, recall, and manual booking outside [[RATAN]]. The CN Trade Migration settlement requirement characterizes OSCAR as a manual settlement and recall tool or process.

The Exception Handling source additionally describes OSCAR as an operations system used as a manual-booking fallback for Razor NACK failures.

## Razor NACK exception handling

The Exception Handling source states that when a Razor NACK places a cashflow in `FAILED`, OPS can either:

- Use `ReInstate` to process the cashflow again.
- Manually book the cashflow in OSCAR.

That source does not define OSCAR booking controls, audit evidence, or reconciliation requirements.

## Cashflow Blotter source

The Cashflow Blotter source names AMH / Oscar for a SWIFT-suppressed cashflow requiring payment after value date. For a fully suppressed cashflow requiring both payment and settlement accounting after value date, it names Oscar.

That source does not define Oscar’s process or ownership.

## NSTP Workflow source

The NSTP Workflow source states that if Cashflow Suppression was applied incorrectly and payment plus settlement accounting are required after value date, the case must be handled through Oscar. It also names Oscar as one of the systems for:

- Payment remediation after an incorrect Payment Suppression.
- Remediation of failed settlements identified after value date.

The source does not establish whether Oscar performs the remediation directly or orchestrates downstream payment and accounting actions.

## CN Trade Migration settlement source

The CN Trade Migration settlement requirement states that, under the preferred approach, an individual request to recall a historically settled amount and resettle an amended amount may require:

1. Recalling the original amount in Oscar.
2. Releasing the new amount through [[RATAN]].

Under the suppression alternative, that source states that Oscar is also required for:

- Gross recall.
- Manual incremental settlement.

## Murex 2.11 DOI source

The Murex 2.11 DOI identifies Oscar as the manual-payment fallback for urgent cashflows affected by outbound MQ incidents.

Its use is conditional. Operations must first establish that:

- The payment is absent from [[RATAN]].
- Making a manual payment does not create a duplication risk.

The DOI does not define the proof, approval, or audit evidence required for this decision.

## Beneficiary BIC Netting Demo source

The Beneficiary BIC Netting Demo source references OSCAR as an external route for arranging manual payment when cashflows are suppressed and handled outside [[murex]] in the reported Beneficiary BIC netting operating scenario.

This source does not establish OSCAR’s ownership, technical integration, payment lifecycle role, controls, or whether its use is current production behavior.

## Role in the Murex KR interface

The `Ratan and Murex KR 50216.md` source identifies OSCAR as a manual fallback destination when automated processing cannot resume a payment or when replay does not resolve a [[RATAN]] or [[enisis]] issue. Korea FMO may draft the payment in OSCAR instead of manually drafting the MX message in [[enisis]].

That source does not define OSCAR’s system ownership, approval controls, message format, reconciliation requirements, or relationship to [[enisis]].
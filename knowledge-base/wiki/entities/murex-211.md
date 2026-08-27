---
type: entity
title: Murex 2.11
created: 2026-08-22
updated: 2026-08-23
tags: [murex, trading-platform, trade-lifecycle, payments, murex-211, trading-system, cash-settlement, vostro-ssi]
related: [murex-payment-trade-lineage-identifiers, murex-to-ratan-cashflow-integration, how-should-ratan-correlate-murex-counterparty-assignment-cashflows, ratan, ssi-plus, tds3, cfi-code-mapping-for-murex-vostro-ssi, murex-211-vostro-ssi-data-quality]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Murex Counterparty Assignment - Original Trade id Changed.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex 2.11 Vostro SSI.md"]
---
# Murex 2.11

Murex 2.11 is the upstream trade-processing platform referenced in the RATAN cashflow integration. It is also the source system and trade population associated with the Vostro SSIs described in the functional requirement.

## Role in settlement processing

Existing Murex 2.11 Vostro SSIs are intended to be reused by [[ratan]] rather than replaced with a separate RATAN-specific population.

Murex 2.11 cashflows require RATAN to perform CFI-code stamping before SSI lookup. The CFI code historically stamped on Murex 2.11 trades in [[tds3]] provides the basis for RATAN’s retained two-character value. The source does not specify whether this prefix is used for direct lookup, intermediate classification, or fallback processing.

## Trade lineage and Counterparty Assignment

The issue-tracking source reports that a Murex 2.11 Counterparty Assignment market event changes a trade’s Original Trade Id. This reported behaviour is significant because RATAN relies on Original Trade Id to group cashflows associated with a booking.

The source does not provide event payloads, field paths, or a confirmed replacement-lineage mechanism. Event-specific handling remains under investigation in [[how-should-ratan-correlate-murex-counterparty-assignment-cashflows]].

## Vostro SSI data concerns

Murex 2.11 Vostro SSI records have reported gaps in branch information, Settlement Account, and Settlement Means. Settlement Account and Settlement Means are blank for 98.8% of the reviewed population. See [[murex-211-vostro-ssi-data-quality]].

## Related integration scope

- [[murex-payment-trade-lineage-identifiers]] documents identifiers used to preserve payment and trade lineage.
- [[murex-to-ratan-cashflow-integration]] covers the Murex-to-RATAN cashflow integration dependency.
- [[ssi-plus]] and [[cfi-code-mapping-for-murex-vostro-ssi]] provide related settlement and CFI-code context.
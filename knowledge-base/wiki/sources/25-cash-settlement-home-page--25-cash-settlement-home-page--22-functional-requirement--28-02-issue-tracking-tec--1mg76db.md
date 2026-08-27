---
type: source
title: Murex Counterparty Assignment - Original Trade id Changed
authors: []
year: 2026
url: ""
venue: Internal functional requirement issue tracking and technical debt
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, counterparty-assignment, trade-lineage, technical-debt, issue-tracking]
related: [murex-211, murex-payment-trade-lineage-identifiers, murex-to-ratan-cashflow-integration, murex-ratan-reversal-and-replacement-lifecycle, how-should-ratan-correlate-murex-counterparty-assignment-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Murex Counterparty Assignment - Original Trade id Changed.md"]
---
# Murex Counterparty Assignment - Original Trade id Changed

## Summary

This issue record states that RATAN groups cashflows belonging to the same booking using the Murex Original Trade Id. The documented design agreement is that this identifier remains unchanged throughout the trade lifecycle, including booking and market events.

The source reports that the Murex 2.11 special market event **Counterparty Assignment** changes the Original Trade Id. This violates the grouping assumption used by RATAN and creates an unresolved trade-lineage and cashflow-correlation issue.

No approved alternative correlation key, target grouping outcome, or remediation approach is specified. The source should therefore be treated as an issue statement rather than an implementable requirement.

## Reported Normal-Flow Example

The source provides the following example for new booking and Trade C&R processing. The table is preserved verbatim because its identifier categories and final row appear internally inconsistent.

| **Murex Event** | **Original Trade Id** | **Trade ID** | **Payments** | **Payment Snapshot** | **RATAN Process** |
| --- | --- | --- | --- | --- | --- |
| New booking | 99434373 | 99434373 | 112877123 | '112877123' | 112877123 is the only payment under the original trade 112877123 |
|  |  |  |  |  |  |
| Trade C&R | 99434373 | 99706143 | 113352621 | '112877123','**113352621**' | **113352621 **is the additional payment under the original trade 112877123 |
|  |  |  |  |  |  |
| Trade C&R | 99434373 | 99713131 | 113363859 | 112877123','113352621','**113363859**','**113369339**' | **113363859 **and **113369339 **are the additional payments under the original trade 112877123 |
| 113369339 | 112877123','113352621','**113363859**','**113369339**' |  |  |  |  |

## Counterparty Assignment Exception

The source identifies Counterparty Assignment in [[murex-211]] as an exception to Original Trade Id stability, but supplies no concrete before-and-after event data.

| **Murex Event** | **Original Trade Id** | **Trade ID** | **Payments** | **Payment Snapshot** | **RATAN Process** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Implications

- [[murex-payment-trade-lineage-identifiers]] cannot treat Original Trade Id as universally immutable when Counterparty Assignment is in scope.
- [[murex-to-ratan-cashflow-integration]] depends on upstream Murex lineage-field behaviour for booking-level cashflow grouping.
- The source does not establish that Counterparty Assignment follows the reversal or replacement behaviour documented in [[murex-ratan-reversal-and-replacement-lifecycle]].
- The required correlation mechanism and RATAN processing outcome remain open in [[how-should-ratan-correlate-murex-counterparty-assignment-cashflows]].

## Evidence Limitations

The exception-case table is empty. The source does not identify the replacement Original Trade Id, relevant Murex message fields, a durable assignment identifier, the observed RATAN failure mode, or the intended operational resolution.

The normal-flow example also mixes Original Trade Id and payment identifiers in its RATAN-process descriptions. It supports the stated design assumption, but does not establish canonical field mappings or identifier values.
---
type: source
title: Non Economic amendment(FMRP) Cashflows
authors: []
year: 2023
url: ""
venue: Internal functional requirement
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, ratan, stella, cashflows, non-economic-amendments, settlement]
related: [non-economic-cashflow-amendment-handling, six-attribute-cashflow-equivalence, cashflow-lineage-and-operational-visibility, how-should-projected-original-cashflows-be-represented-after-non-economic-amendment, what-is-the-authoritative-matching-algorithm-for-non-economic-cashflow-amendments, what-is-the-tlm-and-ratan-eod-reconciliation-treatment-for-suppressed-non-economic-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# Non Economic amendment(FMRP) Cashflows

This functional requirement defines Ratan handling for non-economic trade amendments initiated in Stella. Stella creates a new trade version, withdraws prior-version cashflows, and emits replacement cashflows even where settlement economics have not changed.

Ratan must preserve the original cashflows as the operational settlement record when replacement cashflows meet the defined equivalence test. Replacement records remain necessary for lineage, status synchronization to Stella, and confirmation-version bridging; they are not deleted.

## Classification and handling requirements

A withdrawn cashflow and a newly created replacement cashflow are non-economic equivalents only when all of these attributes match:

1. Booking Entity (FMID)
2. Counterparty (FMID)
3. Payment Currency
4. Payment Amount
5. Payment Value Date
6. Receive/Pay Direction

The assessment is at cashflow level. In a partial amendment, matching legs remain represented by their original operational cashflows, while changed replacement legs are treated as new cashflows and undergo Suppression, Netting, NSTP, and exception processing.

For fully equivalent replacements, Ratan must:

- retain backend mappings such as `C1 → C3 → C5`;
- keep the original cashflows visible to Settlement Ops;
- suppress replacements from the cashflow blotter and downstream publication;
- synchronize applicable Released, Netted, or Settled statuses to the latest active Stella cashflow; and
- map confirmation of the latest trade version back to original operational cashflows.

## Initial trade booking

| Product | Trade Date | Trade ID | Major Version | Cashflow ID | Cashflow Event | Cashflow Version | Booking Entity | Counterparty | Pay/Receive | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | 2023-08-15 | T1 | V1 | C1 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V1 | C2 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |

## First fully non-economic amendment

| Product | Trade Date | Trade ID | Major Version | Cashflow ID | Cashflow Event | Cashflow Version | Booking Entity | Counterparty | Receive/Pay | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | 2023-08-15 | T1 | V2 | C1 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C2 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C3 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C4 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |

## Subsequent fully non-economic amendment

| Product | Trade Date | Trade ID | Major Version | Cashflow ID | Cashflow Event | Cashflow Version | Booking Entity | Counterparty | Receive/Pay | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | 2023-08-15 | T1 | V2 | C3 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C4 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C5 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C6 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |

## Partial non-economic amendment: FX-rate update

| Product | Trade Date | Trade ID | Major Version | Cashflow ID | Cashflow Event | Cashflow Version | Booking Entity | Counterparty | Receive/Pay | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | 2023-08-15 | T1 | V2 | C1 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C2 | Withdrawal | 2 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C3 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V2 | C4 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 730 | 2023-08-17 |

## Trade-confirmation treatment

| Product | Trade Event | Trade Action | Event Comment | Trade Date | Trade ID | Major Version | Confirmation Status | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | Trade | Book | New trade booking | 2023-08-15 | T1 | V1 | SENT | Doc sent to client |
| FX Spot | Trade | Update | Non Eco amendment | 2023-08-15 | T1 | V2 | CONFIRMED | No new doc sent to client |

| Product | Trade Date | Trade ID | Major Version | Trade confirmed | Cashflow ID | Cashflow Event | Cashflow Version | Booking Entity | Counterparty | Receive/Pay | Currency | Amount | Value Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FX Spot | 2023-08-15 | T1 | V1 | Y | C1 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Receive | USD | 100 | 2023-08-17 |
| FX Spot | 2023-08-15 | T1 | V1 | Y | C2 | New | 1 | SCB SHANGH*SHA | JP MORGAN CHASE*SHA | Pay | CNO | 720 | 2023-08-17 |

## Downstream boundary

Only original operational cashflows are sent to [[razor]] for SWIFT generation and onward delivery to [[fmsre]] and AMH. The originals are also sent to [[lms]] and exposed through the Ratan EOD cashflow API. Equivalent replacement cashflows are absent from all three downstream paths.

The stated absence of accounting and reconciliation impact is qualified by an unresolved requirement to confirm suppressed-replacement status treatment for Ratan EOD and [[tlm]] reconciliation.
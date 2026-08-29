---
type: source
title: Netting Rules Static Data
authors: []
year: 0
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, ratan, netting, static-data, cn-day-1]
related: [ratan, netting-eligibility-rules, manual-cashflow-netting, what-are-the-ratan-netting-rule-match-and-precedence-semantics, what-is-the-ratan-nstp-hold-and-release-lifecycle-for-netting-eligible-cashflows, what-is-the-approved-scope-and-roadmap-for-cn-auto-and-potential-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Rules Static Data.md"]
---
# Netting Rules Static Data

This undated functional-requirement fragment defines intended static-data categories for cashflow netting in [[ratan]].

For CN Day 1, only the **Netting eligibility rule** remains in scope. It identifies cashflows eligible for netting and holds them as NSTP. settlement ops filters the pending-netting cashflows and performs netting manually.

The proposed Potential netting rule, Auto netting rule, and separate GUI tiles are explicitly marked as removed from CN Day 1 scope. The source does not establish whether those designs were cancelled permanently, deferred, or planned for another release.

## Active CN Day 1 Rule Structure

The supplied active rule structure is:

| Attribute | Operator | Logical Model Field | Can be Blank? | Sample | Optional |
| --- | --- | --- | --- | --- | --- |
| Booking Entity FM Code | IS | Entity.Booking_Entity_SCI_FMCODE |  | SCB SHANGH*SHA, SCB CN CHO*CHO |  |
| Client FM Code | IS | Entity.Counterparty_SCI_FMCODE |  | BARCLAYS FX*LDN |  |
| Product Type | IS/IN | Instrument_Common.ISDA_Taxonomy | Y | InterestRate:CrossCurrency:Basis |  |

Only Product Type is explicitly marked blankable. The supplied `Optional` column is otherwise unpopulated.

## Removed CN Day 1 Designs

### Auto Netting Rule

This removed proposal would have held cashflows in an auto-netting pool for an EOD job to net without manual intervention. Resultant cashflows would still require review and approval through a multi-exception process.

| Attribute | Operator | Logical Model Field | Can be Blank? | Sample |
| --- | --- | --- | --- | --- |
| Booking Entity FMID/FM Code | IS | Entity.Booking_Entity_SCI_FMID Entity.Booking_Entity_SCI_FMCODE |  |  |
| Portfolio | IS |  | Y |  |
| Client FMID/FM Code | IS | Entity.Counterparty_SCI_FMID Entity.Counterparty_SCI_FMCODE |  | 10036739 BARCLAYS FX*LDN |
| Product Type? | IS/IN | Instrument_Common.CFI_Code Instrument_Common.ISDA_Taxonomy | Y | SRACCP InterestRate:CrossCurrency:Basis |
| Currency | IS/IN | Cashflow.Payment_Currency | Y | USD |
| Currency Pair | IS/IN |  | Y |  |
| Auto Netting Shifter | IS |  |  | VD-5/VD-4/VD-3/VD-2/VD-1 |

### Potential Netting Rule

This removed proposal would not have held cashflows as NSTP. Instead, it would have applied a separate Ratan-to-[[razor]] release cutoff.

| Attribute | Operator | Logical Model Field | Can be Blank? | Sample |
| --- | --- | --- | --- | --- |
| Booking Entity FMID/FM Code | IS | Entity.Booking_Entity_SCI_FMID Entity.Booking_Entity_SCI_FMCODE |  |  |
| Portfolio | IS |  | Y |  |
| Client FMID/FM Code | IS | Entity.Counterparty_SCI_FMID Entity.Counterparty_SCI_FMCODE |  | 10036739 BARCLAYS FX*LDN |
| Product Type? | IS/IN | Instrument_Common.CFI_Code Instrument_Common.ISDA_Taxonomy | Y | SRACCP InterestRate:CrossCurrency:Basis |
| Currency | IS/IN | Cashflow.Payment_Currency | Y | USD/Blank |
| Currency Pair | IS/IN |  | Y | USD/TRY |

## Gaps

The source ends at “Netting Rule Execution & Exception Fix:” and supplies no execution or exception-resolution detail. It also does not define `IS` or `IN`, rule ordering, duplicate-match handling, effective dating, audit controls, or the NSTP release lifecycle.
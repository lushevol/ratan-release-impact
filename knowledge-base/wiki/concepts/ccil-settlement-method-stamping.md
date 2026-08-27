---
type: concept
title: CCIL Settlement-Method Stamping
created: 2026-08-22
updated: 2026-08-22
tags: [CCIL, settlement-method, enrichment, MxML, Stella, FMRP]
related: [ccil-guaranteed-and-non-guaranteed-netting, mxml-adaptor-service, ratan, stella, murex-2-11, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# CCIL Settlement-Method Stamping

## Purpose

Settlement-method stamping classifies eligible cashflows as `Settlement Method = CCIL` so that NSTP, filtering, and the correct netting action can be applied.

## Tactical Implementation

For Murex 2.11 bookings, Rule 4.1 is implemented in the [[mxml-adaptor-service]]. The conditions are:

```text
Entity.Booking_Entity_SCI_FMID == '4'
Instrument_Common.Murex_Product_Family=='IRD' and Instrument_Common.Murex_Product_Group=='IRS'
Entity.Counterparty_SCI_FMID is 400021949 or the FMID from the above non guaranteed CCIL client static data list
Cashflow.Payment_Currency is INO
```

The non-guaranteed FMID list is copied from Murex 2.11 into tactical Ratan logical static data. Both the copy and this classification logic are expected to be retired after Murex 2.11 decommissioning.

## Strategic and FMRP Implementations

The strategic design assigns CCIL identification and stamping to [[stella]], using a golden source for non-guaranteed CCIL clients.

FMRP 8.0 flow notes also require Ratan Settlement to convert some flows from `GROSS` to `CCIL`, allowing IRS-netting resultants to reach `CCIL Guarantee` or `CCIL Netting` auto-netting rules.

## Control Boundary

Input flows classified as `CCIL` should not be conflated with every resultant settlement method. The source specifies `CASH` for the manually generated non-guaranteed resultant and shows later final auto-netting resultants as `Gross`. This lifecycle requires clarification.
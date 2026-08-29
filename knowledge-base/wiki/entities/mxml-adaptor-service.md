---
type: entity
title: MxML adaptor service
created: 2026-08-22
updated: 2026-08-22
tags: [MxML, adaptor, settlement-method, Murex-2-11, Ratan]
related: [murex-2-11, ratan, scbml, ccil-settlement-method-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CCIL Netting.md"]
---
# MxML adaptor service

## Role

The MxML adaptor service is the tactical implementation point for Rule 4.1, which enriches eligible Murex 2.11 cashflows with `Settlement Method = CCIL` before processing in [[ratan]].

## Rule 4.1: Settlement Method Stamping

The source specifies all of the following conditions:

```text
Entity.Booking_Entity_SCI_FMID == '4'
Instrument_Common.Murex_Product_Family=='IRD' and Instrument_Common.Murex_Product_Group=='IRS'
Entity.Counterparty_SCI_FMID is 400021949 or the FMID from the above non guaranteed CCIL client static data list
Cashflow.Payment_Currency is INO
```

This logic is tactical and is expected to be discarded after Murex 2.11 decommissioning. The strategic design moves CCIL identification and stamping to stella.
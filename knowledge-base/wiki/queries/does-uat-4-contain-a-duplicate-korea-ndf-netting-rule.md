---
type: query
title: Does uat-4 Contain a Duplicate Korea NDF Netting Rule?
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, uat-4, auto-netting, NDF, duplicate-rules]
related: [korea-static-settlement-configuration, seoul, nds-auto-netting, ratan-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Does uat-4 Contain a Duplicate Korea NDF Netting Rule?

## Question

Is the SCB/London NDF auto-netting rule duplicated in `uat-4`, and if so, is the duplication intentional and harmless?

## Evidence

The source labels the following rule as `KR SCB/LDN NDF auto netting (duplicate in uat-4)`:

```text
Entity__Booking_Entity_SCI_FMID == "10036645" && Entity__Counterparty_SCI_FMID == "10075222" && Cashflow__Payment_Currency in ("USD", "EUR") && Instrument_Common__Murex_Product_Type == "FXD" && Instrument_Common__Murex_Product_Typology == "NDF" && Portfolio__Booking_Entity_Trade_Portfolio_Name != "COM_KRO_BTB" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The source does not identify the duplicate rule ID, priority, creation history, or removal status.

## Required resolution

Compare the active `uat-4` rule set, determine whether both rules can act on the same cashflow, and remove or formally justify the duplicate.
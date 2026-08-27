---
type: concept
title: Gross-to-UTIL Settlement Update
tags: [GROSS, UTIL, settlement-method, FX, utilization, static-data]
related: [settlement-method-update, ratan, gross-to-util-settlement-update, what-is-the-authoritative-ratan-utilization-static-data-and-fmid-eligibility-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Settlement Method Update.md"]
---
# Gross-to-UTIL Settlement Update

The Gross-to-UTIL path changes an eligible Gross or blank-method cashflow to `UTIL` settlement.

## Eligibility

The source specifies all of the following conditions:

```text
Settlement method IN ('GROSS', "")
cashflow status IN (WAITING, READY + NA + NA)
data_source_system != Ratan
ISDA_Taxonomy IN (
  'ForeignExchange:Forward',
  'ForeignExchange:Spot',
  'ForeignExchange:Swap'
)
event reason != 'reversal'
```

`READY + NA + NA` is preserved as written because its meaning is not defined. The source also does not clarify whether a blank settlement method is a valid business state or an unset or legacy value.

## Processing

For an eligible cashflow, the action:

1. Sets the settlement method to UTIL.
2. Reinstates the cashflow for Util settlement.
3. Sets the payment amount to the remaining amount.
4. Post-settles as Util.
5. Stamps settlement means from client static-data setup.

The backend checks utilization static data for eligible entities identified by FMID. The source does not define missing-configuration behavior, lookup precedence, or the exact settlement-means values.
---
type: source
title: "Lien Settlement Process — Cashflow Migration"
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflow-migration, lien, murex, ratan, settlement]
related: [murex, murex-211, ratan, ratan-cashflow-lifecycle-service, cashflow-migration, cashflow-migration-readiness, lien-driven-cashflow-nstp, trade-to-cashflow-lien-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration.md"]
---
# Lien Settlement Process — Cashflow Migration

## Summary

This functional requirement defines how [[ratan]] should preserve the settlement control currently provided by Murex BAU when Murex payments are migrated to RATAN. Murex applies or removes Lien at the trade level and generates a dedicated payment NSTP exception. RATAN must apply an equivalent `Lien` exception to the underlying migrated cashflows.

The requirement covers interest, notional, and other payment types. When Lien is active, affected cashflows must be NSTP. After Lien is removed, subsequent cashflows may become STP if no other exception applies.

Murex trades and cashflows are populated as separate business objects and handled through separate data flows. The requirement does not define the correlation key, status interface, event ordering, or treatment of already-created future cashflows.

## Functional Scenarios

| Scenario | Expected RATAN behavior |
|---|---|
| Lien added when the trade is booked | All underlying cashflows generate a `Lien` exception and are NSTP. |
| Lien added during the trade lifecycle | Cashflows after the Lien update generate a `Lien` exception. |
| Lien removed before maturity | Cashflows after Lien removal do not generate a `Lien` exception and may be STP if no other exception is populated. |

## Murex 2.11 Lien Trade Volume

The source reports 519 Lien trades since 2009.

### By product

| Family | Group | Trade Count |
|---|---|---:|
| IRD | LN_BR | 328 |
| IRD | CS | 112 |
| IRD | IRS | 41 |
| IRD | CF | 30 |
| IRD | OSWP | 6 |
| CRD | CDS | 2 |
| **Total** |  | **519** |

### By booking date

| Trade Date | Trade Count |
|---|---:|
| 2009 | 14 |
| 2013 | 7 |
| 2014 | 13 |
| 2017 | 107 |
| 2018 | 127 |
| 2019 | 131 |
| 2020 | 41 |
| 2021 | 19 |
| 2022 | 12 |
| 2023 | 31 |
| 2024 | 17 |
| **Total** | **519** |

### By booking model

| Booking Model | Trade Count |
|---|---:|
| Structure Trade | 515 |
| Standalone | 4 |
| **Total** | **519** |

### Live Murex Lien trades

The source reports 24 live Murex Lien trades.

| Trade Date | Family | Group | Trade Count |
|---|---|---|---:|
| 2020 | IRD | LN_BR | 1 |
| 2021 | IRD | LN_BR | 1 |
| 2022 | IRD | LN_BR | 5 |
| 2022 | IRD | IRS | 1 |
| 2023 | IRD | LN_BR | 6 |
| 2024 | IRD | LN_BR | 9 |
| 2024 | IRD | CS | 1 |
| **Total** |  |  | **24** |

## Architecture and Control Implications

- Lien originates as a trade-level Murex attribute but is enforced as a cashflow-level RATAN settlement exception.
- RATAN needs a reliable association between each Murex cashflow, its originating trade, and the effective Lien status.
- Lien changes appear to require event-time or effective-date handling rather than a simple current-state lookup.
- Removing the Lien exception must not remove or override unrelated settlement exceptions.
- The reported population includes IRD and CRD products, so the control should not be restricted to the currently dominant `LN_BR` group.

## Evidence Limitations

The source does not identify an authoritative Lien field, event, API, or message format. It does not specify the trade-to-cashflow correlation key, acceptance tests, reconciliation controls, operational owner, or behavior when trade and cashflow messages arrive out of order.

The definition of “live” is also unspecified. It is unclear whether it means currently Liened, unsettled, active in Murex, or otherwise in scope for migration. The source screenshots referenced in the original document are not available in the ingested content.

## Related Wiki Topics

- [[concepts/lien-driven-cashflow-nstp]] describes the required settlement behavior.
- [[concepts/trade-to-cashflow-lien-correlation]] captures the separate trade and cashflow data-flow constraint.
- [[queries/how-does-ratan-correlate-murex-lien-status-to-cashflows]] tracks the unresolved interface design.
- [[queries/what-is-the-effective-date-rule-for-lien-cashflow-nstp]] tracks the unresolved temporal interpretation.

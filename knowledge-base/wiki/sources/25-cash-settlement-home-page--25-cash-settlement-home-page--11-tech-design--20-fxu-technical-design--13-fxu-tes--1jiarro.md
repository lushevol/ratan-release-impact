---
type: source
title: FXU Phase 2 Test Case
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [fxu, cash-settlement, test-case, settlement-method, cashflow-blotter]
related: [fxu, ratan, cashflow-blotter, fx-utilization, fxu-utilization-validation, transaction-synchronization, settlement-method-update, trade-level-cashflow-update, what-is-the-authoritative-fxu-settlement-method-transition-matrix, what-is-the-scope-of-the-fxu-bulk-update-limit, how-are-partial-trade-level-fxu-update-results-classified]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/FXU Phase2 Test Case.md"]
---
# FXU Phase 2 Test Case

This source records Phase 2 UI test cases for the Cashflow Blotter **Settlement Method Update** action. The feature changes eligible settlement-method values and operates on the complete set of cashflows associated with selected trades.

It supplies acceptance evidence for UI eligibility, validation, automatic trade expansion, presentation of insufficient cashflows, ordering, and trade-level completion notification. It does not define backend API, persistence, transaction, retry, or event-publication semantics.

## Eligibility Predicate

The right-menu action is available under the following stated condition:

```text
1 & (2 || 3)

1. profile: RATAN_STRATEGIC_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release

2. Settlement Method in ('GROSS','')
   and cashflow status in (WAITING, READY+NA+NA)
   and data_source_system != Ratan
   and ISDA_Taxonomy in (
       'ForeignExchange:Forward',
       'ForeignExchange:Spot',
       'ForeignExchange:Swap'
   )

3. Settlement method='UTIL'
   and cashflow status in (WAITING, READY, PASTDUE)
   and data_source_system != Ratan
   and ISDA_Taxonomy in (
       'ForeignExchange:Forward',
       'ForeignExchange:Spot',
       'ForeignExchange:Swap'
   )
```

The required profile applies to both branches. Cashflows originating from [[ratan]] are excluded. The stated FX taxonomies are `ForeignExchange:Forward`, `ForeignExchange:Spot`, and `ForeignExchange:Swap`.

`READY+NA+NA` is preserved as written. The source does not establish whether it is a composite status, a display convention, or a documentation error.

## Dialog Fields

The update dialog displays:

- Cashflow Id
- Trade Id
- Settlement Method
- Payment Amount
- Cashflow Status
- Booking Entity
- Counterparty FMCODE
- Currency
- Pay/Receive
- Value Date

## Recorded Test Cases

| No | Scenario | Evidence |
| --- | --- | --- |
| 1 | When cashflow satisfies update condition, will display "**Settlement Method Update**" menu | `cf:007373080220`, `007372108581`, `007372675350`, `007372675460`, `007372516507`, `007301243277`, `007336027907`; screenshots `image-2026-4-30_13-36-14.png` |
| 2 | Click Settlement Method Update menu, consistency validation: 1. settlement method value not same 2. limitation for bulk update is 100 cashflow | Screenshots `image-2026-4-30_16-39-47.png`, `image-2026-4-30_16-40-52.png`, `image-2026-5-20_23-20-28.png` |
| 3 | If user only selected 1 cashflow in cashflow blotter, will query all cashflows under the same trade, then will display on dialog. | `cf:007372135160`; trade `7150119619`; screenshot `image-2026-5-8_10-40-39.png` |
| 4 | Warning: "**System automatically selected all cashflows under trades**". Condition: selected cashflow count != by trade id query cashflow count | `cf:007372135160`; trade `7150119619`; screenshots `image-2026-4-30_17-2-16.png` and no-warning case `image-2026-4-30_17-17-3.png` |
| 6 | `GROSS <=>""` | Screenshot `image-2026-4-30_17-29-51.png` |
| 7 | If Trade id include not eligible update condition cashflow under, will display these not eligible cashflows on insufficient cashflow | Trade `7150557500`; screenshot `image-2026-4-30_17-28-1.png` |
| 8 | Sort by Trade Id ASC | Screenshot `image-2026-5-20_23-28-35.png` |
| 9 | Response for success/fail would be trade level and notification | Screenshots `image-2026-5-20_23-33-34.png`, `image-2026-5-20_23-33-51.png`, `image-2026-5-20_23-38-24.png`, `image-2026-5-21_11-41-5.png` |

Scenario 5 is absent from the supplied table.

## Observed Functional Behavior

A selected cashflow is expanded to all cashflows under its `Trade Id`. If the count selected by the user differs from the count found through trade-based lookup, the UI warns that all cashflows under the trades were automatically selected.

The UI validates that the requested settlement-method value is not already the current value and enforces a stated limit of 100 cashflows. The source does not clarify whether this limit is applied before or after trade expansion.

A trade can contain cashflows that are not eligible for the requested change. Those records are shown as insufficient cashflows, while final success or failure feedback is reported at trade level. The source does not explain the classification of a trade with mixed eligible, ineligible, successful, or failed cashflows.

## Related Knowledge

This test evidence extends [[fx-utilization]], [[fxu-utilization-validation]], and [[transaction-synchronization]] with Phase 2 Cashflow Blotter behavior. It should be read alongside [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--okbgq5]] when evaluating the authoritative FXU design and API contract.
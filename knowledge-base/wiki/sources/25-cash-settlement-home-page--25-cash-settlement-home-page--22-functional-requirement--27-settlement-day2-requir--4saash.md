---
type: source
title: RFI Nostro Stamping Based on Portfolio
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11718757"
venue: "Cash Settlement Home Page Functional Requirement"
tags: [cash-settlement, RATAN, RFI, Nostro, Korea, SSI-stamping, functional-requirement]
related: [ratan, scb-london, scb-korea, rfi-nostro-account, portfolio-based-rfi-nostro-stamping, rfi-portfolio-economic-amendment, nostro-type-static-data-model, rfi-swift-account-propagation, mt210-message-generation, swift, ebbs, cashflow-versioning, ssi-stamping-behavior-differences]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# RFI Nostro Stamping Based on Portfolio

## Summary

This functional requirement defines portfolio-based RFI Nostro selection for Korea-market cashflows processed by [[entities/ratan|RATAN]]. SCB London deals as a Registered Foreign Institution in Korea and must settle applicable transactions through a dedicated RFI Nostro account held with SCB Korea.

The change is limited to **cashflow SSI stamping**. Trade SSI stamping remains unchanged and is deferred to a separate strategic trade-stamping solution.

## Traceability and review status

- Azure DevOps work item: [11718757](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11718757)
- Requirement review date: 2026-02-09
- Attendees: Dinesh, Babu, Shiva
- Formal requirement sign-off: not recorded

The document should therefore be treated as a reviewed requirement draft until formal approval is confirmed.

## Required behavior

For an RFI portfolio, RATAN must select Nostro static data using:

1. Booking Entity
2. Currency
3. Portfolio

A single matching RFI Nostro is stamped automatically. Multiple matches generate the existing missing-Nostro exception and allow manual selection from cashflow details. If no RFI Nostro matches, processing continues through the existing fallback flow.

The RFI portfolios listed in the requirement are:

- `IR_SWP_KOR_NYRF_STL`
- `IR_SWP_KOR_RFI_STL`
- `IR_SWP_KOR_RFI`
- `IR_SWP_KOR_NYRF`

Vostro-stamping logic is unchanged. For an RFI portfolio, Vostro stamping must not overwrite the RFI Nostro stamp. The selection logic must remain product-agnostic.

## Static-data changes

| Status | Field name | Field type | Mandatory? | Display in list view? | Value | Allow update? | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| New | Nostro Type | dropdown | N | Y | RFI DEFAULT | N | When creating a new Nostro, the value is `DEFAULT`; the user can select another dropdown value. |
| New | Portfolio | text | Mandatory when Nostro Type = RFI | Y |  | Y | The user can input multiple portfolio values. |
| Impacted | Primary |  | Disabled when Nostro Type = RFI |  |  |  | An RFI Nostro cannot be primary. |

Duplicate checking must use:

```text
Booking Entity + Currency + Settlement Means + Settlement Account + Nostro Type
```

The requirement also states that two RFI records cannot be created for the same entity, currency, settlement means, and settlement account. It does not definitively state whether portfolio values are included in duplicate identity.

The Nostro Type must be visible in the adhoc SSI/split-popup selection list and in cashflow details.

## Amendment behavior

A portfolio change from non-RFI to RFI, or from RFI to non-RFI, is an economic amendment. The latest cashflow version must be processed, with withdrawal and new cashflow events.

If a technical failure prevents RATAN from determining the RFI indicator, the change must default to economic-amendment treatment.

A non-RFI to non-RFI portfolio change is not an economic amendment; the withdrawal and new event are expected to offset in the group blotter.

## Exceptions and manual selection

If Vostro settlement means or settlement account does not match the Nostro settlement instruction, RATAN generates an SI-mismatch exception. The user must manually amend the Vostro SSI before processing can continue.

The adhoc SSI flow allows a user to select an RFI Nostro even for a non-RFI portfolio. The requirement does not define the authorization, audit, warning, or maker/checker controls for this override.

## SWIFT and accounting impacts

The RFI account number must be propagated to:

- Payment field 53
- MT210 tag 25 for KRW

The SWIFT change requires integration testing with downstream systems. The requirement does not specify the exact field-53 option, account formatting, or complete message mapping.

When SWIFT suppression occurs before stamping:

- RFI cashflows must generate accounting using the RFI Nostro EBBS account.
- Non-RFI cashflows must generate accounting using the non-RFI Nostro EBBS account.

These accounting outcomes are related to [[entities/ebbs|EBBS]] configuration and are distinct from LMS feed behavior.

## Scope boundary

Trade stamping remains product-related BAU processing. The requirement explicitly defers RFI trade stamping to a separately deployed strategic solution. Once the cashflow logic is enabled, in-scope cashflows use the RFI Nostro while trades continue to follow the existing process.

A common future solution may support other special Nostro-selection attributes, such as portfolio, strategy, typology, or another FMRP attribute. This is an architectural consideration rather than a confirmed delivery commitment.

## Business scenarios

The requirement covers:

1. RFI Nostro creation, multiple portfolio values, disabled Primary flag, and duplicate prevention.
2. RFI outgoing payment stamping.
3. RFI incoming receipt stamping and MT210 tag 25.
4. RFI outgoing payment with Vostro/Nostro SI mismatch.
5. RFI incoming receipt with Vostro/Nostro SI mismatch.
6. Non-RFI outgoing payment using the standard non-RFI Nostro.
7. Non-RFI incoming receipt with notice-to-receive disabled.
8. Non-RFI incoming receipt with notice-to-receive enabled.
9. Adhoc SSI selection with visible Nostro Type.
10. Non-RFI to RFI economic amendment.
11. RFI to non-RFI economic amendment.
12. Non-RFI to non-RFI non-economic amendment.
13. RFI SWIFT-suppressed accounting.
14. Non-RFI SWIFT-suppressed accounting.
15. Unchanged trade stamping.

## Open issues

- Scenarios 7 and 8 describe non-RFI portfolios but their expected results say that the cashflow is stamped to the RFI Nostro. This conflicts with the scenario descriptions and the RFI/non-RFI accounting distinction.
- The source alternates between “KR ccy” and ISO currency `KRW`.
- Portfolio matching semantics for records containing multiple portfolio values are unspecified.
- The lookup key and duplicate key are not aligned.
- Multiple matches are called a “missing Nostro” exception although the condition is ambiguity.
- Field-53 scope and formatting are not defined.
- The RFI indicator, “save confirmed” status, “economic changes,” and `CCS` are not formally defined.

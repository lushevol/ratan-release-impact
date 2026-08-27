---
type: source
title: Profile USD Limit
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ratan, authorization, usd-limits, maker-checker, functional-requirement]
related: [ratan, stella, razor, fmo-ops, profile-based-usd-authorization-limits, cashflow-usd-equivalent-authorization-calculation, profile-limit-static-data-governance, high-value-exception-dependency, settle-as-gross-maker-checker-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# Profile USD Limit

## Purpose

This functional requirement defines role-based USD authorization limits for cashflow and payment operations in Ratan. It introduces differentiated operational profiles, maker/checker controls for profile and business-rule data, and USD-equivalent payment calculation using Stella FX rates.

The requirement is a business specification. It does not establish that the proposed profiles, mappings, limits, or controls have been implemented, approved, or deployed.

## Operational control objective

FMO Ops requires profiles differentiated by operational seniority to control BAU operational risk. Junior users should handle payments below predefined thresholds, while senior users should receive higher approval thresholds. Thresholds are intended to be maintained as static data.

The source describes the following profile additions:

- Profile 5: on-shore Middle Office role with limited actions such as Netting and cashflow affirmation.
- Profile 6: global Maker profile.
- Profiles 7–10: global checker profiles with progressively higher limits.

Profile 5 is described in the narrative but has no corresponding row in the profile table.

## Proposed profile matrix

The source table is incomplete and has column-alignment inconsistencies. The values below preserve the stated identifiers, limits, and entitlements without treating the matrix as implementation-ready.

| SL | Persona | Profile Description | Current RATAN Profile | New RATAN Profile | Static Profile Actions | Business Rules Profile Actions | Equivalent RAZOR Profile | USD Limit | Settlement Actions Allowed | Settlement High Risk Actions Allowed |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | FMO user excluding Setts/Conf | FMO Read Only Profile | `FMO_RO` | `-` | `-` | `-` | `-` | `0` | `-` | `-` |
| 2 | Non FMO user | Non-FMO Read Only Profile | `NON_FMO_RO` | `-` | `0` |  |  |  |  |  |
| 3 | PSS user | PSS Read Only Profile | `PSS_RO` | `-` | `0` |  |  |  |  |  |
| 4 | Middle Office user | FMO Middle Office Profile | `FMO_MO` | `-` | `0` |  |  |  |  |  |
| 6 | FMO Maker | FMO Maker Profile | `FMO_OPS` | `FMO_OPS_MKR` | `0` | Maker actions such as SI Input and Netting |  |  |  |  |
| 7 | FMO Checker (Standard) | FMO Clerk Profile | `FMO_OPS_BOC` | `GBL_BOC_ST` |  | Maker actions plus approval of exceptions below USD 30 Million |  | `< 30 Million` |  |  |
| 8 | FMO Officer Profile | FMO Officer Profile | `FMO_OPS_BO` | `GBL_BO_ST` |  | Maker actions plus approval of exceptions below USD 100 Million |  | `< 100 Million` |  |  |
| 9 | FMO Checker (High Value) | FMO Lead Profile | `FMO_OPS_SUP` | `FMO_OPS_BOL` |  | Maker actions plus approval of exceptions below USD 1 Billion | `GBL_BOL_ST` appears in the row but its column relationship is unclear | `< 1 Billion` |  | Approve Adhoc Netting; amendment or cancellation after payment release; exceptions at or above USD 100 Mio; and CPN across FX and Deriv |
| 10 | FMO Manager Profile | FMO Manager Profile | `FMO_OPS_BOM` | `GBL_BOM_ST` |  | Maker actions plus approval of exceptions up to USD 4 Billion |  | `<= 4 Billion` |  |  |
| 11 | Static Data Maker | Static Maker Profile | `-` | `FMO_STA_MKR` | Client Level Netting Flag |  | `0` |  | `-` | `-` |
| 12 | Static Data Checker | Static Checker Profile | `-` | `FMO_STA_CKR` | `0` |  |  |  |  |  |
| 13 | Business Rules Maker | Settlement Business Rules Maker | `-` | `FMO_BR_MKR` |  | Maintain profile USD limits, Suppression Rules Table, NSTP Rules Table, and Netting Rules Table | `0` |  |  |  |
| 14 | Business Rules Approver | Settlement Business Rules Approver | `-` | `FMO_BR_APR` | `0` |  |  |  |  |  |

The table does not consistently populate RAZOR mappings, settlement actions, or high-risk actions. Profile 9 contains both `FMO_OPS_BOL` and `GBL_BOL_ST` in positions that do not align unambiguously with the declared headers.

## Profile and Limit Static Data GUI

Record creation, update, and deletion require maker/checker control.

The maker form includes:

| Field Name | Field Type | Comment |
|---|---|---|
| Profile Name | Text | Type in by user |
| Limit | Numeric | Type in by user |

The source states that the current authorization limit is calculated on the fly without a table. The target state is a Ratan-specific database table with four important fields:

```text
1 Profile
2 Currency
3 USDConverted
4 Limit
```

No DDL, data types, keys, effective dates, audit attributes, approval states, or maker/checker status fields are supplied. The physical schema must therefore be designed separately.

## USD authorization calculation

The cashflow supplies the following logical-model fields:

```text
Cashflow.Payment_Currency
Cashflow.Payment_Amount
```

For USD payments, the payment amount is used directly. For non-USD payments, Ratan calls the Stella FX Conversion API, retrieves `spotRate`, and multiplies the non-USD payment amount by that rate.

```text
If Cashflow.Payment_Currency == USD:
    USD authorization amount = Cashflow.Payment_Amount

Otherwise:
    Retrieve Stella spotRate where:
      baseCurrency = Cashflow.Payment_Currency
      quoteCurrency = USD

    USD authorization amount = Cashflow.Payment_Amount × spotRate
```

The specified API contract is:

```text
API fx/rates/date/eodTag/baseCurrency/quoteCurrency
```

The source provides this response example:

```js
Response Payload : { "status":"SUCCESS", "data": [ { "date": "2021-03-15", "eodTag": "OFFICIAL_EOD_UK", "baseCurrency": "GBP", "quoteCurrency": "USD", "spotRate": "1.356" } ] }
```

The requirement does not define the rate date, `eodTag` selection, fallback or failure behavior, precision, rounding, stale-rate handling, multiple-rate selection, or whether the rate used is persisted with the authorization decision.

## Authorization behavior

When a trade is booked, the system should determine whether the user has sufficient authority to verify or approve the cashflow. If authorized, the UI should show the Submit/Approve button; otherwise, the button should not be displayed.

This stated UI behavior must be supplemented by server-side authorization enforcement. The requirement does not distinguish clearly between maker submission and checker approval.

## Open issues

- Profile 5 is missing from the matrix.
- Profile identifiers and RAZOR mappings are ambiguous, particularly for profile 9.
- Threshold boundaries are inconsistent: profiles 7–9 use `<`, while profile 10 uses `<=`.
- The relationship between general monetary limits and high-risk actions is undefined.
- The meaning of `USDConverted` is unclear.
- Maker/checker lifecycle, segregation of duties, audit, effective dating, and rollback behavior are unspecified.
- The complete entitlement matrix requires confirmation before implementation.

## Related wiki topics

This requirement extends [[entities/ratan]] with profile-based authorization controls and depends on [[entities/stella]] for non-USD conversion. It also references [[entities/razor]] through proposed profile equivalences and relates to [[stakeholders/fmo-ops]], [[concepts/high-value-exception-dependency]], and [[concepts/settle-as-gross-maker-checker-workflow]].

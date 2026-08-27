---
type: source
title: Auto DVP UAT Testing
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day2, auto-dvp, eBBS, UAT, Ratan]
related: [auto-dvp-ebbs, dvp-exception-lifecycle, ebbs-rta-notification-validation, cashflow-lineage-and-amendment-correlation, split-cashflow-dvp-handling, ratan, stella, murex, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# Auto DVP UAT Testing

## Document status

This document is a UAT test specification for Settlement Day2 Auto DVP behavior involving Ratan, Murex, Stella, and eBBS. The `Test Result` and `Tested By` fields are blank in the source. The expected outcomes must therefore be treated as requirements to validate, not as evidence of completed testing or confirmed production behavior.

## Systems and roles

- **Ratan** receives Murex and Stella cashflows, applies maker/checker release controls, tracks cashflow statuses and DVP exceptions, and consumes EBBS RTA notifications.
- **Murex** supplies covered cashflows. The tested CCS eligibility condition is `Instrument_Common__ISDA_Taxonomy == "IRD|CS"`.
- **Stella** supplies covered cashflows. The tested CCS eligibility values are the four cross-currency taxonomies listed below.
- **eBBS** supplies the RTA notification that drives Receive-side settlement and possible Pay-side DVP-exception closure.

## Eligibility and correlation rules

### Murex product eligibility

```text
Instrument_Common__ISDA_Taxonomy == "IRD|CS"
```

### Stella product eligibility

```text
InterestRate:CrossCurrency:FixedFloat
InterestRate:CrossCurrency:Basis
InterestRate:CrossCurrency:FixedFixed
InterestRate:CrossCurrency:FloatFloat
```

### Cashflow linkage

```text
Murex:  same tradeid + payment date
Stella: same tradeid + major version + payment date
```

### RTA validation

A qualifying RTA notification satisfies:

```text
Currency in RTA = Currency of C1 in Ratan
Amount in RTA = Amount of C1 in Ratan
Payment Date of C1 in Ratan
    <= Value Date in RTA
    <= Payment Date of C1 in Ratan + 2 Business Day
```

The negative validation case includes:

```text
Amount in RTA != Amount of C1 in Ratan
```

or:

```text
Value Date in RTA > Payment Date of C1 in Ratan + 2 Business Day
```

## Scenario outcomes

| # | Scenario | Expected result |
|---:|---|---|
| 1 | Scope entity, CCS, Receive-side RTA, Pay DVP exception | C1 becomes `Settled`; C2’s DVP exception auto-closes; the UI shows a green `DVP Received` tag on the Pay cashflow. |
| 2 | Non-scope, non-Africa entity, CCS | C1 becomes `Settled`; C2 retains its DVP exception unless manually closed. |
| 3 | Scope entity, non-CCS product | C1 becomes `Settled`; C2 retains its DVP exception unless manually closed. |
| 4 | Scope entity, CCS, no DVP exception | C1 becomes `Settled`; C2 remains `Waiting` unless manually operated. The source questions whether this scenario exists. |
| 5 | Pay-side RTA notification | C2 becomes `Settled`; C1 remains `Waiting` unless manually operated. |
| 6 | Receive present and Pay arrives later | C1 becomes `Settled`; subsequently received C2 has no DVP exception. |
| 7 | Matching currency and amount with valid value-date window | C1 becomes `Settled`; C2’s DVP exception auto-closes. |
| 8 | Amount mismatch or value date more than two business days late | C1 becomes `Settled`; C2 retains its DVP exception. |
| 9 | One Receive linked to split Pay children | S1 settles; S2 and S3 remain `Waiting` with exceptions; S2 and S3’s DVP exceptions auto-close. |
| 10 | One Receive linked to multiple non-split Pay cashflows | C1 settles; C2 and C3 retain their DVP exceptions. |
| 11 | Receive withdrawal | The original C1 settles, then the withdrawal version returns to `Waiting`; C2 retains its DVP exception. |
| 12 | Pay withdrawal | C1 and C2 initially settle; withdrawn C2 returns to `Waiting` and retains its DVP exception. |
| 13 | Pay amendment with unchanged trade ID | C2 becomes `Cancelled`; replacement C3 is `Waiting`; C3’s DVP exception auto-closes. |
| 14 | Receive amendment with unchanged trade ID | C1 becomes `Cancelled`; replacement C3 settles; C2’s DVP exception auto-closes. |
| 15 | Pay amendment with changed trade ID | C2 becomes `Cancelled`; replacement C3 remains `Waiting` with its DVP exception. |
| 16 | Receive amendment with changed trade ID | C1 becomes `Cancelled`; replacement C3 settles; C2 retains its DVP exception. |

## Test identifiers

| Scenario range | Murex identifiers | Stella identifiers |
|---|---|---|
| 1 | C1 `M0Q508180103`; C2 `M0Q508180104` | C1 `0AP508190105`; C2 `0AP508190106` |
| 2 | C1 `M0Q508180203`; C2 `M0Q508180204` | C1 `0AP508190201`; C2 `0AP508190202` |
| 3 | C1 `M0Q508180305`; C2 `M0Q508180304` | C1 `0AP508190301`; C2 `0AP508190302` |
| 4 | C1 `M0Q508180405`; C2 `M0Q508180404` | C1 `0AP508190401`; C2 `0AP508190402` |
| 5–8 | IDs beginning `M0Q5081805xx` through `M0Q5081808xx` | IDs beginning `0AP5081905xx` through `0AP5081908xx` |
| 9 | C1 `M0Q508180901`; C2 `M0Q508180902`; S1–S3 `S00000123097`–`S00000123099` | C1 `0AP508190901`; C2 `0AP508190902`; S1–S3 `S00000123375`–`S00000123377` |
| 10–16 | IDs beginning `M0Q5081810xx` through `M0Q5081816xx` | IDs beginning `0AP5081910xx` through `0AP5081916xx` |

Scenario 1 references defect `ADO BUG-15655146`. No execution result or tester is recorded for any scenario.

## Interpretation

The scenarios specify a directional rule: a qualifying eBBS RTA notification for a released Receive cashflow can settle that Receive cashflow and close a linked Pay-side DVP exception. The rule appears to require covered cashflows, an eligible booking entity, an eligible CCS product, valid linkage, maker/checker release of the Receive cashflow, a qualifying RTA notification, and an existing Pay-side DVP exception.

The specification distinguishes split Pay children from ordinary one-to-many Pay cashflows. It also indicates that unchanged trade IDs allow amended cashflows to inherit the original DVP relationship, whereas changed trade IDs create a new relationship that does not inherit automatic closure.

The source leaves several implementation details unresolved: the seven scope countries, the treatment of Africa entities, the distinction between split and non-split relationships, the exact status and exception representation after closure, withdrawal-version identity, the lineage algorithm, the RTA business-day calendar, and whether an RTA currency mismatch independently blocks Auto DVP.

## Related pages

- [[concepts/auto-dvp-ebbs]]
- [[concepts/dvp-exception-lifecycle]]
- [[concepts/ebbs-rta-notification-validation]]
- [[concepts/cashflow-lineage-and-amendment-correlation]]
- [[concepts/split-cashflow-dvp-handling]]
- [[entities/ratan]]
- [[entities/murex]]
- [[entities/stella]]
- [[entities/ebbs]]
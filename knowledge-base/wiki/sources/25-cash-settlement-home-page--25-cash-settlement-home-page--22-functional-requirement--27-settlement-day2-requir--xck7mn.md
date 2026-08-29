---
type: source
title: Cash Settlement Auto Netting Business User Case Testing
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, settlement-day2, functional-requirement, testing]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-resultant-cashflow-lifecycle, netting-un-net-lifecycle, business-calendar-relative-netting-time, netting-scenario-priority, cashflow-blotter-action-eligibility, ratan, cash-settlement-home-page, sci, pending-auto-netting-state, cross-rule-netting-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Business user case testing.md"]
---
# Cash Settlement Auto Netting Business User Case Testing

## Scope

This source records business user case testing for Settlement Day2 [[concepts/cashflow-auto-netting]] in the Cash Settlement Home Page context. The tests cover Netting Static Blotter rule management, scheduled auto-netting execution, cashflow eligibility, resultant generation, release from [[entities/ratan]], withdrawal, un-netting, calendar-relative timing, rule precedence, cross-rule isolation, and rule refresh.

The reported test period was 2025-06-13 through 2025-06-20. Most cases are marked `Y`, but several contain environmental issues, inconsistent configuration, incomplete result fields, or explicitly unresolved behavior.

## Common lifecycle

The principal tested lifecycle is:

1. Create and activate an auto-netting rule in Netting Static Blotter.
2. Book cashflows matching the rule.
3. Keep eligible cashflows in `state = 'WAITING'` with sub-state `Pending Auto Netting` before the configured netting time.
4. Trigger the scheduled job at or after the configured netting time.
5. Set aggregated source cashflows to `NETTED` and create a resultant cashflow.
6. Affirm the resultant and apply the configured NSTP control.
7. Release the resultant from Ratan.

The tested NSTP levels include `NSTP_MAKER_CHECKER`, `NSTP_CHECKER_ONLY`, and `FULL_STP`.

## Test case findings

### AC-Settlement-AutoNetting-001 — Bilateral Netting

Two eligible cashflows were processed using a bilateral rule. The tested condition was:

```text
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") &&
((Entity__Booking_Entity_SCI_FMID == "10075222" &&
  Entity__Counterparty_SCI_FMID in ("401050605")))
```

The reported configuration was:

```text
Netting Date Time: VD-1 9:00
STP Level: NSTP_MAKER_CHECKER
Netting Type: bilateral netting
```

The expected and reported flow was that both cashflows entered `WAITING / Pending Auto Netting`, became `NETTED`, produced an affirmed resultant with the configured NSTP exception and payment type `Bilateral Netting`, and were released from Ratan.

The test fixture used cashflow identifiers `M00015726002` and `M00015726003`, with modified trade IDs `15726002` and `15726003`.

### AC-Settlement-AutoNetting-002 — CCIL Netting

The CCIL rule condition was:

```text
Settlement_Method in ("CCIL") &&
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The reported configuration was:

```text
Netting Date Time: VD-1 9:00
STP Level: NSTP_CHECKER_ONLY
Netting Type: CCIL Netting
```

Two matching cashflows entered `Pending Auto Netting`, were combined into an affirmed resultant with the configured NSTP exception and payment type `CCIL Netting`, and the resultant was released.

The test used substituted trade, cashflow, and tracking identifiers. Original values were retained in parentheses in the source. These substitutions describe test-fixture preparation and do not establish eligibility of the original production identifiers.

### AC-Settlement-AutoNetting-003 — BIC Netting

The tested BIC condition was:

```text
Entity__Counterparty_SCI_BIC_Net_Flag == "Y" &&
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

The counterparty FMID was changed to `400091560`, corresponding to BIC `RBOSGB2RTCM`. The scenario title and expected result identify this as `BIC Netting`, with expected payment type `BIC Netting`.

However, the testing sample states `Netting Type: CCIL Netting`. The source therefore confirms that the BIC eligibility condition was exercised, but does not resolve whether the generated payment type should be `BIC Netting` or `CCIL Netting`.

### AC-Settlement-AutoNetting-004 — Single Cashflow

A single cashflow matched a bilateral rule and entered `WAITING / Pending Auto Netting`. After the scheduled job, it remained `WAITING`, became affirmed, received the configured NSTP exception, and was released from Ratan.

No explicit resultant was reported. The case therefore indicates that auto-netting processing can apply affirmation and NSTP controls to a single eligible cashflow without demonstrating multi-cashflow aggregation.

### AC-Settlement-AutoNetting-005 — Cashflows Booked After Netting Time

Two cashflows booked after the configured netting time remained in `Pending Auto Netting` until the next scheduled execution. The expected behavior was that they would then become `NETTED`, produce an affirmed resultant with the configured NSTP exception, and be released.

The actual-result field says that this case was covered by earlier cases, so it is corroborating rather than independently documented evidence.

### AC-Settlement-AutoNetting-006 — Netting Time Calculation

The source records the following calendar-relative calculations:

| Cashflow | Currency | Payment Date | Date from Netting Static | Auto netting date | Explanation |
| --- | --- | --- | --- | --- | --- |
| C1 | SGD | 1st Apr. 2025 (Tuesday) | VD-1 | 20250328 (Last Friday) | SGD holiday on Monday, 2025/03/31 |
| C2 | CNY | 1st Apr. 2025 (Tuesday) | VD-1 | 20250331 (Monday) | Working day on Monday, 2025/03/31 |
| C3 | CNY | 7th Apr. 2025 (Monday) | VD-1 | 20250406 (Sunday) | CNY working weekend on Sunday, 2025/04/06 |
| C4 | GBP | 21st Apr. 2025 (Holiday) | VD | 20250421 (Holiday) | Payment date is a weekend or holiday |

The C1 and C2 examples support currency-calendar-sensitive calculation. The source explicitly states that the C3 case has a problem, so `20250406` must not be treated as validated authoritative behavior. C4 appears to preserve the payment date even when it is a holiday.

The database validation reference was:

```sql
select * from cash_netting_service.ratan_auto_netting_cashflow a
where a.cashflow_id ='M00015726789'
```

### AC-Settlement-AutoNetting-007 — Multiple Matching Rules

The scenario tested two overlapping rules:

| Rule | Creation time | Netting time |
| --- | --- | --- |
| Rule1 | 2025-05-28 09:00 | VD 09:00 |
| Rule2 | 2025-05-28 09:20 | VD 09:30 |

The stated behavior was that the latest-created rule would be tagged to a matching cashflow. The execution used later test creation times and reported:

```text
C1: M00015720029
C2: M00015720030
Resultant: N00000003123
```

This is evidence for observed latest-created-rule selection, but it does not establish whether precedence is based on database creation time, effective time, rule version, or refresh order.

### AC-Settlement-AutoNetting-008 — Cross-Rule Netting

Two rules shared booking entity and counterparty but matched different products:

| Rule | Matching condition | Configuration |
| --- | --- | --- |
| Rule1 | Product A | `VD-1`, `CHECKER_ONLY`, `Bilateral Netting` |
| Rule2 | Product B | `VD-1`, `CHECKER_ONLY`, `Bilateral Netting` |

The cashflows were:

```text
C1: M00015720031
    Payment date: 2025-06-10
    Product: COM|SWAP

C2: M00015720032
    Payment date: 2025-06-10
    Product: IRD|IRS
```

Both cashflows entered `Pending Auto Netting`, were affirmed, received the configured `CHECKER_ONLY` exception, and were released individually. They were not combined across rules. This supports [[concepts/cross-rule-netting-isolation]].

### AC-Settlement-AutoNetting-009 — Withdrawal Before Netting

The test identifiers were:

```text
C1: M00015720006
C2: M00015720007
C3: M00015720008
Resultant: N00000003057
```

C1 was withdrawn before scheduled execution and became `CANCELLED`. C2 and C3 were then netted into `N00000003057`, which was affirmed and released.

The source reports a development-environment problem on 2025-06-13. Later evidence dated 2025-06-16 appears to support the intended behavior, making this successful but environment-contingent evidence.

### AC-Settlement-AutoNetting-010 — Withdrawal After Netting

The test used:

```text
C1: M00015720009
    Amount: 0.05
    Currency: CNY
    Payment date: 2025-06-02

C2: M00015720010
    Amount: 0.04
    Currency: CNY
    Payment date: 2025-06-02

C3: M00015720011
    Amount: 0.03
    Currency: CNY
    Payment date: 2025-06-02

First resultant: N00000003068
Replacement resultant: N00000003070
```

The observed sequence was:

1. C1 and C2 were combined into `N00000003068`.
2. C3 remained `WAITING / Pending Auto Netting`.
3. C1 was withdrawn.
4. `N00000003068` became `DEAD` and C1 became `CANCELLED`.
5. C2 returned to `WAITING / Pending Auto Netting`.
6. A subsequent run combined C2 and C3 into `N00000003070`.
7. The replacement resultant was released.

The automation created the first resultant before C3 was created, so execution differed from the nominal three-cashflow scenario. The lifecycle nevertheless provides strong evidence for automatic un-netting and compensating re-netting.

### AC-Settlement-AutoNetting-011 — Refresh After New Rule Creation

The source identifiers were:

```text
C1: M00015720039
C2: M00015720040
C3: M00015720041
```

Before rule creation, the cashflows were in:

```text
C1: WAITING / Pending Netting
C2: WAITING / Pending Exception
C3: READY / no sub-state
```

After creating the rule, all three became `WAITING / Pending Auto Netting`. The scheduled job then netted them into an affirmed resultant with the configured NSTP exception, and the resultant was released.

This supports refresh or re-evaluation of existing cashflows when a new rule becomes live.

### AC-Settlement-AutoNetting-012 — Refresh After Existing Rule Update

The source used:

```text
M01744718888 - PENDING NETTING
M01744711234 - PENDING EXCEPTION
M01744711343 - READY
M01744713319 - PENDING AUTO NETTING
Resultant: N00000003129
```

The expected behavior was that the first three cashflows, which match the updated rule, would become `WAITING / Pending Auto Netting`, while the fourth cashflow, which matched the current rule but not the updated rule, would no longer have that sub-state. The first three would then be netted into `N00000003129` and released.

The result column is blank despite screenshots and a reported resultant. This is partially evidenced and requires confirmation before being treated as an approved selective-refresh rule.

### AC-Settlement-AutoNetting-013 — Refresh After Rule Disablement

The source identifiers were:

```text
C1: M00015720020
C2: M00015720021
C3: M00015720022
C4: M00015720023
```

After disabling the rule, the expected behavior was that the cashflows would no longer have sub-state `Pending Auto Netting`.

The test is marked `Y`, but C1 was reported in `Pending Exception`, with a note that an automated trigger may have caused the unexpected state. The expected replacement state after disablement is not specified.

## Evidence quality and limitations

Strong evidence includes the standard rule-driven lifecycle, resultant generation and release, cross-rule isolation, and withdrawal-after-netting compensation.

Moderate evidence includes single-cashflow processing, processing after netting time, latest-created-rule selection, and calendar-relative timing.

Qualified evidence includes the C3 CNY date, selective refresh after rule update, disablement cleanup, and BIC payment-type semantics. Screenshot references are retained in the original source but are not independently interpretable here because image contents are unavailable.

## Open questions

- What is the authoritative precedence when multiple active rules match?
- Does a single matching cashflow generate a resultant, or only receive affirmation and NSTP processing?
- Can `VD-1` intentionally resolve to a currency working weekend?
- What state replaces `Pending Auto Netting` after rule disablement?
- What is the exact refresh scope after an existing rule is updated?
- Does BIC Netting produce a BIC-specific payment type, or was the test configured as CCIL Netting?

## Related wiki pages

The source extends [[concepts/cashflow-auto-netting]], [[concepts/auto-netting-rule-management]], [[concepts/netting-resultant-cashflow-lifecycle]], [[concepts/netting-un-net-lifecycle]], [[concepts/business-calendar-relative-netting-time]], [[concepts/netting-scenario-priority]], cashflow blotter action eligibility, [[entities/ratan]], [[entities/cash-settlement-home-page]], and sci.
---
type: concept
title: Cashflow Auto Netting
created: 2026-08-22
updated: 2026-08-23
tags: [cashflow, auto-netting, netting, RATAN, settlement, settlement-day2, uat]
related: [ratan, auto-netting-rule-management, business-calendar-relative-netting-time, cashflow-exception-handling, cashflow-failure-and-reinstatement, pending-fixing-stp-nstp-control, ad-hoc-cashflow-netting, rfr-auto-netting, ccs-auto-netting, irs-interest-auto-netting, uat-test-case, booking-and-counterparty-fmcode, cashflow-identifier, settlement-day2-requirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# Cashflow Auto Netting

Cashflow Auto Netting is the proposed RATAN process and settlement capability for automatically grouping or offsetting eligible cashflows at a configured future netting datetime, with the aim of reducing or consolidating settlement movements.

The UAT material describes Cashflow Auto Netting as a capability under test in the Settlement Day2 Requirement context. The functional requirement defines the processing model below. The UAT sample itself does not specify the netting algorithm or prove that any record was successfully netted.

## Processing Model

1. A cashflow is evaluated after manual netting rule checks and before multiple-exception checks.
2. A cashflow matching an auto-netting rule enters **Pending Auto Netting**.
3. It remains there until the rule's calculated netting datetime.
4. At execution, cashflows are grouped within the rule that selected them.
5. The Day 1 backend netting key is Booking Entity, Counterparty, Currency, and Payment Date.
6. The resultant cashflow is routed to Pending Exception and held NSTP.

A cashflow that arrives after its scheduled netting datetime is routed to Pending Netting rather than being held for auto netting.

## Rule Isolation and Selection

There is no cross-rule netting. A cashflow selected by a Product A rule must not net with a cashflow selected by a Product B rule merely because the backend key values otherwise match.

When a cashflow matches multiple rules, the rule with the earliest calculated netting datetime wins. Equal calculated times are ordered by system creation time. Configurable rule priority is not in Day 1 scope.

## Exceptions and Reversals

If only one eligible cashflow remains at execution, it is released to multiple-exception checking and should trigger **Single Cashflow**.

A manually or system-un-netted component skips auto-netting rule checks and is held NSTP. If an upstream cancellation occurs before execution, the cancelled cashflow is removed from the queue. If cancellation occurs after netting, the resultant is deadened, the withdrawn component is cancelled, and surviving components are released to Pending Exception.

## UAT Coverage

The supplied UAT material provides 184 candidate cashflow records across CITIC, HKEX, LCH, SAL, TAIFEX, and SCH cohorts. It demonstrates broad venue and regional coverage, but it does not establish that the records met the functional eligibility rules or that any record was successfully netted.

London is the dominant booking location, with 129 records across HKEX, LCH, and SAL. The LCH cohort is the largest individual group, with 69 records. Hong Kong, Taipei, and China are represented through the remaining cohorts.

## UAT Evidence Boundaries

The sample contains booking-entity FMCODEs, counterparty FMCODEs, and cashflow identifiers. It does not contain:

- Amounts
- Currencies
- Value dates
- Directions
- Products
- Accounts
- Statuses
- Netting keys
- Expected results
- Execution results
- Defects

These omissions prevent the sample from defining eligibility or grouping behavior. The capability should therefore be evaluated together with the separate functional rule set and a UAT execution record.

The UAT source is linked through [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1p3a3x|Cashflow Auto Netting UAT Testing Sample]].

## Day 1 Boundaries

Currency-pair conditions, additional netting keys such as `structure id`, and configurable rule priority are explicitly deferred. The structure-ID scenario in the functional requirement is illustrative future behavior, not approved Day 1 functionality.

This concept is grounded in a functional requirement and a UAT sample. It should not be treated as evidence of implementation, successful testing, or production deployment.
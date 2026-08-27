---
type: source
title: Hard Blocker Go-Live Checklist
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, settlement-day-2, go-live, ratan, nstp, hard-blocker]
related: [ratan, murex, cash-settlement-home-page, settlement-day-2, hard-blocker-exception, swap-agent-coupon-release-block, cashflow-suppression-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# Hard Blocker Go-Live Checklist

## Summary

This document specifies go-live requirements for a `HARD_BLOCKER` NSTP rule in the Cash Settlement and Settlement Day 2 workflow. The rule prevents release from Ratan for specified Swap Agent cashflows and for cashflows explicitly marked as hard blockers.

The document provides configuration values, expected front-end behavior, required back-end service versions, and SQL validation queries. It does not contain completed pass/fail results, validation timestamps, named sign-off owners, or rollback criteria. It should therefore be treated as a go-live specification and validation checklist rather than evidence that deployment was completed.

## NSTP rule configuration

```text
((Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type in ("Coupon", "Interim MTM")) || Cashflow__Is_Hard_Blocker == true)
```

| Field | Value |
| --- | --- |
| Exception Code | `Hard Block Swap Agent` |
| Operation Level | `MAKER_CHECKER` |
| Exception Category | `HARD_BLOCKER` |
| Bulk Eligible | Not ticked |
| Requestor/Eops reference | `Hard Block Swap Agent-Single cashflow` |
| eOps | `SCH202G210A1190925068117` |
| Status | Blank |

The expression has two branches:

1. `Instrument_Common__Murex_Product_Strategy` is `SWAP_AGENT` and `Cashflow__Payment_Type` is `Coupon` or `Interim MTM`.
2. `Cashflow__Is_Hard_Blocker` is `true`.

The second branch is broader than the Swap Agent-specific condition.

## Front-end checklist

| No. | Area | Action | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Settlement NSTP Rule (New) | Perform CRUD operations and add an exception configuration. | `HARD_BLOCKER` appears in the Exception Category drop-down list. | `attachments/image-2025-9-11_16-34-16.png` |
| 2 | Cashflow Blotter - Single Cashflow | Open a cashflow with a hard-blocker exception and fix the exception. | The hard-blocker exception code appears first under `HARD_BLOCKER` and uses an error color equivalent to the high-risk exception color. | `attachments/image-2025-9-11_14-46-51.png` |
| 3 | Cashflow Blotter - Single Cashflow | A maker selects **Submit**. | Submission is blocked and the following message appears: `This is a Swap Agent Coupon or Interim MTM cashflow, can't be release from Ratan.` | `attachments/image-2025-9-11_14-56-28.png` |
| 4 | Cashflow Blotter - Single Cashflow | A checker selects **Approve**. | Approval is blocked and the same error message appears. | Same as item 3 |
| 5 | Cashflow Blotter - Bulk fix exception | Select multiple cashflows, including hard-blocked items, and select **Bulk Submit**. | Hard-blocked items receive a validation error, are displayed with strikethrough formatting, and are not posted to the back end. | `attachments/image-2025-9-11_14-59-58.png`; `attachments/image-2025-9-11_15-0-18.png` |

## Back-end checklist

| Service | Required version | Validation SQL |
| --- | --- | --- |
| `ratan-cash-settlement-netting-service` | `1.5.7` | `select * from cash_netting_service.t_cashflow tc where tc.message like '%hardBlockerComponentType%' and tc.created_at > '2025-09-27';` |
| `ratanone-rule-service` | `2.3.11` |  |
| `ratan-rule-service` | `2.2.4.5` |  |
| `ratanone-db-repository` | Not specified | Validate suppression-field records and activated versions. |

### Cashflow message validation

```sql
select * from cash_netting_service.t_cashflow tc where tc.message like '%hardBlockerComponentType%' and tc.created_at > '2025-09-27';
```

### Suppression-field validation

```sql
--check below field exists or not and check version is correct.
-- field config
select * from ratan_rule_service.ratan_suppression_fields_config where id in ('a770a624-b4dd-4dfd-bf41-d889cf78222f');

-- field
select * from ratan_rule_service.ratan_suppression_fields where id in('069b1939-577f-47d4-8253-901e89d40777');

-- ratan_suppression_fields_xpath
select * from ratan_rule_service.ratan_suppression_fields_xpath where id in ('5bfa098c-1142-4764-9ee8-996cf3f0b61f');

--check version
select * from ratan_rule_service.ratan_suppression_fields_activated_version a where table_name in ('ratan_suppression_fields_config','ratan_suppression_fields');
```

## Evidence limitations and open issues

The checklist does not establish that the rule or service versions were deployed successfully. The blank status field and absent execution results leave deployment and validation unresolved.

The expected error message is specific to Swap Agent Coupon or Interim MTM cashflows, although the rule also matches any cashflow with `Cashflow__Is_Hard_Blocker == true`. The source does not define the correct message for non-Swap Agent hard blockers.

The source also does not specify whether bulk submission partially processes valid cashflows when the same selection contains hard-blocked items, or whether the entire batch is rejected. The date filter `tc.created_at > '2025-09-27'` is not explained as a deployment date, test-data cutoff, or diagnostic boundary.

See [[is-the-hard-blocker-rule-deployed-and-validated]], [[what-error-message-applies-to-non-swap-agent-hard-blockers]], and [[does-bulk-submit-partially-process-valid-cashflows]].
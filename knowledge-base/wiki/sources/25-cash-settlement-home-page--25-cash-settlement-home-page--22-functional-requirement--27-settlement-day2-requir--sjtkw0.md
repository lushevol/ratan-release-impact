---
type: source
title: Cash Settlement Day2 Cashflow Auto Netting Test Cases
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/Swap+Agent+Day2"
venue: Confluence
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, bilateral-netting, swap-agent, day2-testing]
related: [ratan, netting-static-blotter, ratan-cashflow-blotter, pending-auto-netting-state, cross-rule-netting-isolation, netting-rule-change-cashflow-refresh, business-calendar-relative-netting-time, cashflow-multi-exception-generation, netting-resultant-cashflow-lifecycle, cashflow-failure-and-reinstatement, swap-agent, swap-agent-mtm-coupon-netting-separation, netting-job-retry, trade-level-clearing-id-propagation, netting-type-derivation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---
# Cash Settlement Day2 Cashflow Auto Netting Test Cases

## Scope

This functional test-case specification covers two related suites in Ratan:

- Bilateral auto-netting, including rule creation, pending-queue behavior, netting-date calculation, netting-type derivation, post-netting handling, and rule-ID isolation.
- Swap Agent Day2 auto-netting, including MTM/Coupon segregation, retry behavior, resultant suppression, resultant labels, and Clearing ID display.

The source records expected and actual results, but every formal `Test Statue` field is blank. Matching expected and actual text therefore indicates recorded evidence, not necessarily a formally signed-off pass.

## Bilateral Netting Test Cases

| TestCase Number | TestCase Name | Test Step | Expect Result | Actul Result | Test Statue |
| --- | --- | --- | --- | --- | --- |
| TC_001 | Bilateral Netting Auto Functionality Same Booking Entity, Counterparty, Currency, Value Date, and Payment Type Auto Netting with netting type as CCIL netting in netting static blotter Auto Netting with netting type as BIC netting in netting static blotter | 1: Identify cashflows with the same booking entity, counterparty, currency, value date, and payment type 2: Wait until the designated netting time. 3: Verify that the system automatically nets the identified cashflows together. 4: Check the netting report or transaction summary to confirm the netted result. | Describe the expected behavior or state of the system after each step. | Describe the expected behavior or state of the system after each step. | |
| TC_002 | Verify that newly created netting rules only affect cashflows materialized after rule creation. | 1. Data Ops creates a new netting rule(`Rule1`). 2. Generate a new cashflow (`CF1`). | Historical cashflows remain unaffected. The new cashflow (`CF1`) enters the `Pending Auto Netting` queue. | Describe the expected behavior or state of the system after each step. | |
| TC_003 | Verify that when the historical data status is "pending netting," and the user performs a "Failed/Reinstate" operation, the status of the historical data changes to "pending auto netting." | 1.user manually Failed/Reinstate 2.cash flow will Restart the process and return to pending auto netting | cashflow return to pending auto netting | cashflow return to pending auto netting | |
| TC_004 | Verify System will calculate the netting date based on cashflow currency related calendar | 1.Enter cashflows of different currencies with dates changed to weekends, and verify if the auto netting day is the same day or will be on Friday. | The auto netting day will meet the expected time | The auto netting day will meet the expected time | |
| TC_005 | Verify data ops disable the netting static, the historical cashflow hold in pending auto netting queue will **still be netted** with previous properties | 1.disable Netting static 2.the historical cashflow hold in pending auto netting queue will **still be netted** | the historical cashflow hold in pending auto netting queue will **still be netted** | the historical cashflow hold in pending auto netting queue will **still be netted** | |
| TC_006 | Automatically Apply Updated Netting Rules | 1. Create an auto netting rule (set netting date-time, STP level, netting type, etc.). 2. Add several cashflows to the pending auto netting queue. 3. Update the execution details of the netting rule (e.g., modify netting date-time or netting type). 4. Trigger the netting process. | The cashflows in the pending queue automatically apply the updated netting rules. No manual refresh is required, and the system uses the updated rules for netting processin | The cashflows in the pending queue automatically apply the updated netting rules. No manual refresh is required, and the system uses the updated rules for netting processin | |
| TC_007 | Verify the default value of the Netting Type field | 1.Open the page and check the initial value of the Netting Type field | The default value of the Netting Type field is blank | The default value of the Netting Type field is blank | |
| TC_008 | Verify rule conditions trigger automatic update of Netting Type | 1.Add the rule condition `Settlement method == "CCIL"` and `Counterparty SCI FMID <> 400021949 | The Netting Type field is automatically updated to `"CCIL netting | The Netting Type field is automatically updated to `"CCIL netting | |
| TC_009 | Verify rule conditions trigger Netting Type to "BIC netting | 1.Add the rule condition `Counterparty_SCI_BIC_Net_Flag == "Y" | The Netting Type field is automatically updated to `"BIC netting" | The Netting Type field is automatically updated to `"BIC netting" | |
| TC_010 | Current time is after the netting data/time,user set cross | 1.The user set post netting time is "cross". | Perform a multi-exception check | Perform a multi-exception check | |
| TC_011 | Current time is after the netting data/time,user set pending netting | 2.The user set post netting time is "pending netting" | it will remain in the pending netting state | it will remain in the pending netting state | |
| TC_012 | Verify Netting State UI | 1.select Netting data time vd or vd-1 2.select stp level ( - NSTP_MAKER_CHECKER - NSTP_CHECKER_ONLY - FULL_STP ) 3. select netting type Bilateral netting or swap agent netting 4.select post netting time pending netting or cross | All the rules were successfully created and implemented in the Rantan system. | All the rules were successfully created and implemented in the Rantan system. | |
| TC_013 | Verify that only cashflows with the same netting key + rule ID can be netted. Cross-rule netting is not allowed. | 1.set up rule1 2.set up rule2 3.rule1 and rule2 rule id is different | Cashflows hitting Rule 1 and Rule 2 two cashflow cannot be netted. | Cashflows hitting Rule 1 and Rule 2 two cashflow cannot be netted. | |

## Swap Agent Day2 Test Cases

| TestCase Number | TestCase Name | Test Step | Expect Result | Actul Result | Test Statue |
| --- | --- | --- | --- | --- | --- |
| TC_001 | Verify that eligible Swap Agent cashflows are netted based on the defined rules | 1. Enable the auto netting function. 2. Trigger the netting process | Cashflows with the same attributes are netted together. "MTM" cashflows are not netted with "Coupon" cashflows. | Cashflows with the same attributes are netted together. "MTM" cashflows are not netted with "Coupon" cashflows. | |
| TC_002 | Verify that "MTM" cashflows are not netted with "Coupon" cashflows | 1. Enable the auto netting function. 2. Trigger the netting process. | "MTM" cashflows are not netted with "Coupon" cashflows | "MTM" cashflows are not netted with "Coupon" cashflows | |
| TC_003 | Verify that cashflows with different attributes are not netted | 1.Create multiple cashflows with the following attributes: `Product_Strategy = "SWAP_AGENT"` `Payment_Type = "Coupon"` At least one attribute (Booking Entity, Counterparty, Currency, Value Date) is different 2.Enable the auto netting function 3.Trigger the netting process | Cashflows with different attributes are not netted | Cashflows with different attributes are not netted | |
| TC_004 | Verify that the system retries the netting process 30 minutes after a job failure | 1. Wait for the initial auto-netting job to fail. 2. Wait 30 minutes for the retry job to trigger. 3. Monitor the system logs or output for the retry job. | The retry job starts 30 minutes after the initial failure. Eligible cashflows are successfully netted in the retry job. | The retry job starts 30 minutes after the initial failure. Eligible cashflows are successfully netted in the retry job. | |
| TC_005 | Verify that Netting resultant cashflows of type "coupon" are correctly suppressed | 1. Perform the Netting operation. 2. Check the Netting resultant cashflows. 3. Verify that Netting resultant cashflows of type "coupon" are suppressed. | Netting resultant cashflows of type "coupon" are suppressed. Original cashflows remain unaffected. | Netting resultant cashflows of type "coupon" are suppressed. Original cashflows remain unaffected. | |
| TC_006 | Verify that Netting resultant cashflows of type "MTM" are correctly suppressed | 1. Perform the Netting operation. 2. Check the Netting resultant cashflows. 3. Verify that Netting resultant cashflows of type "MTM" are suppressed. | Netting resultant cashflows of type "MTM" are suppressed. Original cashflows remain unaffected. | Netting resultant cashflows of type "MTM" are suppressed. Original cashflows remain unaffected. | |
| TC_007 | Verify MTM Netting Result | 1. Create an original cash flow with type "MTM". 2. Trigger the auto Netting process. 3. Check the Netting resultant cash flow type. | The Netting resultant cash flow type is "SAL or SWAP AGENT MTM Netting" | The Netting resultant cash flow type is "SAL or SWAP AGENT MTM Netting" | |
| TC_008 | Verify Coupon Netting Result | 1. Create an original cash flow with type "Coupon". 2. Trigger the auto Netting process. 3. Check the Netting resultant cash flow type. | The Netting resultant cash flow type is "SAL or SWAP AGENT Coupon Netting" | The Netting resultant cash flow type is "SAL or SWAP AGENT Coupon Netting" | |
| TC_009 | Verify Clearing ID Display for Murex Cashflow | 1. Create a Murex trade and ensure its UDF contains a Clearing ID. 2. Run the cashflow generation process. 3. Open the Cashflow Blotter and check the Clearing ID field for the Murex cashflow. | The Clearing ID field for the Murex cashflow correctly displays the trade-level Clearing ID | The Clearing ID field for the Murex cashflow correctly displays the trade-level Clearing ID | |
| TC_010 | Verify Clearing ID Field is Blank for Non-Murex Cashflows | 1. Create a non-Murex trade. 2. Run the cashflow generation process. 3. Open the Cashflow Blotter and check the Clearing ID field for the non-Murex cashflow. | The Clearing ID field for non-Murex cashflows is blank | The Clearing ID field for non-Murex cashflows is blank | |

## Findings and Limitations

The source supports the following scoped findings:

- Bilateral cashflows with matching processing attributes can be auto-netted, while different rule IDs form a hard boundary.
- Newly materialized cashflows enter `Pending Auto Netting`; historical cashflows are described as unaffected by newly created rules.
- Failed/reinstated historical cashflows return to `pending auto netting`.
- Disabling Netting Static does not prevent already queued historical cashflows from netting with previous properties.
- Pending cashflows can apply updated netting-rule execution details without a manual refresh.
- `Netting Type` can be derived as `"CCIL netting"` or `"BIC netting"` from rule conditions.
- A `cross` post-netting setting triggers a multi-exception check, while `pending netting` retains the pending state.
- Swap Agent processing separates MTM and Coupon cashflows, retries after 30 minutes following a job failure, suppresses netting resultants while preserving originals, and uses distinct resultant labels.
- Clearing ID is displayed for Murex cashflows when present on the trade UDF and is blank for non-Murex cashflows.

The source does not establish:

- The exact weekend and currency-calendar algorithm.
- Which queued cashflow properties are snapshotted versus dynamically re-read.
- Precedence when both CCIL and BIC conditions match.
- The lifecycle state or technical mechanism represented by resultant suppression.
- Formal pass status, execution dates, environments, tester names, logs, or defect references.

These limitations should be considered alongside what is the authoritative auto netting cutoff time semantics and what are the ratan netting rule match and precedence semantics.

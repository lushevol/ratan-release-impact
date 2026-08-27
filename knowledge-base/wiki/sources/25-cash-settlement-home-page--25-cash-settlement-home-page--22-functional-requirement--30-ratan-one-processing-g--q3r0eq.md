---
type: source
title: "Ratan One Processing Guide — Business Rules Maintenance"
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, business-rules, settlement, maker-checker, FMO]
related: [ratan, fmo-post-trade-portal, rule-service, business-rule-maintenance, ratan-rule-lifecycle-management, maker-checker-settlement-control, swift-versus-cashflow-suppression, settlement-accounting-suppression, auto-netting-rule-management, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md"]
---
# Ratan One Processing Guide — Business Rules Maintenance

## Scope

This operational guide describes how the Settlements team maintains RATAN One business rules through the front end as part of business-as-usual operations. The process is intended to reduce dependency on Change Releases while retaining approval, segregation-of-duties, testing, and audit controls.

The guide covers authorization limits, Settlement NSTP Rules, cashflow suppression, SWIFT suppression, auto-netting rules, and legacy FX and Equity blotters.

## Governance process

The documented process is:

1. Define the rule purpose, scope, and impact on entities and counterparties.
2. Submit the complete proposal to the MT for review.
3. Obtain MT review of the rule's clarity and impact.
4. After approval, raise an eOPS request for Data Ops to configure the rule in the FMO Post Trade Portal.
5. The designated maker and checker test the rule in UAT.
6. Release the rule to production after successful testing. Amendments identified during UAT return to the MT for review and must pass UAT again.
7. Record the rule and MT approval date in the DOI.
8. Review every rule annually through the MT or a delegate, recording the review date and reviewer in the DOI.

The guide warns that incorrect rule setup can cause payment failure, reconciliation breaks, or excessive NSTP.

## Rule Engine Blotter

The guide states that RATAN One upgraded its Rule Service engine to Drools in 2023 and migrated rule creation, maintenance, and execution to Rule Service. Rule blotters share common features, while the rule engine supports customization.

Documented operations include:

- Selecting a target rule blotter.
- Creating rules with a mandatory reason and optional comment.
- Combining different rule fields as `AND` conditions.
- Grouping rules for complex scenarios.
- Submitting rules for checker approval or rejection.
- Creating dry-run rules that do not execute immediately.
- Disabling live rules and activating dry-run rules for users with operate permission.
- Updating existing live rules with a reason and pending checker review.
- Viewing record-level and whole-rule history.
- Exporting rules.
- Filtering by rule field.

The guide states that rule makers and checkers should be different people for creation and updates. This appears to require clarification against the overview statement that a checker can also perform maker actions.

## Rule tables

The listed business-rule tables are:

- Authorization Limits
- Settlement NSTP Rules (New)
- Suppression Rules [Cashflow]
- Suppression Rules [Swift]
- Auto Netting Rules
- Settlement NSTP Rules [FX & Equity]
- Suppression Rules [FX & Equity]

### Authorization Limits

Authorization limits are aligned with RAZOR so users can approve cashflows within delegated authority. The guide says these limits are not normally expected to change during BAU, although new profiles or amended limits may be configured. New or amended rules require UAT testing before production update.

### Settlement NSTP Rules [NEW]

These rules prevent straight-through processing of cashflows when configured parameters match. The potential increase in NSTP cashflow volume must be assessed before adding a rule or removing an existing rule.

### Cashflow suppression

A matching cashflow suppression rule prevents the cashflow from being sent downstream to RAZOR, FMSRE, or AMH. The cashflow generates neither Payment nor Settlement Accounting. The guide therefore requires careful assessment to avoid payment failures and reconciliation breaks.

The guide says the current cashflow suppression rules were replicated from Murex 2.11.

### SWIFT suppression

A matching SWIFT suppression rule prevents SWIFT/payment generation in RAZOR. The guide identifies the following RATAN profiles as able to update the SWIFT Suppression Rule tile:

- `FMO_BR_APR`
- `FMO_BR_MKR`
- `FMO_OPS`
- `FMO_OPS_SUP`

The guide states that no SWIFT suppression rules were currently configured.

### Auto Netting Rules

The Auto Netting Rules table can configure cashflow auto netting at a predefined date and time. The guide explicitly states that this capability was not required for China Day 1 and was not covered. It also identifies an enhancement requirement to add `VD-1` to the rule.

### Legacy FX and Equity tables

The FX and Equity NSTP and suppression blotters support legacy flows and are maintained by legacy `OPS` and `OPS_SUP` profiles. They are not covered in this guide. The stated future direction is to move the legacy flow to the Strategic flow.

## Rules approval history

The source records two approved NSTP rules:

```text
Rule: NSTP Rule
Criteria: Cashflow.Booking_System_Event==NonEcoAmend
Reason: To prevent duplicate payments on non financial amendments due to SI change from MX2.11; rule changed from 'High Risk NSTP ' to 'NSTP'
Approval history values shown: 2023-11-16 2023-11-21
Approved by: Prakash Gopi

Rule: NSTP Rule
Criteria: Cashflow.Booking_System_Event==Amendment
Reason: To prevent duplicate payments on financial changes done after non financial amendments due to SI change from MX2.11; rule changed from 'High Risk NSTP ' to 'NSTP'
Approval history values shown: 2023-11-17 2023-11-21
Approved by: Prakash Gopi
```

The source labels these values as an `Approval Date` but provides two dates in each row without explaining their meanings.

## Rules review history

The source contains an empty Rules Review History table:

| # | Review Date | Reviewed By | Comments |
|---|---|---|---|
| | | | |

This does not establish that the required annual review has occurred.

## Evidence limitations

The User Access, FMO Post Trade Portal, Architecture, and Login sections contain no substantive content. The SWIFT suppression section points to a missing further-details reference, and the production link for Settlement NSTP Rules is absent. The guide is operational documentation rather than evidence of technical enforcement, interface contracts, or completed annual reviews.

## Related pages

- [[entities/ratan]]
- [[entities/fmo-post-trade-portal]]
- [[entities/rule-service]]
- [[concepts/business-rule-maintenance]]
- [[concepts/ratan-rule-lifecycle-management]]
- [[concepts/maker-checker-settlement-control]]
- [[concepts/swift-versus-cashflow-suppression]]
- [[concepts/settlement-accounting-suppression]]
- [[concepts/auto-netting-rule-management]]
- [[entities/murex-2-11]]
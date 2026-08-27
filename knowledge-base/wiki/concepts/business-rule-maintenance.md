---
type: concept
title: Business-Rule Maintenance
created: 2026-08-22
updated: 2026-08-22
tags: [business-rules, BAU, governance, settlement, UAT]
related: [ratan, fmo-post-trade-portal, rule-service, ratan-rule-lifecycle-management, maker-checker-settlement-control, annual-business-rule-review, cashflow-authorization-limits]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md"]
---
# Business-Rule Maintenance

Business-rule maintenance is the controlled BAU process for proposing, configuring, testing, approving, releasing, and reviewing settlement rules without relying on a Change Release for every change.

## Intended control sequence

A proposed rule should document its purpose, scope, affected entities or counterparties, and operational impact. The proposal is then submitted to the MT for review. After approval, an eOPS request directs Data Ops to configure the rule in the [[entities/fmo-post-trade-portal]]. Designated maker and checker users test the configuration in UAT before production release.

Changes identified during UAT return to the MT for review and must be retested. The final rule and approval date are recorded in the DOI. The MT or delegate reviews each rule annually and records the reviewer and date.

## Risk assessment

The guide specifically identifies the following risks:

- Payment failure.
- Reconciliation breaks.
- Excessive NSTP volume.
- Incorrect routing or suppression of settlement cashflows.

Cashflow suppression requires particular care because a match prevents forwarding to RAZOR, FMSRE, and AMH and produces neither Payment nor Settlement Accounting.

## Scope of controls

RATAN One uses a ring-fenced group of users for Strategic workflow rule maintenance. The guide describes Maker/Checker controls, UAT prerequisites, approval evidence, and annual review obligations. It does not establish whether the portal technically enforces every governance step.

## Open control questions

The source is inconsistent about whether a checker may also perform maker actions. It also describes immediate disable and activate actions for users with operate permission, which may not follow the general approval sequence. These matters require an authoritative entitlement and workflow interpretation.

## Related pages

- [[concepts/maker-checker-settlement-control]]
- [[concepts/ratan-rule-lifecycle-management]]
- [[concepts/annual-business-rule-review]]
- [[stakeholders/data-ops]]
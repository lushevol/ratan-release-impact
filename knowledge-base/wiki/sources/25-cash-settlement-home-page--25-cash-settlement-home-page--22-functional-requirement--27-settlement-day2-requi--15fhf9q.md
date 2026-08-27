---
type: source
title: Migrating BCS to Strategic Workflow
authors: []
year: 2026
url: ""
venue: ""
tags: [cash-settlement, bcs, fmrp, strategic-workflow, migration, functional-requirements]
related: [bcs, fmrp, stella, lms, razor, bcs-vs-fmrp-strategic-workflow, bcs-strategic-workflow-migration, ssi-stamping-behavior-differences, cashflow-stamping-versus-settlement-lms-feed, bcs-cdu-match-status-confirmation, strategic-workflow-static-data-configuration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# Migrating BCS to Strategic Workflow

## Summary

This functional-requirement document describes an early discovery and requirements-gap assessment for migrating **BCS** cashflow processing into the **Strategic Workflow**. **FMRP** is the target or reference implementation, while **Stella** is expected to provide cashflows in Strategic format and **LMS** remains a downstream integration.

The document identifies behavioral differences and unresolved requirements involving business rules, user profiles, static data, SSI stamping, Swift generation, accounting, CDU confirmation, STP eligibility, LMS timing, Cashflow Blotter enrichment, and historical data migration. It does not establish that the migration is approved, implemented, deployed, or UAT-validated.

## Requirements Matrix

| Feature | Description | Dependency | Comment |
| --- | --- | --- | --- |
| Cashflow consumption | need to consume the cashflow in strategic flow - message bridge filter | reply on Stella to send the cashflow in strategic format | |
| Business rules | Need to review existing rules and confirm if any exclusion/inclusion to be considered - NSTP rules - Suppression rule （Swift/Cashflow） | | |
| User Profile | FMO_OPS is used for legacy flow, user need to switch the profile | | |
| Static data | NA Legacy flow and strategic flow share the same static - Nostro static - currency cut off - branch code mapping to be configured in FMRP process: - bridge account - swift related BIC (sender, 53, 58) | | |
| SSI stamping | - FMRP will have ****** in the query condition while current BCS not - FMRP SCB receive will pick primary nostro if no vostro, BCS does not have such logic | | |
| Swift Generation | if any specific logic from Razor side - to be analyzed or replay BCS prod data and recon - if we can use common DV prefix for BCS data instead of EQ prefix? impact to LMS as well, | | |
| Accounting | country scope: SG, UK, HK(fmid =2), JE EBBS accounting only? static data (bridge account) | | |
| CDU confirmation | - currently BCS cashflow is consuming the match status from CDU instead of TDS3 trade info - currently BCS STP process only enabled for internal clients (configured white list) | | |
| LMS integration | currently BCS will send LMS feed after cashflow stamped while FMRP will only send once cashflow released/settled | | |
| Available field for cash | BCS process will query trade to additionally get below field value and set to cashflow blotter Equity Instrument Reference Parent Trade Instrument ![image-2025-11-12_10-49-0.png](attachments/image-2025-11-12_10-49-0.png) | | |
| Historical data migration | | | |

## Key Findings

- Strategic-format intake depends on a message bridge filter and on Stella sending the required format.
- Existing BCS NSTP, Swift-suppression, and cashflow-suppression rules require explicit review; parity with FMRP is not demonstrated.
- Users currently associated with the legacy flow use the `FMO_OPS` profile and must move to the profile required by Strategic Workflow.
- Shared static-data values still require configuration in FMRP. The listed items include Nostro static, currency cut-off, branch-code mapping, bridge account, and Swift-related BICs for the sender, `53`, and `58`.
- FMRP SSI stamping differs from BCS: FMRP uses `******` in the query condition, and FMRP SCB receive selects the primary nostro when no vostro exists.
- Swift-generation behavior requires Razor analysis, replay of BCS production data, reconciliation, and a decision on whether BCS data can use a common `DV` prefix instead of `EQ`.
- The proposed accounting scope is SG, UK, HK (`fmid =2`), and JE, but EBBS-only treatment is not confirmed.
- BCS currently consumes match status from CDU rather than TDS3 trade information, and its STP process is restricted to internal clients on a configured whitelist.
- BCS sends the LMS feed after cashflow stamping; FMRP sends it only after cashflow release or settlement.
- BCS enriches the Cashflow Blotter with `Equity Instrument Reference` and `Parent Trade Instrument` values queried from the trade.
- Historical-data migration is listed without scope or acceptance criteria.

## Evidence and Limitations

The source is a concise requirements matrix rather than an implementation specification, production replay, test report, or approval record. It does not provide:

- The Strategic message contract or message-bridge filter criteria.
- Authoritative static-data values, ownership, environment, or deployment evidence.
- SSI query examples or selection precedence.
- The meaning and downstream contract of the `DV` and `EQ` prefixes.
- The authoritative confirmation source for the target workflow.
- The final EBBS accounting scope.
- Historical-data migration scope, reconciliation method, or acceptance criteria.

The distinctions between BCS and FMRP should therefore be preserved as migration questions and compatibility risks, not treated as final target-state decisions.

## Related Pages

The comparative view is captured in [[bcs-vs-fmrp-strategic-workflow]]. The migration scope is described in [[bcs-strategic-workflow-migration]], with detailed topics covering [[ssi-stamping-behavior-differences]], [[cashflow-stamping-versus-settlement-lms-feed]], [[bcs-cdu-match-status-confirmation]], and [[strategic-workflow-static-data-configuration]].
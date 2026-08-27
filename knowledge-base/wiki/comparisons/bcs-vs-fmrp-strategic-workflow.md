---
type: comparison
title: BCS versus FMRP in Strategic Workflow
tags: [bcs, fmrp, strategic-workflow, cash-settlement, migration]
related: [bcs, fmrp, bcs-strategic-workflow-migration, ssi-stamping-behavior-differences, cashflow-stamping-versus-settlement-lms-feed, bcs-cdu-match-status-confirmation, strategic-workflow-static-data-configuration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# BCS versus FMRP in Strategic Workflow

## Purpose

This comparison records the differences identified between the current **BCS** flow and **FMRP** as the Strategic Workflow target or reference implementation. The source does not confirm which differences are approved target behavior.

## Comparison

| Area | BCS | FMRP or Strategic Workflow implication | Migration concern |
| --- | --- | --- | --- |
| Cashflow intake | Current cashflow-processing flow | Cashflows must be consumed in Strategic format through a message bridge filter, with Stella as the sending dependency | Confirm the message contract, filter criteria, and retry behavior |
| Business rules | Existing NSTP, Swift-suppression, and cashflow-suppression rules require review | Rule parity is not established | Confirm inclusions, exclusions, and exception behavior |
| User profile | `FMO_OPS` is used for the legacy flow | Users must switch to the Strategic Workflow profile | Confirm permissions and operational provisioning |
| Static data | Legacy flow uses shared settlement static data | FMRP still requires configuration for Nostro static, currency cut-off, branch mapping, bridge account, and Swift BICs | Validate parity and deployment ownership |
| SSI stamping | Does not currently use `******` in the query condition; no primary-nostro fallback is identified | Uses `******`; FMRP SCB receive selects the primary nostro when no vostro exists | Decide whether the difference is intentional and test routing outcomes |
| Swift generation | Requires analysis of Razor logic and replay/reconciliation of BCS production data; currently uses `EQ` prefix | Possible common `DV` prefix is under consideration | Confirm identifier compatibility and LMS impact |
| Accounting | Candidate scope includes SG, UK, HK (`fmid =2`), and JE | EBBS-only treatment is unresolved | Confirm accounting scope and bridge-account configuration |
| Confirmation | Consumes match status from CDU rather than TDS3 trade information | Target confirmation source is not stated | Establish the authoritative source of truth |
| STP eligibility | Enabled only for internal clients on a configured whitelist | Target whitelist behavior is not stated | Confirm whether the restriction remains |
| LMS feed | Sent after cashflow stamping | Sent only after cashflow release or settlement | Assess timing, reconciliation, and downstream processing impact |
| Cashflow Blotter enrichment | Queries trade values for `Equity Instrument Reference` and `Parent Trade Instrument` | Target field contract is not specified | Confirm field mappings, nullability, and transformation rules |
| Historical data | Migration requirement is listed without detail | Target treatment is unspecified | Define scope and reconciliation criteria |

## Assessment

BCS and FMRP cannot be treated as behaviorally identical based on this source. The highest-risk differences concern SSI selection, Swift identifiers, confirmation source, STP eligibility, accounting scope, and LMS timing. [[bcs-strategic-workflow-migration]] should remain an open migration assessment until these differences have authoritative contracts and validation evidence.
---
type: source
title: Uber & FXU Technical Live Plan
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, uber, fxu, release-planning, readiness]
related: [uber-fxu-technical-live-and-business-go-live-2026, technical-live-versus-business-live, release-branch-synchronization-and-deployment-gating, what-was-the-final-authorized-deployment-manifest-for-the-2026-03-28-uber-technical-release, what-exactly-separates-eg-np-sa-uber-technical-live-from-business-live, what-controls-authorized-ces-to-be-open-by-default-for-performance-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
authors: []
year: 2026
url: ""
venue: "Internal release-readiness plan"
---
# Uber & FXU Technical Live Plan

This continuously updated release-control plan proposes a technical release targeted for 2026-03-28. Its stated purpose is to reduce repeated Uber-branch merges, development conflict-resolution work, regression effort, and the risk of missed changes.

The source is planning and readiness evidence, not conclusive evidence that the technical release or FXU business go-live completed as intended. Its service matrix includes updates after the target date, including April pipeline records and FXU Phase 2 activity.

## Target and scope

**Target Release Date:** 2026-03-28

| Scope item | Content |
| --- | --- |
| 1 | UBER processing onboarding for EG/NP/SA, without enabling FXU (live on 4th Apr) |
| 2 | Validation flag (New) |
| 3 | SCBML processing for other entities |

The plan therefore distinguishes UBER onboarding for EG, NP, and SA from FXU enablement. [[technical-live-versus-business-live]] records the unresolved boundary raised by PSS: opening production flow data may constitute business live rather than technical live.

## Release-page scope notes

1. CES go live plan, open CES (as default) for PT.
2. Open search tile only available for dev, not for ops
3. BAU scope
4. In scope story?

The CES note does not specify environment, approved user population, duration, approval, rollback, or its relationship to [[002-place-ces-entitlement-mediation-in-auth-service]] and [[003-adopt-two-layer-ces-emergency-disablement]]. The OpenSearch statement is a release-specific access intent, not evidence of a platform-wide implementation or authorization policy.

## Readiness observations

The plan defines readiness prerequisites across code preparation, branch synchronization, prioritized-story and bug-fix verification, BAU alignment, environment preparation, performance testing, regression, production-data processing, and PSS engagement.

Several recorded dates and comments indicate incomplete or delayed readiness work:

- FMRP1 readiness was due 2026-03-04 and recorded as actual 2026-03-06.
- Regression for the 21st release was due 2026-02-27 and recorded as actual 2026-03-06.
- SCBML performance testing was recorded on 2026-03-06, with a stated need to rerun full PT at previous volume.
- Case Enrichment / settlement-method regression is marked “Delayed.”
- PSS requested OLA refresh, exception responsibility clarification, Solace backlog monitoring, knowledge transfer, VAT confirmation, ASRM updates, and Precab/onboarding checklists.

These records demonstrate planned controls and schedule pressure; they do not prove that all entry criteria were closed.

## Explicit deployment controls

A passing pipeline is not treated as deployment authorization. The following component-level controls are explicitly recorded:

| Named subject | Release branch/version recorded | Pipeline / status recorded | Deployment control or comment |
|---|---|---|---|
| `51358-ratan-cash-settlement-group-management-service` | `release/v3.0.0` | Pipeline 20260325.7; UT coverage `Pass` | `DO NOT DEPLOY!!`; rollback version screenshot referenced. |
| `51358-ratan-cash-settlement-orchestration` | `release/v4.0.0` | Pipeline 20260326.5; UT coverage `Pass` | `DO NOT DEPLOY!!` |
| `51358-mfe-cashflow-blotter` | `release/v1.41.1` | Pipeline 20260326.1; UT coverage not stated | `DO NOT DEPLOY!!` |
| `51358-ratan-cash-settlement-fx-utilization-service` | `release/v1.0.0` | Pipeline 20260326.3; UT coverage `Pass` | `DO NOT DEPLOY!!` |
| `51358-ratanone-db-repository` | `develop main` | Multiple Uber and FXU database pipelines | `DO NOT DEPLOY!!`; “Confirmed by Caroline, no need to deploy” for UAT4 and FMRP1. |
| `51358-ratanone-opensearch-agent` | `release/v1.0.1` | Pipeline 20260331.6; UT coverage `Pass` | No “do not deploy” annotation recorded. |

The exclusions apply only to these named components in this plan. They do not establish a general deployment status for other services.

## FXU Phase 2 scope

| Service name | version | Sync with UBER Tech Release Branch | Deployed Env | Pipeline |
| --- | --- | --- | --- | --- |
| utilization service | 2.0.0 | | | |
| message-bridge | | | | |
| accounting-service | v2.1.0 | | deployed on UAT4 | ~~[Pipelines - Run 20260415.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=11627267&view=results)~~ [Pipelines - Run 20260416.5](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=11672798&view=results) |
| group-service | | | | |
| lifecycle-service | | | | |
| query-service | | | | [Pipelines - Run 20260312.3](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=10929532&view=results) |
| orchestration | v4.1.0 | | deployed on UAT4 | ~~[Pipelines - Run 20260312.1](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=10927281&view=results)~~ [Pipelines - Run 20260420.5](https://dev.azure.com/sc-ado/FMQPR/_build/results?buildId=11732014&view=results) |
| db-repo | | | | |
| fe | | | | |

## Caveats

- The 2026-03-28 target predates several pipeline records in the source. This may reflect post-release updates, a delayed release, or a reused release page.
- Some synchronization cells appear to reference pull requests for unrelated repositories and require repository-level validation.
- The static-data-service branch is ambiguous: a struck-through `release/v4.0.3` is followed by `release/v4.2.0`, while the displayed URL retains `release/v4.0.3`.
- The source gives a 4 April FXU target but lacks an authoritative cutover sequence, approved activation record, or final production validation. See [[what-is-the-authoritative-2026-04-04-fxu-go-live-cutover-and-time-zone-sequence]].
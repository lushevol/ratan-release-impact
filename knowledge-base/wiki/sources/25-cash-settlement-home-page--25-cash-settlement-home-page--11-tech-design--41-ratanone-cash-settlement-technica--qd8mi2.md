---
type: source
title: "EG NP SAU UBER Roll Out and FXU Business Go-Live Runbook on 04 04"
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/Release+On+2026-04-04+CR%3A+RATAN+Settlement+-+FXU+Biz+Go-Live"
venue: Confluence
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, uber, fxu, release-runbook, go-live, cash-settlement]
related: [ratan-pss, tdsx, tds3, sabre-pss, edmi, uvt, release-readiness-group-completion-validation, upstream-cashflow-replay-for-group-completion, what-is-the-approved-idempotent-replay-procedure-for-missing-uber-cashflows, what-is-the-authoritative-2026-04-04-fxu-go-live-cutover-and-timezone-sequence, message-bridge, uber-inbound-message-idempotency-and-error-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---

# EG, NP, and SAU UBER Rollout and FXU Go-Live Runbook

## Purpose and scope

This runbook describes the intended operational activities for the 2026-04-04 FXU business go-live and UBER rollout for EG, NP, and SAU. The release work item is [Release On 2026-04-04 CR: RATAN Settlement - FXU Biz Go-Live - Derivative Strategy Projects](https://confluence.global.standardchartered.com/display/DSP/Release+On+2026-04-04+CR%3A+RATAN+Settlement+-+FXU+Biz+Go-Live).

The procedure covers pre-release UVT, EDMI backlog validation, cashflow-group completeness checks, conditional upstream replay or publisher control, Message Bridge shutdown, RATAN installation, and post-release UVT.

The document is an operational plan. Its `Status` and `Evidence` fields are blank, so it does not establish that the release activities were executed or that the go-live succeeded.

## Coordination

- **TDSX:** Rui Li and Ray Guo; SABRE PSS contact: `SABRE.PSS@sc.com`
- **RATAN:** Ruiheng Cao, Xinmiao Huang, and Yonghua Li; RATAN PSS contact: `RATAN_PSS_SME@sc.com`
- **MO:** Responsible for booking new trades and performing UVT.
- **Release scope:** EG, NP, and SAU; several runbook comments use `SA` instead of `SAU`.

## Intended sequence

1. Book new trades and perform pre-release UVT on 2026-04-03.
2. Confirm that the EDMI topic and queue have no message backlog at 9:30 AM SGT on 2026-04-04.
3. Confirm that no incomplete groups or `PENDING` group messages exist for the scoped booking entities at 9:45 AM SGT.
4. If a specific cashflow is missing, ask upstream support to publish or replay it so the group can complete.
5. If many EDMI messages are stuck while publishing continues, ask SABRE PSS to stop the publisher during the permitted green window.
6. Stop Message Bridge during the stated release window.
7. Install RATAN using AIG as the reference.
8. Perform post-release UVT from 2026-04-04 through 2026-04-06.

The country-specific TDS3 and TDSX publisher stop was struck through because stopping only EG, NP, and SA was reported as infeasible. The corresponding publisher restart step was also struck through, and no replacement restart or normalization procedure is documented.

## Group-completion validation SQL

The runbook specifies the following checks for booking entity IDs `401036553`, `400007847`, and `400991880`:

```sql
Whether has group not 'COMPLTED'(expect no records):
select g.* from ratan_cashflow_group_management_service.ratan_cashflow_group g, ratan_cashflow_group_management_service.ratan_cashflow_group_message gm where gm.booking_entity_id in ('401036553', '400007847', '400991880') and g.status != 'COMPLETED' and g.id = gm.group_id ;

Whether has group message 'PENDING' (expect no "PENDING"):
select gm.status, count(status) from ratan_cashflow_group_management_service.ratan_cashflow_group_message gm where gm.booking_entity_id in ('401036553', '400007847', '400991880') group by gm.status ;
```

The first label contains the apparent typo `COMPLTED`, while the executable predicate uses `COMPLETED`. The query predicate is the more precise evidence for the intended status value, but the canonical status contract should be confirmed.

## Operational limitations and ambiguities

- The selective country-level publisher suspension was rejected as infeasible.
- The runbook contains duplicate step number `6`.
- It mixes SGT and CST without providing conversions or an explicit ordering.
- `10:00PM SGT`, `12:00AM SGT`, and `13:00AM SGT` are ambiguous or invalid in the surrounding daytime sequence.
- The Message Bridge stop window is written as `10:00AM SGT - 13:00AM SGT`.
- The runbook does not define the threshold for “lots of messages stuck.”
- The replay procedure does not specify authorization, idempotency keys, ordering, reconciliation, or post-replay evidence.
- No execution timestamps, SQL results, status updates, or evidence links are recorded.

## Evidence boundary

This source is strong evidence for intended ownership, planned controls, and proposed validation queries. It is not evidence of completed deployment, successful UVT, cleared backlog, completed groups, or successful recovery actions.

## Related operational context

The planned Message Bridge shutdown extends the operational context of [[message-bridge]]. The replay contingency should be considered alongside [[uber-inbound-message-idempotency-and-error-state]] and [[message-bridge-deduplication-key-lifecycle]], but this runbook does not establish their implementation behavior.

---
type: project
title: UBER and FXU Technical Live and Business Go-Live 2026
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratanone, uber, fxu, release, go-live]
related: [technical-live-versus-business-live, release-branch-synchronization-and-deployment-gating, what-was-the-final-authorized-deployment-manifest-for-the-2026-03-28-uber-technical-release, what-exactly-separates-eg-np-sa-uber-technical-live-from-business-live, what-is-the-authoritative-2026-04-04-fxu-go-live-cutover-and-time-zone-sequence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
status: active
owner: "Xinmiao Huang and Chen Yang"
start_date: 2026-02-11
target_date: 2026-04-04
---
# UBER and FXU Technical Live and Business Go-Live 2026

## Objective

Prepare RatanOne Cash Settlement for UBER processing for EG, NP, and SA while avoiding repeated branch merges and their associated conflict-resolution and regression costs. The plan separately targets FXU business live for 2026-04-04.

## Scope boundaries

- The proposed technical-release target is 2026-03-28.
- UBER processing onboarding is scoped for EG, NP, and SA.
- FXU is explicitly not to be enabled in the March technical-release scope.
- SCBML processing for other entities and a new validation flag are included.
- Several pipeline-passing services are explicitly excluded from deployment.

The permitted production behavior for the “technical live” state remains unresolved. See [[technical-live-versus-business-live]] and [[what-exactly-separates-eg-np-sa-uber-technical-live-from-business-live]].

## Readiness controls

The plan calls for branch consistency, code freeze and regression, BAU alignment, FMRP1 environment readiness, SCBML performance testing, production-data processing tests, and PSS engagement.

PSS raised operational dependencies including refreshed OLA responsibilities, Uber-consumption backlog monitoring, knowledge transfer, VAT approval, ASRM updates, and onboarding artifacts. The source does not document final closure of these items.

## Delivery status

The source contains post-target-date pipeline entries and FXU Phase 2 UAT4 deployment records. It is therefore insufficient to determine whether the March technical release occurred on schedule or which artifacts reached production.

The authoritative deployment manifest, change record, timestamps, excluded components, rollback versions, and production validation remain open in [[what-was-the-final-authorized-deployment-manifest-for-the-2026-03-28-uber-technical-release]].

## Key dependencies

- [[ratanone]]
- [[uber]]
- [[fxu]]
- [[scbml]]
- [[ratan-pss]]
- [[opensearch]]
- [[fmaa]]
- [[002-place-ces-entitlement-mediation-in-auth-service]]
- [[003-adopt-two-layer-ces-emergency-disablement]]
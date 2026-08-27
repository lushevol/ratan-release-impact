---
type: concept
title: Technical Live versus Business Live
created: 2026-08-24
updated: 2026-08-24
tags: [release-management, go-live, feature-enablement, operational-readiness]
related: [uber-fxu-technical-live-and-business-go-live-2026, release-branch-synchronization-and-deployment-gating, what-exactly-separates-eg-np-sa-uber-technical-live-from-business-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan.md"]
---
# Technical Live versus Business Live

Technical live is the deployment of code or supporting infrastructure into a production-capable environment without necessarily enabling business processing. Business live is the authorized activation of business flows, users, downstream effects, and operational responsibility.

In the UBER and FXU plan, UBER onboarding for EG, NP, and SA is framed as a technical release while FXU enablement is deferred to a stated later business-live date. PSS challenged this classification: opening EG, NP, or SA flow data could itself be business live.

## Required boundary definition

A release should explicitly state whether each of the following is enabled:

- upstream message ingestion;
- cashflow processing and persistence;
- business-user visibility;
- downstream settlement, accounting, or SWIFT transmission;
- operational monitoring and incident ownership;
- external-party or country activation.

A pipeline pass, deployment, and feature enablement are distinct states. The source does not define this activation boundary, so the release classification remains unresolved.
---
type: entity
title: 51358-ratanone-swift-service
created: 2026-08-22
updated: 2026-08-23
tags: [ratan, swift, enisis, mt-mx, korea, microservice, java, release]
related: [ratan, chg1016055, ratan-settlement-korea, swift-mt-mx-integration, settlement-message-routing, story-9971484, india-routing-account-slash-normalization, was-story-9971484-deployed-and-validated-in-production]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/capture slash for India routing account number.md"]
---
# 51358-ratanone-swift-service

`51358-ratanone-swift-service` is a RATAN backend microservice responsible for SWIFT-related integration and message mapping. It is associated with SWIFT-related release scope in [[chg1016055]] and is identified for the INR routing-account slash enhancement governed by [[story-9971484]].

## 2026 Korea and ENISIS Release Scope

The 2026 release-plan source records the following scope:

- ENISIS real-time ingress and egress for MT/MX messages.
- Korea MT210 support.
- KR MX configuration.
- Reuse of `IngressSourceSystem RATAN` for Korea ENISIS processing.
- Code optimization.

### Release Artifact

- Deployment step: `5`
- Branch: `release/v4.3.0.1`
- Package: `4.3.0.1-20260723.3`
- Pipeline run: `20260723.3`
- Owner: Fengke Wu

The package was recorded as merged with `main` and associated with the 2026-07-25 ISO release under `CHG1015864`.

### Production Verification

PIT queries `RATANONE_SWIFT_SERVICE.SWIFT_STATIC_DATA_SENDER_BIC` for `k_fmid = '10036645'`. The source provides screenshot evidence but does not transcribe the returned sender BIC records.

## India Routing-Account Slash Enhancement

The 2025 functional-requirement source identifies this service for the INR routing-account slash enhancement under [[story-9971484]].

### Recorded Change Artifacts

- Feature branch: `feature/9971484_IndiaRoutingAccountNo`
- Intended release branch: `release/v3.3.3`
- Intended pull request: `2321516`
- Pipeline run: `20260109.3`
- Build ID: `9929817`
- Stated version requiring verification: `3.3.2-20251121.7`

### Modified Components

The source names the following implementation and test components:

- `SwiftMapping.java`
- `MT103_202CovTest.java`
- `MT103Test.java`
- `MT202FlipTest.java`
- `MT202Test.java`

The 2025 functional-requirement source does not prove that the stated version was deployed. Deployment and validation remain tracked by [[was-story-9971484-deployed-and-validated-in-production]].
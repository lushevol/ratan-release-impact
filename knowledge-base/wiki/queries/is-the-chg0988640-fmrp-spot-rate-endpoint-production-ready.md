---
type: query
title: Is the CHG0988640 FMRP Spot-Rate Endpoint Production-Ready?
created: 2026-08-22
updated: 2026-08-22
tags: [query, FMRP, production-readiness, inter-entity-netting, CHG0988640]
related: [chg0988640, fmrp, inter-entity-netting-spot-rate-retrieval, ratan-inter-entity-netting-operational-readiness]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md"]
---

# Is the CHG0988640 FMRP Spot-Rate Endpoint Production-Ready?

## Question

Is the FMRP endpoint documented in the CHG0988640 onboarding questionnaire the actual production configuration, or is it only a development/UAT example?

## Evidence

The source gives:

```text
https://sabre-dev-cloud-global.uk.standardchartered.com/fmrp-fx-fxcs/uat/rate/{date}/OFFICIAL_EOD/USD
```

The URL contains both `dev` and `/uat/`. The source does not provide a production URL, caller identity, authentication method, certificate arrangement, timeout, retry backoff, idempotency policy, fallback rate policy, or behavior after three failed attempts.

## Required resolution

Confirm the production endpoint and deployment configuration, the owning RATAN service or job, the scheduler timezone, rate-date semantics, holiday behavior, failure alerting, and recovery procedure.

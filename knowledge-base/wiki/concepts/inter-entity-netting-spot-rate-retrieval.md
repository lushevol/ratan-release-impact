---
type: concept
title: Inter-Entity Netting Spot-Rate Retrieval
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, spot-rate, FMRP, rate-retrieval, cron]
related: [inter-entity-netting, ratan, fmrp, chg0988640, what-is-the-canonical-auto-netting-job-schedule-and-timezone, is-the-chg0988640-fmrp-spot-rate-endpoint-production-ready]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md"]
---

# Inter-Entity Netting Spot-Rate Retrieval

## Definition

Inter-Entity Netting requires an official end-of-day USD spot rate retrieved through an FMRP interface. The source describes the call as real-time but invokes it from a scheduled inter cron task.

The stated endpoint is:

```text
https://sabre-dev-cloud-global.uk.standardchartered.com/fmrp-fx-fxcs/uat/rate/{date}/OFFICIAL_EOD/USD
```

The stated schedule is:

```text
0 0 1 * * TUE-SAT
```

This appears to run at 01:00 on Tuesday through Saturday, but the scheduler timezone is not documented.

## Claimed resilience

The onboarding questionnaire claims that the interface automatically retries three times and writes an error log when the interface fails. It does not specify retry intervals, backoff, timeout, alerting, transaction-blocking behavior, fallback to a previous rate, or manual recovery.

The source also claims protocol-level ACK/NACK, pre-send NFR/schema validation, and atomic transactional writes. These are release assertions and should not be generalized to every RATAN integration without corroborating design or test evidence.

## Readiness concerns

The endpoint contains `dev` and `/uat/`, which creates an unresolved production-readiness concern. The source does not identify:

- The production URL.
- Authentication or caller identity.
- Certificate or trust-store configuration.
- Timeout and retry policy details.
- The meaning of `{date}`.
- Holiday and prior-business-day handling.
- Idempotency or duplicate-request behavior.
- The owning RATAN service or scheduled-job implementation.
- The behavior when all retries fail.

These issues are tracked in [[queries/is-the-chg0988640-fmrp-spot-rate-endpoint-production-ready]] and [[queries/what-timezone-governs-the-inter-entity-netting-rate-fetch-cron]].

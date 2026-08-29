---
type: source
title: Netting Test Result
authors: []
year: 2025
url: ""
venue: Internal technical design document
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, performance-testing, lifecycle-update, retry]
related: [cashflow-netting-performance, lifecycle-batch-status-update-api, cashflow-batch-transaction-atomicity, cash-settlement-performance-and-stress-testing, does-netting-meet-the-required-throughput-sla-at-production-volume, what-are-the-bounded-retry-idempotency-and-dead-letter-controls-for-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result.md"]
---
# Netting Test Result

This internal test record reports two Cash Settlement netting execution observations and one controlled retry scenario for the lifecycle batch status update api.

## Netting observations

| Input cashflows | Recorded duration | Approximate throughput | Reported exception |
|---:|---:|---:|---|
| 5,000 | 1.9 minutes | 43.9 cashflows/second, assuming 1.9 minutes equals 114 seconds | `cashflowN00000013565` moved to `TechFailed` because booking entity or counterparty `fmcode` was missing |
| 1,994 | 47.3 seconds | 42.2 cashflows/second | None reported |

The two observed throughputs are close, but the source provides only two runs. It does not identify the environment, hardware, configuration, concurrent workload, input-data distribution, repetitions, percentile latency, or acceptance target. These observations are therefore indicative test evidence, not proof of a production SLA.

The source includes screenshots for netting execution, resultant cashflows, resultant cashflow events, and samples of component cashflow events. The 5,000-cashflow run also demonstrates that a missing booking-entity or counterparty `fmcode` can cause an individual cashflow to transition to `TechFailed`.

## Controlled duplicate-index retry

The source tests duplicate unique-index recovery through:

```bash
curl --location 'localhost:8991/v2/ratan/lifecycle/update/status/batch/transactional' \
--header 'Content-Type: application/json' \
--data '{
    "lifecycleRequests": [
        {
            "cashflowId": "M01750766262",
            "businessVersion": "0",
            "minorVersion": "23",
            "ratanAction": "Comment",
            "nettingId": "10000023",
            "comment": "wufengke"
        },
        {
            "cashflowId": "M01750767483",
            "businessVersion": "0",
            "minorVersion": "23",
            "ratanAction": "Comment",
            "nettingId": "10000023",
            "comment": "wufengke"
        }
    ]
}'
```

Reported sequence:

1. Execution was paused in debug mode before database execution.
2. `M01750767483` was manually changed from revision `23` to `26` in a database client.
3. Execution resumed; the duplicate-conflicted item failed and only one saved domain event was returned.
4. The application triggered a retry.
5. The final revision of `M01750767483` became `27`.
6. The retry was reported as successful.

This controlled scenario demonstrates one successful retry path, but it does not establish the violated unique constraint, caller-visible atomicity, domain-event idempotency, retry count, backoff, conflict classification, dead-letter behavior, or behavior under production concurrency.

## Related pages

- [[cashflow-netting-performance]] records the scope and limits of these netting measurements.
- cashflow batch transaction atomicity tracks the unresolved partial-persistence and event-consistency semantics.
- does netting meet the required throughput sla at production volume tracks the missing performance acceptance criteria.
- what are the bounded retry idempotency and dead letter controls for cashflow processing tracks retry and idempotency controls not specified by this test.
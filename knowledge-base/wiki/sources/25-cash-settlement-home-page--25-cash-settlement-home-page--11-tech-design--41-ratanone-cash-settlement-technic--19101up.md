---
type: source
title: PT Result for UBER
authors: []
year: 2025
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber, performance-testing, scbml, stp]
related: [uber, scbml, uber-scbml-performance-regression-testing, does-uber-adoption-meet-the-scbml-no-regression-performance-requirement, why-do-round-1-uber-performance-test-record-counts-not-reconcile, what-are-the-netting-and-unnetting-performance-results-for-uber-integration, does-message-bridge-change-uber-end-to-end-stp-performance, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku, tdsx-uber-message-listener, netting-service, solace-to-kafka-fan-in]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md"]
---
# PT Result for UBER

## Summary

This source records a first-round performance-test observation for the Uber integration. Its mandatory objective is to show that Uber adoption does not affect the existing [[scbml]] flow. A secondary, nice-to-have objective is to show that Uber messages perform better than SCBML messages.

The documented test is explicitly **without message bridge**. It reports one mixed-workload Settlement STP measurement but provides no SCBML-only control run, pre-Uber baseline, acceptance threshold, percentile latency, throughput, error rate, resource telemetry, or timing-boundary definition. It is therefore preliminary performance evidence rather than a demonstration of either stated objective.

## Scope and objectives

The stated performance-test scope is:

| SN. | Description |
| --- | --- |
| 1 | Settlement STP flow |
| 2 | Netting/UnNetting |

The stated objectives distinguish two claims:

1. Uber adoption has no performance impact on the existing SCBML flow — mandatory.
2. Uber message performance is better than SCBML message performance — nice to have.

The source provides no Netting/UnNetting result and no separate Uber-versus-SCBML measurement.

## Round 1 workload

Round 1 was run without Message Bridge.

| Source | Stated volume |
| --- | ---: |
| Murex | 7,000 |
| Stella | 7,000 |
| Uber | 100 messages / 200 cashflows |

## Reported Settlement STP time cost

| Average | Maximum | Minimum | Total |
| ---: | ---: | ---: | ---: |
| `00:00:03.401777` | `00:00:14.553234` | `00:00:01.474934` | `13737` |

The timing start and end events represented by “Settlement STP Time Cost” are not defined.

## Persisted-record count query

The source records the following SQL verbatim. The `tr` token before the third scalar subquery is preserved as written and may prevent direct execution.

```sql
select
	*
from
	(
	select
		count(1)
	from
		ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history rcsh
	where
		cashflow_id like 'M01XMX%'
		and create_time >= '2025-11-21 04:50:00'
		and active = 'ACTIVE') as murex_cashflow,
	(
	select
		count(1)
	from
		ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history ready
	where
		cashflow_id like '1XSA%'
		and create_time >= '2025-11-21 04:50:00'
		and active = 'ACTIVE') as stella_cashflow,
	tr
(
	select
		count(1)
	from
		ratan_cashflow_group_management_service.ratan_cashflow_group_message rcgm,
		ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history hi
	where
		rcgm.trade_id like '1UN%'
		and rcgm.created_at > '2025-11-21 04:50:00'
		and rcgm.cashflow_id = hi.cashflow_id
		and hi.active = 'ACTIVE') as uber_message;
```

Recorded query output:

```text
count|count|count|
-----+-----+-----+
 6773| 6967|  200|
```

## Interpretation limits

The observed Murex count is 227 below the stated workload of 7,000, and the Stella count is 33 below that target. The `uber_message` result is 200, matching the stated Uber cashflow count rather than the stated 100-message count; the source does not explain whether each Uber message generated two cashflows.

The reported STP total of 13,737 does not equal the simple sum of the displayed counts (13,940). The measured population or aggregation rule behind the total is undocumented.

Because the run has neither a matched SCBML-only baseline nor an Uber-versus-SCBML comparison, it does not establish no regression or Uber performance superiority. Because Message Bridge was excluded, it also does not establish end-to-end production-path performance. Related integration design is documented in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku]].
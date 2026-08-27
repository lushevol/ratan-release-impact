---
type: query
title: What Is the RATAN Counterparty Cache Freshness and Failure Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, cache, counterparty-data, freshness, failure-handling, monitoring]
related: [ratan-counterparty-data-integration, ratan, dqsl, bpsi, sci, what-is-the-authoritative-ratan-operational-monitoring-and-alerting-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---
# What Is the RATAN Counterparty Cache Freshness and Failure Policy?

The source states that RATAN refreshes cached SCI counterparty data daily at `03:00 SGT` and makes a real-time downstream request on a cache miss. It does not define the cache lifecycle or failure policy.

## Questions to Resolve

- What cache keys, storage technology, retention period, and expiry policy apply?
- Does the scheduled refresh cover all counterparties or only a selected population?
- What happens if the `03:00 SGT` refresh fails partially or completely?
- Can RATAN display stale data, and how is staleness identified to users or operators?
- Do real-time cache-miss results populate or update the cache?
- What occurs when DQSL, BPSI, or SCI is unavailable during a cache miss?
- Which metrics, alerts, owners, and escalation procedures apply to refresh health, cache-miss rate, and downstream failures?

## Evidence

[[ratan-counterparty-data-integration]] is the current evidence for the refresh schedule and real-time fallback. It provides no SLA, stale-data policy, monitoring threshold, or recovery procedure.
---

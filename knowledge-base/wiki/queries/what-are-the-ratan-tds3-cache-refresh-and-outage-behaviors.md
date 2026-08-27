---
type: query
title: What Are the RATAN–TDS3 Cache-Refresh and Outage Behaviors?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tds3, cache, data-freshness, outage, blotter]
related: [ratan-tds3-trade-lake-integration, ratan, tds3]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
---
# What Are the RATAN–TDS3 Cache-Refresh and Outage Behaviors?

RATAN is documented as both storing TDS3 trade data for the trade blotter and making real-time TDS3 queries for blotter display. It also caches `trade_external_id` and `clearing_organization_trade_id` for the cashflow blotter. The interaction of these patterns is unspecified.

## Information Needed

- Which trade and cashflow fields are persisted, cached, or queried live.
- Cache TTL, refresh triggers, invalidation rules, and retention periods.
- Freshness and latency targets for stored versus live blotter data.
- The user-visible and processing behaviour when TDS3 is unavailable.
- Whether stale data can be displayed and how it is identified.
- Retry, fallback, reconciliation, and recovery procedures after an outage.
- Whether latest-trade-version retrieval during manual validation has a separate outage policy.

Clarifying these behaviours is necessary to determine whether RATAN's blotter and settlement data can be relied upon during TDS3 latency, interruption, or delayed data publication.
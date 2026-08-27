---
type: query
title: How Are Disconnected Cashflow Notifications Recovered?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-notification, websocket, recovery, replay, reliability]
related: [query-service, cash-settlement-data-entitlement, websocket-zombie-session, websocket-session-lifecycle-and-pure-lookup, ces-data-entitlement-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# How Are Disconnected Cashflow Notifications Recovered?

## Question

When a cashflow-blotter WebSocket client disconnects and later reconnects, what mechanism restores cashflow notifications missed during the disconnected interval?

## Why This Is Open

The documented incident supports dropping outbound messages addressed to sessions already removed from the registry. That is the correct behavior for preventing zombie sessions, but it does not provide end-to-end notification recovery.

The frontend is reported to reconnect automatically, yet a reproduction observed that notifications emitted after the client received error `4500` were not received after reconnecting. No replay contract, cursor, durable per-user queue, snapshot refresh, or blotter reconciliation procedure is specified.

## Evidence Needed

- The authoritative semantics of error `4500` in the deployed SockJS/WebSocket stack.
- Whether the frontend performs a fresh authoritative blotter query after reconnect.
- Whether Kafka event offsets, event IDs, or timestamps can support per-client replay.
- Expected recovery-time and completeness requirements for cashflow updates.
- Whether entitlement filtering is consistently applied to any replay or refresh path.
- Operational metrics for disconnects, missing-session outbound drops, reconnects, and recovery completion.

## Related Context

[[websocket-session-lifecycle-and-pure-lookup]] defines the safe behavior for stale outbound work. [[cash-settlement-data-entitlement]] and [[ces-data-entitlement-integration]] need an explicit reliability contract that covers both authorization and delivery recovery.
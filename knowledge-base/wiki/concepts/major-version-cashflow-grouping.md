---
type: concept
title: Major-Version Cashflow Grouping
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, cashflow-events, major-version, grouping, SCBML]
related: [ratanone, scbml, cashflow-group-management-service, cashflow-group-and-message-state-machines, release-readiness-group-completion-validation, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events.md"]
---
# Major-Version Cashflow Grouping

Major-version cashflow grouping is the proposed RATANONE method of organizing related cashflow events by a stable trade ID and a trade-level major version.

## Group identity

The conceptual group key is:

```text
(tradeId, majorVersion)
```

A sequence count identifies each event's position and the expected number of events within the group. For example, `1_5` represents the first event of five.

Major version is carried in the cashflow identifier. Trade ID is sourced differently for Stella and Murex cashflows, while the sequence count is carried in the SCBML `cashflowSequence` link identifier.

## Processing gates

A group is eligible for processing only when:

1. All expected events in the group have arrived.
2. No earlier major-version group remains in a pending state.

This separates group completeness from predecessor ordering. `PENDING_PRE_GROUP` represents the condition in which the current group is complete or otherwise known but must wait for earlier groups.

The design proposes that `COMPLETED` and `PENDING_WITHDRAWAL` predecessor events can cause later pending groups to resume. It does not specify how expected counts are persisted, how excess events are handled, or how missing and duplicate messages are recovered.
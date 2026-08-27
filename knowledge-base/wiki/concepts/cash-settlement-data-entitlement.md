---
type: concept
title: Cash Settlement Data Entitlement
created: 2026-08-24
updated: 2026-08-24
tags: ["cash-settlement", "data-entitlement", "authorization", "access-control", "data-sovereignty", "regulatory-control", "m7", "ces", "jsonb"]
related: ["25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--29-cash-settlement-system-design--2--1d8dihe", "where-is-cash-settlement-data-entitlement-enforced", "ces", "query-service", "ssdr", "ces-data-entitlement-integration", "entitlement-based-notification-delivery", "auth-service", "fmaa", "canonical-ces-field-to-cashflow-jsonb-mapping", "does-one-hour-ces-entitlement-cache-ttl-meet-access-revocation-requirements"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Data Entitlement Fetch Flow.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# Cash Settlement Data Entitlement

Cash Settlement data entitlement is the mechanism and policy-driven restriction that limits a user's access to business data and cashflows according to the user's location, function, and conditions evaluated by [[ces|CES]]. The documented business driver is mitigation of M7 regulatory risk.

It is distinct from EMS2 function entitlement: the documented design retains [[ems2|EMS2]] function-entitlement behavior while CES supplies data-access filters.

## Policy characteristics

The documented business scenarios imply that an entitlement decision may need to evaluate:

- the user's location;
- the user's function or role;
- the country or domicile of the requested business data;
- supported-country assignments;
- country-specific prohibitions; and
- explicit exceptions, such as production-support access.

The source requires configurable restrictions that support:

- onshore access boundaries;
- cross-country support arrangements;
- GBS support assignments;
- explicit country prohibitions; and
- narrowly defined production-support exceptions.

These examples are not the final policy. Country Compliance teams are expected to provide the actual prohibitions and approvals.

## CES condition model

CES returns field/value allow-list conditions and may provide a logical indicator such as `OR`. CES Data Profiles, which are role-linked, generally take precedence over HR-profile-linked Data Policies.

RATAN converts the CES model according to the enforcement interface:

- A Specification JSON representation feeds JPA and JSONB filtering for GraphQL cashflow queries.
- JSONB SQL predicates are injected into SSDR SQL.
- A cashflow event is directly evaluated for WebSocket delivery.

All documented implementations are constrained to fields available in `cashflow_data.cashflow`. An unknown field does not necessarily produce an SQL error; it can silently result in no matching cashflows. The supported CES field catalogue and source-to-storage mapping require an authoritative contract in [[canonical-ces-field-to-cashflow-jsonb-mapping]].

## Enforcement scope and boundaries

The preliminary business scope covers:

- [[ssdr]];
- GraphQL access to [[cashflow-blotter]];
- Cashflow history;
- WebSocket notification subscriptions;
- potentially Group blotter; and
- potentially `/v1/query/cashflows`.

BCS blotter is explicitly excluded from day-one scope.

Entitlement must be considered across both request-response and long-lived subscription interfaces. The technical CES integration describes the following enforcement methods:

- **GraphQL:** entitlement constraints are added transparently to cashflow blotter queries.
- **SSDR:** CES-derived JSONB predicates are appended to the SQL `WHERE` clause.
- **WebSocket:** an outbound interceptor checks whether each event matches the recipient's conditions before user-specific delivery.

The source does not define whether policies filter records only or also protect aggregates, counts, exports, pagination metadata, history, notification payloads, and already-established sessions.

## Entitlement retrieval and caching

[[auth-service|auth-service]] retrieves CES results using [[fmaa|FMAA]] authentication, caches them in Redis for a documented default of 3,600 seconds, and provides the entitlement result to consumers. [[query-service|Query Service]] applies the result without maintaining an additional entitlement cache.

## Failure and emergency behavior

The intended normal behavior is fail-closed. A user query fails when CES is unavailable, the user is not onboarded, entitlement data is missing, or values are empty.

A separate emergency control can disable CES enforcement globally or for individual users. When this bypass is active, consumers receive `enabled: false` or otherwise revert to behavior without CES data filtering. This is a privileged availability downgrade, not ordinary authorization behavior, and must be governed as such. See [[adopt-two-layer-ces-emergency-disablement]] and [[what-controls-govern-ces-entitlement-emergency-bypass]].

## Current control gap

Cashflow blotter and Cashflow notification are described as using mock entitlement as of 10 December 2025. The source supplies no guarantee that mock entitlement is compliant, complete, or suitable for production controls.

[[ces]] is the stated strategic target, while the detailed enforcement contract remains open.

## Freshness limitation

The one-hour Redis cache reduces dependency on CES but can delay enforcement of a new restriction or revocation. The source describes this latency as tolerated but does not evidence business approval for urgent revocation or data-sovereignty scenarios. See [[does-one-hour-ces-entitlement-cache-ttl-meet-access-revocation-requirements]].
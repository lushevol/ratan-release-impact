---
type: concept
title: Java LocalDateTime and PostgreSQL Timestamp Semantics
created: 2026-08-24
updated: 2026-08-24
tags: [java, localdatetime, zoneddatetime, postgresql, timestamp, timezone]
related: [utc-runtime-and-database-timezone-standardization, what-is-the-approved-indonesia-business-timezone-and-temporal-data-model, postgresql, ratan-indonesia]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia.md"]
---
# Java LocalDateTime and PostgreSQL Timestamp Semantics

Java and PostgreSQL temporal mappings must preserve the intended business meaning of a value: an unambiguous instant, a local date and time, or a date-only business value.

The source labels Java `LocalDateTime` conversions to database timestamps, strings, and `ZonedDateTime` as having no impact. That conclusion is conditional and cannot be treated as a general guarantee because the source does not document column types, conversion APIs, or the assumed timezone.

## Java types

`LocalDateTime` contains date and wall-clock time fields with no offset or timezone. A value returned by `LocalDateTime.now()` reflects the JVM default timezone at creation, but the resulting value does not carry that timezone and is not inherently UTC.

Use a timezone-explicit type for an event instant:

- `Instant` for a global point in time.
- `OffsetDateTime` for an instant with an explicit numeric offset.
- `ZonedDateTime` where regional-zone rules are material.

Converting a `LocalDateTime` to `ZonedDateTime` requires selecting a `ZoneId`. Different selected zones can represent different instants for the same local fields.

## PostgreSQL types

PostgreSQL distinguishes two materially different timestamp types:

- `timestamp without time zone` stores date and time fields without conversion. It is appropriate only for intentionally zone-free local values.
- `timestamp with time zone` (`timestamptz`) represents an instant. PostgreSQL normalizes storage and renders values using the session timezone.

Mapping `LocalDateTime` to `timestamptz` requires an assumed timezone. A mapping is therefore not timezone-independent merely because no visible field adjustment occurs.

## Design implication

[[utc-runtime-and-database-timezone-standardization]] provides a consistent default for infrastructure and operational timestamps. It does not determine the correct type for settlement cutoffs, Indonesia holidays, accounting dates, or reporting dates. Those semantics require an approved domain policy, tracked in [[what-is-the-approved-indonesia-business-timezone-and-temporal-data-model]].
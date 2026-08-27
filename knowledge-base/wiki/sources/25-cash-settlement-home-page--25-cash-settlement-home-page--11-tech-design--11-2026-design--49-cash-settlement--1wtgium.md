---
type: source
title: UTC Time zone impact - Indonesia
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan-indonesia, cash-settlement, timezone, utc, jvm, postgresql]
related: [utc-runtime-and-database-timezone-standardization, java-localdatetime-and-postgresql-timestamp-semantics, what-is-the-approved-indonesia-business-timezone-and-temporal-data-model, cash-settlement-platform, ratan-indonesia, postgresql, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia.md"]
---
# UTC Time zone impact - Indonesia

This technical impact note identifies JVM and PostgreSQL timezone defaults as operational dependencies for the Indonesia Cash Settlement deployment. Its stated direction is to configure application and database environments to UTC.

## Source content

### Has impact

| Case | Sample | Solution |
| --- | --- | --- |
| LocalDateTime.now() will be based on the JVM time zone | `attachments/image-2026-5-12_14-21-36.png` | 1. vm options: `-Duser,timezone=UTC` 2. OS env variable: `export TZ=UTC` |
| Job scheduled cron will be based on JVM time zone | `attachments/image-2026-5-12_14-23-21.png` | |
| Run now()/date function in DB script will be based on DB server time zone | now()/current_date/current_timestamp | 1. postgresql.conf → Timezone = UTC 2. alter database set timezone |

### No impact

| Case | Sample |
| --- | --- |
| Java LocalDateTime ↔ DB timestamp | `attachments/image-2026-5-12_14-58-7.png` `attachments/image-2026-5-12_14-58-34.png` |
| Jave LocalDateTime ↔ String | `attachments/image-2026-5-12_15-11-30.png` `attachments/image-2026-5-12_15-9-51.png` |
| Jave LocalDateTime ↔ ZonedDateTime | `attachments/image-2026-5-12_15-33-1.png` `attachments/image-2026-5-12_15-4-46.png` |

## Interpretation and limitations

The source supports adopting a UTC operational baseline for [[cash-settlement-platform]] and [[ratan-indonesia]]. JVM default time affects `LocalDateTime.now()` and may affect cron evaluation, while PostgreSQL timezone settings affect temporal functions and date boundaries.

The supplied JVM option is recorded above exactly as written. It requires validation before deployment: the conventional Java system property is `-Duser.timezone=UTC`, not `-Duser,timezone=UTC`.

The “No impact” classifications are not sufficient as an approved temporal-data design. The attached screenshots are not inspectable in the supplied text, and the note does not specify PostgreSQL column types, JDBC or ORM mappings, parsing formats, scheduler implementation, or explicit `ZoneId` usage. In particular, `LocalDateTime` is zone-free rather than UTC.

[[java-localdatetime-and-postgresql-timestamp-semantics]] documents the type-mapping distinction. [[utc-runtime-and-database-timezone-standardization]] records the configuration layers requiring validation. The unresolved business-date policy is tracked in [[what-is-the-approved-indonesia-business-timezone-and-temporal-data-model]].
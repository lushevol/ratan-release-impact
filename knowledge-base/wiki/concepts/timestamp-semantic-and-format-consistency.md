---
type: concept
title: Timestamp Semantic and Format Consistency
created: 2026-08-24
updated: 2026-08-24
tags: [timestamps, iso-8601, utc, parsing, precision, api-design]
related: [ratan-indonesia-time-zone-contract, audit-trail, does-idns-time-to-utc-incorrectly-reinterpret-z-suffixed-utc-timestamps]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# Timestamp Semantic and Format Consistency

Timestamp meaning and timestamp serialization are separate contract elements. A label such as “Local Time” does not establish whether an API value is a local wall-clock reading, a UTC instant to display locally, or an incorrectly labelled value.

## Semantically distinct forms

- **Naive date-time:** `2026-07-20T01:15:14.395524` has no zone and cannot identify an instant until a zone is assigned.
- **UTC date-time:** `2026-06-24T10:34:26.086282Z` identifies a UTC instant.
- **Offset-aware date-time:** `2026-07-16T04:12:47+00:00` identifies an instant using an explicit offset.
- **Regional textual date-time:** `Mon Jul 20 01:15:07 WIB 2026` declares a regional zone but is not a standard ISO API representation.

A parser must retain whether an offset was supplied. Accepting offsetless and `Z`-suffixed values through one path risks changing the meaning of an explicit UTC instant.

## Precision

The source records fractions from microseconds through nine digits, including `2026-07-27T10:10:29.236599555`. A platform policy must either preserve the source precision or document permitted truncation. JavaScript `Date` is millisecond-precision, so values beyond three fractional digits need deliberate handling when round-trip preservation is required.

## Evidence in Indonesia Cash Settlement

The source labels numerous `Z`-suffixed values as Local Time and documents an `IdnsTimeToUtc` path that shifts `Z`-suffixed values by seven hours. This is a contract ambiguity, not proof that every affected screen is defective. Field-level implementation and rendered-result testing are required.
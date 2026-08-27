---
type: query
title: What Is the Canonical Indonesia Cash Settlement Timestamp Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, timestamps, utc, api-contract, audit]
related: [ratan-indonesia-time-zone-contract, timestamp-semantic-and-format-consistency, ratan-indonesia, audit-trail, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# What Is the Canonical Indonesia Cash Settlement Timestamp Contract?

The source inventory records a mixed set of UTC, local, naive, offset-aware, and WIB-formatted timestamps. It does not establish a consistent owner or conversion boundary for individual fields.

## Questions to resolve

- Which layer owns conversion for each field: upstream producer, service, BFF, or UI?
- Are Local Time-labelled values ending in `Z` stored UTC instants intended for local display, or local values incorrectly serialized as UTC?
- Is UTC+7 the universal display zone for Indonesia business activity, or does display depend on a business or legal location?
- Which fields require precision beyond milliseconds?
- What replaces the struck-through `trade.execution_Date_Time` and `auto affirm - local date time` fields?
- Which requirements apply to audit-time storage, API serialization, immutability, and display?

## Expected output

Publish a per-field contract covering owner, business meaning, source zone, storage zone, API format, display zone, conversion owner, and precision. The contract should be accepted before UAT and production handover for [[ratan-indonesia-onshoring-2026]].

Related evidence is summarized by [[ratan-indonesia-time-zone-contract]] and [[timestamp-semantic-and-format-consistency]].
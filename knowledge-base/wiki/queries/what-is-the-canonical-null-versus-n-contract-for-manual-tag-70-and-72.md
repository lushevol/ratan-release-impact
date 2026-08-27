---
type: query
title: What Is the Canonical Null versus N Contract for Manual Tag 70 and Tag 72?
created: 2026-08-23
updated: 2026-08-23
tags: [adhoc-ssi, swift, backward-compatibility, nullability, cashflow]
related: [adhoc-ssi-api, manual-swift-tag-70-and-72-flags]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/Adhoc SSI API.md"]
---
# What Is the Canonical Null versus N Contract for Manual Tag 70 and Tag 72?

Existing cashflows have `Manual_Tag_70` and `Manual_Tag_72` set to `null`, while the maker rule specifies `N` when the respective field was not updated.

## Questions

- Does `null` mean the same as `N`, or does it represent a distinct legacy state?
- Must cashflow-details consumers display null as blank, `N`, or another value?
- Must downstream consumers tolerate null values?
- Are historic cashflows expected to be backfilled?
- Must newly created cashflows without manual changes persist `N` rather than null?

A canonical answer is required to maintain backward-compatible behavior across persisted cashflows and query consumers.
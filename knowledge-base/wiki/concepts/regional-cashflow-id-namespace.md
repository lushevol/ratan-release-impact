---
type: concept
title: Regional Cashflow ID Namespace
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-id, netting, splitting, namespace, indonesia]
related: [ratan-id, cashflow-splitting, cashflow-netting-renetting, indonesia-cash-settlement-onshoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design.md"]
---
# Regional Cashflow ID Namespace

A regional cashflow ID namespace prevents generated netting and splitting identifiers from colliding when Ratan GDC and Ratan ID use independent database sequences that each begin at 1.

The Indonesia design proposes replacing hard-coded `N` and `S` prefixes with configurable regional prefixes, suggested as `NID` and `SID`. This change affects the generated identifiers used by [[cashflow-splitting]] and [[cashflow-netting-renetting]].

The source examples are internally inconsistent: they specify `NID` and `SID` as input prefixes but render the output with the existing `N` prefix. Before implementation, the canonical format must define prefix value, total length, zero-padding width, sequence scope, uniqueness guarantee, validation rules, and compatibility obligations for downstream consumers.
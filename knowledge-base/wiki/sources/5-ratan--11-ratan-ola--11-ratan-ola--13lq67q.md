---
type: source
title: RATAN OLA Inventory
authors: [Hao Zhang, Nan Ma]
year: 2025
url: ""
venue: ""
tags: [RATAN, OLA, service-management, decommissioning]
related: [ratan, fm-data-platform-dqsl-rt, asset-control, operational-level-agreement, hao-zhang, nan-ma]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN - OLA/RATAN - OLA.md"]
---
# RATAN OLA Inventory

## Scope

This document is an operational agreement inventory for application relationships involving `RATAN`. It contains a section for live applications with RATAN as provider and a visible table for decommissioned applications. The available content is incomplete: OLA document references, status values, approval email sign-offs, and some other governance fields are blank.

## Decommissioned Applications

The source table is reproduced below with its original values and formatting preserved.

| App | Party A (Provider) | Party B (Consumer) | OLA Document | Status | Approval Email Sign-off | Last Sign-off Date | OLA Expiry Date | Document Author | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RATAN | ~~FM-DATA-PLATFORM(DQSL-RT)~~ | ~~RATAN~~ | ~~~~ | | | 2024-03-14 | 2026-03-14 | @@Hao Zhang | |
| RATAN | ~~RATAN~~ | ~~Asset Control~~ | ~~~~ | | | 2025-07-14 | 2026-07-14 | @Nan Ma | Only common features(login, title access control, theme toggle, common look and feel) are eligible for post trade portal PSS to support if any incident occurs on production |

## Recorded Relationships

- `FM-DATA-PLATFORM(DQSL-RT)` is recorded as the provider to `RATAN`.
- `RATAN` is recorded as the provider to `Asset Control`.
- Both relationships are displayed under **Decommissioned Applications** and use strikethrough formatting for the provider and consumer names. This indicates apparent decommissioning, but the source does not provide a confirmed lifecycle status or decommissioning date.

## Governance Metadata

For the `FM-DATA-PLATFORM(DQSL-RT)` to `RATAN` relationship:

- Last sign-off date: `2024-03-14`
- OLA expiry date: `2026-03-14`
- Document author: `Hao Zhang`

For the `RATAN` to `Asset Control` relationship:

- Last sign-off date: `2025-07-14`
- OLA expiry date: `2026-07-14`
- Document author: `Nan Ma`

Both rows have blank OLA document, status, and approval email sign-off fields. A last sign-off date therefore cannot be treated as proof that approval email evidence is available.

## Support Boundary for Asset Control

The `RATAN` to `Asset Control` comment limits production post-trade portal PSS support to common features:

- Login
- Title access control
- Theme toggle
- Common look and feel

The source does not define PSS, identify its owner, specify support hours or response targets, or state whether the limitation remains applicable after the apparent decommissioning.

## Interpretation and Limitations

The heading referring to live applications and the table referring to decommissioned applications create an unresolved categorisation issue. The future OLA expiry dates also coexist with decommissioned-looking formatting. The source does not establish whether the relationships are live, expired, decommissioned, or pending decommissioning.

`RATAN` is not equated with [[ratanone]] by this source. No technical architecture, API contract, service-level metric, or decommissioning procedure is provided.

## Legend

The source contains a `Legend` heading without accompanying content.
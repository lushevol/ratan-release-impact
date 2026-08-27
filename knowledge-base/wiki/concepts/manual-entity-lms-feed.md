---
type: concept
title: Manual-Entity LMS Feed
created: 2026-08-22
updated: 2026-08-22
tags: [lms, downstream-feed, settlement, ratan, manual-entities]
related: [manual-entity-settlement-enablement, settlement-suppression-exceptions, ratan, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/01 Enabling Settlement for Manual Entities.md"]
---
# Manual-Entity LMS Feed

The manual-entity settlement scope requires Ratan to feed LMS for every active entity row, including entities whose settlement cashflows remain suppressed.

## Feed scope

| Entity | FMID | Feed to LMS |
| --- | ---: | --- |
| BAHRAIN | `10036430` | Y |
| DOHA | `300010782` | Y |
| SLATE_QFC | `401081696` | Y |
| KENYA | `300011525` | Y |
| ZAMBIA | `10041903` | Y |
| UGANDA | `10041902` | Y |
| TANZANIA | `10040387` | Y |
| GHANA | `10037477` | Y |
| NIGERIA | `300084297` | Y |
| SRI LANKA | `10036647` | Y |
| FCBUSLANKA | `10022098` | Y |
| HANOI | `10041530` | Y |
| KARACHI | `10036655` | Y |
| DHAKA | `300011470` | Y |

## Independence from settlement

`SLATE_QFC` demonstrates the required separation:

- Ratan settlement cashflows: suppressed.
- LMS feed: enabled.
- Full settlement static data: not required.
- `STRATEGIC_FM_LIST`: excluded.

Therefore, settlement suppression must not be used as a blanket filter for LMS delivery. LMS testing was tracked through the source's CPT and UAT materials, including Tranche 1 verification.
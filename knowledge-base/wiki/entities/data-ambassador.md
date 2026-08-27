---
type: entity
title: Data Ambassador
tags: [data-access, integration, cash-settlement, tds3]
related: [tds3, trade-information-sourcing-for-cash-settlement]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# Data Ambassador

## Role in the Design

Data Ambassador is the proposed access layer in Option 1 of the [[trade-information-sourcing-for-cash-settlement]] analysis. The unnamed Cashflow service would use it to query [[tds3]] for required trade information on each cashflow event.

## Design Implications

The source attributes two properties to this option:

- It would limit the trade data retained or used within the Payment domain and avoid a full trade-data silver copy.
- It would introduce a new dependency into cashflow processing.

The source does not establish whether Data Ambassador is a synchronous API, event interface, cache, or another data-access mechanism. It also does not define authentication, authorization, timeout, retry, fallback, availability, latency, or observability behavior.

## Status

Data Ambassador is documented as a proposed component of an architectural option, not as a confirmed Cash Settlement integration.

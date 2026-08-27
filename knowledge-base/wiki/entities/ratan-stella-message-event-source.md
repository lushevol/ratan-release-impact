---
type: entity
title: ratan_stella_message_event_source
tags: [cashflow, data-source, cn-settlement, nstp]
related: [confirmation-driven-nstp-exception-auto-closure, trade-cashflow-exception-version-correlation, trade-service-trade-events]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# ratan_stella_message_event_source

`ratan_stella_message_event_source` is identified in the source design as the cashflow data source used to look up CN Settlement cashflows by `tradeId` and `tradeVersion` during confirmation-driven NSTP exception auto-close processing.

The source does not provide its schema, ownership, authoritative CN Settlement indicator, or query definition. The use of `tradeVersion` is subject to the version mapping documented in [[trade-cashflow-exception-version-correlation]].
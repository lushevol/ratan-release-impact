---
type: query
title: Which Trade Information Sourcing Option Is Approved for Cash Settlement?
tags: [cash-settlement, trade-information, architecture, open-question]
related: [trade-information-sourcing-for-cash-settlement, tds3, data-ambassador]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# Which Trade Information Sourcing Option Is Approved for Cash Settlement?

## Question

Has Cash Settlement approved direct per-event querying of [[tds3]] through [[data-ambassador]], or continued use of the existing trade service that consumes all TDS3 trades?

## Evidence

The source describes both options and lists their trade-offs, but records no selected option, decision owner, approval date, environment scope, or implementation plan.

## Information Needed

Resolution should identify:

- The selected sourcing pattern and its scope.
- The approving authority and approval date.
- The concrete Cashflow and trade services involved.
- Availability, latency, timeout, retry, fallback, and observability requirements.
- Storage, retention, replication-lag, governance, and ownership requirements if a silver copy is used.
- The required contract for Entity LEID, Trader ID, and Instrument.

## Status

Open. The source is not sufficient to create an ADR or claim an approved architecture.

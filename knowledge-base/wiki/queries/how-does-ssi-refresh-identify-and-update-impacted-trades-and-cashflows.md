---
type: query
title: How Does SSI Refresh Identify and Update Impacted Trades and Cashflows?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, SSI-refresh, notifications, reconciliation, cashflow]
related: [ssi-refresh-propagation, ssi-stamping-reference-data, static-reference-data-synchronization, trade-level-ssi-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md"]
---
# How Does SSI Refresh Identify and Update Impacted Trades and Cashflows?

## Question

What event, lookup, and processing contract identifies affected current-version trade results and cashflows after SSI data changes?

## Current proposal

The design intends to refresh trade stamping results and cashflow SSI, then notify downstream systems. It limits refresh to the latest major version and proposes a single-partition notification topic for sequential consumption.

## Required resolution

Define the change event, impacted-record query, current-version rule, transaction boundaries, ordering, deduplication, retries, replay, failure recovery, downstream delivery guarantees, and reconciliation process. The design must also explain how refresh interacts with cashflows that have already been stamped or sent downstream.
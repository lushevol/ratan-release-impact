---
type: query
title: How Are Event-Published Cashflows Identified in a Full Uber Snapshot?
created: 2026-08-24
updated: 2026-08-24
tags: [uber-message, event-attribution, cashflow, versioning]
related: [uber-message, full-state-event-attributed-messaging, trade-cashflow-correlation-by-trade-version, cashflow-business-and-message-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# How Are Event-Published Cashflows Identified in a Full Uber Snapshot?

## Question

What identifier distinguishes cashflows affected by the triggering business event from unchanged cashflows included in the complete parent-trade snapshot?

## Evidence

The source proposes checking trade tracking version and cashflow version, but does not define a matching algorithm or authoritative identifier.

## Required resolution

Compare trade tracking versions, cashflow business versions, message versions, event IDs, correlation IDs, and explicit affected-object markers. Confirm behavior for multiple events, retries, amendments, and concurrent updates.
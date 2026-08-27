---
type: concept
title: Single-Cashflow Auto-Netting Exception
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, nstp, exception-handling, lifecycle, scbml]
related: [auto-netting-job-time, lifecycle-service, ratan-rule-service, nstp, payment-stp-exception-catalogue, what-is-the-canonical-scbml-indicator-and-xpath-for-settle-as-single]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# Single-Cashflow Auto-Netting Exception

A single-cashflow auto-netting exception is the intended route for an eligible auto-netting group that contains exactly one cashflow when current time reaches or passes `jobTime`.

[[lifecycle-service]] is to invoke the `SettleAsSingle` action, returning that cashflow to `QUEUED`. [[ratan-rule-service]] is then intended to add an [[nstp]] rule that creates a “Single Cashflow” exception based on an SCBML indicator.

The source is ambiguous about the SCBML representation:

- `SettleAsSingle` is the lifecycle action and is described as the NSTP rule condition.
- `SingleCashflow` is separately named as a new SCBML indicator.
- The XPath for `SingleCashflow` is explicitly unconfirmed.

Consequently, the exception trigger, canonical field name, XPath, field value, and NSTP mapping remain open. This design should not be read as confirmation that the exception is implemented or active.
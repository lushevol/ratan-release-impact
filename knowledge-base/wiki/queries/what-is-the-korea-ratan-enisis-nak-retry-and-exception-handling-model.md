---
type: query
title: What Is the Korea RATAN-ENISIS NAK Retry and Exception Handling Model?
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, nak, exception-handling, retry, operations]
related: [ratan, enisis, ratan-enisis-fm-solace-integration, swift-status-lifecycle-and-reconciliation, what-is-the-authoritative-swift-generation-exception-and-timeout-handling-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# What Is the Korea RATAN-ENISIS NAK Retry and Exception Handling Model?

Exception processing is listed as a RATAN delivery task but is not specified.

The source distinguishes MT NAKs, which provide a FIN error code such as `T28027`, from MX NAKs, which provide free-text NAK detail in `StatusMessage`. RATAN does not consume optional structured `StatusAttributes`.

The missing model must define timeout thresholds, retry eligibility and limits, idempotency and duplicate handling, dead-letter treatment, message-to-cashflow state updates, manual remediation ownership, and handling of correlation failures.
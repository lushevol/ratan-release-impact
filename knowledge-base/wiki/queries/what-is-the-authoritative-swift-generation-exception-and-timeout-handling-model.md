---
type: query
title: What Is the Authoritative SWIFT Generation Exception and Timeout Handling Model?
created: 2026-08-23
updated: 2026-08-23
tags: [swift, exception-handling, timeout, retry, operational-control]
related: [ratan-swift-message-generation, swift-status-lifecycle-and-reconciliation, fmswiftgateway]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# What Is the Authoritative SWIFT Generation Exception and Timeout Handling Model?

## Question

How should RATAN handle missing mandatory fields, technical generation failures, gateway timeouts, EOD failure transitions, retries, reinstatement, and replay?

## Evidence

Templates repeatedly state that missing mandatory values should populate an exception. However, the closed open-question entry for missing mandatory fields, technical issues, and integration timeout says “no exception handling.”

FMSwiftGateway technical ACK/NACK is expected within five minutes, but the requirement does not specify timeout ownership or outcome. It separately states that generation failures remain `READY` until an EOD job changes them to `FAILED`.

## Required resolution

A versioned operational contract should define validation points, error ownership, status transitions, retry idempotency, replay authority, operator action, and reconciliation evidence.
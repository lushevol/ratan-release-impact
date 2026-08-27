---
type: query
title: What Is the Authoritative RATAN-TIS API Error Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, tis, api, error-handling, korea-migration]
related: [ratan-tis-payment-query-integration, ratan, tis, korea-cash-settlement-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# What Is the Authoritative RATAN-TIS API Error Contract?

## Question

What HTTP status, response body, `msg` value, and data shape must RATAN return to TIS for no-data dates, unavailable value dates, validation errors, authentication failures, and service failures?

## Evidence

The source documents HTTP `200`, `400`, `401`, `404`, and `500`. It separately states that successful queries return `msg = "success"` and that data absence, missing value date, or service errors return `msg = "failed"`.

It does not specify whether no data is represented by:

- HTTP `200` with `msg = "failed"`;
- HTTP `404`;
- an empty `rows` array;
- absent or `null` `data`; or
- another error payload.

## Why it matters

TIS needs deterministic retry, operator, and reconciliation behavior. An ambiguous no-data contract can cause a valid empty date to be treated as an interface failure or an actual failure to be silently accepted.

## Needed decision

Define the HTTP method, request body if any, status-code mapping, response schema for each outcome, stable error codes, error messages, and retry policy.
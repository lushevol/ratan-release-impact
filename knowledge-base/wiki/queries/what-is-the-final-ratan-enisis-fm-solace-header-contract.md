---
type: query
title: What Is the Final RATAN-ENISIS FM Solace Header Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [fm-solace, headers, correlation, ims, korea-migration]
related: [ratan, enisis, fm-solace, ratan-enisis-fm-solace-integration, swift-message-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# What Is the Final RATAN-ENISIS FM Solace Header Contract?

The source requires request-response propagation of correlation and tracing fields, but leaves part of the envelope unresolved.

Several `X-Outbound-Property-*` fields are described as allowed to be empty in ENISIS logic. Conversely, `trackingId`, `sender`, `domainName`, `initiatedTimestamp`, and `countryCode` are marked mandatory for Solace while also being pending alignment among OLTP, KR EDMi, and FM Solace.

The final contract must identify, for every header, its mandatory status, authoritative producer, validation rule, response behavior, and treatment when absent.
---
type: query
title: Is Technical ACK FirstSentOK Terminal for RATAN-ENISIS Korea Messages?
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, acknowledgement, amh, settlement-status, retry]
related: [ratan, enisis, ratan-enisis-fm-solace-integration, swift-status-lifecycle-and-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# Is Technical ACK FirstSentOK Terminal for RATAN-ENISIS Korea Messages?

The requirement maps AMH `Status=2` and `StatusText=FirstSentOK` to a technical acknowledgement and says RATAN receives `ACK received` in `StatusMessage`.

It does not state whether this is terminal, whether ENISIS subsequently sends `FinalSentOK` or `FinalCancelled`, or what RATAN status, retry, and cashflow-processing behavior applies while a message has only technical acknowledgement.

Resolution requires the agreed ENISIS response lifecycle and RATAN state-transition specification.
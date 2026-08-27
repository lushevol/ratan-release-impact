---
type: entity
title: Ratan PSS
created: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
tags: ["ratan", "pss", "settlement-operations", "support", "mq", "support-team", "release-operations"]
related: ["ratan", "fmrp", "murex-pss", "settlement-ops", "fmrp-cashflow-status-synchronization", "ratan-one-rule-service", "message-bridge", "release-readiness-group-completion-validation"]
updated: 2026-08-24
---

# Ratan PSS

Ratan PSS is a support and operational function referenced in two source contexts:

- The Murex 2.11 cashflow-integration DOI describes Ratan PSS as responsible for investigating RATAN-side processing and connectivity issues.
- The RATAN rollout runbook assigns RATAN PSS release-readiness and deployment activities.

## Murex 2.11 cashflow integration responsibilities

According to the Murex 2.11 cashflow-integration DOI, Ratan PSS is responsible for:

- Investigating payments in `SNTR` that have been sent to RATAN but remain unacknowledged.
- Checking RATAN connectivity and processing when an acknowledgement is not received.
- During inbound MQ incidents, verifying whether a released request was received and whether an acknowledgement was sent.
- Coordinating with [[murex-pss]] when inbound or outbound processing requires investigation.
- Notifying Settlement users when they need to manually trigger `Status WriteBack` to resend a status update to Murex 2.11.
- Investigating missing mandatory attributes when the documented alert-only fallback is triggered.

The DOI instructs Operations to wait five minutes and refresh the payment view before escalating an unacknowledged `SNTR` payment to Ratan PSS. The DOI does not define a named team mailbox, formal ownership boundary, or service-level agreement for Ratan PSS.

## RATAN rollout runbook responsibilities

The RATAN rollout runbook assigns RATAN PSS responsibility for:

- Confirming that the EDMI topic and queue have no message backlog.
- Validating that no incomplete groups or `PENDING` group messages exist for EG, NP, and SAU.
- Stopping Message Bridge during the release window.
- Installing RATAN using AIG as the reference.

The runbook records planned responsibilities only; it provides no completion status or execution evidence.
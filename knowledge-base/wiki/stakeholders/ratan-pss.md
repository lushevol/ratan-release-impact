---
type: stakeholder
title: RATAN PSS
created: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
tags: ["ratan", "production-support", "ola", "approval", "operations", "cashflow", "pss", "support", "cash-settlement"]
related: ["ratan", "operational-level-agreement-for-settlement-interfaces", "korea-ratan-settlement-migration", "fm-solace", "ratan-batch-ack-nack-gating", "uk-murex-ratan-high-volume-cashflow-feeding", "murex-pss", "cash-settlement-exception-handling", "cash-settlement-ola-break-monitoring", "cash-settlement-dependent-service-failure"]
updated: 2026-08-23
---

# RATAN PSS

RATAN PSS is the Production Support Services function identified in RATAN operational-agreement approval and production-support escalation contexts. The exception-handling runbook identifies RATAN PSS as the primary Ratan operational support group.

## Exception-handling responsibilities

According to the exception-handling runbook, RATAN PSS has the following responsibilities:

- Monitor Ratan service availability and restart inactive Camunda, Lifecycle Service, and Murex adaptor services.
- Investigate Lifecycle Service technical-failure and pending-exception signals.
- Coordinate with DQSL PSS and BPSI PSS when the BPSI API path fails.
- Notify OPS when restored services require cashflow reinstatement or replay.
- Perform second-level monitoring for pending cashflow groups and alert [[murex-pss]] when groups remain incomplete.
- Monitor or escalate Murex status write-back OLA breaks and Ratan-to-Razor OLA breaks.

The exception-handling source does not define a formal SLA, on-call boundary, or authority to initiate recovery actions directly.

## Operational-agreement involvement

According to the Korea RATAN settlement-migration source, the RATAN-to-[[fm-solace]] OLA is waiting for approval from RATAN PSS.

That source does not identify individual approvers, approval dates, decision records, or whether RATAN PSS is also the formal sign-off group for the TLM and TIS OLAs.

## Batch-processing escalation involvement

According to the UK Murex-to-RATAN cashflow-feeding source, RATAN PSS is the production-support function to which RATAN batch NACK issues are escalated during UK Murex-to-RATAN CSV feed processing, involving [[murex-pss]].

That source does not define RATAN PSS's escalation timing, ownership boundaries, or operational runbook.
---
type: concept
title: Operational Level Agreement for Settlement Interfaces
created: 2026-08-23
updated: 2026-08-23
tags: [ola, operations, settlement, support, monitoring, release-governance]
related: [korea-ratan-settlement-migration, korea-murex-ratan-interface-readiness, ratan, ratan-pss, korea-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md"]
---
# Operational Level Agreement for Settlement Interfaces

## Definition

An Operational Level Agreement (OLA) defines operational ownership, support expectations, monitoring responsibilities, escalation arrangements, and interface obligations between systems or support functions.

## Role in the Korea Migration

The Korea migration note uses OLA status as a release-readiness control for:

- Korea Murex to RATAN;
- RATAN to FM Solace;
- RATAN to TLM;
- RATAN to TIS.

FM Solace is awaiting approval from [[stakeholders/ratan-pss]]. TLM and TIS are pending PSS review and sign-off. The Korea Murex-to-RATAN entry still has unresolved MQ, COMP-trade, and monitoring details.

## Required Evidence

An OLA should be associated with:

- an identifiable version;
- named operational owners;
- documented monitoring and alerting;
- escalation and incident procedures;
- support coverage;
- review and approval records;
- a clear relationship to the applicable release or change record.

The source does not include these artifacts. Its “Before go live version” and “New version” fields are largely blank.

## Documentation Versus Approval

The source marks several ASRM changes as `DONE`, but completed runbook edits do not establish that the related OLA or interface has been approved or operationally validated.
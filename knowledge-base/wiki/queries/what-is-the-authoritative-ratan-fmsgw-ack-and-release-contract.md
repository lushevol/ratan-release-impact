---
type: query
title: What Is the Authoritative RATAN-FMSGW ACK and Release Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, fmsgw, acknowledgement, swift, message-release]
related: [fmsgw, amh, fmsgw-manual-validation-queues, manual-entity-settlement-enablement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/004 KENYA SCB KENYA B NBO(GBS).md"]
---
# What Is the Authoritative RATAN-FMSGW ACK and Release Contract?

The UAT confirms that FMSGW returned ACK messages to RATAN in successful inbound, exception, and approval-gated scenarios. It also states that `MT202COV` should be released when `MT103` receives an ACK successfully.

The authoritative contract remains unclear:

- At what stage is an ACK emitted: receipt, validation completion, AMH acceptance, or final release?
- Which identifier correlates `MT103` and `MT202COV`?
- What happens when the associated MT103 ACK is rejected, delayed, duplicated, lost, or times out?
- Are ACK semantics identical for standard, back-value, high-value, and cancellation flows?
- What retry, idempotency, and operational-recovery controls apply?

The Kenya UAT supports successful tested behavior only and does not answer these contract questions.
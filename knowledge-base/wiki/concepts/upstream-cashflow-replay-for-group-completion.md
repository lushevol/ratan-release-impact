---
type: concept
title: Upstream Cashflow Replay for Group Completion
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-replay, group-completion, recovery, uber, release-operations]
related: [sabre-pss, cashflow, release-readiness-group-completion-validation, uber-inbound-message-idempotency-and-error-state, message-bridge-deduplication-key-lifecycle, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# Upstream Cashflow Replay for Group Completion

Upstream cashflow replay is the proposed contingency for a RATAN group that remains incomplete because a required message or cashflow is missing.

The runbook assigns SABRE PSS to publish or replay the specific cashflow needed to allow the group to complete. It also describes a broader publisher-stop intervention when many EDMI messages are stuck while continuous publishing continues.

## Required controls not specified by the runbook

Before this becomes a repeatable recovery procedure, the operating contract should define:

- The authorized operator and approval conditions.
- The canonical cashflow or message identifier used for replay.
- Idempotency and duplicate-delivery behavior across the upstream system, Message Bridge, and RATAN.
- Ordering requirements and handling of partial group state.
- Post-replay group and message validation.
- Evidence required to close the incident or release gate.

This concept is related to, but distinct from, Kafka retry or DLT recovery. The source describes human-operated upstream publication and EDMI monitoring rather than an automated retry mechanism.

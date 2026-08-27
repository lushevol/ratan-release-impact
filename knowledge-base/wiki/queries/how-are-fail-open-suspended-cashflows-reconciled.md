---
type: query
title: How Are Fail-Open SUSPENDED Cashflows Reconciled?
tags: [open-question, resilience, reconciliation, cash-settlement, operational-risk]
related: [fail-open-rule-service-evaluation, ratan-suspended-cashflow-rule-filtering, ratan-rule-service, retry-exhaustion-compensation, dead-letter-queue-recovery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# How Are Fail-Open SUSPENDED Cashflows Reconciled?

Rule-service failure causes the workflow to continue rather than suspend an eligible cashflow. Determine whether these bypasses are:

- Persisted with a rule-evaluation outcome and correlation ID.
- Alerted on through defined thresholds.
- Re-evaluated after service restoration.
- Recalled or compensated if `GroupReadyEvent` or STP output has already occurred.
- Auditable separately for SCBML and Uber sources.

No reconciliation, monitoring, or remediation mechanism is specified in the design.
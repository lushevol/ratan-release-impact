---
type: query
title: What Is the Ratan-Wide Retry-Exhaustion and DLQ Recovery Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, retry, dead-letter-queue, compensation, operational-ownership]
related: [retry-exhaustion-compensation, dead-letter-queue-recovery, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--34-ratan-common-compensation-solutio--hjtzet, trade-validation-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan common Compensation Solution.md"]
---
# What Is the Ratan-Wide Retry-Exhaustion and DLQ Recovery Contract?

The reported Group Management incident shows that a retry-exhausted trade-status event can leave payments pending trade validation. Ratan needs an authoritative contract for messages that cannot complete normal processing.

## Questions to resolve

- What failure classes are retried, dead-lettered, replayed, reconciled, compensated, or manually escalated?
- Does DLQ routing retain the original message, and for how long?
- What do “dropped” and terminal disposition mean operationally?
- Which service or team owns DLQ monitoring, triage, replay authorization, and audit records?
- What payload, error, correlation, and business-state metadata must be retained?
- Which events are idempotent and safe to replay?
- How are affected business records identified and reconciled after a terminal failure?
- What SLOs apply to DLQ backlog age, replay success, and time spent pending trade validation?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--34-ratan-common-compensation-solutio--hjtzet]] requests common exception handling and compensation but does not define the recovery contract.

## Related pages

- [[retry-exhaustion-compensation]]
- [[dead-letter-queue-recovery]]
- [[trade-validation-gating]]
---
type: entity
title: SABRE PSS
created: 2026-08-24
updated: 2026-08-24
tags: [sabre, support-team, publisher-control, cashflow-replay]
related: [upstream-cashflow-replay-for-group-completion, edmi, release-readiness-group-completion-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# SABRE PSS

SABRE PSS is the contingency operator assigned to upstream publication and publisher-control activities during the RATAN UBER and FXU release.

## Runbook responsibilities

SABRE PSS may be asked to:

- Publish or replay a specific missing cashflow so that a group can complete.
- Stop a publisher if many EDMI messages are stuck while continuous publishing continues.
- Start or stop publishing within the SABRE green window.

The runbook does not define replay authorization, idempotency safeguards, the threshold for stopping a publisher, or the post-recovery reconciliation procedure.

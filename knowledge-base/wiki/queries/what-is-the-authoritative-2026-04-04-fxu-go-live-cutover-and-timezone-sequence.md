---
type: query
title: What Is the Authoritative 2026-04-04 FXU Go-Live Cutover and Time-Zone Sequence?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, release-management, timezone, cutover, fxu, uber]
related: [release-readiness-group-completion-validation, ratan-pss, sabre-pss, tdsx, tds3, message-bridge, uvt]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# What Is the Authoritative 2026-04-04 FXU Go-Live Cutover and Time-Zone Sequence?

The runbook contains unresolved sequencing and time notation issues that could affect publisher control, Message Bridge shutdown, RATAN installation, and post-release validation.

The authoritative plan should resolve:

- The intended meaning of `10:00PM SGT` and `12:00AM SGT`.
- The invalid `13:00AM SGT` notation in the Message Bridge window.
- The conversion and ordering between SGT and CST.
- The repeated step number `6`.
- The replacement for the cancelled TDS3 and TDSX publisher stop and restart steps.
- Whether `SA` and `SAU` refer to the same rollout scope.
- The exact publisher-stop threshold for a large EDMI backlog.
- The required restart, reconciliation, and evidence-capture steps.

The source does not establish which interpretation is correct, and its blank status and evidence fields do not confirm that any proposed sequence was executed.

---
type: entity
title: EDMi
created: 2026-08-23
updated: 2026-08-24
tags: [edmi, operations, cash-settlement, korea, migration, messaging, backlog-monitoring, release-readiness]
related: [korea-cash-settlement-migration, sabre-pss, message-bridge, release-readiness-group-completion-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/EG   NP   SAU UBER Roll Out & FXU Business Go-Live Runbook on 04 04.md"]
---
# EDMi

## Role in the Korea Migration

EDMi is listed as an operational and development support function for the Korea cash-settlement migration.

The Korea migration source does not define EDMi's system responsibilities, interface ownership, or technical scope.

## Release-Readiness Monitoring

The RATAN UBER and FXU go-live runbook describes EDMI as a topic and queue platform monitored as a release-readiness dependency.

RATAN PSS is expected to confirm that EDMI has no message backlog before release. If many messages are stuck while publishing continues, SABRE PSS may be asked to stop the publisher.

The go-live runbook does not define EDMI retention, backlog thresholds, ownership boundaries, or recovery evidence.
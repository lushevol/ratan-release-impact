---
type: query
title: How Does RATAN Handle SSI Change Notifications?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, ssi, solace, notifications, event-processing]
related: [ssi-change-notification, ssi-plus, solace, ratan-ssi-stamping, 5-ratan--17-ratan-interfaces--19-ratan-and-ssi-50509--zpvcrt]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# How Does RATAN Handle SSI Change Notifications?

SSI+ publishes update, addition, and deletion notifications to RATAN through Solace. The source does not state RATAN's processing behaviour after receipt.

## Questions

- Does RATAN persist, validate, deduplicate, and acknowledge notifications?
- How are delayed, duplicated, missed, or out-of-order events handled?
- Is replay available after a consumer outage?
- Which notifications trigger cashflow re-evaluation?
- Are downstream settlement systems informed of resulting changes?

The documented requirement for RATAN PSS to monitor the Solace subscription indicates an operational dependency, but not the application-level recovery procedure.
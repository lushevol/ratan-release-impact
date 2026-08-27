---
type: comparison
title: RATAN Uber Migration Options
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, uber, migration, scbml, json, architecture]
related: [uber, scbml, ratan, uber-legacy-workflow-isolation, ratan-strategic-json-data-model, lifecycle-compatibility-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# RATAN Uber Migration Options

## Comparison

| Option | Inbound and outbound model | Effort | Risk to current flow | Advantages | Disadvantages |
| --- | --- | --- | --- | --- | --- |
| Current BAU Flow | FMRP and Murex use SCBML inbound and outbound | - | - | Preserves the current flow | Does not implement the strategic Uber model |
| Strategic RATAN Settlement Data Model principle | FMRP uses UBER inbound; strategic RATAN JSON outbound; Murex is also considered in the migration | Medium | High | One strategic movement; a single strategic data model; eventual removal of SCBML from RATAN processing | Full migration has higher risk and may affect Murex |
| Murex flow no impact principle | Uber uses the strategic JSON model while Murex remains SCBML | Medium plus the effort of managing two workflows | Medium | Minimizes risk to Murex | Requires two workflows and both SCBML and JSON in the RATAN data model |
| Smallest change principle | Uber uses JSON; Murex remains SCBML; SCBML is additionally supported in the strategic model | Small | Low | Only Group Service and Camunda message extraction are mandatory sensitive changes; other services can migrate incrementally | SCBML remains for a long time |

## Interpretation

The options trade strategic simplicity against migration safety. The source's later proposal is a hybrid: isolate the Uber workflow, preserve the legacy workflow, and use compatibility and routing mechanisms where callers cannot be made message-type aware.

This comparison should not be treated as an accepted architecture decision. The final choice, routing ownership, compatibility period, and cutover controls remain unresolved.
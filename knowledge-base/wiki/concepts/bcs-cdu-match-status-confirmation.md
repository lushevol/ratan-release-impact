---
type: concept
title: BCS CDU Match-Status Confirmation
tags: [bcs, cdu, tds3, confirmation, stp, whitelist]
related: [bcs, cdu, tds3, bcs-strategic-workflow-migration, bcs-vs-fmrp-strategic-workflow]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# BCS CDU Match-Status Confirmation

## Definition

BCS CDU match-status confirmation is the current BCS behavior in which cashflow processing consumes match status from CDU rather than trade information from TDS3.

## STP Eligibility

The source also states that BCS STP processing is enabled only for internal clients configured on a whitelist.

## Migration Questions

The Strategic Workflow target must clarify:

- Whether CDU remains the authoritative confirmation source.
- Whether TDS3 trade information has any replacement or supplementary role.
- Whether the internal-client whitelist remains applicable.
- How confirmation statuses and STP eligibility are represented and reconciled.

No target-state interface contract or whitelist is provided by the source.
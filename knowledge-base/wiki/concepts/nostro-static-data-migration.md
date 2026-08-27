---
type: concept
title: Nostro Static-Data Migration
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, migration, historical-data, identifiers, static-data]
related: [nams, ssi-plus, nostro-centralization, nostro-notification-and-refresh, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Nostro Static-Data Migration

## Definition

Nostro static-data migration covers the movement from TP-system-owned Nostro data to the centralized `NAMS` and `SSI+` operating model, including identifier continuity and downstream refresh behavior.

## Historical cashflows

The source explicitly asks whether a historical cashflow linked to a Nostro ID should be refreshed. It does not provide a decision.

Possible policies include:

- Preserve historical associations as originally recorded.
- Refresh all historical references to centralized identifiers.
- Refresh only active or unsettled cashflows.
- Preserve original identifiers while maintaining an old-to-new cross-reference.

These alternatives have different audit, reconciliation, deletion, and operational consequences. The policy is tracked in [[queries/should-historical-cashflows-refresh-nostro-identifiers]].

## Required decisions

Migration design must establish:

- Canonical Nostro identifier ownership.
- Old-to-new identifier mapping.
- Treatment of deleted or superseded records.
- Scope of historical versus active refresh.
- Reconciliation and rollback procedures.
- Interaction with notification-driven refresh.

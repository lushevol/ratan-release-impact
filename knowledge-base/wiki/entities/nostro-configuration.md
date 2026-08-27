---
type: entity
title: Nostro Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, nostro, maker-checker]
related: [static-configuration-management, pending-configuration-change-isolation, bicnetting-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Nostro Configuration

Nostro Configuration is an existing static-configuration domain managed through a maker/checker workflow.

In the source's description, the main table stores the configuration record and changes its status through values such as `ADD_PENDING`, `UPDATE_PENDING`, `DELETE_PENDING`, `SAVE_CONFIRMED`, `DISCARDED`, and `DELETE_CONFIRMED`. A companion audit table records the corresponding workflow events.

The design uses Nostro as a comparison baseline and argues that duplicating this implementation for every future configuration domain would repeat CRUD APIs, status handling, validation, audit recording, gateway registration, entitlements, and frontend work.

Status-filtered effective reads are described as difficult to reason about, particularly when an update is pending and consumers must continue receiving the previous approved configuration.
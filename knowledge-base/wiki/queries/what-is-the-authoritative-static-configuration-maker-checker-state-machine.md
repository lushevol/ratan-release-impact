---
type: query
title: What Is the Authoritative Static Configuration Maker/Checker State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, maker-checker, state-machine]
related: [shared-static-configuration-maker-checker-engine, ratan-static-config-maker-request, static-configuration-auditability, pending-configuration-change-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# What Is the Authoritative Static Configuration Maker/Checker State Machine?

The proposed request table names `pending`, `confirmed`, `rejected`, and `cancelled` statuses, while the existing Nostro and BicNetting implementations use more detailed values such as `ADD_PENDING`, `UPDATE_PENDING`, `DELETE_PENDING`, `SAVE_CONFIRMED`, `DISCARDED`, and `DELETE_CONFIRMED`.

The authoritative state machine remains undefined. It must specify:

- Valid transitions for create, update, delete, approval, rejection, and cancellation.
- Maker/checker separation-of-duties rules.
- Treatment of system-generated changes.
- Concurrency and optimistic-lock behavior.
- Idempotent retries.
- Whether a target can have more than one pending request.
- Atomic persistence of the effective record, request status, and audit event.
- Terminal-state retention and recovery behavior.

The source recommends reusable workflow mechanics but does not select or formalize a state machine.
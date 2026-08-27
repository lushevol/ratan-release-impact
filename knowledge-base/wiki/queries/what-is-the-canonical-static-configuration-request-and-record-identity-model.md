---
type: query
title: What Is the Canonical Static Configuration Request and Record Identity Model?
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, identity, maker-checker, api]
related: [shared-static-configuration-maker-checker-engine, ratan-static-config-maker-request, pending-configuration-change-isolation, static-configuration-auditability]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# What Is the Canonical Static Configuration Request and Record Identity Model?

The proposed APIs use `{target_id}` for update, delete, cancel, approve, and reject actions, while `ratan_static_config_maker_request` has its own `id` and uses a nullable `target_id`.

The identity model must define:

- Which identifier is used for pending create requests.
- Whether approval and rejection address a request ID, a domain record ID, or both.
- How one logical configuration is linked across its full lifecycle.
- Whether multiple pending requests may target one domain record.
- How stale or conflicting requests are rejected.
- How audit events correlate to requests and effective records.

This question is unresolved by the source and should be answered before the shared API or database model is implemented.
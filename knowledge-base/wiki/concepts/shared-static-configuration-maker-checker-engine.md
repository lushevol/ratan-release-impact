---
type: concept
title: Shared Static Configuration Maker/Checker Engine
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, maker-checker, workflow-engine, configuration]
related: [static-configuration-management, ratan-static-config-maker-request, ratan-static-config-audit-log, pending-configuration-change-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Shared Static Configuration Maker/Checker Engine

A shared static-configuration maker/checker engine is the proposed reusable backend mechanism for submitting, approving, rejecting, cancelling, and auditing configuration changes.

Under the separated-table design, domain configuration tables remain typed and domain-specific. The engine stores pending requests in [[entities/ratan-static-config-maker-request]] and writes common audit events to [[entities/ratan-static-config-audit-log]].

The approach is intended to provide common UI management APIs while leaving service-facing fetch behavior to each configuration domain. It requires explicit authorization, target-table allowlisting, request identity rules, transaction boundaries, idempotency, concurrency handling, and state-transition definitions before implementation.
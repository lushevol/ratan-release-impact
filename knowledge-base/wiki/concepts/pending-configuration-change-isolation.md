---
type: concept
title: Pending Configuration Change Isolation
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, configuration, version-control, maker-checker]
related: [static-configuration-management, shared-static-configuration-maker-checker-engine, ratan-static-config-maker-request]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# Pending Configuration Change Isolation

Pending configuration change isolation keeps unapproved maker requests separate from effective configuration records.

The proposed model stores approved data in a typed domain table and pending changes in `ratan_static_config_maker_request`. Service reads therefore return the current approved record without requiring consumers to interpret workflow statuses. A pending update does not replace the effective version until checker approval.

This differs from status-managed designs such as the source's Nostro and BicNetting implementations, where effective reads require status filtering. Isolation can simplify retrieval and version semantics, but it introduces requirements for atomic approval, duplicate-request prevention, conflict detection, and clear UI presentation of effective records alongside pending proposals.
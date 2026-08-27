---
type: concept
title: Cashflow Group Completeness Gating
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, group-management, stp, workflow, message-processing]
related: [ratan-cash-settlement-group-management-service, ratan, force-stp, what-controls-govern-force-stp-for-incomplete-cashflow-groups]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# Cashflow Group Completeness Gating

Cashflow group completeness gating is the RATANONE control under which upstream cashflow messages with the same trade ID and major version are treated as one cashflow group. The Group Management Service persists received messages and only publishes the group to workflow after all messages have arrived.

Where a message is lost or a leg is missing, the source permits rare manual force-STP through the UI. It also describes a resend capability when the cashflow blotter misses a payment.

The design does not define expected legs, completeness calculation, timeout behavior, idempotency, approval control, or reconciliation for a forced group. These gaps are tracked in [[what-controls-govern-force-stp-for-incomplete-cashflow-groups]].
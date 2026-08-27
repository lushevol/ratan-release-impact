---
type: entity
title: MB
created: 2026-08-24
updated: 2026-08-24
tags: [messaging, component, active-active, unresolved]
related: [message-racing-prevention-in-dual-dc-deployments, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Active-Active to Active-Passive.md"]
---
# MB

MB is an undefined system or component referenced in Option-2 of the Indonesia Cash Settlement Platform architecture.

The source states that MB startup should be restricted manually to avoid message racing if the two-cluster design operates as Active-Active. It does not expand the acronym or identify MB’s messages, brokers, consumers, state, or ownership model.

The component and its required dual-data-centre fencing mechanism are tracked in [[queries/what-is-mb-and-how-is-dual-dc-message-processing-fenced]].

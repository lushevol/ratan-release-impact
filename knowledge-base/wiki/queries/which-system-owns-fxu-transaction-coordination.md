---
type: query
title: Which System Owns FXU Transaction Coordination?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, architecture, transaction-synchronization, open-question]
related: [fxu, ratan, tds3, razor, transaction-synchronization, fxu-technical-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# Which System Owns FXU Transaction Coordination?

The FXU design presents three alternatives but does not record a selected architecture:

1. FXU coordinates transactions among TDS3, RATAN, and FXU.
2. RATAN coordinates those transactions.
3. RATAN owns accounting and persistence, with TDS3 involved only when remaining-amount synchronization requires transactional control.

The decision affects exception-management ownership, accounting responsibility, persistence scope, and consistency controls. The missing architecture diagrams do not establish sequencing or failure semantics.

## Evidence to resolve

Confirm the selected option, transaction boundaries, compensation behavior, retry policy, and the owner for Option 3 exception handling.
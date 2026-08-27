---
type: concept
title: RATAN-RAZOR Amendment Propagation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, razor, amendments, withdrawal, cashflow-lifecycle]
related: [ratan, razor, cashflow-business-and-message-versioning, released-settled-amendment-control, ratan-lms-action-event-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# RATAN-RAZOR Amendment Propagation

The documented RATAN-to-RAZOR amendment rule is conditional on settlement state.

- An original Murex flow (`01`) is sent to RAZOR as a `New` event.
- A reverse flow (`02`) is represented in RATAN as a `Withdrawal` of the original RATAN cashflow.
- RATAN sends the withdrawal to [[razor]] only when original flow `01` is settled.
- If original flow `01` is not settled, RATAN suppresses both the original and reverse flows from RAZOR.
- A correction (`03`) has a new RATAN ID and is sent as `New`; the source says it is set to NSTP pending user intervention.

This rule differs from the documented LMS condition, where withdrawal transmission depends on whether the original had already been sent to [[lms]], rather than whether it was settled.
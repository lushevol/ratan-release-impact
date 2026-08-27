---
type: entity
title: VPA
created: 2026-08-22
updated: 2026-08-22
tags: [vpa, allocation, cashflows, fmrp, stella]
related: [mw, stella, ratan, allocation-cashflow-state-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# VPA

VPA is an intermediate component in the allocation flow documented for FMRP. The source gives the flow as:

```text
MW → VPA → Stella
```

The allocation event is expected to generate cashflows for both the block trade and child trades. Block-trade cashflows use `SUSPENDED`, while child-trade cashflows use `PROJECTED`.

The source states that RATAN should filter cashflows from allocation events, but does not define whether filtering is based on event type, allocation flag, cashflow status, or a combination.
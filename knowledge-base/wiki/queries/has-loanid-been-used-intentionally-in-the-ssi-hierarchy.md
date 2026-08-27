---
type: query
title: Has LOANID Been Used Intentionally in the SSI Hierarchy?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, ssi, loaniq, onboarding, legacy]
related: [loaniq, ssi-selection-hierarchy, tag-20-logic, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list.md"]
---
# Has LOANID Been Used Intentionally in the SSI Hierarchy?

The SSI Stamping Hierarchy checklist specifies `CN/MY/IN/SG/LOANID old logic`, while the routing, source-system, and Tag 20 sections consistently refer to [[loaniq]].

## Questions to Resolve

- Is `LOANID` a typographical variant of `LOANIQ`?
- Is `LOANID` a separate identifier or configuration domain?
- If it is distinct, which SSI hierarchy and routing rules apply to it?
- Which operational team owns the authoritative SSI exception list?

No normalization should be applied until the identifier is confirmed.

## Related Pages

- [[loaniq]]
- [[ssi-selection-hierarchy]]
- [[tag-20-logic]]
- [[ratan]]
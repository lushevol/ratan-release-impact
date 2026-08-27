---
type: query
title: What Is the Authoritative Netting State Name and Un-Netting Resultant Identity?
tags: [netting, un-netting, cashflow-status, data-quality]
related: [cashflow-netting-and-un-netting, cashflow-netting-and-un-netting-state-transitions, cashflow-blotter, murex-2-11, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md"]
---
# What Is the Authoritative Netting State Name and Un-Netting Resultant Identity?

The deprecated source uses `NETTING` in its status matrix but `Netted` for netted components in its detailed example. It creates resultant cashflow `C105`, then later marks `C103` as the dead resultant even though `C103` is already a Murex component.

Resolve the durable component state, transient processing states, resultant identity, component restoration rules, and Netting ID clearing behavior. The same example also reports inconsistent amendment amounts, so it cannot safely define an implementation contract.
---
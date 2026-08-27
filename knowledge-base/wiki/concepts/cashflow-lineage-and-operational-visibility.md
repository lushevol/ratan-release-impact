---
type: concept
title: Cashflow Lineage and Operational Visibility
created: 2026-08-24
updated: 2026-08-24
tags: [cashflows, lineage, operational-visibility, ratan, stella]
related: [non-economic-cashflow-amendment-handling, cashflow-version-concurrency-control, cashflow-business-and-message-versioning, fmrp-cashflow-publication-lifecycle, fmrp-cashflow-status-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# Cashflow Lineage and Operational Visibility

For repeated fully non-economic amendments, [[ratan]] retains transitive backend mappings such as `C1 → C3 → C5` and `C2 → C4 → C6`.

The original cashflow remains the sole operationally visible record for [[settlement-ops]]. The latest linked [[stella]] cashflow remains the target for status synchronization, including Released, Netted, and Settled statuses. This separates the stable settlement-facing record from the currently active source-system version.

Equivalent replacement cashflows must not be published to [[razor]], [[lms]], or the Ratan EOD cashflow API. They must nevertheless remain auditable lineage records because they support lifecycle updates and trade-confirmation mapping.

The required representation where an original visible cashflow remains Projected while its latest replacement progresses through lifecycle states is unresolved; see [[how-should-projected-original-cashflows-be-represented-after-non-economic-amendment]].
---
type: concept
title: EMS2 Function Filtering and EMS3 Data Filtering
created: 2026-08-24
updated: 2026-08-24
tags: [EMS2, EMS3, function-filtering, data-filtering, authorization]
related: [ems2, ems3, region-entitled-drawer-filtering, ratan-entitlement-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# EMS2 Function Filtering and EMS3 Data Filtering

The design proposes separating two entitlement concerns:

- **EMS2 function filtering:** whether a user can access or perform a feature or action.
- **EMS3 data filtering:** which regional data, drawers, or blotters should be visible; the documented example is `regionFilter`.

The existing `filterDrawers` behavior is associated with EMS2, and the source says no immediate refactor into an `Ems2AuthFilter` is required. The intended future distinction is architectural guidance rather than a complete contract.

The source does not define precedence when a user passes one filter but fails the other, nor does it establish whether downstream APIs repeat the EMS3 check.
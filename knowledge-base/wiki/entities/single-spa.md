---
type: entity
title: Single-SPA
created: 2026-08-24
updated: 2026-08-24
tags: [single-spa, micro-frontends, frontend-architecture]
related: [ratanone, ratanone-ui-performance, iframe-micro-frontend-loading-priority]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# Single-SPA

## Role in the source

Single-SPA is identified as a possible future framework for replacing or supplementing RatanOne’s iFrame-based micro-frontend composition.

The source argues that iFrame composition provides useful style isolation and cross-domain messaging, but may become harder to optimize as the number of blotters increases. It also identifies duplicated resources and the inability to load shared core JavaScript in the shell as potential limitations.

No migration decision was approved. The source provides no migration plan, cost estimate, compatibility analysis, or acceptance criteria.
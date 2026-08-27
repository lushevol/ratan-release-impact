---
type: entity
title: application_tile
created: 2026-08-24
updated: 2026-08-24
tags: [application-tile, database, configuration, post-trade-portal]
related: [fmo-post-trade-portal, application-tile-filter-storage-options, region-entitled-drawer-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# application_tile

## Role

`post_trade_portal_service.application_tile` stores the tile and blotter configuration consumed by FMO Post Trade Portal.

The adopted design adds a `filterRule` configuration value to this table. The affected lifecycle operations are insert, update, verify, and deactivate.

## Configuration responsibility

The table associates a tile with a region filter. The source recommends validating raw JSON before update or insert and using a typed `List<Drawer>` model rather than `List<Map<String, Object>>`.

Option 3 proposes moving reusable filter definitions to `post_trade_portal_service.application_tile_filter` and adding `filter_code` to `application_tile`, but Option 1 is the documented current implementation.
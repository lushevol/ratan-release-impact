---
type: concept
title: Application-Tile Filter Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [configuration, application-tile, JSON, filter-rule, schema-design]
related: [application-tile, application-tile-filter-storage-options, region-entitled-drawer-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# Application-Tile Filter Configuration

Application-tile filter configuration stores the rule used to decide whether a drawer or blotter is included in the login response.

The current design stores one `filterRule` value on `application_tile`. The rule contains:

- `filterType`, such as `region`;
- EMS3 parameters, including `appId` and `appName`;
- an expression evaluated against entitlement data.

All insert, update, verify, and deactivate paths must preserve and validate this configuration. The source recommends validating raw JSON before persistence and representing the returned drawers as `List<Drawer>` rather than `List<Map<String, Object>>`.

A normalized alternative stores reusable rules in `application_tile_filter` and references them with `application_tile.filter_code`.
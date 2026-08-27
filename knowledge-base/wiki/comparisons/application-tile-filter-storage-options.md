---
type: comparison
title: Application-Tile Filter Storage Options
created: 2026-08-24
updated: 2026-08-24
tags: [application-tile, schema-design, filter-configuration, JSON]
related: [application-tile, application-tile-filter-configuration, region-entitled-drawer-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# Application-Tile Filter Storage Options

| Option | Design | Status in source | Main implication |
| --- | --- | --- | --- |
| Option 1 | Add one `filterRule` column to `application_tile`. | Adopted in current code | Minimal schema change; all tile lifecycle operations must handle the rule. |
| Option 2 | Add separate columns for filter type, parameters, and rule. | Alternative | Makes fields explicit but increases schema surface. |
| Option 3 | Add `application_tile_filter` with reusable filter records and reference it with `filter_code`. | Alternative | Supports centralized reuse and governance but requires an additional table and relationship. |

Option 3's proposed schema is:

```sql
CREATE TABLE post_trade_portal_service.application_tile_filter ( id int4 GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE) NOT NULL, code varchar NULL, is_active bool NOT NULL, filter_type varchar(255) NULL, filter_rule json NULL, CONSTRAINT application_tile_filter_pk PRIMARY KEY (id) );
```

```sql
ALTER TABLE post_trade_portal_service.application_tile ADD filter_code varchar NULL;
```

The source does not define a migration plan from Option 1 to Option 3.
---
type: entity
title: 51358-mfe-cashflow-blotter
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, microfrontend, cashflow, Indonesia]
related: [indonesia-ui-microfrontend-isolation, regional-frontend-dual-build, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# 51358-mfe-cashflow-blotter

`51358-mfe-cashflow-blotter` provides Indonesia cashflow, grouping, dashboard, authorization, netting, threshold, and utilization screens.

## Indonesia output

The shared repository produces:

```text
GDC: ratan_cashflow_blotter.js
Indonesia: idns_cashflow_blotter.js
```

The Indonesia artifact is served through:

```text
/static/idns/idns_cashflow_blotter/idns_cashflow_blotter.js
```

Documented Indonesia screens include:

```text
Cashflow Blotter[ID]: indonesia_cashflow
Grouping Blotter[ID]: indonesia_cashflow_group_management
Cashflow Dashboard[ID]: indonesia_cashflow_dashboard
Authorization Limits[ID]: indonesia_cashflow_authorization_limits
BIC Netting Static[ID]: indonesia_cashflow_bic_netting_static_table
Nostro Threshold Static[ID]: indonesia_cashflow_splitting_static
Utilization Static[ID]: indonesia_cashflow_utilization_static_table
```

The UI requirements include Indonesia-only booking-entity dropdown values and dashboard links to the Indonesia Cashflow Blotter and Grouping Blotter.
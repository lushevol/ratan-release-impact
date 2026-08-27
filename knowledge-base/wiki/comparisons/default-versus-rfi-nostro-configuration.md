---
type: comparison
title: DEFAULT versus RFI Nostro Configuration
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, default, static-data, comparison]
related: [rfi-nostro-stamping-based-on-portfolio, dedicated-nostro-selection, ratanone-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Change List and API.md"]
---
# DEFAULT versus RFI Nostro Configuration

| Aspect | `DEFAULT` | `RFI` |
|---|---|---|
| Purpose | Conventional, non-dedicated Nostro configuration | Portfolio-dedicated Nostro configuration |
| `nostroType` | `DEFAULT` | `RFI` |
| `dedicated` value | Must be `null` | Must be non-null |
| Portfolio metadata | Not applicable | Provided as `dedicated.portfolio` in static-data contracts |
| Classification updates | `nostroType` cannot be updated | `nostroType` cannot be updated |
| Dedicated-data updates | No dedicated data is permitted | Dedicated information may be updated |
| Cashflow-detail representation | `Nostro_Type: "DEFAULT"` and `Dedicated: null` | `Nostro_Type: "RFI"` and `Dedicated: { Portfolio: ... }` |

Both types are returned when a Nostro query omits or supplies an empty `nostroType` filter. The source does not specify whether a matching RFI Nostro must take priority over a matching DEFAULT Nostro; that question is tracked in [[what-is-the-authoritative-rfi-nostro-selection-and-fallback-rule]].
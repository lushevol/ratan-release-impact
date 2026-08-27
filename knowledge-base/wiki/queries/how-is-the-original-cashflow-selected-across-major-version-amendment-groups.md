---
type: query
title: How Is the Original Cashflow Selected Across Major-Version Amendment Groups?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, amendment, major-version, mapping]
related: [group-management-service, cashflow-replacement-mapping, ratan-cashflow-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# How Is the Original Cashflow Selected Across Major-Version Amendment Groups?

The design says that [[group-management-service]] groups cashflows by trade ID and major version. Its POC example nevertheless maps original C301 at major version `1` to replacement C302 in the amendment group at major version `2`.

The deterministic cross-version lookup algorithm is absent. It must define the trade-level search scope, candidate-selection order, behaviour for multiple prior New events, and treatment of chained non-economic replacements.
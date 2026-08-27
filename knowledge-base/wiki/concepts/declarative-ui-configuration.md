---
type: concept
title: Declarative UI Configuration
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, ui, configuration, security, validation]
related: [unified-json-configuration, static-configuration-management, frontend-backend-form-validation, should-ratan-static-config-service-store-functions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# Declarative UI Configuration

Declarative UI configuration represents presentation and selectable behavior as validated data rather than executable code. It is appropriate for labels, tooltips, widths, visibility, field references, permitted operators, status lists, and quick-filter definitions.

The `mfe-cashflow-blotter` inventory includes functions for date calculation, sorting, and conditional styling, as well as component identifiers such as `QuickSearchInput`. These should not be serialized as arbitrary JavaScript by a configuration service.

A hybrid approach keeps implementation in the deployed frontend and stores allow-listed identifiers and parameters remotely:

```json
{
  "styleRule": "QUEUED_WITHOUT_SUBSTATE",
  "comparator": "ID",
  "component": "QuickSearchInput"
}
```

The frontend must reject unknown identifiers. This preserves a controlled code boundary while enabling governed updates to data and supported behavior selection.
---
type: entity
title: 51358-mfe-rules
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, microfrontend, settlement-rules, Indonesia]
related: [indonesia-ui-microfrontend-isolation, regional-frontend-dual-build, ratan-global-rule-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# 51358-mfe-rules

`51358-mfe-rules` provides Indonesia settlement, suppression, and netting rule screens.

## Indonesia output

The shared repository produces:

```text
GDC: ratan_rules.js
Indonesia: idns_rules.js
```

The Indonesia artifact is exposed through:

```text
/static/idns/idns_rules/idns_rules.js
```

Documented Indonesia routes are:

```text
Settlement NSTP Rules New[ID]: indonesia_new_nstp_rules
Suppression Rules [Swift][ID]: indonesia_swift_suppression_rules
Suppression Rules [Cashflow][ID]: indonesia_cashflow_suppression_rules
Netting [ID]: indonesia_new_netting_rules
```

Global rule synchronization from GDC to Indonesia is an explicit UI requirement. The source does not define the synchronization message contract or approval semantics.
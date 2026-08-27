---
type: entity
title: 51358-mfe-ratan-container
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, microfrontend, Indonesia, Cash Settlement Platform]
related: [indonesia-ui-microfrontend-isolation, regional-frontend-dual-build, fmo-post-trade-portal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# 51358-mfe-ratan-container

`51358-mfe-ratan-container` provides the regional container microfrontend for the Cash Settlement Platform.

## Indonesia output

The shared repository produces:

```text
GDC: ratan_container.js
Indonesia: idns_container.js
```

The Indonesia artifact is exposed through:

```text
/static/idns/idns_container/idns_container.js
```

Its documented Indonesia routes include:

```text
/indonesia_cashflow_blotter_cn/*
/indonesia_rules_blotter/*
/indonesia_nostro_static_container/*
```

The source records Indonesia deployment for this component and identifies URL-prefix and route changes as the relevant implementation work.
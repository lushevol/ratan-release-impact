---
type: entity
title: 51358-mfe-nostro-static
created: 2026-08-24
updated: 2026-08-24
tags: [frontend, microfrontend, Nostro, Indonesia]
related: [indonesia-ui-microfrontend-isolation, regional-frontend-dual-build]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia.md"]
---
# 51358-mfe-nostro-static

`51358-mfe-nostro-static` provides the Indonesia Nostro Static screen.

## Indonesia output

The shared repository produces:

```text
GDC: ratan_nostro_static.js
Indonesia: idns_nostro_static.js
```

The Indonesia artifact is served through:

```text
/static/idns/idns_nostro_static/idns_nostro_static.js
```

The documented route is:

```text
Nostro Static[ID]: indonesia_nostro_static
```

The Indonesia implementation includes a URL prefix, an Indonesia route, and a version guard.
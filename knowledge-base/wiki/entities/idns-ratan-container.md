---
type: entity
title: "@fm/idns_ratan_container"
tags: [frontend, microfrontend, indonesia, runtime-package]
related: [ratan-indonesia, ratan-gdc, region-aware-ui-build-dependency-remapping, indonesia-ui-microfrontend-isolation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md"]
---
# @fm/idns_ratan_container

`@fm/idns_ratan_container` is the Indonesia-specific Ratan container package proposed for an ID build of the Cash Settlement UI.

In the shared-repository option, webpack selects this package when `REGION=ID`. The source does not provide its version contract, runtime origin, dependency compatibility requirements, or deployment ownership. See [[region-aware-ui-build-dependency-remapping]].
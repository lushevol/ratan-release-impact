---
type: entity
title: SABRE SDK
created: 2026-08-24
updated: 2026-08-24
tags: [sdk, dependency, sabre, cash-settlement]
related: [ratanone, message-bridge, orchestration, netting-service, swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/UBER Precious Metals.md"]
---
# SABRE SDK

SABRE SDK is the versioned dependency identified as a prerequisite for UBER Precious Metals changes across RATAN domain services.

The documented upgrade is:

```text
Current: v7.23-RELEASE-20260130.2-17e9c9eb
Target:  v7.46-RELEASE-20260805.2-1aaadb3e
```

The source lists `message-bridge`, `orchestration`, `group`, `lifecycle`, `query`, `netting`, `swift`, `utilization`, `open-search`, and `ssi-stamping` as impacted services.

## Naming ambiguity

The source also uses “SEBRA SDK” when describing the dependency. It does not determine whether this is a typo for SABRE SDK or a distinct component. The exact dependency identity should be confirmed before implementation planning.
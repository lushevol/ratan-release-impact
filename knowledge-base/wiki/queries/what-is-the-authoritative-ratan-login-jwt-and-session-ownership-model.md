---
type: query
title: What Is the Authoritative Ratan Login, JWT, and Session Ownership Model?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, login, jwt, session-management, authorization]
related: [single-ui-bff, ratanone-api-gateway, ratanone-auth-server]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md"]
---
# What Is the Authoritative Ratan Login, JWT, and Session Ownership Model?

The source assigns login and JWT issuance to [[single-ui-bff]], token validation and Redis sessions to [[ratanone-auth-server]], and routes `/api/auth/` through [[ratanone-api-gateway]]. Confirm the actual runtime call chain and ownership for login, issuance, validation, refresh, blacklist, and session persistence.
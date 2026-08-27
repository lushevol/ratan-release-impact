---
type: concept
title: Presigned URL Access Control
created: 2026-08-24
updated: 2026-08-24
tags: [security, presigned-url, minio, authorization, audit]
related: [minio, minio-storage-service, api-gateway, resilience4j]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# Presigned URL Access Control

Presigned URL access control governs time-limited direct downloads from object storage after an application has authorized a user.

The proposal generates MinIO GET URLs with a 15-minute expiry after an application-level `TRADE_VIEWER` role and department check. Direct download reduces application bandwidth and connection pressure, but a URL can be shared until expiry and generally cannot be individually revoked after issuance.

The required policy should define permitted methods, expiry bounds, object scope, content-disposition handling, issuer and user audit correlation, download logging, network exposure of MinIO endpoints, and whether single-use or replacement controls are required.
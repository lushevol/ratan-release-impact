---
type: concept
title: RATAN-HashiCorp Credential Lifecycle
tags: [ratan, hashicorp-vault, credential-rotation, credential-refresh, hot-update]
related: [ratan, hashicorp-vault, control-m, ratan-secrets-management, what-is-the-authoritative-ratan-hashicorp-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Hashicorp 51460.md"]
---

# RATAN-HashiCorp Credential Lifecycle

## Overview

RATAN interface `51460` documents a two-phase credential lifecycle:

```text
rotate -> retrieve -> refresh
```

Rotation changes credentials in the upstream target system through HashiCorp Vault. Refresh retrieves the new credentials and loads them into RATAN components. These phases have separate responsibilities and should not be treated as one operation.

## Phase 1: Rotate

The `ratan_hashicorp_all.sh` script calls:

```http
POST /v1/{mount}/rotate-role/{role}
```

The documented effect is to invalidate existing credentials, generate new cryptographically random credentials, and apply the change to the target system. Examples include PostgreSQL `ALTER USER` and an AD reset.

This is an authoritative upstream change. Old credentials may be revoked before RATAN has received the replacement credentials.

## Phase 2: Refresh

The script retrieves the newly rotated credentials through:

```http
GET /v1/{mount}/static-cred/{role}
```

It then sends the credentials to RATAN's internal API:

```http
POST /v1/hashicorp/refresh
```

The stated outcome is a hot update of RATAN components without restarting the application. The source describes `RAT_HCV_REFRESH` as refreshing all HashiCorp accounts to Redis.

## Operational risk

The separation between rotation and refresh creates a failure window. If retrieval, the RATAN refresh API, Redis, or cluster-wide propagation fails after successful rotation, RATAN may retain invalid credentials.

The source does not define:

- Retry or rollback behavior
- Partial-account recovery
- Atomicity across RATAN nodes
- Credential consistency checks
- Emergency rotation outside the March, July, and November cadence
- Authentication and authorization for the refresh API
- Conditions requiring the stop and restart jobs

These gaps are tracked in [[what-is-the-authoritative-ratan-hashicorp-interface-contract]].
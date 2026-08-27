---
type: concept
title: RATAN Secrets Management
tags: [ratan, secrets-management, hashicorp-vault, redis, control-m, runtime-credentials]
related: [ratan, hashicorp-vault, control-m, ratan-hashicorp-credential-lifecycle, redis-client-outage-recovery, ratan-operational-resilience-plans]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Hashicorp 51460.md"]
---

# RATAN Secrets Management

## Purpose

RATAN uses HashiCorp Vault as a runtime secrets-management dependency for database, Active Directory, and OUD credentials. The integration is intended to provide programmatic and dynamic access rather than relying on manually distributed static credentials.

## System relationships

The documented flow connects the following components:

1. [[hashicorp-vault]] stores and rotates the managed credentials.
2. `ratan_hashicorp_all.sh` invokes Vault rotation and retrieval operations.
3. RATAN receives replacement credentials through `POST /v1/hashicorp/refresh`.
4. `RAT_HCV_REFRESH` refreshes HashiCorp accounts to Redis.
5. RATAN components use the refreshed credentials without an application restart.
6. [[control-m]] coordinates checking, rotation, refresh, and cluster-control jobs.

The source does not confirm whether Redis is a cache, a distribution mechanism, or the runtime source for every RATAN component. It also does not specify whether credentials are stored in plaintext, encrypted, or tokenized.

## Operational cadence

The `RATAN_FULL_HCV` Control-M parent folder is associated with monthly enablement of HashiCorp, VIP, and clusters in March, July, and November. The source does not provide exact dates or times.

## Security and resilience considerations

The interface requires explicit controls for:

- Vault and refresh-API authentication and authorization
- TLS protection
- Secret exposure prevention in logs and job output
- Redis access control and retention
- Failure after upstream rotation but before RATAN refresh
- Inconsistent credentials across cluster nodes
- Vault, Redis, or Control-M unavailability
- Audit evidence for rotation and refresh

These controls are not specified in the source and require confirmation before the integration can be treated as a complete operational contract.
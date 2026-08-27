---
type: source
title: Ratan and HashiCorp 51460
authors: [Yunzhe Ta]
year: 2026
url: ""
venue: Confluence
tags: [ratan, hashicorp-vault, secrets-management, credential-rotation, control-m, interface-51460]
related: [ratan, hashicorp-vault, control-m, ratan-hashicorp-credential-lifecycle, ratan-secrets-management, what-is-the-authoritative-ratan-hashicorp-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Hashicorp 51460.md"]
---

# Ratan and HashiCorp 51460

## Source context

This document describes interface `51460`, the integration between RATAN and HashiCorp Vault for runtime secrets management and credential rotation. The source records an update by `@Yunzhe Ta` on 2026-01-28 and a review by `@Yunzhe Ta` and `@Jie Cai` on 2026-01-29. Its status field is blank, although the document states that status should become `Published` after review.

The integration provides programmatic and dynamic access to credentials at runtime for databases, Active Directory (AD), and OUD accounts.

## Control-M job inventory

| Application Name | Control-M Job Name | Description |
| --- | --- | --- |
| RATAN | `RATAN_FULL_HCV` (parent folder) | Enables HashiCorp, VIP, and clusters on all servers monthly in March, July, and November |
| RATAN | `RAT_HCV_CHECK` | Checks all HashiCorp account rotation information |
| RATAN | `RAT_HCV_REFRESH` | Refreshes all HashiCorp accounts to Redis |
| RATAN | `RAT_HCV_ROTATE` | Rotates all HashiCorp accounts |
| RATAN | `RAT_RESTART_ALL_SERV_HCV` | Restarts VIP and the whole cluster from ARK servers |
| RATAN | `RAT_STOP_ALL_SERV_HCV` | Stops all services on the whole cluster |

The source does not specify exact trigger times, job dependencies, retry policies, alerting, or job ownership.

## Managed account inventory

The source lists the following HashiCorp-managed accounts:

```text
DB   ratanone_ratanprd_003
DB   ratanprd_003
DB   ratanone_ratanprd_001
DB   ratanprd_001
DB   ratanone_ratanone_dmp
DB   ratanone_dmp
AD   svc.ratanone.001
OUD  srv.51358.ratanone.001
OUD  ratan_prod
OUD  ratan_edmi_prod
```

The document does not state whether this is the complete production inventory. It also does not provide the Vault mount, role, environment mapping, or ownership for each account.

## End-to-end credential flow

RATAN implements a documented two-phase lifecycle:

1. **Rotate:** The `ratan_hashicorp_all.sh` script calls Vault's native rotation endpoint for each configured role. Rotation invalidates existing credentials, generates new credentials, and applies the change to the target system. Examples include PostgreSQL `ALTER USER` and an AD reset.
2. **Refresh:** The script retrieves the newly rotated credentials from Vault and sends them to RATAN's internal refresh API. RATAN hot-updates components without restarting the application.

The documented interfaces are:

```http
POST /v1/{mount}/rotate-role/{role}
GET /v1/{mount}/static-cred/{role}
POST /v1/hashicorp/refresh
```

No request or response schemas, authentication headers, authorization model, TLS requirements, timeout values, retry behavior, idempotency guarantees, or error codes are provided.

## Operational dependencies

The documented flow involves:

- [[hashicorp-vault]] as the upstream secrets-management system
- [[ratan]] as the application receiving refreshed credentials
- [[control-m]] as the scheduler and orchestrator
- Redis as the refresh destination and internal distribution or caching layer
- ARK servers for VIP and cluster service control

The source does not establish whether Redis stores plaintext, encrypted, or tokenized credentials, nor whether all RATAN cluster nodes are updated atomically.

## Operational tensions and gaps

Vault rotation is described as immediately revoking old credentials, while retrieval and RATAN refresh occur in a separate phase. A failure between these phases could leave RATAN unable to authenticate. The document does not define rollback, retry, partial-account recovery, or emergency rotation procedures.

The same job family contains stop and restart operations even though refresh is described as a hot update that does not require an application restart. The conditions requiring those jobs are not documented.

The source also leaves unresolved:

- The authoritative Vault mount and role values
- The complete production account inventory
- Authentication and authorization for `POST /v1/hashicorp/refresh`
- Redis protection, retention, and credential expiry behavior
- Cluster-wide consistency guarantees
- Control-M schedules, dependencies, owners, and alerts
- Ownership of Vault, Control-M, Redis, ARK servers, and the RATAN refresh API
- Whether the document status should be set to `Published`

## Related documentation

The source includes an OLA reference:

[RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

See [[ratan-hashicorp-credential-lifecycle]] for the rotate-to-refresh sequence and [[what-is-the-authoritative-ratan-hashicorp-interface-contract]] for unresolved interface-contract questions.
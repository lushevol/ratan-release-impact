---
type: entity
title: Hashicorp
created: 2026-08-24
updated: 2026-08-25
tags: [hashicorp, vault, secrets-management, api, database, ratan, indonesia, credential-vault, privileged-identities]
related: [ratan-srack-subnet-connectivity, ratan-indonesia-network-segmentation, cash-settlement-platform, ratan, privileged-identity-management, secrets-vaulting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md", "RATAN/RATAN -Security/RATAN -Security.md"]
---

# Hashicorp

## Role in RATAN

Hashicorp provides the API used by the RATAN application to retrieve account details. The application API endpoint is:

```text
https://vault.global.standardchartered.com:8200
```

Additional documented endpoints are:

```text
10.4.38.167
10.95.202.147
10.95.202.148
10.92.202.142
10.92.202.143
Port: 8200
```

## RATAN security inventory

The RATAN security inventory uses `Hashicorp` as the vault designation for the following identities:

- `ratanprd_001` — application database account
- `ratanone_dmp` — read-only production database account
- `svc.ratanone.001` — DQSL API authentication connection
- `srv.51358.ratanone.001` — OUD account for SOLACE
- `ratan_prod` — OUD account for FMAA
- `ratan_edmi_prod` — OUD account for Kong API

The RATAN security source does not explicitly name the product as HashiCorp Vault. It provides no rotation schedule, vault paths, ownership details, or access-review evidence.

## Database connectivity

The database-server network section identifies port `6524` for Hashicorp-related access. The source requires the following source networks in `CIB_FM_CJ_51358_EPG_SVR_SRC_GRP`:

```text
10.92.202.0/24
10.95.202.0/24
```

The documented port distinction is:

- `8200` — Hashicorp API port
- `6524` — port identified for the database-server firewall requirement
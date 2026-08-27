---
type: entity
title: HashiCorp Vault
tags: [hashicorp, vault, secrets-management, credential-rotation, ratan]
related: [ratan, control-m, ratan-hashicorp-credential-lifecycle, ratan-secrets-management, what-is-the-authoritative-ratan-hashicorp-interface-contract]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Hashicorp 51460.md"]
---

# HashiCorp Vault

## Role in RATAN

HashiCorp Vault is the upstream secrets-management system in RATAN interface `51460`. It provides programmatic and dynamic runtime access to credentials for database, Active Directory, and OUD accounts.

Vault is the authoritative system for the documented credential-rotation phase. RATAN invokes Vault to rotate credentials and then retrieves the newly generated credentials for distribution to RATAN components.

## Interfaces used

```http
POST /v1/{mount}/rotate-role/{role}
GET /v1/{mount}/static-cred/{role}
```

The source does not identify the concrete `mount` or `role` values, authentication requirements, authorization controls, response schemas, or failure behavior.

## Managed credential categories

The documented account inventory includes:

- PostgreSQL or other database accounts
- Active Directory service account `svc.ratanone.001`
- OUD accounts `srv.51358.ratanone.001`, `ratan_prod`, and `ratan_edmi_prod`

The source lists six database accounts and four directory accounts, but does not confirm that the list is exhaustive.

## Relationship to RATAN

The documented sequence is Vault rotation followed by RATAN refresh. See [[ratan-hashicorp-credential-lifecycle]] and [[ratan-secrets-management]].

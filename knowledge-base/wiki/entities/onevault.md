---
type: entity
title: OneVault
tags: [credential-vault, secrets-management, ratan, privileged-identities]
related: [ratan, privileged-identity-management, secrets-vaulting, service-account-decommissioning]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# OneVault

## Role in RATAN Security

OneVault is recorded as the vault for several RATAN Linux and database identities:

- `ratansup`
- `itrs`
- `ratanprd_003`
- `nginxadm`
- the struck-through `nginx` record

The source marks these records as vaulted in OneVault, but does not provide vault paths, rotation schedules, access logs, or accountable owners.

## Lifecycle Caveats

`ratansup` is marked “not in use.” `ratanprd_003` is described as no longer used after services moved to `ratanprd_001` on 13 July 2024. The `nginx` record is struck through and marked as apparently unused pending checking.

Vault presence should not be treated as evidence that an identity remains active, has been disabled, or has been removed from OneVault.

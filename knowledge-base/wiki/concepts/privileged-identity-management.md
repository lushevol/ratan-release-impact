---
type: concept
title: Privileged Identity Management
tags: [privileged-identities, service-accounts, ratan, access-governance]
related: [ratan, active-directory, onevault, hashicorp, secrets-vaulting, credential-lifecycle-management, service-account-decommissioning]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Privileged Identity Management

Privileged identity management (PID) covers the governance of service and privileged accounts, including ownership, vaulting, permitted use, rotation, review, and retirement.

## RATAN Inventory

The RATAN inventory includes Linux, database, Active Directory, OUD, API, and web-team identities. Ten identities are explicitly marked as vaulted in OneVault or Hashicorp. `ratanrt` is described as `non interactive`, but its vaulting status is not stated.

The recorded identities support RATAN connections to DQSL API, SOLACE, FMAA, Kong API, and database services.

## Control Gaps

Most `Owner` and `Status` fields are blank. The inventory therefore does not establish accountability, current use, credential rotation, access review, or decommissioning evidence.

Lifecycle states are not interchangeable:

- `ratansup` is marked “not in use.”
- `ratanprd_003` is described as no longer used after the migration to `ratanprd_001`.
- `nginx` is struck through and remains pending checking.
- `nginxadm` is active in the inventory and associated with the Web BAU team.

These records require confirmation before they can be treated as retired or compliant.

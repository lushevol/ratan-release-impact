---
type: query
title: Are RATAN Service Identities Owned, Vaulted, and Decommissioned?
tags: [ratan, service-accounts, privileged-identities, audit]
related: [ratan, privileged-identity-management, secrets-vaulting, service-account-decommissioning, onevault, hashicorp]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Are RATAN Service Identities Owned, Vaulted, and Decommissioned?

## Question

Are RATAN’s service and privileged identities assigned accountable owners, stored in the appropriate vault, actively used only where required, and decommissioned when obsolete?

## Scope

Prioritise:

- `ratanrt`, whose `non interactive` description does not establish vaulting;
- `ratansup`, marked “not in use” in OneVault;
- `ratanprd_003`, described as unused after migration to `ratanprd_001`;
- `nginx`, marked as apparently unused pending checking;
- `nginxadm`, associated with the Web BAU team.

## Evidence Needed

Confirm the owner, current use, system dependencies, vault location, credential rotation, account status, group memberships, disablement or deletion, and removal of stale vault secrets.

The source has substantial blank `Owner` and `Status` fields, so it is insufficient to answer the question without additional operational evidence.

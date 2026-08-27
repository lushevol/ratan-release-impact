---
type: concept
title: Service-Account Decommissioning
tags: [service-accounts, identity-lifecycle, ratan, decommissioning]
related: [ratan, privileged-identity-management, credential-lifecycle-management, onevault]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Service-Account Decommissioning

Service-account decommissioning is the controlled withdrawal of an unused identity, including dependency confirmation, disablement, credential removal, access-group cleanup, vault cleanup, and evidence retention.

## RATAN Candidates

The inventory identifies three different lifecycle situations:

- `ratansup` — marked “not in use.”
- `ratanprd_003` — described as no longer used after services moved to `ratanprd_001` on 13 July 2024.
- `nginx` — struck through and described as apparently unused, pending checking.

These statements are not equivalent to confirmed disablement or deletion. The source does not provide owners, status values, disablement dates, dependency checks, or removal evidence.

## Required Confirmation

For each candidate, confirm current use, system dependencies, accountable owner, account disablement, group membership removal, vault-secret retirement, and any required audit evidence.

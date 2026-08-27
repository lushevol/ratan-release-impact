---
type: query
title: What Is the Authoritative RATAN-HashiCorp Interface Contract?
tags: [ratan, hashicorp-vault, interface-contract, credential-rotation, open-question]
related: [ratan, hashicorp-vault, control-m, ratan-hashicorp-credential-lifecycle, ratan-secrets-management]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and Hashicorp 51460.md"]
---

# What Is the Authoritative RATAN-HashiCorp Interface Contract?

## Question

Which specification defines the complete production contract for RATAN interface `51460`, including Vault role mappings, refresh payloads, security controls, orchestration, and failure recovery?

## Known contract elements

The source documents these endpoint paths:

```http
POST /v1/{mount}/rotate-role/{role}
GET /v1/{mount}/static-cred/{role}
POST /v1/hashicorp/refresh
```

It also identifies the implementation script `ratan_hashicorp_all.sh`, the `RATAN_FULL_HCV` Control-M folder, and the jobs `RAT_HCV_CHECK`, `RAT_HCV_REFRESH`, `RAT_HCV_ROTATE`, `RAT_RESTART_ALL_SERV_HCV`, and `RAT_STOP_ALL_SERV_HCV`.

## Missing contract details

The authoritative specification has not been identified for:

- Vault mount and role values for each managed account
- Request and response schemas
- Authentication, authorization, and TLS requirements
- Error codes, retries, timeouts, and idempotency
- Recovery when rotation succeeds but retrieval or refresh fails
- Atomicity and consistency across RATAN cluster nodes
- Redis storage protection and credential retention
- Control-M dependencies, schedules, owners, alerts, and escalation
- Conditions requiring service stop and restart despite hot refresh support
- Emergency rotation procedures
- Definitive status of the reviewed source document

## Evidence boundary

The source provides endpoint signatures and high-level process descriptions, but it does not establish a complete API or operational specification. Resolution requires the implementation documentation, Vault configuration, Control-M definitions, RATAN refresh-service contract, and security runbooks.
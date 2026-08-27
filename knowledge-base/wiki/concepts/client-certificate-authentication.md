---
type: concept
title: Client Certificate Authentication
tags: [certificates, tls, ratan, integrations]
related: [ratan, certificate-lifecycle-management, appviewx]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Client Certificate Authentication

Client certificate authentication uses a certificate presented by a client system to authenticate to an integration counterpart.

## RATAN Integrations

The source identifies two client-side RATAN certificates:

- `51358-ratan` for integration with Enterprise Solace and Hashicorp.
- `ratan-stella.gdc.standardchartered.com` for integration with STELLA SDK.

Both are recorded as Microsoft Enterprise certificates with an expiry date of 7/16/2026 and a source status of `Valid`. Their current status must be verified because the inventory predates the 2026-08-25 ingest date.

The source does not specify renewal owners, trust-store configuration, or contingency credentials.

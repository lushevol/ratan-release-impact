---
type: concept
title: Certificate Lifecycle Management
tags: [certificates, pki, ratan, renewal, security-operations]
related: [ratan, appviewx, client-certificate-authentication]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# Certificate Lifecycle Management

Certificate lifecycle management covers certificate issuance, deployment, validity monitoring, renewal, replacement, and retirement.

## RATAN Certificate Estate

The source identifies `EJBCA / MSPKI` as the certificate type and AppViewX as the certificate-information tool. It records Microsoft Enterprise certificates for:

- `51358-ratan`, used for RATAN client integration with Enterprise Solace and Hashicorp;
- `fmo-shell.gdc.standardchartered.com`, used as the RATAN HTTPS server certificate;
- `ratan-stella.gdc.standardchartered.com`, used for RATAN client integration with STELLA SDK.

The same inventory contains three struck-through EJBCA certificates labelled expired.

## Verification Requirements

The source labels the Microsoft Enterprise certificates expiring on 7/16/2026 as `Valid`. Because the wiki ingest date is 2026-08-25, those records require live verification in AppViewX and at the relevant endpoints.

A complete lifecycle review should confirm:

- current certificate validity and chain;
- deployment on every listed host;
- renewal owner and renewal status;
- counterpart trust-store compatibility;
- retirement of obsolete EJBCA certificates and dependent trust entries.

The inventory’s validity labels are point-in-time records, not current evidence.

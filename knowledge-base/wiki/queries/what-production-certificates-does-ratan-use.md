---
type: query
title: What Production Certificates Does RATAN Use?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, certificates, production, inventory, pki, security]
related: [ratan, appviewx, ejbca, mspki, tls-certificates, certificate-renewal, 5-ratan--15-ratan-security--27-ratan-certificate-details--1fpjjab]
sources: ["RATAN/RATAN -Security/RATAN - Certificate Details.md"]
---
# What Production Certificates Does RATAN Use?

The RATAN certificate-details reference records “Production External Certificates: None,” while also identifying [[ejbca]], [[mspki]], and [[appviewx]] as certificate-information references.

## Why This Is Open

The statement can establish only that no production external certificates are listed in the document. It does not clarify whether:

- RATAN has no production external certificates;
- certificate records are maintained solely in AppViewX or another system;
- internal or private certificates are excluded;
- the document is incomplete or outdated; or
- non-production certificates exist outside the documented scope.

## Evidence Needed

An authoritative certificate inventory should identify, for each RATAN certificate:

- subject names and environments;
- certificate type, including the meaning of `APP Role`;
- issuer and managing system;
- expiry date and renewal owner;
- deployment endpoint or service;
- whether the certificate is externally exposed; and
- the authoritative monitoring and renewal process.

The investigation should also establish the respective roles of [[ejbca]], [[mspki]], and [[appviewx]].
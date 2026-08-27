---
type: query
title: What Is the Current Validity and Renewal Owner of RATAN Certificates?
tags: [ratan, certificates, pki, renewal, appviewx]
related: [ratan, certificate-lifecycle-management, client-certificate-authentication, appviewx]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Security/RATAN -Security.md"]
---

# What Is the Current Validity and Renewal Owner of RATAN Certificates?

## Question

Are the RATAN certificates labelled `Valid` in the inventory still valid and deployed correctly, and who owns their renewal?

## Certificates to Verify

- `51358-ratan` — Enterprise Solace and Hashicorp client integration; source expiry date 7/16/2026.
- `fmo-shell.gdc.standardchartered.com` — RATAN HTTPS server certificate; source expiry date 11/1/2026.
- `ratan-stella.gdc.standardchartered.com` — STELLA SDK client integration; source expiry date 7/16/2026.

The two certificates with a source expiry date of 7/16/2026 require immediate verification against AppViewX and the live integration endpoints because that date has passed as of the 2026-08-25 ingest date.

## Evidence Needed

Confirm current validity, certificate chain, deployment on every listed host, renewal owner, renewal status, counterpart trust-store compatibility, and contingency arrangements.

The source also lists expired EJBCA certificates. Determine whether their dependent trust-store entries and configuration references were removed during the apparent transition to Microsoft Enterprise.

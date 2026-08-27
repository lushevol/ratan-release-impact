---
type: entity
title: EJBCA
created: 2026-08-25
updated: 2026-08-25
tags: [EJBCA, PKI, certificate-authority, certificate-management, ratan]
related: [primekey, mspki, ratan, ejbca-to-mspki-migration, appviewx, tls-certificates, 5-ratan--15-ratan-security--27-ratan-certificate-details--1fpjjab]
sources: ["RATAN/RATAN -SME/Ratan Pending PID remediations, vulnerabilities, cert renewal.md", "RATAN/RATAN -Security/RATAN - Certificate Details.md"]
---

# EJBCA

## Role and source references

The RATAN pending-remediations tracker identifies `EJBCA` as the source side of the migration tracked for [[ratan]]. The source labels it **EJBCA (PrimeKey)**.

The RATAN certificate-details source names EJBCA alongside [[mspki]], but does not define EJBCA's operational role for [[ratan]]. It may be a certificate authority, PKI component, certificate-information source, or an integration in the certificate-management workflow. This requires confirmation before assigning ownership or authority status.

The certificate-details source also directs certificate information to [[appviewx]].

Neither source specifies EJBCA's deployment version, certificate inventory, or operational owner. The sources also do not establish whether EJBCA was decommissioned after the migration.

## Migration relationship

The pending-remediations tracker records an EJBCA-to-[[mspki]] migration for Ratan with status **Complete**. This is a recorded tracker status, not independent evidence of platform retirement or full certificate migration.
---
type: entity
title: MSPKI
created: 2026-08-25
updated: 2026-08-25
tags: [MSPKI, PKI, certificate-management, migration-target, ratan]
related: [ratan, ejbca, ejbca-to-mspki-migration, certificate-renewal, appviewx, tls-certificates, 5-ratan--15-ratan-security--27-ratan-certificate-details--1fpjjab]
sources: ["RATAN/RATAN -SME/Ratan Pending PID remediations, vulnerabilities, cert renewal.md", "RATAN/RATAN -Security/RATAN - Certificate Details.md"]
---
# MSPKI

## Role in RATAN migration

The [[ratan]] EJBCA-to-MSPKI migration tracker identifies `MSPKI` as the target platform. The tracker records the migration status as **Complete**.

The tracker does not establish whether the migration completed certificate renewal, removed all EJBCA dependencies, or changed the wider certificate-management process.

## References in certificate details

The RATAN certificate-details document names `MSPKI` alongside [[ejbca]]. That document directs users to [[appviewx]] to inspect certificate information.

This reference does not establish that MSPKI itself is a certificate authority, PKI service, repository, environment, or another specific component of the RATAN certificate-management workflow.

## Qualification

Neither source expands the acronym `MSPKI` or defines its implementation, responsibility, scope, ownership, or deployment context. It should therefore be preserved as an unresolved technical identifier until those details are confirmed.
---
type: concept
title: EJBCA-to-MSPKI Migration
created: 2026-08-25
updated: 2026-08-25
tags: [PKI, certificate-authority, migration, EJBCA, MSPKI]
related: [ratan, ejbca, mspki, certificate-renewal]
sources: ["RATAN/RATAN -SME/Ratan Pending PID remediations, vulnerabilities, cert renewal.md"]
---
# EJBCA-to-MSPKI Migration

## Definition

An EJBCA-to-MSPKI migration is the movement of certificate-management or public-key-infrastructure capability from [[ejbca]] to [[mspki]].

## Source-specific status

For the CI [[ratan]], the migration tracker records `MSPKI` as the target and **Complete** as the status.

The source does not provide enough evidence to determine:

- Which certificates or components were migrated.
- Whether EJBCA was decommissioned for Ratan.
- Whether the migration included certificate renewal.
- Whether operational validation or formal sign-off occurred.
- Whether any vulnerabilities or PID remediations were resolved.

Migration completion should therefore be tracked separately from certificate-renewal completion and remediation closure.
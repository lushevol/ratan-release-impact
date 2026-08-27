---
type: source
title: Ratan Pending PID Remediations, Vulnerabilities, and Certificate Renewal
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-25
updated: 2026-08-25
tags: [Ratan, PKI, certificate-migration, PID-review, remediation-tracking]
related: [ratan, ejbca, primekey, mspki, lwws, ejbca-to-mspki-migration, pid-review, certificate-renewal, what-pid-remediations-and-vulnerabilities-remain-for-ratan]
sources: ["RATAN/RATAN -SME/Ratan Pending PID remediations, vulnerabilities, cert renewal.md"]
---
# Ratan Pending PID Remediations, Vulnerabilities, and Certificate Renewal

## Scope

This source contains a certificate-authority migration tracker for the CI named `Ratan` and a brief note about the 2024 PIDs review. The source itself is undated; the year in this page reflects the explicit reference to the 2024 review.

## Certificate migration tracker

The source records the following exact tracker data:

| **CI Name** | **Components** | **EJBCA to MSPKI** | **Comments** | **Status** |
| --- | --- | --- | --- | --- |
| Ratan | - | MSPKI |  | **Complete** |

The recorded scope is [[ratan]]'s migration from [[ejbca]] to [[mspki]]. The status is **Complete**, but the source does not provide a migration date, certificate inventory, validation evidence, rollback plan, or sign-off.

## 2024 PIDs review

The source states:

> PIDs Review (2024): updated into LWWS tool

This records an update of the 2024 PIDs review into [[lwws]]. It does not provide PID identifiers, review results, outstanding actions, remediation owners, due dates, or closure evidence.

## Evidence limitations

The filename references pending PID remediations, vulnerabilities, and certificate renewal, but the document body does not provide:

- Vulnerability identifiers or severity ratings.
- PID names, identifiers, or review outcomes.
- Remediation status by issue.
- Remediation owners or deadlines.
- Certificate names, expiry dates, or renewal status.
- Ticket, dashboard, or approval links.

The migration status must therefore not be interpreted as evidence that all vulnerabilities, PID remediations, or certificate renewals are complete. The relationship between this record and the existing [[certificate-renewal]] concept remains unconfirmed.

## Open question

The distinction between migration completion and remediation closure is tracked in [[what-pid-remediations-and-vulnerabilities-remain-for-ratan]].
---
type: concept
title: RATAN Post-Release SSI Update Restriction
tags: [ratan, ssi, cashflow, released-status, settlement]
related: [ratan-ssi-stamping, tis, tis-cashflow-eligibility-rules, authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# RATAN Post-Release SSI Update Restriction

The RATAN–TIS interface source states that once a cashflow reaches `Released` status on the RATAN side, SSI updates are not supported.

This is a source-qualified operational constraint relevant to downstream TIS consumption and to [[ratan-ssi-stamping|RATAN SSI Stamping]]. It does not describe the SSI stamping implementation.

## Unspecified behavior

The source does not identify:

- the SSI fields affected;
- the enforcement point or system component;
- whether correction, cancellation, or exception paths exist;
- whether the restriction continues unchanged after `Settled` status;
- whether `Released` has the same lifecycle meaning across RATAN interfaces.

Accordingly, the statement should not be generalized into a RATAN-wide lifecycle rule without corroborating design evidence.
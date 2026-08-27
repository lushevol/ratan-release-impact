---
type: concept
title: RATAN Temporary Technical Recovery
created: 2026-08-25
updated: 2026-08-25
tags: [RATAN, technical-recovery, temporary-workaround, exception-management]
related: [ratan, strategic-flow, bcs-flow, pss, development-team, azure-devops, ratan-transient-failure-recovery, ratan-technical-recovery-governance]
sources: ["RATAN/RATAN -Projects/Temporary tech recovery process for Handling Technical Failure Exceptions v1.0.md"]
---

# RATAN Temporary Technical Recovery

RATAN Temporary Technical Recovery is a controlled interim workaround for Strategic Flow cashflows that fail for technical reasons.

## Governing principle

Temporary recovery is exception-only. It may restore or reinstate processing, but it must not become BAU or substitute for permanent technical remediation.

PSS may execute the recovery only after the procedure is documented, approved by the relevant Product Owner, and tracked through an ADO ticket. Development remains accountable for root-cause analysis, permanent fixes, and automation.

## Scope

Included:

- Strategic Flow cashflow failures caused by technical issues.

Excluded:

- BCS Flow, which retains the existing Ops replay process.
- Data issues, which remain in Ops BAU processes.
- Business exceptions, which remain with MO or Business correction processes.

## Required controls

Each exception must have:

- An approved recovery procedure.
- A named Development owner.
- A committed permanent-fix ETA.
- Review at the KTLO prioritization call every two weeks.

The expected end state is permanent remediation or automation that eliminates recurring PSS intervention.

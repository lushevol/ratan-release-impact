---
type: query
title: Was NDS Auto Netting Fully Retested After the Missing-Leg Issue?
tags: [nds, auto-netting, korea, testing, data-quality, fixing]
related: ["nds-auto-netting", "nd-irs-nd-ccs-netting", "ratan-settlement-korea", "murex-korea", "pending-fixing"]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md"]
---
# Was NDS Auto Netting Fully Retested After the Missing-Leg Issue?

## Question

After Murex Korea data was rechecked and repushed, was the missing related NDS-leg scenario re-executed successfully with auditable NDS auto-netting outcomes?

## Evidence

The source records a closed issue stating that no related NDS leg was present in RATAN when NDS netting needed testing. The documented causes were insufficient source data and fixing-date timing for KOFR, KRO, KOFR CMP, SONIA GBP, TONAR JSCC, and several USD SOFR variants.

The remedial action was to recheck the Murex Korea testing environment and repush related data. The source marks the issue closed but does not identify the repushed records, resulting component and resultant cashflows, zero-amount suppression cases, or rerun date.

## Information needed

- Identifiers and counts for the repushed related legs.
- Evidence of a post-repush NDS auto-netting run.
- Counts and statuses of resultant and single-resultant cashflows.
- Evidence that any zero-value resultant cashflows were correctly suppressed.
- Confirmation that fixing-date dependencies were represented in the rerun population.
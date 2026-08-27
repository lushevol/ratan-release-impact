---
type: concept
title: Split Cashflow Downstream Integration
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, integration, murex, stella, lms, ssdr, dqsl]
related: [cashflow-splitting, ratan-cashflow-lifecycle-state-machine, murex-2-11, tds3, lms, stella, ssdr, dqsl, clearing-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# Split Cashflow Downstream Integration

Split cashflow integration requires downstream systems to receive the appropriate status, payment, reversal, and extract information for parents and children.

## Observed behavior

- Murex scenarios show Ratan sending released status messages and Murex receiving them for gross splits, withdrawals, and net-resultant split children.
- The Stella scenario records the TDS3 sequence `PROJECTED -> SPLIT -> PROJECTED -> RELEASED`.
- DQSL is described as able to query and return split information to surrounding systems.
- FMMIS logic was updated and tested.
- SSDR extract validation remained in progress.
- TLM confirmation was pending.
- GoAML depended on EOD report generation.
- CIS was descoped.

## LMS qualification

LMS cases are marked `Pass`, but their evidence reports missing parent or netting-resultant messages, missing suppressed-child messages, and a released child received twice. Child messages were received in several cases.

The UAT therefore does not establish a clean LMS sign-off. Parent-versus-child forwarding, suppression behavior, duplicate prevention, and withdrawal reversal messaging require reconciliation.

For suppression semantics, distinguish [[concepts/clearing-swift-suppression]] from full cashflow suppression.
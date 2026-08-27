---
type: comparison
title: LMS Source-Value Proposals
created: 2026-08-24
updated: 2026-08-24
tags: [LMS, RATAN, cash-settlement, integration, proposal]
related: [source-stack-flow-name-propagation, lms-cashflow-feed-eligibility, lms, ratan, netting-resultant-stack-derivation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# LMS Source-Value Proposals

## Decision

Proposal 1 is the confirmed implementation. Proposal 2 was rejected.

| Dimension | Proposal 1 — confirmed | Proposal 2 — rejected |
| --- | --- | --- |
| LMS schema | Reuses the existing LMS data-source field | Adds a separate stack-flow field |
| Blade/Stella LMS source | `FMRPSTELLA` | Retains `FMRP` |
| LOANIQ/Stella LMS source | `FMRPSTELLA-LOANIQ` | Retains `LOANIQ` |
| Murex stack value | `FMRPMUREX` | `MUREX` |
| Murex LMS source | Expected by tests as `FMRPMUREX`; specification contains ambiguous combined text | Retains `FMRP` |
| Legacy compatibility | `FMRP` and `LOANIQ` remain accepted | Preserved directly |
| New LMS field | No | Yes |
| Deployment implication | Requires stack derivation before source-field change | Requires separate field support |

## Rationale

Proposal 1 provides the workflow-specific identity through an existing LMS field and avoids expanding the LMS feed schema. It was confirmed with the LMS team and supports an LMS release before the RATAN release.

Proposal 2 remains useful as historical context, but it is not an implementation alternative unless the decision is revisited.

## Risks

The confirmed proposal still has unresolved details:

- The Murex LMS source is inconsistently written as `FMRPSTELLA FMRPMUREX`, while tests expect `FMRPMUREX`.
- Mixed-stack netting behavior is not fully specified.
- Exact hyphenation for `FMRPSTELLA-LOANIQ` is not consistently represented in the source.
- The `STELLA` Tag20 prefix requires debit-cashflow validation.

See [[what-is-the-canonical-murex-stack-flow-and-lms-source-value]] and [[what-is-the-authoritative-mixed-stack-netting-rule]].
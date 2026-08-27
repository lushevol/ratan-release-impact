---
type: concept
title: LMS Feed Source Identification
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lms, source-identification, message-sender, stack-flow]
related: [ratanone, lms, scbml, what-is-the-authoritative-ratan-lms-message-sender-and-stack-flow-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan - LMS feed.md"]
---
# LMS Feed Source Identification

LMS feed source identification is the LMS-specific mapping of an original trade-source system to identifiers emitted by [[ratanone]]. It separates three distinct values:

1. The original trade-source classification.
2. The Ratan-set `MessageSender`.
3. The proposed LMS `Stack Flow`.

## Proposed mapping

- `MUREX/STELLA` maps to `MessageSender = FMRP` and proposed `Stack Flow = FMRPSTELLA`.
- `LOANIQ` maps to `MessageSender = LOANIQ` and proposed `Stack Flow = FMRPSTELLA-LOANIQ`.

The LoanIQ stack-flow value is distinct from the Murex/Stella default, even though it retains the `FMRPSTELLA` prefix. The source gives no rationale for that naming convention.

## SCBML relationship

The source states that the proposed stack-flow values can be inherited from [[scbml]]. This is a possible compatibility relationship, not evidence that SCBML is the approved authority or that the values are already implemented.

## Implementation dependency

[[lms]] must be compatible with the mapping before the Ratan change can be safely deployed. The source does not define field casing, serialization, permitted-value governance, backward compatibility for historic records, validation evidence, or rollback behavior.

The unresolved interface contract is tracked in [[what-is-the-authoritative-ratan-lms-message-sender-and-stack-flow-contract]].
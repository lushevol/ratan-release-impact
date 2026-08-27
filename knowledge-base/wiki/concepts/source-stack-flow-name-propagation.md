---
type: concept
title: Source Stack Flow Name Propagation
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, stack-flow, SCBML, LMS, RATAN, integration]
related: [lms, ratan, fmrp, stella, murex-211, lms-cashflow-feed-eligibility, murex-ratan-cashflow-message-contract, surrounding-system-integration, netting-resultant-stack-derivation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# Source Stack Flow Name Propagation

## Definition

`Source_Stack_Flow_Name` is a SCBML message value that identifies the trade workflow stack used by a cashflow. RATAN consumes it to dispatch cashflows to the appropriate settlement process. Under the confirmed Proposal 1, the value is propagated into the existing LMS data-source field rather than being added as a new LMS field.

## Message Mapping

The stack-flow value is read from:

```text
/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender[@systemScheme="http://www.sc.com/coding-scheme/stack-flow"]
```

It is written to the LMS data-source message sender identified by:

```text
/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender systemScheme='http://www.sc.com/coding-scheme/system-1-0'
```

## Accepted Values and Routes

| Stack-flow value | Workflow or source | Settlement process | Expected LMS source |
| --- | --- | --- | --- |
| `BCSSTELLA` | BCS through Stella | BCS | `STELLA` |
| `NativeSTELLA` | Native Stella | No RATAN flow | Not applicable |
| `FMRPSTELLA` | Blade through Stella | FMRP | `FMRPSTELLA` |
| `FMRPSTELLA-LOANIQ` | LOANIQ through Stella | FMRP | `FMRPSTELLA-LOANIQ` |
| `FMRPMUREX` | Murex | FMRP | Expected by tests: `FMRPMUREX` |

`FMRPSTELLA-LOANIQ` must be treated as an exact identifier. Variants with inserted spaces are inconsistent representations in the source and should not be assumed valid.

## Compatibility

LMS remains compatible with legacy source values `FMRP` and `LOANIQ`. This allows the LMS release to precede the RATAN release and avoids a hard deployment-time dependency.

The change applies to both new and withdrawal messages where the relevant event exists. The source records successful representative tests for `FMRPSTELLA` and `FMRPMUREX` new and withdrawal events, while LOANIQ withdrawal coverage is absent.

## Scope and Limitations

This concept describes the accepted direct-flow mapping. It does not resolve:

- The ambiguous Proposal 1 Murex entry `FMRPSTELLA FMRPMUREX`.
- The canonical mixed-stack netting rule.
- Whether `STELLA` always uses Tag20 prefix `EQ`, including debit cashflows.
- Whether the two-release rollout has completed.

See [[netting-resultant-stack-derivation]] and [[what-is-the-canonical-murex-stack-flow-and-lms-source-value]] for the unresolved contracts.
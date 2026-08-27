---
type: source
title: Source Stack Flow Name in LMS Feed
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, LMS, RATAN, FMRP, Stella, stack-flow, integration]
related: [source-stack-flow-name-propagation, netting-resultant-stack-derivation, lms-source-value-proposals, lms, ratan, fmrp, stella, cashflow-netting-and-auto-un-netting, surrounding-system-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md"]
---

# Source Stack Flow Name in LMS Feed

## Summary

This functional requirement defines how `Source_Stack_Flow_Name` identifies trade workflow stacks passing through SABRE and how RATAN uses that value to dispatch cashflows to settlement processes. The confirmed design, Proposal 1, maps the stack-flow value into the existing LMS data-source field. Proposal 2, which would add a separate stack-flow field to the LMS feed, was rejected.

The change covers direct cashflows, withdrawal events, netting resultants, backward compatibility, and a two-release deployment sequence.

## Stack-Flow Values

The source identifies the following values:

- `BCSSTELLA` — BCS flow.
- `NativeSTELLA` — does not flow to RATAN.
- `FMRPSTELLA` — FMRP flow.
- `FMRPSTELLA-LOANIQ` — FMRP flow.
- `FMRPMUREX` — proposed accepted value for Murex-originated FMRP cashflows.

The relevant SCBML paths are:

```text
Stack field:
/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender[@systemScheme="http://www.sc.com/coding-scheme/stack-flow"]

Data source field in LMS feed:
/scb:SCBML/scb:header/scb:originationDetails/scb:messageSender/scb:messageSender systemScheme='http://www.sc.com/coding-scheme/system-1-0'
```

## Current Process

| Cashflow Data Source | Stack Flow Value | Settlement Process | Trade Original Source System | Netting Resultant Source Value | Netting Resultant Stack Value | Swift/Accounting | Source Value sent to LMS | Tag20 Prefix |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCSSTELLA→ Stella | BCSSTELLA | BCS | TBC | null | null | RAZOR | STELLA | EQ |
| Blade→ Stella | FMRPSTELLA | FMRP | Blade | if component are the same, derive the value if not, set to null | null | RATAN | FMRP | DV |
| Blade | null | null | RAZOR (For EGNPSA) | NA | FX |
| LOANIQ→ Stella | FMRPSTELLA-LOANIQ | FMRP | LOANIQ | LOANIQ | null | RAZOR | LOANIQ | LQ |
| Murex | null | FMRP | null | null | null | RATAN | FMRP | DV |

## Confirmed Proposal 1

Proposal 1 obtains the stack-field value and sets the LMS data-source field to that value. The source records that this approach was confirmed with the LMS team.

| Cashflow Data Source | Stack Flow Value | Settlement Process | Netting Resultant Stack Value | Swift/Accounting | Source Value sent to LMS | Tag20 Prefix |
| --- | --- | --- | --- | --- | --- | --- |
| BCSSTELLA→ Stella | BCSSTELLA | BCS | | RAZOR | STELLA | EQ |
| Blade→ Stella | FMRPSTELLA | FMRP | FMRPSTELLA | RATAN | FMRPSTELLA | DV |
| RAZOR (For EGNPSA) | NA | FX |
| LOANIQ→ Stella | FMRPSTELLA-LOANIQ | FMRP | FMRPSTELLA-LOANIQ | RATAN | FMRPSTELLA-LOANIQ | LQ |
| Murex | FMRPMUREX | FMRP | if component are the same, derive the parent value if not, set the value to FMRPSTELLA | RATAN | FMRPSTELLA FMRPMUREX | DV |

The intended direct-flow changes are:

- Blade/Stella LMS source: `FMRP` → `FMRPSTELLA`.
- LOANIQ/Stella LMS source: `LOANIQ` → `FMRPSTELLA-LOANIQ`.
- Murex stack value: unspecified or `null` in the current process → `FMRPMUREX`.

The Murex LMS source entry `FMRPSTELLA FMRPMUREX` is ambiguous. Integration tests expect the exact value `FMRPMUREX`, so the combined entry should not be treated as a settled canonical contract.

## Rejected Proposal 2

Proposal 2 would have added the stack-field value as a separate field in the LMS feed while retaining broad legacy source values. It was explicitly rejected.

| Cashflow Data Source | Stack Flow Value | Settlement Process | Netting Resultant Stack Value | Swift/Accounting | Source Value sent to LMS | Stack flow value in LMS feed | Tag20 Prefix |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BCSSTELLA→ Stella | BCSSTELLA | BCS | | RAZOR | Stella | BCSSTELLA | EQ |
| Blade→ Stella | FMRPSTELLA | FMRP | FMRPSTELLA | RATAN | FMRP | FMRPSTELLA FMRP | DV |
| RAZOR (For EGNPSA) | NA | | FX |
| LOANIQ→ Stella | FMRPSTELLA-LOANIQ | FMRP | FMRPSTELLA-LOANIQ | RATAN | LOANIQ | FMRPSTELLA-LOANIQ | LQ |
| Murex | MUREX | FMRP | if component are the same, derive the parent value if not, set the value to FMRPSTELLA | RATAN | FMRP | FMRPSTELLA MUREX | DV |

## Netting and Deployment

The source states that netting-resultant stack values must be derived before the LMS source-field change. The documented deployment sequence is:

1. Deploy stack-value derivation in the netting service.
2. In a later release, change the data-source value sent in the LMS feed.

This sequence addresses cashflows netted before the change and released after the change. The source contains a `Netting derive logic` heading but does not provide a complete algorithm. The same-stack rule, mixed-stack fallback, comparison attribute, and exact value formatting therefore require confirmation in [[netting-resultant-stack-derivation]] and [[what-is-the-authoritative-mixed-stack-netting-rule]].

## Backward Compatibility

The source confirms that LMS continues to map legacy values `FMRP` and `LOANIQ`. LMS can release its change before the RATAN release without creating a release-time dependency on the new RATAN behavior.

SIT and UAT connectivity were reported as acceptable from the LMS side, with sample messages to be provided for connectivity testing.

## Integration Test Evidence

| Stack Flow Value | Test Step | Expected Result | Test Data | Status | Comment |
| --- | --- | --- | --- | --- | --- |
| FMRPSTELLA | 1. cashflow received in Ratan and SI stamped 2. maker/checker approve the transaction 3. swift sent and cashflow moved to Released status 4. Withdrawal event received and released | 1.new message sent to LMS with source field value set to "FMRPSTELLA" 2. withdrawal message sent to LMS with source field value set to "FMRPSTELLA" | ~~006148455905 new event sent to LMS~~ 006148455910 new event sent to LMS 006148455910 withdrawal sent to LMS~~ ~~ | New and Withdrawal is received as expected | test DB refreshed, rebook another cashflow for withdrawal event |
| FMRPSTELLA -LOANIQ | 1. cashflow received in Ratan and SI stamped 2. maker/checker approve the transaction 3. cashflow sent and status moved to Released | 1. message sent to LMS with source field value set to "FMRPSTELLA -LOANIQ" | 006164794767 new event sent to LMS | New is received as expected | currently there is no withdrawal event for LOANIQ cashflow |
| FMRPMUREX | 1. cashflow received in Ratan and SI stamped 2. maker/checker approve the transaction 3. swift sent and cashflow moved to Released status 4. Withdrawal event received and released | 1. message sent to LMS with source field value set to "FMRPMUREX" 2. withdrawal message sent to LMS with source field value set to "FMRPMUREX" | M01737519205 new event sent to LMS M01737519205 Withdrawal event sent to LMS | New and withdrawal is received as expected | |
| STELLA | 1. cashflow received in Ratan and SI stamped | 1. message sent to LMS with source field value set to "STELLA" | 104838976010 new event sent to LMS 005565870127 ew event sent to LMS | New is received as expected New is received as expected | @Kaiyuan Xue Can you please book a debit cashflow to confirm if the Tag20 PREFIX is fine? |
| FMRPSTELLA -LOANIQ | 1. 2 cashflow received in Ratan and SI stamped 2. user net the cashflow 3. maker/checker approve the netting resultant cashflow 4. swift sent and cashflow moved to Released status | 1. message sent to LMS with source field value set to "FMRPSTELLA -LOANIQ" | (net 006164794768,006164794768) N00000037098 new event sent to LMS | New is received as expected | |
| FMRPMUREX | 1. 2 cashflow received in Ratan and SI stamped 2. user net the cashflow 3. maker/checker approve the netting resultant cashflow 4. swift sent and cashflow moved to Released status | 1. message sent to LMS with source field value set to "FMRPMUREX" | (M01737519206/M01737519207) N00000037066 new event sent to LMS | New is received as expected | no withdrawal event for netting resultant cashflow after released |
| FMRPSTELLA | 1. 2 cashflow received in Ratan and SI stamped (component have different stack) 2. user net the cashflow 3. maker/checker approve the netting resultant cashflow 4. swift sent and cashflow moved to Released status | 1. new message sent to LMS with source field value set to "FMRPSTELLA | (M01737519209/ 006148455906 ) N00000037131 new event sent to LMS | New is received as expected | no withdrawal event for netting resultant cashflow after released |
| FMRP | Mock cashflow message with source value set to FMRP | | 106148455910 new event sent to LMS | New is received as expected | |
| LOANIQ | Mock cashflow message with source value set to LOANIQ | | 106164794767 new event sent to LMS | New is received as expected | |

## Open Questions

- Is the canonical Murex LMS source value exactly `FMRPMUREX`?
- Is `FMRPSTELLA FMRPMUREX` an alternative-value list, a concatenated value, or a documentation error?
- What is the exact mixed-stack netting algorithm?
- Are comparisons based on `Source_Stack_Flow_Name`, the LMS source value, or another attribute?
- Are values containing spaces around the hyphen invalid?
- Is the `STELLA` Tag20 prefix `EQ` valid for debit cashflows?
- What is the withdrawal-event behavior for LOANIQ and netting resultants?
- Has each stage of the two-release deployment been completed?

## Related Wiki Topics

- [[source-stack-flow-name-propagation]]
- [[netting-resultant-stack-derivation]]
- [[lms-source-value-proposals]]
- [[lms-cashflow-feed-eligibility]]
- [[murex-ratan-cashflow-message-contract]]
- [[cashflow-netting-and-auto-un-netting]]
- [[surrounding-system-integration]]
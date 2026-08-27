---
type: source
title: Cash Settlement — Korea Migration
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/FMRP/Korea+Murex+Summary"
venue: Confluence
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea, migration, murex, ratan, reference-hub]
related: [korea-cash-settlement-migration, comp-status-driven-stp, static-data-readiness, ratan-swift-message-generation, swift-message-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md"]
---
# Cash Settlement — Korea Migration

## Summary

This document is a reference hub for the Korea cash-settlement migration. It links the principal material for scope and planning, system interfaces, `COMP`-driven STP, static data, functional and hybrid testing, release documentation, and operational contacts.

The source identifies a migration path from Korea Murex to RATAN and the following downstream workstreams:

- RATAN to OLTP for real-time accounting.
- RATAN to TIS for the manual-payment API.
- RATAN to TLM for accounting reconciliation.
- RATAN to ENISIS for SWIFT-related processing.

The document is an index and staffing reference rather than an authoritative functional specification. The linked documents must be reviewed before deriving interface contracts, acceptance criteria, implementation details, test results, or production-readiness conclusions.

## Reference Links

- [Korea Murex Summary - FM re-platforming](https://confluence.global.standardchartered.com/display/FMRP/Korea+Murex+Summary)
- [Cash Settlements Migration - Korea - FM re-platforming](https://confluence.global.standardchartered.com/display/FMRP/Cash+Settlements+Migration+-+Korea)
- [Cash Settlements Migration -Korea- Scope & Plan](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3588497557)
- [COMP status to drive STP process](https://confluence.global.standardchartered.com/display/DSP/COMP+status+to+drive+STP+process)
- [Korea Cashflow Migration -Ratan to OLTP Accounting(draft)](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3625133574)
- [Ratan to TIS](https://confluence.global.standardchartered.com/display/DSP/Ratan+to+TIS)
- [Cash Settlement - Korea Accounting Recon - RATAN->TLM](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Korea+Accounting+Recon+-+RATAN-%3ETLM)
- [RATAN to ENISIS](https://confluence.global.standardchartered.com/display/DSP/RATAN+to+ENISIS)
- [Swift Comparison between Korea Murex and RATAN](https://confluence.global.standardchartered.com/display/DSP/Swift+Comparison+between+Korea+Murex+and+RATAN)
- [Static date summary](https://confluence.global.standardchartered.com/display/DSP/Static+date+summary)
- [Cash Settlement Migration - Korea Test cases](https://confluence.global.standardchartered.com/display/FMRP/Cash+Settlement+Migration+-+Korea+Test+cases)
- [End to End Testing for Korea Migration](https://confluence.global.standardchartered.com/display/DSP/End+to+End+Testing+for+Korea+Migration)
- [Korea OLA and other release related DOCs](https://confluence.global.standardchartered.com/display/DSP/Korea+OLA+and+other+release+related+DOCs)

## Contact Availability Roster

The source does not define the calendar year or the meanings of `P`, `L`, and `PH`. `Sat` and `Sun` are retained as supplied.

| Functions | Name | Apr-27 | Apr-28 | Apr-29 | Apr-30 | 01-May | 02-May | 03-May | 04-May | 05-May | 06-May | 07-May | 08-May | 09-May | 10-May | 11-May | 12-May | 13-May | 14-May | 15-May |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Overall | Jin, Yeon Su | P | P | P | P | PH | Sat | Sun | L | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| TIS | Lee, Su Jung | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| EDMi | Moon, Ho Hwan | P | P | P | P | PH | Sat | Sun | L | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| ENISIS | Park, Jung Hyeon | P | P | L | P | PH | Sat | Sun | L | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| PMO | Sun, Bo Ra | L | L | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| TIS | TIS-Dev (Kim, Hyeong Joon) | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| OLTP | OLTP-Dev (Jung, So Yeon) | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| EDMi | EDMi-Dev (Han, Se Woon) | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| PM | Kim, Meen Sun | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| Murex | Park, Hee Jin | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |
| Ops | Yang, Ji Hoon | P | P | P | P | PH | Sat | Sun | P | PH | P | P | P | Sat | Sun | P | P | P | P | P |

## Evidence Boundaries

The source supports the existence of the named workstreams, test tracks, release references, and contact roster. It does not establish:

- Interface payloads, error handling, retry behavior, or reconciliation rules.
- Test execution results or formal sign-off.
- Static-data completeness or production readiness.
- Approved on-call coverage or escalation procedures.
- The definition, authority, lifecycle, or precedence of `COMP` status.
- Whether the roster dates refer to 2026.

## Related Wiki Topics

The migration connects to [[entities/murex]], [[entities/enisis]], [[concepts/static-data-readiness]], [[concepts/ratan-swift-message-generation]], [[concepts/swift-message-reconciliation]], and [[projects/cashflow-migration]]. The relationship between `COMP`-driven STP and existing validation or manual-STP controls remains unresolved.
---
type: source
title: "2023 Q4 Cash Settlement Home Page Analysis"
authors: []
year: 2023
url: ""
venue: ""
tags: [cash-settlement, q4-2023, delivery-planning, RATAN, trade-blotter]
related: [cash-settlement-home-page, ratan, razor, stella, ebbs, settlement-integration-static-data-readiness, 2023-q4-cash-settlement-delivery-planning]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis.md"]
---
# 2023 Q4 Cash Settlement Home Page Analysis

## Scope

This historical analysis covers Q4 2023 delivery planning and status updates for the [[entities/cash-settlement-home-page]], RATAN settlement workstreams, Trade Blotter/Trade Review capabilities, and related operational and integration activities. Updates in the source are dated from 2023-11-03 through 2023-11-27.

The document records planning and analysis evidence. A status such as “analysis completed”, “solution reviewed”, “testing in progress”, or “ready for DR” should not be interpreted as proof of production deployment or final acceptance.

## Q4 sprint schedule

| Q4 Sprints | Start Date | End Date |
|---|---|---|
| Sprint 2 | 2023-10-16 | 2023-10-27 |
| Sprint 3 | 2023-10-30 | 2023-11-10 |
| Sprint 4 | 2023-11-13 | 2023-11-27 |
| Sprint 5 | 2023-11-30 | 2023-12-10 |
| Sprint 6 | 2023-12-11 | 2023-12-22 |
| Sprint 7 | 2023-12-25 | 2024-01-05 |
| Sprint 8 | 2024-01-08 | 2024-01-19 |
| Sprint 9 | 2024-01-22 | 2024-02-02 |

Although labelled Q4, the schedule extends into January and February 2024.

## Cash Settlement workstream plan

| Task | Ticket / Feature | Assignee | Planning Sprint | Source status or latest update |
|---|---|---|---|---|
| CN Settlement — Nostro Refresh Q4 | `RATAN-14507` / `FEATURE 1837934` | Yash | Sprint 2 | Completed; reviewed with PO/ops and ready for development handover on 2023-11-03 |
| New Trade Booking (CPT) Support | `RATAN-14722` / `FEATURE 1837980` | Wayne | Sprint 2–3 | CPT testing was in progress on 2023-11-03; MO booking completed by 2023-11-10 |
| Trade Level SSI Stamping for CDU | `RATAN-15997` / `FEATURE 1838010` | Yash | Sprint 3–4 | IRS/CCS/Fixing Notice analysis completed on 2023-11-27; implementation continued into Sprint 5 with a target completion date of 2023-12-01 |
| Cashflow Detail Page Enhancements Q4 2023 | `RATAN-16757` / `FEATURE 1837967` | Yash | Sprint 3–5 | Q4 epic reported as completed; stories in an Epic moved from Q3 remained open |
| EBBS engagement and analysis for accounting | `RATAN-16878` / `FEATURE 1837974` | Yash | Sprint 3–9 | High-level flow analysis started; detailed engagement with the EBBS team was beginning on 2023-11-27 |
| TM Day 1 — Trade Migration Cashflows Handling | `RATAN-16787` / `FEATURE 1837978` | Wayne | Sprint 3–4 | Draft options were reviewed with Leena and Dinesh without major concerns; operations feedback remained pending |
| STP & NSTP Enhancements Q4 | `RATAN-15995` / `FEATURE 1837925` | Lina Feng | Sprint 3–5 | Two of four user stories were completed; the remaining two targeted the end of Sprint 5 |
| Revamp RATAN-LMS Feed Model | `RATAN-16806` / `FEATURE 1837985` | Lina Feng | Sprint 3–4 | New-flow analysis was underway; LMS PO and operations confirmation remained pending |
| RAZOR FX Trade — Cashflow Status Writeback to STELLA for Hard Block | `RATAN-12334` / `FEATURE 1837947` | Lina Feng | Sprint 3–5 | Proposed solution reviewed; open items targeted for Sprint 5 |
| New Entity Onboarding Analysis (SG, UI, IN, TW, HK) | `RATAN-16879` / `FEATURE 1837935` | Lina Feng | Sprint 5–9 | Planned to resume after the December block leave |
| Realtime Settlements Dashboard for Senior Stakeholder (MVP) | `RATAN-11612` / `FEATURE 1837988` | Yash | Sprint 5–6 | Planned to start in January 2024 |

## Trade Blotter and Trade Review workstreams

The Trade Blotter/Trade Review schedule used the following sprint sequence:

| Q4 Sprints | Start Date | End Date |
|---|---|---|
| Sprint 1 | 2023-10-16 | 2023-10-27 |
| Sprint 2 | 2023-10-30 | 2023-11-10 |
| Sprint 3 | 2023-11-13 | 2023-11-27 |
| Sprint 4 | 2023-11-30 | 2023-12-10 |
| Sprint 5 | 2023-12-11 | 2023-12-22 |
| Sprint 6 | 2023-12-25 | 2024-01-05 |
| Sprint 7 | 2024-01-08 | 2024-01-19 |
| Sprint 8 | 2024-01-22 | 2024-02-02 |

| Epic | Story | JIRA/ADO Ticket | Assignee | Planning Sprint | Comment |
|---|---|---|---|---|---|
| Feed FX Trades from RATAN to RAZOR |  |  |  |  | On 2023-11-03, 99% of rules were confirmed and a minor question remained with the RAZOR team. On 2023-11-13, the only open question was expiry-event synchronization between STELLA and RAZOR. Requirement finalized on 2023-11-20 |
| MO Detective Controls |  | `RATAN-16851` |  |  | Three rules were in development on 2023-11-20; one new rule awaited Kunal’s business requirement and one P&L rule was in solution engagement with Liam |
| Auto Notification in Trade Blotter with Filter |  | `RATAN-14586` / `Feature 1838136` | Jill | Sprint 2–3 |  |
| Trade Review Requirements in Q4 |  |  |  |  | Enhancement requirements for the trade detail page were being collected on 2023-11-20; underlying user stories were to be reviewed with Dinesh |
| Eco Affirmation Status update from Ratan to CDU PS |  | `RATAN-15816` |  |  |  |
| Implement CDUPS Confirmation Document to Trade Blotter |  |  |  |  |  |
| Integrate Trade Review with Exception Ticket (ET) |  |  |  |  |  |
| Application onboarding support (CDUPS & SSI+) |  |  |  |  |  |

## Other project and operational activities

| Task Desc | Assignee | Planning Sprint | Comment | Status Update |
|---|---|---|---|---|
| KeyStore | Carrie |  | UAT planned in Nov (EOD1); EOD2 and EDO3 in Jan 2024 | EBBS account mappings were received from RAZOR. EOD1 data was sent to RAZOR on 2023-11-17. One EBBS mapping remained pending from the program team on 2023-11-24 |
| SFX | Carrie |  | DR planned in March 2024; target change in May 2024 | Lifecycle testing and LMS sample-data testing were supported. RATAN was confirmed ready for DR, while PM planning remained pending |
| LoanIQ | Carrie |  | Day 1 release planned for February 2024 | SIT started on 2023-11-08. Testing encountered an FMID mapping issue from TDS3; manual sample-message changes were used for diagnostic verification. Later updates covered source-system filtering, the NSTP rule for structure trades, and aligned field values. The basic term-loan flow passed on 2023-11-24 |
| BAU Analysis task | Carrie |  |  | Vostro SSI notification refresh, value-date-range search in Trade Blotter, release testing and UAT sign-off, data-entitlement verification, and LMS enhancement verification |

## Findings

The portfolio combined settlement processing, trade booking, SSI stamping, cashflow detail, accounting feeds, trade migration, STP/NSTP rules, lifecycle status writeback, entity onboarding, and realtime reporting. Delivery progress was uneven: several analysis activities were complete or reviewed, while testing, implementation, dependency confirmation, and operational approval remained open.

The main risks were system-specific and integration-related:

- EBBS account and FMID mappings.
- Source-system filtering when updating cashflow status through the STELLA API.
- Expiry-event synchronization between STELLA and RAZOR.
- Lifecycle status updates during RAZOR testing.
- NSTP rules for structure trades and netting.
- Unfinalized booking-model assumptions for ND cross-currency trades.
- Operations, program, LMS PO, static-data, and DR approvals.

LoanIQ testing used manually updated sample messages while the FMID issue remained unresolved. This supports diagnostic testing but is weaker evidence than end-to-end validation using production-representative messages.

## Historical status limitations

The source does not establish:

- Final completion of all four STP/NSTP user stories.
- Final resolution of STELLA–RAZOR expiry-event synchronization.
- The authoritative owner of EBBS account mappings.
- Implementation of the RATAN-LMS feed-model redesign.
- Final approval of all MO detective controls.
- Delivery of the realtime settlement dashboard MVP.
- Final operational or DR approvals after the November updates.

These questions should be resolved using later delivery, testing, or approval records. The source should therefore be treated as historical Q4 2023 planning evidence, not current-state documentation.

## Related systems and pages

The work relates to [[entities/ratan]], [[entities/stella]], [[entities/ebbs]], [[entities/sfmrp]], [[entities/ssi-plus]], [[concepts/settlement-method-stamping]], [[concepts/nstp-exception-handling]], [[concepts/non-trade-event-cashflow-updates]], [[concepts/cashflow-lifecycle-state-machine]], [[concepts/static-data-readiness]], [[projects/prime-trade-migration]], and [[concepts/live-versus-full-cashflow-volume-reporting]].
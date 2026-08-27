---
type: source
title: H1 - H2 Booking Model Historical Data Analysis
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, booking-model, h1, h2, cashflow-group, cutover]
related: [h1-booking-model, h2-booking-model, h1-h2-historical-cashflow-group-continuity, cashflow-group-force-completion-on-cancellation, what-is-the-authoritative-h1-h2-historical-group-identity-and-cutover-rule, what-are-the-force-completion-semantics-for-cancelled-historical-cashflow-groups, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/H1 -  H2 booking model historical data analyse.md"]
authors: []
year: 2026
url: ""
venue: Internal technical design
---
# H1 - H2 Booking Model Historical Data Analysis

This undated scenario analysis describes expected adaptor behavior when the booking model switches from H1 to H2 on the 15th in March. It specifies that H2 realtime events must continue processing cashflow groups initially created under H1.

The source uses the inclusive H1 grouping condition:

```text
MxSystemDate <= VD <= MxSystemDate+9
```

The scenarios demonstrate that a three-cashflow group remains `PENDING` at a cashflow count of 2 and becomes `COMPLETED` at a count of 3. A separate cancellation scenario states that a `CNCL` member found in a historical group causes the adaptor to send force complete to that group.

## Case 1: VD after H2

| | Send Date | Group | MxSystemDate | VD | Status | Adaptor Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Realtime (H1) | 10th (Monday) | C1 C1 SNTR C2 INIT C3 INIT | 10th | 18th(Tue) | PENDING | MxSystemDate <= VD <= MxSystemDate+9 C1 C2 C3 in same group |
| Switch to model 2 | | | | | | |
| Realtime (H2) | 17th(Monday) | C2 C1 SNTR C2 SNTR C3 INIT | 17th | 18th(Tue) | PENDING | Find C2 already in group C1/C2/C3, cashflow count = 2 |
| Realtime (H2) | 17th(Monday) | C3 C1 SNTR C2 SNTR C3 SNTR | 17th | 18th(Tue) | COMPLETED | Find C2 already in group C1/C2/C3, cashflow count = 3 |

## Case 2: H1 MxSystemDate+9 = H2

| | Send Date | Group | MxSystemDate | VD | Status | Adaptor Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Realtime (H1) | 6th (Thursday) | C1 C1 SNTR C2 INIT C3 INIT | 6th(Thursday) | 15th(Saturday) | PENDING | MxSystemDate <= VD <= MxSystemDate+9 C1 C2 C3 in same group |
| Realtime (H1) | 14th(Friday) | C2 C1 SNTR C2 SNTR C3 INIT | 14th | 15th(Saturday) | PENDING | Find C2 already in group C1/C2/C3, cashflow count = 2 |
| Switch to model 2 | | | | | | |
| Realtime (H2) | 15th(Saturday) | C3 C1 SNTR C2 SNTR C3 SNTR | 15th | 15th(Saturday) | COMPLETED | Find C2 already in group C1/C2/C3, cashflow count = 3 |

## Case 3: VD = H2

| | Send Date | Group | MxSystemDate | VD | Status | Adaptor Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Realtime (H1) | 6th | C1 C1 SNTR C2 INIT C3 INIT | 17th(Monday) | 17th | PENDING | MxSystemDate <= VD <= MxSystemDate+9 C1 C2 C3 in same group |
| Switch to model 2 | | | | | | |
| Realtime (H2) | 15th(Friday) | C2 C1 SNTR C2 SNTR C3 INIT | 17th | 17th | PENDING | Find C2 already in group C1/C2/C3, cashflow count = 2 |
| Realtime (H2) | 15th(Saturday) | C3 C1 SNTR C2 SNTR C3 SNTR | 17th | 17th | COMPLETED | Find C2 already in group C1/C2/C3, cashflow count = 3 |

## Case 4: CNCL after H2 go-live date

| | Send Date | Group | MxSystemDate | VD | Status | Adaptor Behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Realtime (H1) | 10th (Monday) | C1 C1 SNTR C2 INIT C3 INIT C4 INIT | 10th | 19th | PENDING | MxSystemDate <= VD <= MxSystemDate+9 C1 C2 C3 in same group |
| Realtime (H1) | 15th(Friday) | C2 C1 SNTR C2 SNTR C3 INIT C4 INIT | 17th | 17th | PENDING | Find C2 already in group C1/C2/C3/C4 cashflow count = 2 |
| Switch to model 2 | | | | | | |
| Realtime (H2) | 15th(Saturday) | C4 C1 SNTR C2 SNTR C4 SNTR C3 CNCL | 17th | 17th | COMPLETED | Find C2 already in group C1/C2/C3/C4 cashflow count = 4 C3 found in C1/C2/C3/C4 , send force complete to group |

## Interpretation Limits

The document is a behavioral scenario specification, not an implementation design or test-execution record. It does not define H1 or H2, the durable group-identity key, force-completion side effects, or duplicate and retry handling.

Several scenario values require clarification: Case 3 contains send dates earlier than its `MxSystemDate`, Case 4 changes the displayed `VD` between rows, and multiple rows instruct the adaptor to find `C2` when the incoming cashflow is `C3` or `C4`. These could represent intentional lookup conventions or documentation defects.

See [[h1-h2-historical-cashflow-group-continuity]] for the continuity requirement and [[cashflow-group-force-completion-on-cancellation]] for the narrow cancellation rule.
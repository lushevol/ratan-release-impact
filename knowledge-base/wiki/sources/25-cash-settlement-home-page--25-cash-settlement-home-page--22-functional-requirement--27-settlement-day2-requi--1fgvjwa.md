---
type: source
title: Inter Entity Netting Volume Tracker
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, auto-netting, volume-tracking, settlement-day-2, operational-metrics]
related: [inter-entity-netting-coverage-metrics, netting-eligibility-rules, auto-netting-static-go-live-sequencing, what-is-the-auto-netting-benefit-calculation, what-caused-inter-entity-netting-coverage-to-drop-in-june-and-august-2026, what-are-the-correct-dates-for-inter-entity-netting-rule-creation-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Inter Entity Netting Volume Tracker

This operational tracker records daily Inter Entity Netting volumes, the population excluded above the `100K` threshold, in-scope and netted counts, reported auto-netting benefit, and coverage percentages. It also records netting-rule creation milestones for named entity pairs.

## Findings

The tracker shows near-complete reported in-scope coverage on most business days from 26 June through 30 July 2026, generally between 98% and 100%. It also shows two material periods of lower coverage:

- 22–25 June, when `Netted vs in scope` ranged from 1% to 24%.
- 31 July and subsequent reported rows, when `Netted vs in scope` ranged from 73% to 87%.

The tracker supports these observations but does not identify their root causes. In particular, it does not establish that recorded netting-rule creation events caused either improvements or deteriorations.

The `>100K` out-of-scope population can substantially reduce `Netted vs Total` even when `Netted vs in scope` is high. The `Auto netting benefit` value is frequently lower than `Total Netted`; its calculation, unit, and intended operational interpretation are not defined.

## Source Data

| Payment Date | Total cashflow | out of scope(>100K) | in Scope (<=100K) | Total Netted | Auto netting benefit | Netted vs in scope | Netted vs Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 06-08-2026 | HK vs CHO netting rule created |
| 06-09-2026 | 110 | 82 | 28 | 22 | 22 | 79% | 20% |
| 06-10-2026 | 40 | 30 | 10 | 10 | 10 | 100% | 25% |
| 06-11-2026 | 28 | 18 | 10 | 10 | 8 | 100% | 36% |
| 06-12-2026 | 38 | 16 | 22 | 20 | 20 | 91% | 53% |
| 6/15/2026 | 40 | 14 | 26 | 24 | 24 | 92% | 60% |
| 6/16/2026 | 22 | 10 | 12 | 10 | 10 | 83% | 45% |
| 6/17/2026 | 1008 | 674 | 334 | 332 | 332 | 99% | 33% |
| 6/18/2026 | 70 | 26 | 44 | 44 | 44 | 100% | 63% |
| 6/18/2016 | UK vs TW netting rule created |
| 6/19/2026 | 4 | 0 | 4 | 4 | 4 | 100% | 100% |
| 6/22/2026 | 5173 | 1596 | 3577 | 44 | 44 | 1% | 1% |
| 6/23/2026 | 675 | 215 | 460 | 76 | 59 | 17% | 11% |
| 6/24/2026 | 938 | 373 | 565 | 68 | 60 | 12% | 7% |
| 6/25/2026 | 699 | 274 | 425 | 104 | 104 | 24% | 15% |
| 6/26/2026 | 876 | 94 | 782 | 778 | 416 | 99% | 89% |
| 6/29/2026 | 2435 | 958 | 1477 | 1462 | 973 | 99% | 60% |
| 6/30/2026 | 642 | 88 | 554 | 548 | 299 | 99% | 85% |
| 07-01-2026 | 989 | 319 | 670 | 664 | 343 | 99% | 67% |
| 07-02-2026 | 512 | 258 | 254 | 252 | 145 | 99% | 49% |
| 07-03-2026 | 360 | 79 | 281 | 280 | 174 | 100% | 78% |
| 07-06-2026 | 1400 | 288 | 1112 | 1104 | 602 | 99% | 79% |
| 07-07-2026 | 613 | 71 | 542 | 530 | 291 | 98% | 86% |
| 07-07-2016 | UK vs AG netting rule created |
| 07-08-2026 | 744 | 86 | 658 | 650 | 338 | 99% | 87% |
| 07-09-2026 | 672 | 93 | 579 | 578 | 299 | 100% | 86% |
| 07-10-2026 | 575 | 48 | 527 | 526 | 314 | 100% | 91% |
| 7-13-2026 | 2318 | 1408 | 910 | 896 | 517 | 98% | 41% |
| 7/14/2026 | 1048 | 331 | 717 | 712 | 378 | 99% | 68% |
| 7/15/2026 | 2111 | 736 | 1375 | 1372 | 909 | 99.70% | 65% |
| 7/15/2026 | DFC vs UK netting rule created |
| 7/16/2026 | 1141 | 192 | 949 | 948 | 498 | 99.80% | 83% |
| 7/17/2026 | 847 | 38 | 809 | 808 | 424 | 99.80% | 95% |
| 7/20/2026 | 1048 | 53 | 995 | 992 | 530 | 99.70% | 95% |
| 7/21/2026 | 760 | 38 | 722 | 718 | 392 | 99.45% | 94% |
| 7/22/2026 | 871 | 261 | 610 | 608 | 340 | 99.70% | 70% |
| 7/23/2026 | 654 | 142 | 512 | 512 | 273 | 100.00% | 78% |
| 7/24/2026 | 290 | 36 | 254 | 252 | 152 | 99.20% | 87% |
| 7/27/2026 | 1718 | 509 | 1209 | 1204 | 773 | 99.50% | 70% |
| 7/28/2026 | 589 | 99 | 490 | 486 | 263 | 99% | 83% |
| 7/29/2026 | 1098 | 99 | 999 | 998 | 518 | 99.80% | 91% |
| 7/30/2026 | 932 | 286 | 646 | 644 | 445 | 99.80% | 69% |
| 7/31/2026 | UK vs SG netting rule created |
| 7/31/2026 | 751 | 180 | 571 | 474 | 267 | 83% | 63% |
| 7/31/2026 | UK vs Dubai netting rule created |
| 08-03-2026 | 1850 | 444 | 1406 | 1226 | 692 | 87% | 66% |
| 08-04-2026 | 1267 | 401 | 866 | 644 | 378 | 74% | 51% |
| 05-08-2026 | 1430 | 351 | 1079 | 888 | 496 | 82% | 62% |
| 06-08-2026 | 1346 | 283 | 1063 | 814 | 443 | 77% | 60% |
| 07-08-2026 | 1774 | 698 | 1076 | 790 | 450 | 73% | 45% |

## Data Quality Caveats

The source uses inconsistent date formats. The entries `6/18/2016` and `07-07-2016` are retained as written, although they interrupt the otherwise 2026 timeline. The final `05-08-2026` through `07-08-2026` entries are chronologically ambiguous without confirmation of the date convention.

The identifiers HK, CHO, TW, AG, and DFC are not expanded in the source. They should not be treated as canonical organization names without verification.

See [[inter-entity-netting-coverage-metrics]] for interpretation of the tracker fields and what is the auto netting benefit calculation for the unresolved benefit metric.
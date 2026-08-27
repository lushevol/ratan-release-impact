---
type: source
title: CPT — Tranche 1 LMS Verification
created: 2026-08-23
updated: 2026-08-23
tags: [cpt, uat, tranche-1, manual-entities, lms, settlement]
related: [lms, manual-entity-lms-reference-data-feed, tranche-1-lms-verification-coverage, tranche-1-uat-coverage-status, what-is-the-evidenced-lms-verification-status-for-all-tranche-1-cashflows, what-blocks-local-currency-lms-verification-for-tanzania-sri-lanka-vietnam-and-bangladesh, what-is-the-manual-entity-lms-feed-contract-and-reconciliation-evidence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/05 CPT/01 CPT -Tranche1-LMS verification.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# CPT — Tranche 1 LMS Verification

This CPT tracker records planned LMS verification for 14 Tranche 1 manual-entity cashflow scenarios, dated 11-Aug-26, covering Pakistan, Kenya, Zambia, Tanzania, Sri Lanka, Vietnam, and Bangladesh.

## Tracker data

| No | **Trade ID** | **Legal Entity** | **Value Date** | **Amount** | **Cashflow id ** | if send to LMS | LMS test result | LMS tested by | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 109833274 | PAKISTAN | 11-Aug-26 | 1 USD | M00128221756 | Y | | | |
| 2 | 109853542 | PAKISTAN | 11-Aug-26 | 1 PKR | M00128236898 | Y | | | |
| 3 | 109837964 | KENYA | 11-Aug-26 | 1 USD | M00128226418 | Y | | | |
| 4 | 109838348 | KENYA | 11-Aug-26 | 1 KES | M00128225482 | Y | ![image-2026-8-11_17-15-27.png](attachments/image-2026-8-11_17-15-27.png) | | 2026-08-11 ![image-2026-8-14_15-35-21.png](attachments/image-2026-8-14_15-35-21.png) |
| 5 | 109838404 | ZAMBIA | 11-Aug-26 | 1 USD | M00128226432 | Y | | | |
| 6 | 109838410 | ZAMBIA | 11-Aug-26 | 1 ZMW | M00128226451 | Y | | | |
| 7 | 109856952 | TANZANIA | 11-Aug-26 | 1 USD | M00128240066 | Y | | | |
| 8 | 109839223 | TANZANIA | 11-Aug-26 | 1 TZS | M00128227135 | | | | 2026-08-13 PO is checking with downstream ,waiting for feedback ![image-2026-8-14_15-34-18.png](attachments/image-2026-8-14_15-34-18.png) |
| 9 | 109829856 | SRI LANKA | 11-Aug-26 | 1 USD | M00128219026 | Y | | | |
| 10 | 109833099 | SRI LANKA | 11-Aug-26 | 1 LKO | | | | | 2026-08-17 Need MO to book trade ,ops user released the cashflow ,then update the cashflow on this page to ask LMS to verify |
| 11 | 109833072 | VIETNAM | 11-Aug-26 | 1 USD | M00128221617 | Y | | | |
| 12 | 109833271 | VIETNAM | 11-Aug-26 | 1 VNO | | | | | 2026-08-17 Need MO to book trade ,ops user released the cashflow ,then update the cashflow on this page to ask LMS to verify |
| 13 | 109836414 | BANGLADESH | 11-Aug-26 | 1 USD | M00128224487 | Y | | | |
| 14 | 109836663 | BANGLADESH | 11-Aug-26 | 1 BDO | | | | | 2026-08-17 Need MO to book trade ,ops user released the cashflow ,then update the cashflow on this page to ask LMS to verify |

## Recorded status

Ten rows are marked `Y` in the **if send to LMS** column. The tracker does not define whether `Y` means configured eligibility, source dispatch, confirmed LMS ingestion, or completed verification.

The **LMS test result** and **LMS tested by** fields are blank for all rows except the Kenya KES row, which contains an image attachment rather than a textual result. The attachment content is not available in the supplied text; it cannot support a recorded pass, fail, receipt, or reconciliation conclusion.

The record therefore identifies intended or indicated LMS routing, not demonstrated end-to-end LMS verification.

## Unresolved local-currency cases

- TANZANIA, Trade ID `109839223`, Cashflow ID `M00128227135`, amount `1 TZS`, has no LMS-send indication. The tracker records that PO was checking with downstream and awaiting feedback on 2026-08-13.
- SRI LANKA, Trade ID `109833099`, amount `1 LKO`, has no cashflow ID or LMS result.
- VIETNAM, Trade ID `109833271`, amount `1 VNO`, has no cashflow ID or LMS result.
- BANGLADESH, Trade ID `109836663`, amount `1 BDO`, has no cashflow ID or LMS result.

For the Sri Lanka, Vietnam, and Bangladesh cases, the tracker records the sequence: MO books the trade, an Operations user releases the cashflow, the tracker is updated with the cashflow, and LMS is asked to verify.

`LKO`, `VNO`, and `BDO` are retained exactly as recorded. This source does not define or validate these values.

## Related records

This tracker provides execution-status evidence for [[manual-entity-lms-reference-data-feed]] and a narrow LMS-focused view of [[tranche-1-uat-coverage-status]]. It does not establish a complete LMS feed contract or reconciliation outcome; see [[what-is-the-manual-entity-lms-feed-contract-and-reconciliation-evidence]].
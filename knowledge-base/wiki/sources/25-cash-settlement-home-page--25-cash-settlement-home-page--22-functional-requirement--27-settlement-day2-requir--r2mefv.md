---
type: source
title: LMS UAT2 Self-Testing
authors: []
year: 2025
url: ""
venue: "UAT2 self-testing record"
tags: [lms, uat2, cashflow, lifecycle-events, settlement]
related: [lms, lms-cashflow-lifecycle-message-eligibility, why-do-released-nos-cashflows-have-different-lms-send-outcomes, what-is-the-lms-outcome-for-swift-suppressed-withdrawal-before-release, what-caused-the-uat2-error-for-xsw-and-fxd-cashflows, manual-entity-lms-reference-data-feed, cashflow-suppression-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Self testing.md"]
---
# LMS UAT2 Self-Testing

This informal UAT2 self-testing record is dated 2025-10-23. It records sample cashflows, screenshots, and selected LMS CSV/XML artifacts for release, withdrawal, suppression, non-send, and error scenarios.

The record establishes test execution and artifact capture. It does not, on its own, prove payload correctness, LMS acknowledgement, reconciliation, downstream processing, defect closure, business sign-off, or production deployment.

## Recorded test data

| Smaple | snip | send to LMS |  |
| --- | --- | --- | --- |
| M00202510117 CURR\|OPT\|SMP M00202510118 CURR\|OPT\|SMP N00000050686 CURR\|OPT\|SMP Booking entity 10075222 Counterparty 400617196 Settlement means:NOS cashflow status :Released | `image-2025-10-23_10-47-58.png`; `image-2025-10-23_11-26-48.png`; `image-2025-10-23_11-27-6.png` | `image-2025-10-23_11-29-37.png` |  |
| M00202510120 CURR\|OPT\|SMP M00202510122 CURR\|FXD\|FXD N00000050700 -NULL Booking entity 10075222 Counterparty 400617196 Settlement means:NOS cashflow status :RELEASED | `image-2025-10-23_13-43-16.png`; `image-2025-10-23_14-2-14.png` | `image-2025-10-23_14-1-17.png` |  |
| Single NOS M00202510123 CURR\|OPT\|SMP Released | `image-2025-10-23_14-58-6.png`; `image-2025-10-23_14-58-40.png`; `image-2025-10-23_15-2-0.png`; `image-2025-10-23_15-2-43.png` | `image-2025-10-23_14-57-55.png`; `image-2025-10-23_15-3-38.png` |  |
| M00202510132 CURR\|FXD\|FXD NOS Released Withdrawal | `image-2025-10-25_9-45-11.png`; `image-2025-10-25_9-45-48.png`; `image-2025-10-25_9-46-51.png`; `image-2025-10-25_9-47-17.png`; `image-2025-10-25_9-50-20.png`; Withdrawal event; `image-2025-10-25_10-3-59.png`; `image-2025-10-25_10-4-18.png`; `image-2025-10-25_10-5-15.png`; `image-2025-10-25_10-13-26.png` | `image-2025-10-25_9-49-31.png`; Released; `image-2025-10-25_9-53-22.png`; Withdrawal; `image-2025-10-25_10-7-35.png`; released; `image-2025-10-25_10-14-11.png`; `lms_message_202510251009.csv`; `M00202510132NEW-RELEASED-SEND TO LMS.XML`; `M00202510132WITHDRAWAL-RELEASED-SEND TO LMS.XML` |  |
| M00202510136 swift suppressed withdrawal before released | `image-2025-10-26_12-1-52.png`; `image-2025-10-26_12-2-29.png`; `image-2025-10-26_12-3-46.png`; `image-2025-10-26_12-5-10.png`; `image-2025-10-26_12-9-7.png` | `image-2025-10-26_12-14-42.png`; `image-2025-10-26_12-11-56.png`; `lms_message_202510261211.csv`; `lms_message_202510261203.csv` |  |
| M00202510124 CURR\|FXD\|FXD Settlement means:OVER ACCOUNT NOT SEND TO LMS cashflow status :RELEASED | `image-2025-10-26_11-2-32.png`; `image-2025-10-23_15-10-15.png`; `image-2025-10-23_15-11-32.png`; `image-2025-10-24_11-46-17.png` | `image-2025-10-23_15-8-32.png`; `image-2025-10-23_15-14-2.png`; `image-2025-10-23_15-14-23.png` |  |
| M00202510128 NOS CURR\|FXD\|FXD 401036553 NOT SEND TO LMS Released | `image-2025-10-24_14-10-15.png`; `image-2025-10-25_9-40-16.png` | `image-2025-10-25_9-40-48.png` |  |
| ,M00202510119,CURR\|OPT\|XSW M00202510121,CURR\|OPT\|FXD | ERROR `image-2025-10-23_10-53-1.png`; `image-2025-10-23_10-53-18.png` |  |  |

## Findings bounded by the record

- `M00202510132` is the strongest lifecycle-test evidence because the source names distinct artifacts for release and withdrawal: `M00202510132NEW-RELEASED-SEND TO LMS.XML` and `M00202510132WITHDRAWAL-RELEASED-SEND TO LMS.XML`.
- For `M00202510124`, the source explicitly states: `Settlement means:OVER ACCOUNT NOT SEND TO LMS cashflow status :RELEASED`. This supports a non-send outcome for that sample; it is not sufficient to establish a universal `OVER` eligibility rule.
- Several released NOS samples appear in the source's send-to-LMS test area, while `M00202510128` explicitly states `NOT SEND TO LMS Released`. Therefore, NOS and Released status are not sufficient attributes to infer LMS eligibility from this record.
- `M00202510136` covers SWIFT-suppressed withdrawal before release, with two LMS CSV artifacts. The intended and observed LMS event behavior cannot be determined without inspecting those artifacts.
- `M00202510119` and `M00202510121` are marked `ERROR`, but the error message, processing stage, expectation, and disposition are not retained in the readable source text.

## Scope boundary

This document concerns cashflow lifecycle-message testing for [[lms]]. It is adjacent to, but does not define, the reference-data feed addressed by [[manual-entity-lms-reference-data-feed]]. It also provides scenario evidence relevant to [[cashflow-suppression-rule]], without establishing whether SWIFT suppression changes LMS eligibility.
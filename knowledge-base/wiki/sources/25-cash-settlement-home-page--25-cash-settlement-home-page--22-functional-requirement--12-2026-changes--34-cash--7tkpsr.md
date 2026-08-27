---
type: source
title: Swift Generation UAT Cases Retest
authors: []
year: 2026
url: ""
venue: Internal UAT retest evidence
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, uat, retest, swift-mx, fmsgw, ratan]
related: [korea-cash-settlement-migration, ratan, fmswiftgateway, amh, ratan-swift-message-generation, swift-message-reconciliation, swift-status-lifecycle-and-reconciliation, swift-mx-regression-retest-normalization, what-is-the-final-retest-disposition-for-korea-swift-cases-142-145]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Swift Generation UAT cases retest.md"]
---
# Swift Generation UAT Cases Retest

This source records Korea Migration UAT retest evidence for SWIFT MX requests sent through the RATAN-to-FMSGW route:

`v1/settlement/51358-ratanone/fmsgw/-/scbml-4.0/cash/swift/mx`

The supplied AMHMessage envelopes cover `pacs.008.001.08`, `pacs.009.001.08`, and `camt.056.001.08`, with `54949-FMSGW-MX` as the application identifier. They evidence traffic from [[ratan]] through [[fmswiftgateway]] using [[amh]] envelopes.

## Retest outcomes

| Cases | UAT cashflow ID | Retest cashflow ID | Recorded differences | Recorded result |
|---|---|---|---|---|
| 138, 140 | `N00000243205` | `N00000246711` | `CreDt`, `CreDtTm`, `EndToEndId` | PASS |
| 141 | `M00005815324` | `M0000W815324` | `CreDt`, `CreDtTm` | PASS |
| 142, 143, 144, 145 | `M00005743907` | `M0000W743907` | Not recorded | Not recorded |
| 152, 156, 157, 158 | `M00005815186` | `M0000W815187` | `CreDt`, `CreDtTm`, `EndToEndId` | PASS |

The source header repeats `retest cashflowId` for two columns. Based on the content, the first holds the retest cashflow ID and the second holds the retest SWIFT payload.

## Passed direct-payment evidence

Cases 138 and 140 passed for a `pacs.008.001.08` request from `SCBLKRSEXXX` to `KOEXKRSEXXX`. The comparison retained the USD `117982.51` amount, `INDA` settlement method, settlement account `0963-THR-001030018`, and `/FIN53/KOEXKRSEXXX` instruction.

Case 141 passed for a `pacs.009.001.08` request from `SCBLKRSEXXX` to `SCBLUS33XXX`. The comparison retained USD `30000000`, `INDA` settlement method, settlement account `3582070313001`, the `CHASUS33XXX` and `KODBKRSEXXX` creditor route, and `/FIN53/SCBLUS33XXX`.

For these passed cases, UAT fixtures contained placeholder timestamps of `9999-12-31T00:00:00+00:00`; retests contained actual July 2026 creation timestamps.

## Passed cover-payment and cancellation evidence

Cases 152, 156, 157, and 158 passed as a cover-payment sequence:

- A customer `pacs.008.001.08` from `SCBLKRSEXXX` to `CZNBKRSEXXX` with `SttlmMtd=COVE`.
- A cover `pacs.009.001.08` from `SCBLKRSEXXX` to `KOEXKRSEXXX` with `swift.cbprplus.cov.03`.
- `camt.056.001.08` cancellations addressed separately to `CZNBKRSEXXX` for the customer payment and `KOEXKRSEXXX` for the cover payment.

The sequence retained USD `115814.05`, the reimbursement account `0963-THR-001030018`, and the customer/creditor context for HYUNDAI MOTOR SECURITIES CO LTD. The cancellation requests reference their corresponding original `pacs.008` or `pacs.009` messages, UETRs, settlement amount and date, and cancellation reason `NARR`.

This is UAT evidence for the Korea cover-payment and cancellation route described by [[ratan-swift-message-generation]] and [[swift-status-lifecycle-and-reconciliation]], not production-validation evidence.

## Unadjudicated cases 142–145

The source does not record either a difference classification or PASS/FAIL result for cases 142–145. They must not be considered passed on the basis of this document.

The supplied UAT and retest payloads differ in more than creation timestamps:

- `EndToEndId` changes from `NOTPROVIDED` to generated `DV70M0000W743907`.
- The interbank settlement date changes from `2026-06-19` to `2026-05-15`.
- The next-agent instruction changes from `/FIN53/SCBLUS33XXX/INF/ ABA NO` to `/FIN53/SCBLUS33XXX`.
- The associated `camt.056.001.08` message has runtime creation timestamps and references retest payment data.

Because UAT and retest use different cashflow IDs, some differences may be fixture-specific. Formal disposition remains tracked in [[what-is-the-final-retest-disposition-for-korea-swift-cases-142-145]].

## Interpretation boundary

The source supports accepted runtime timestamp differences for the explicitly passed groups. It also evidences `EndToEndId` generation in the passed `pacs.008` examples, but does not establish a universal rule for every Korea SWIFT MX message type. See [[swift-mx-regression-retest-normalization]].
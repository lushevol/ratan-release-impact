---
type: source
title: Manual Entity (NG GH QA BH UG) Testing with ISO
created: 2026-08-23
updated: 2026-08-23
tags: [uat, manual-entity-settlement, iso-20022, amh, swift, mts, scpay, bahrain, qatar, nigeria, ghana, uganda]
related: [manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, settlement-acknowledgement-flow, amh-acknowledgement-versus-downstream-delivery, scpay-settlement-routing, mts-downstream-settlement-validation, mts, scpay, why-were-nigeria-cases-30-and-31-settled-but-not-received-in-amh, what-was-the-final-outcome-of-bahrain-case-24-in-scpay, why-were-ghana-cases-17-and-18-not-received-in-mts-us, why-was-qatar-case-12-and-its-camt056-scenarios-struck-through, what-are-the-canonical-bic-values-for-manual-entity-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
authors: []
year: 2026
url: ""
venue: "UAT evidence log"
---
# Manual Entity (NG GH QA BH UG) Testing with ISO

This UAT evidence log covers ISO 20022 settlement-message testing for manual entities in Bahrain (BH), Qatar (QA), Nigeria (NG), Ghana (GH), and Uganda (UG). Recorded observations span 2026-08-06 to 2026-08-13.

The evidence distinguishes AMH processing from downstream completion. The source defines `ACKED` as successful processing from the AMH side. A displayed `SETTLED` or `RELEASED` cashflow status is therefore not, by itself, proof of successful delivery to SWIFT, MTS/MTS US, or SCPAY.

## Assessment

- **Bahrain:** Cases 22 and 23 have AMH acknowledgement, SWIFT dispatch, and successful MTS processing. Case 24 remains pending in SCPAY despite being marked `SETTLED`.
- **Qatar:** Retained cases provide positive AMH and, for cases 22–23, MTS processing evidence. Case 12 and its `camt.056.001.08` cancellation messages are struck through without rationale.
- **Nigeria:** Cases 30–31 are marked `SETTLED` but were not received in AMH. Cases 32–33 reached AMH and SCPAY, then required reinitiation.
- **Ghana:** Cases 17–18 were acknowledged by AMH but not received in MTS US; retesting was requested.
- **Uganda:** Cases 17–18 provide AMH acknowledgement evidence only. No downstream delivery result is recorded.

This is mixed operational evidence rather than formal UAT approval or end-to-end sign-off.

## Source Test Data

| Country | UAT case | Message Type | Sender BIC | Receiver BIC | Tag20 | UETR | Cashflow Status | Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BH | case18 | pacs.008.001.08 | SCBLBHBMXXX | CHASGB2LXXX | DV55S00000120436 | faa98b2e-c39b-4928-b380-43430f72057a | RELEASED | 2026-08-06 Pacs.008 - Received in AMH and sent to SWIFT@Shaik Khan Pacs.009.COV - Received in AMH and Got ACKED (ACKED means : From AMH side it is processed successfully) The below txn received in AMH and sent to SWIFT. TXN: DV55S00000120436 Pacs.008 - Received in AMH and sent to SWIFT Pacs.009.COV - Received in AMH and sent to SWIFT |
| BH | case18 | pacs.009.001.08 | SCBLBHBMXXX | SCBLUS33XXX | DV55S00000120436 | 5696513f-93fd-4f53-b4fa-c7f9b31b06b4 | RELEASED | Associated paired message row. |
| BH | case20 | pacs.008.001.08 | SCBLBHBMXXX | SCBLUS33XXX | DV55M00127115448 | 7d31e05f-5519-4c31-90bb-e587a29ef835 | SETTLED | 2026-08-06 Received in AMH and Got ACKED Shaik Khan (ACKED means : From AMH side it is processed successfully) Yes the above payments are received in AMH and sent to SWIFT @Sripadi, Phani Kumar MTS US |
| BH | case21 | pacs.009.001.08 | SCBLBHBMXXX | SCBLUS33XXX | DV55M00127115452 | 40fc95bc-13f7-444b-9853-9837a40131c8 | SETTLED | 2026-08-06 Received in AMH and Got ACKED @Shaik Khan (ACKED means : From AMH side it is processed successfully) Yes the above payments are received in AMH and sent to SWIFT @Sripadi, Phani Kumar MTS US |
| BH | case22 | pacs.008.001.08 | SCBLBHBMAXXX | SCBLUS33XXXX | DV55311106196001 | c98732f3-ea38-46cd-ac67-d844f93e0f82 | SETTLED | 2026-08-12 Received in AMH and Got ACKED @Shaik Khan. Sent to SWIFT. Messages routed to MTS and process successfully in MTS @Sripadi, Phani Kumar. |
| BH | case23 | pacs.009.001.08 | SCBLBHBMAXXX | SCBLUS33XXXX | DV55683874902776 | 6008c6d7-8ea2-441c-bb61-cbfe027d1111 | SETTLED | 2026-08-12 Received in AMH and Got ACKED @Shaik Khan. Sent to SWIFT. Messages routed to MTS and process successfully in MTS @Sripadi, Phani Kumar. |
| BH | case24 | pacs.009.001.08 | SCBLBHBMAXXX | SCBLBHBMXXXX | DV55152971013802 | f8c16d31-83fa-4dd7-be0b-cb884d510158 | SETTLED | 2026-08-12 Received in AMH and Got ACKED @Shaik Khan. Sent to SWIFT. Messages routed to SCPAY and pending to it [Viveka.S@sc.com](mailto:Viveka.S@sc.com). |
| QA | case5 | pacs.008.001.08 | SCBLQAQXXXX | CHASGB2LXXX | DVQAM00127115372 | bddbd829-4552-4453-ac75-f3475a25b4ea | RELEASED | 2026-08-06 @Shaik Khan. |
| QA | case5 | pacs.009.001.08 | SCBLQAQXXXX | SCBLUS33XXX | DVQAM00127115372 | 52582a8c-92ab-4fbd-b77f-b38324fb1e27 | RELEASED | Associated paired message row. |
| QA | ~~case12~~ | ~~pacs.008.001.08~~ | ~~SCBLQAQXXXX~~ | ~~CHASGB2LXXX~~ | ~~DVQAM00127114700~~ | ~~39056667-4c8e-411f-8203-51df69a37bb5~~ | ~~RELEASED~~ | Struck through in source. |
| QA | ~~case12~~ | ~~pacs.009.001.08~~ | ~~SCBLQAQXXXX~~ | ~~SCBLUS33XXX~~ | ~~DVQAM00127114700~~ | ~~9199bf65-00ba-4c97-9fd0-10be60d6ff34~~ |  | Struck through in source. |
| QA | ~~case12~~ | ~~camt.056.001.08~~ | ~~SCBLQAQXXXX~~ | ~~CHASGB2LXXX~~ | ~~DVQAM00127114700~~ | ~~original UETR 39056667-4c8e-411f-8203-51df69a37bb5~~ |  | Struck through in source. |
| QA | ~~case12~~ | ~~camt.056.001.08~~ | ~~SCBLQAQXXXX~~ | ~~SCBLUS33XXX~~ | ~~DVQAM00127114700~~ | ~~original UETR 9199bf65-00ba-4c97-9fd0-10be60d6ff34~~ |  | Struck through in source. |
| QA | case20 | pacs.008.001.08 | SCBLQAQXXXX | SCBLUS33XXX | DVQAM00127115371 | 1d6f630a-7a40-4381-8027-c8f60059a351 | SETTLED | 2026-08-06 Received in AMH and Got ACKED @Shaik Khan. |
| QA | case21 | pacs.009.001.08 | SCBLQAQXXXX | SCBLUS33XXX | DVQAM00127114426 | 683dfff9-60e9-4ae7-abe4-99450ff0dd4a | SETTLED | 2026-08-06 Received in AMH and Got ACKED @Shaik Khan. |
| QA | case22 | pacs.009.001.08 | SCBLQAQXAXXX | SCBLUS33XXXX | DVQA131890016904 | 3e95bcc3-49cf-45b3-b068-d22e7fa4b4df | SETTLED | 2026-08-12 Received in AMH and Got ACKED @Shaik Khan. Sent to SWIFT. Messages routed to MTS and process successfully in MTS @Sripadi, Phani Kumar. |
| QA | case23 | pacs.009.001.08 | SCBLQAQXAXXX | SCBLUS33XXXX | DVQA611659188118 | de5ead10-15a1-4fe1-96ba-8ee46aa35d81 | SETTLED | 2026-08-13 Message received and processed successfully @Sripadi, Phani Kumar. 2026-08-12 received in AMH, ACKED, sent to SWIFT, and processed in MTS. |
| NG | case30 | pacs.008.001.08 | SCBLNGLATSY | SCBLUS33XXX | DV82M00127115444 | 205ee2f0-ee71-4979-96cc-a12508f4cef9 | SETTLED | 2026-08-11 Not received in AMH @Shaik Khan. |
| NG | case31 | pacs.009.001.08 | SCBLNGLATSY | SCBLUS33XXX | DV82M00127115446 | 4e7e33a3-ce14-48f8-a311-1cedb4f0cfcb | SETTLED | 2026-08-11 Not received in AMH @Shaik Khan. |
| NG | case32 | pacs.008.001.08 | SCBLNGLATSY | SCBLNGLAXXX | DV82M00127115547 | 6bbfc62e-6173-496a-8fcf-f8cd91ec7818 | SETTLED | 2026-08-11 Received in AMH and routed to SCPAY @Shaik Khan. 2026-08-13 reinitiate these transactions @Viveka S. |
| NG | case33 | pacs.009.001.08 | SCBLNGLATSY | SCBLNGLAXXX | DV82M00127115563 | 35882399-3ae5-4a2b-b28a-41c0ed55af73 | SETTLED | 2026-08-11 Received in AMH and routed to SCPAY @Shaik Khan. 2026-08-13 reinitiate these transactions @Viveka S. |
| GH | case17 | pacs.009.001.08 | SCBLGHACXXX | SCBLUS33XXX | DV35M00127115443 | ed79cf27-aaee-4b2a-9776-399844af9290 | SETTLED | 2026-08-12 received in AMH and got ACKED. 2026-08-13 Not received in MTS US; need to retest and cover by Kyle automation testing. |
| GH | case18 | pacs.008.001.08 | SCBLGHACXXX | SCBLUS33XXX | DV35M00127115441 | c9bb08b9-58d4-4c43-aac9-868b13d8cd87 | SETTLED | 2026-08-12 received in AMH and got ACKED. 2026-08-13 Not received in MTS US; need to retest and cover by Kyle automation testing. |
| UG | case17 | pacs.009.001.08 | SCBLUGKAXXX | SCBLUS33XXX | DVUGS00000120443 | da90e8f1-a9bd-47bb-b17e-ee0d37bd0d8a | SETTLED | 2026-08-13 received in AMH and got ACKED. |
| UG | case18 | pacs.008.001.08 | SCBLUGKAXXX | SCBLUS33XXX | DVUGS00000120442 | 9883e8f3-6c22-4287-92d8-24a10cc76cf6 | SETTLED | 2026-08-13 received in AMH and got ACKED. |

## Evidence Limitations

The source does not record the final result of Nigeria reinitiation, Ghana retesting, or Bahrain SCPAY processing. It also does not provide a reason for excluding Qatar case 12. BIC values appear in inconsistent forms, including `SCBLUS33XXX` and `SCBLUS33XXXX`; no canonical mapping is supplied.
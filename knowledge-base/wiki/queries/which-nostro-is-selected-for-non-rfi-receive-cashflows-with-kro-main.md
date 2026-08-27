---
type: query
title: Which Nostro Is Selected for Non-RFI Receive Cashflows with KRO MAIN?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, non-rfi, kro-main, receive, mt210, static-data, uat]
related: [portfolio-based-nostro-stamping, notice-to-receive-mt210-control, nostro-stamping, mt210-message-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
---
# Which Nostro Is Selected for Non-RFI Receive Cashflows with KRO MAIN?

## Open Question

For non-RFI KRW/KRO receive cashflows with vostro `KRO MAIN`, is the selected nostro `KRO MAIN` or the RFI nostro?

## Contradictory Source Evidence

Tests 6 and 6.1 are explicitly described as non-RFI receive cases using `KRO MAIN` static data. However, both expected-result descriptions say the cashflow is stamped to the RFI nostro. This conflicts with test 5, which identifies `KRO MAIN` as the non-RFI/primary nostro.

The document's scenario labels and `Notice to Receive` configuration imply `KRO MAIN` is intended, but the expected-result wording must not be treated as authoritative until validated.

## Required Resolution

Correct the UAT cases or obtain execution evidence showing the selected nostro, MT210 payload, and applied `Notice to Receive` configuration for both `N` and `Y` cases.
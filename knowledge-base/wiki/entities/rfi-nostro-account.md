---
type: entity
title: RFI Nostro Account
tags: [settlement-account, Nostro, RFI, Korea, SSI]
related: [ratan, scb-london, scb-korea, portfolio-based-rfi-nostro-stamping, rfi-swift-account-propagation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# RFI Nostro Account

An RFI Nostro account is a dedicated settlement account used for Korea-market cashflows associated with Registered Foreign Institution portfolios.

The requirement states that:

- The account is held with SCB Korea.
- RFI portfolios must be routed to the dedicated RFI Nostro rather than a non-RFI Nostro.
- An RFI Nostro is classified with `Nostro Type = RFI`.
- An RFI Nostro cannot be marked as primary.
- Portfolio values are mandatory for RFI static-data records.
- The account number must be propagated to SWIFT payment field 53 and MT210 tag 25 for KRW.
- Swift-suppressed RFI cashflows must use the corresponding RFI Nostro EBBS account for accounting.

The source names `KRO OTH 1` as the RFI Nostro used in its principal scenarios and `KRO MAIN` as the standard/non-RFI Nostro in several scenarios.

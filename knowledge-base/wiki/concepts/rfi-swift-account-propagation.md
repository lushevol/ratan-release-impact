---
type: concept
title: RFI SWIFT Account Propagation
tags: [RFI, SWIFT, MT210, payment-field-53, account-number, EBBS]
related: [ratan, rfi-nostro-account, swift, mt210-message-generation, ebbs, portfolio-based-rfi-nostro-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# RFI SWIFT Account Propagation

RFI SWIFT account propagation carries the selected RFI Nostro account number from RATAN into downstream payment messages.

The requirement states that:

- The RFI account number must be captured in payment field 53.
- For currency `KRW`, MT210 must contain the account number in tag 25.
- The SWIFT change requires integration testing with downstream systems.
- Swift-suppressed RFI cashflows must use the RFI Nostro EBBS account for accounting.
- Swift-suppressed non-RFI cashflows must use the non-RFI Nostro EBBS account.

The source uses both “KR ccy” and `KRW`; the authoritative currency representation must be confirmed. It also does not define the precise field-53 option, account-number formatting, MT210 schema mapping, or the full set of messages to which field 53 applies.

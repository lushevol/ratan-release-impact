---
type: query
title: What Is the Final RFI SWIFT Field 53 and MT210 Tag 25 Contract?
tags: [RFI, SWIFT, MT210, field-53, tag-25, integration-testing]
related: [rfi-swift-account-propagation, portfolio-based-rfi-nostro-stamping, mt210-message-generation, swift]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# What Is the Final RFI SWIFT Field 53 and MT210 Tag 25 Contract?

The requirement says that the RFI account number must be included in payment field 53 and in MT210 tag 25, while the detailed MT210 rule limits tag 25 to `KRW`.

The final contract needs confirmation for:

- Whether “KR ccy” means `KRW`.
- Which payment message types and field-53 options are in scope.
- The exact account-number format and source field.
- Whether MT210 tag 25 is generated only for RFI cashflows.
- Behavior for non-RFI receipts and notice-to-receive variants.
- Downstream integration-test ownership and acceptance evidence.

---
type: query
title: What Is the Authoritative INR Routing-Account Slash Normalization Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [swift, inr, routing-account, formatting, open-question]
related: [india-routing-account-slash-normalization, 51358-ratanone-swift-service, story-9971484, ratan-swift-message-generation, ssi-driven-swift-field-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/capture slash for India routing account number.md"]
---
# What Is the Authoritative INR Routing-Account Slash Normalization Rule?

The available evidence does not define a single reliable input-to-output rule for leading slashes in INR routing account numbers.

## Evidence to Reconcile

- Manual MT103: input `//30000000056` is shown as output `///30000000056`.
- Manual MT202: input `/30000000056` is shown as output `//30000000056`.
- Auto-stamped MT202: input `///5700000000` is shown as output `//5700000000`.
- Auto-stamped MT103 and MT103Cov: input `///...` is shown as output `//...`.

## Questions

1. What output is required for inputs with zero, one, two, and three leading slashes?
2. Is normalization intentionally different for manual and auto-stamped routing data?
3. Which upstream model, UI, or static-data process supplies `///` values?
4. Is the behavior dependent on MT103, MT202, MT103Cov, MT202Cov, or the specific SWIFT field?
5. Are the documented field outputs compliant with the applicable India routing and SWIFT formatting requirements?

Until answered, the examples should be treated as case-specific evidence rather than a universal formatting algorithm.
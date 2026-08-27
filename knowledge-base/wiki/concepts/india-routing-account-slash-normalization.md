---
type: concept
title: India Routing-Account Slash Normalization
created: 2026-08-23
updated: 2026-08-23
tags: [swift, inr, routing-account, formatting, ratan]
related: [ratan, 51358-ratanone-swift-service, story-9971484, ratan-swift-message-generation, ssi-driven-swift-field-generation, swift-message-reconciliation, what-is-the-authoritative-inr-routing-account-slash-normalization-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/capture slash for India routing account number.md"]
---
# India Routing-Account Slash Normalization

India routing-account slash normalization is the INR-specific handling of leading `/` characters when RATAN renders routing account numbers in SWIFT institution fields.

The documented affected fields are:

- `:54A:` for correspondent routing in MT103Cov.
- `:56A:` for intermediary routing.
- `:57A:` for account-with-institution routing and the corresponding routing field in MT202Cov.

## Input Paths

The source demonstrates two input paths:

1. **Manual entry**, where a user enters account numbers for institution fields.
2. **Auto-stamped routing data**, sourced from `beneficiaryBank:routingAccountNumber`, `intermediaryInformation:routingAccountNumber`, or `correspondentInformation:routingAccountNumber`.

Both paths affect [[ratan-swift-message-generation]], but the available examples do not establish that they follow the same transformation rule.

## Cover-Payment Mapping

The examples show a correspondent routing account rendered in:

- MT103Cov `:54A:`
- MT202Cov `:57A:`

This is a field translation pattern evidenced for INR cover payments. It should not be generalized beyond the documented scope without further validation.

## Unresolved Semantics

Manual examples show an apparent addition of an account-line slash to inputs with zero, one, or two leading slashes. Auto-stamped examples show `///` inputs rendered as `//`. The authoritative behavior, including any distinction by source path or message type, is unresolved and tracked in [[what-is-the-authoritative-inr-routing-account-slash-normalization-rule]].
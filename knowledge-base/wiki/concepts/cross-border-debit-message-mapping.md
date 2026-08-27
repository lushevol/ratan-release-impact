---
type: concept
title: Cross-Border Debit Message Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [cross-border-debit, swift, mt202, mt103, mt292, pacs-009, cbpr-plus]
related: [cross-border-debit-settlement, cross-border-debit-withdrawal-cancellation, vostro-field-57-routing-derivation, what-is-the-authoritative-cross-border-debit-message-format-selection-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# Cross-Border Debit Message Mapping

The UAT evidence indicates that message construction is direction-specific after a cashflow is assigned a `CROSSDEBIT` settlement account.

## Observed Directional Mapping

- **Receive:** cross-debit-mapped MT202 was generated for tested USD, EUR, and GBP cases.
- **Pay:** normal MT103/MT202 mapping was retained in tested USD cases, including MT103 and MT202 cover output.
- **Pay in EUR and GBP:** examples used ISO 20022 `pacs.009.001.08` over `swift.finplus!pc`, while the source still characterizes the behavior as normal MT103/MT202 mapping.
- **Receive withdrawal:** MT292 was generated after withdrawal and maker/checker release.

The source says output was sent to [[lms]], but provides no evidence that LMS accepted or processed it.

## Constraints on Interpretation

The observed FIN/MX split may be determined by currency, direction, booking entity, corridor, BIC, migration status, or another configuration. The UAT document does not define this selection rule. Individual BIC and account values in message samples are examples, not universal mapping requirements.

See [[what-is-the-authoritative-cross-border-debit-message-format-selection-rule]].
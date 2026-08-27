---
type: concept
title: Cross-Border Debit Withdrawal Cancellation
created: 2026-08-23
updated: 2026-08-23
tags: [cross-border-debit, withdrawal, cancellation, mt292, maker-checker, settlement]
related: [cross-border-debit-settlement, cross-border-debit-message-mapping, ratan, lms, split-cashflow-withdrawal-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# Cross-Border Debit Withdrawal Cancellation

Cross-border debit withdrawal cancellation is the UAT-observed lifecycle in which a previously released receive-side `CROSSDEBIT` cashflow is withdrawn, released through maker/checker control, and produces an MT292 cancellation message.

## Observed Lifecycle

1. A receive-side cashflow is stamped or selected with a `CROSSDEBIT` settlement account.
2. The cashflow is released and generates a cross-debit MT202.
3. A withdrawal event reaches [[ratan]].
4. A maker/checker releases the withdrawal.
5. RATAN generates MT292, referring to the original MT202 through field `:11S:202`, and the source states that the message is sent to [[lms]].

The source provides this evidence for USD, EUR, and GBP.

## Boundary

This is distinct from [[split-cashflow-withdrawal-propagation]], which concerns split-cashflow lineage. The source does not specify cancellation timing, duplicate prevention, delivery-failure handling, or reversal-state recovery.
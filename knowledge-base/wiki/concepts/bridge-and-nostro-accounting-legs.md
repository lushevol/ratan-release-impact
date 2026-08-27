---
type: concept
title: Bridge and Nostro Accounting Legs
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, bridge-account, nostro-account, double-entry, korea]
related: [nostro-account-scope, oltp-accounting-message-contract, korea-ratan-oltp-accounting-integration, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Bridge and Nostro Accounting Legs

Each Korea accounting message contains exactly two `AIGJ` account legs:

1. A Bridge or suspense-account leg.
2. A Nostro-account leg.

The legs must carry the same currency and amount with opposite `AIIPJI` directions. For a pay cashflow, the Bridge leg is debit (`10`) and the Nostro leg is credit (`30`); for receive, the directions are reversed.

The Bridge account is `000287` for KRW and `040446` for non-KRW. The Nostro account is sourced from `settlement_Instruction.account.EBBS_Account_Number` in [[ebbs]]. Each message also has exactly one `AIRC` reconciliation record.
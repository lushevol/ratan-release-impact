---
type: concept
title: Nostro Correspondent BIC Normalization
created: 2026-08-23
updated: 2026-08-23
tags: [bic, nostro, reconciliation, oltp, korea]
related: [nostro-account-scope, oltp-accounting-message-contract, bridge-and-nostro-accounting-legs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Nostro Correspondent BIC Normalization

For Korea RATAN-to-OLTP accounting, `AIRCBIC` is sourced from `settlement_Instruction.account.booking_Entity_Correspondent_BIC_code` and normalized to 11 characters.

An eight-character BIC receives three literal ASCII spaces. An 11-character BIC with an `XXX` branch suffix replaces that suffix with three spaces. An 11-character BIC with another suffix is retained. The requirement also illustrates a ten-character input transformed to an eight-character base plus spaces.

NOS cashflows require a populated Nostro correspondent BIC; the requirement asks that it also be maintained for other NOX accounts. Null, invalid-length, lowercase, and malformed BIC handling are not defined.
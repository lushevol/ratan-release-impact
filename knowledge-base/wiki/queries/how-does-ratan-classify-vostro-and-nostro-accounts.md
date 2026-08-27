---
type: query
title: How Does RATAN Classify VOSTRO and NOSTRO Accounts?
tags: [ratan, vostro, nostro, banking, settlement, accounting, reconciliation, foreign-exchange]
related: [vostro-account, nostro-account, correspondent-banking, vostro-vs-nostro, ratan-murex-settlement-cashflow-interface, ratan-oltp-korea-accounting-feed, ratan-fmsgw-settlement-messaging, ratan-enisis-swift-interface]
sources: ["RATAN/RATAN -Knowledge Base/What is VOSTRO NOSTRO.md"]
created: 2026-08-25
updated: 2026-08-25
---
# How Does RATAN Classify VOSTRO and NOSTRO Accounts?

How does RATAN classify, represent, and reconcile VOSTRO and NOSTRO accounts across settlement, accounting, cashflow, and foreign-exchange processes?

## Known from the source

The source establishes only the banking terminology:

- NOSTRO is the account-owning bank’s perspective of its own funds held at another institution.
- VOSTRO is the host bank’s perspective of another institution’s funds held with it.
- The labels are reciprocal and depend on perspective.

## Open questions

Authoritative RATAN documentation is needed to determine:

- Whether VOSTRO or NOSTRO identifiers are stored in account, cashflow, settlement, or counterparty data.
- How account ownership, host institution, currency, and correspondent relationships are represented.
- Whether the labels affect cashflow classification or forecasting.
- How balances and transactions are reconciled.
- How settlement and accounting flows treat these accounts.
- Whether Murex, OLTP, FMSGW, ENISIS, or other RATAN-connected systems have defined mappings.
- Whether foreign-exchange processes use one or multiple NOSTRO, VOSTRO, clearing, or internal settlement accounts.

Until such evidence is available, the terminology pages should not be treated as an implementation contract.

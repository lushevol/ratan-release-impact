---
type: source
title: "What Is VOSTRO NOSTRO"
authors: []
year: 2026
url: ""
venue: "RATAN Knowledge Base"
tags: [banking, correspondent-banking, vostro, nostro, settlement, reconciliation, foreign-exchange]
related: [vostro-account, nostro-account, correspondent-banking, vostro-vs-nostro, how-does-ratan-classify-vostro-and-nostro-accounts]
sources: ["RATAN/RATAN -Knowledge Base/What is VOSTRO NOSTRO.md"]
created: 2026-08-25
updated: 2026-08-25
---
# What Is VOSTRO NOSTRO

## Summary

This RATAN Knowledge Base note explains the reciprocal banking terms **VOSTRO** (“your account”) and **NOSTRO** (“our account”). The distinction depends on the institution’s perspective:

- A **VOSTRO account** is an account held at a bank for another financial institution. It is the host bank’s view of the other institution’s funds.
- A **NOSTRO account** is an account that a bank holds at another financial institution. It is the account-owning bank’s view of its own funds held externally.

The same correspondent account can therefore be a NOSTRO account for the institution that owns the funds and a VOSTRO account for the institution that hosts the account.

## Illustrative case

The note describes a USD account opened by **Industrial and Commercial Bank of China (ICBC)** at **Citibank (USA)** for cross-border USD settlement:

- For ICBC, the account is a **NOSTRO account**.
- For Citibank, the account is a **VOSTRO account** because it holds ICBC’s funds.

## Operational applications

The source associates VOSTRO and NOSTRO accounts with:

- Cross-border transfers through banks’ own externally held accounts and counterparties’ hosted accounts.
- Clearing and reconciliation of settlement positions between financial institutions.
- Foreign exchange settlement, including currency conversion through NOSTRO accounts and recording of customer funds through VOSTRO accounts.

These are high-level banking use cases. The note does not define a particular settlement architecture.

## Source limitation and terminology correction

The first hypothetical VOSTRO example contains a perspective-labeling error. If **Bank B (USA)** opens an account at **Bank A (China)** and Bank A holds Bank B’s funds:

- The account is **VOSTRO from Bank A’s perspective**.
- The account is **NOSTRO from Bank B’s perspective**.

The source should not be interpreted as an authoritative specification for RATAN. It provides no account schemas, journal-entry rules, ownership or balance codes, lifecycle states, reconciliation procedures, APIs, message definitions, or RATAN integration mappings.

See [[vostro-vs-nostro]] for the direct comparison and [[how-does-ratan-classify-vostro-and-nostro-accounts]] for the open RATAN-specific question.

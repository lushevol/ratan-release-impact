---
type: query
title: What Are the Authoritative Korea Accounting Branch Code Mappings?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, accounting, branch-code, oltp, ratan, static-data]
related: [oltp-accounting-message-contract, korea-ratan-oltp-accounting-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# What Are the Authoritative Korea Accounting Branch Code Mappings?

The source uses several branch-related values without documenting their distinct meanings:

- `017` in `AIBRNO`.
- `70` for `SCFB_SEOUL` static data.
- `45` in `X-Outbound-Property-OPICSBranch`.
- `0998` in `BLNG_BR_NO` and `TXN_BR_NO`.

Confirm the semantic owner, format, source, and required use of each value in the RATAN-to-OLTP accounting contract.
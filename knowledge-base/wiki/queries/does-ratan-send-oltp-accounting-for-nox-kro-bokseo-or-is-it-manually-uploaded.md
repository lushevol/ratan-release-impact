---
type: query
title: Does RATAN Send OLTP Accounting for NOX KRO BOKSEO or Is It Manually Uploaded?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, oltp, nox, korea, accounting, operations]
related: [oltp-accounting-eligibility-blacklist, korea-ratan-oltp-accounting-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Does RATAN Send OLTP Accounting for NOX KRO BOKSEO or Is It Manually Uploaded?

The routing conditions identify `KRO BOKSEO` as an NOX account whose accounting enters OLTP. The business table instead says that users manually query SSDR and manually upload accounting into OLTP.

Confirm the authoritative execution path, ownership, and whether RATAN must generate, send, suppress, or merely track the `KRO BOKSEO` accounting entry.
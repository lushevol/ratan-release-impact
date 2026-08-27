---
type: query
title: Is AIRCGBN Null Valid in the RATAN-OLTP Accounting Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [oltp, ratan, accounting, validation, data-contract]
related: [oltp-accounting-message-contract, korea-ratan-oltp-accounting-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# Is AIRCGBN Null Valid in the RATAN-OLTP Accounting Contract?

The field mapping requires `AIRCGBN` to be hardcoded `NULL`, and the request example uses JSON `null`. However, `TXN00029` and `TXN00039` state that an `AIRCGBN` value of `"null"` is an error.

Confirm whether OLTP accepts JSON `null`, requires an omitted field, requires a blank value, or expects another correction indicator. The answer must distinguish a JSON null from the literal string `"null"`.
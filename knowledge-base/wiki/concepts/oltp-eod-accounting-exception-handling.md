---
type: concept
title: OLTP EOD Accounting Exception Handling
created: 2026-08-23
updated: 2026-08-23
tags: [oltp, eod, exceptions, accounting, korea, operations]
related: [kredmi, oscar, ratan-accounting-status-lifecycle, korea-ratan-oltp-accounting-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Korea Cashflow Migration -Ratan to OLTP Accounting.md"]
---
# OLTP EOD Accounting Exception Handling

OLTP EOD runs from 23:30 to 00:30 KST. A rare cashflow delivered during this interval can receive a KREDMI timeout/exception response rather than a normal OLTP result.

When the exception includes `"*body" : "Error"`, RATAN marks the accounting entry `REJECTED` with:

```text
EOD001 — Can not reach to OLTP
```

RATAN displays the failure on its Dashboard. KR OPS manually handles it in [[oscar]] and OLTP. The documented approach is explicitly manual and has no automatic retry.

The requirement does not define a post-timeout inquiry or reconciliation step. Therefore, manual reprocessing could duplicate an entry if OLTP posted it before the response timed out.
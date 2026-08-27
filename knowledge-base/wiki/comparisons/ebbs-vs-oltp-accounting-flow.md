---
type: comparison
title: EBBS vs OLTP Accounting Flow
tags: [ebbs, oltp, accounting, comparison, korea]
related: [ebbs, oltp-accounting, korea-cashflow-migration, accounting-task-retry-exclusion, oltp-scbml-accounting-message]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# EBBS vs OLTP Accounting Flow

| Concern | EBBS | OLTP |
| --- | --- | --- |
| Task initialization | One bridge account per entity assumption | Bridge account depends on currency |
| Validation | Account stamping and EBBS JSON completeness | Account stamping; disable when `settlementMeans = 'NOX'` and `settlementAccount` contains `UUID` or `UISUS` |
| Request storage | `request_info` | `extColumn2` |
| Request contract | EBBS-format JSON | SCBML-wrapped JSON with `TRANDATA` |
| Reversal | Flip account and direction in `request_info` | Flip account and direction in `TRANDATA` in `extColumn2` |
| Publication | Existing EBBS publication function | New publication method and `Cash_Settlement_OLTP_Accounting_KR` |
| Response topic | Existing EBBS topic | `Cash_Settlement_OLTP_Response` |
| Retry | Three retries at four-minute intervals for defined conditions | No retry mechanism; Korea tasks excluded from EBBS retry job |
| SOD message check | Generate if `request_info` is empty | Generate if `extColumn2` is empty |

Both routes share the high-level workflow and SOD schedule. They must remain separate at the payload, persistence, retry, and response-contract boundaries.
---
type: concept
title: Aspire Payment Accounting
created: 2026-08-23
updated: 2026-08-23
tags: [payment-accounting, aspire, ratan, cashflow]
related: [ratan, aspire, aspire-accounting-entry-reversal, aspire-accounting-status-lifecycle, aspire-accounting-static-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Aspire Payment Accounting

Aspire payment accounting is the RATAN capability to generate debit and credit accounting entries for eligible cashflow events and deliver them to [[aspire]] in EOD CSV files.

For a new entry, an SCB pay cashflow debits the bridge account and credits the Nostro account; an SCB receive cashflow debits Nostro and credits bridge. A reversal inverts those postings. Correctness depends on the mappings recorded in [[aspire-accounting-static-data]] and the absent Nostro template.

Eligibility includes specified Released, Settled, FAILED, and SWIFT_SUPPRESSED cashflow states. The accounting capability is distinct from the general lifecycle of [[failed-cashflow-status]] or [[netting-resultant-cashflow]].
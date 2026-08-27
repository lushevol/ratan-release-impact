---
type: query
title: How Does Korea TIS Processing Interact With OLTP Accounting?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, tis, oltp, accounting, payment-processing]
related: [tis, oltp, ratan-tis-payment-query, korea-accounting-and-swift-exception-monitoring, what-is-the-korea-oltp-accounting-exclusion-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Ratan One Processing Guide(DOI)-Korea.md"]
---
# How Does Korea TIS Processing Interact With OLTP Accounting?

The guide positions TIS API retrieval as a replacement for some manual OLTP payment keying. TIS explicitly includes unreversed `Released` or `Settled` cashflows with `STTL_MEANS = NOX` for FMID `10036645`.

Separately, the OLTP accounting section appears to exclude or qualify `NOX` cashflows whose settlement accounts match `UIDD` or `UISUS`.

Confirm whether TIS processing replaces, precedes, coexists with, or creates accounting entries in [[oltp]] for these cashflows. The authoritative answer should define handoff ownership, data mapping, duplicate prevention, and exception recovery.
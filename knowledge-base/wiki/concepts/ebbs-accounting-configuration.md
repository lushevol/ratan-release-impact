---
type: concept
title: EBBS Accounting Configuration
created: 2026-08-23
updated: 2026-08-23
tags: [ebbs, accounting, bridge-account, transaction-codes, settlement]
related: [ebbs, go-live-readiness-for-manual-entity-settlement, tanzania-scb-dar, scb-dhaka-dac-in-country]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche1.md"]
---
# EBBS Accounting Configuration

EBBS accounting configuration is the entity-specific setup required for settlement-accounting generation. In the Tranche 1 checklist, it comprises an EBBS bridge account, posting branch, transaction type, debit transaction code, and credit transaction code.

## Configuration model

The checklist specifies transaction type `RTN` and debit transaction code `478` for all listed Tranche 1 entities. Posting branch and credit transaction code vary by entity.

| FMID | Country | Posting Branch | Txn Type code | Dr Txn Code | Cr Txn Code |
| --- | --- | --- | --- | --- | --- |
| 10041530 | VN | 099 | RTN | 478 | 378 |
| 300011525 | KE | 07800 | RTN | 478 | 278 |
| 10040387 | TZ | 08700 | RTN | 478 | 578 |
| 10041903 | ZM | 01700 | RTN | 478 | 278 |
| 300011470 | BD | 068 | RTN | 478 | 378 |
| 10036655 | PK | 001 | RTN | 478 | 678 |
| 10036647 | LK | 093 | RTN | 478 | 378 |
| 10022098 | LK | 093 | RTN | 478 | 378 |

## Tanzania amendment

The source states that EBBS updated Tanzania's credit transaction code from `278` to `578` on 2026-06-15. The table reflects `578` for `FMID 10040387` / `SCB TANZANI*DAR`. This should be treated as the latest stated configuration until validated against an authoritative EBBS record.

## Bridge-account caveat

The source records bridge account `09111178468` for Bangladesh but says Bangladesh requires double confirmation. It also mentions Qatar as requiring confirmation while providing no Qatar bridge-account row.

See [[ebbs]] and [[go-live-readiness-for-manual-entity-settlement]].
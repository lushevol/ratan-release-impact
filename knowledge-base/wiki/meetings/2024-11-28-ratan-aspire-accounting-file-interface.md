---
type: meeting
title: RATAN Aspire Accounting File Interface
date: 2024-11-28
attendees: [lina, anindya-dasgupta, balaji-sittrarasu, karthick, dendi, ahamed, evelyn, wayne, geoffrey]
action_items: ["Anindya Dasgupta — confirm whether Aspire has concerns with PSGL detailed format and ordering — due date not supplied", "Balaji Sittrarasu — follow up FileIT setup — due date not supplied"]
created: 2026-08-23
updated: 2026-08-23
tags: [meeting, aspire, ratan, fileit, psgl]
related: [ratan, aspire, fileit, aspire-eod-accounting-file-cutoff, fileit-solace-transfer-notifications]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# RATAN Aspire Accounting File Interface

## Attendance

Lina, Anindya, Balaji, Karthick, Dendi, Ahamed, Evelyn, Wayne, and Geoffrey attended.

## Recorded agreements

- The accounting filename was recorded as `RATAN_PAYMENT_TRANSACTION_TH_YYYYMMDD_01.csv`.
- RATAN should produce the same file format as the Murex file.
- Files are sent at 10 PM local time Monday to Friday. Cashflows posted after cutoff are included in the next business-day file, except for the stated 25 December and 1 January exceptions.
- The PSGL format was recorded as `"DV" + Branch code + cashflow ID|Sequence in same cashflow|trade id(for gross)/NET(SPACE)taxonomy(SPACE)counterparty FMCODE(SPACE)cashflow Status`.
- FileIT will be used for transfer. The meeting records that ACK/NACK is not required.

## Actions

- Anindya Dasgupta: confirm whether Aspire has concerns with PSGL detailed format and ordering. Due date not supplied.
- Balaji Sittrarasu: follow up FileIT setup. Due date not supplied.

The statement that ACK/NACK is not required requires interpretation against the configured FileIT acknowledgement notifications; see [[what-is-the-required-ratan-handling-of-fileit-acknowledgements-and-failures]].
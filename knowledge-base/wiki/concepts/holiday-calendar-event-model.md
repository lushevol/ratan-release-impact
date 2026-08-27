---
type: concept
title: Holiday Calendar Event Model
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, holiday-calendar, data-model, cashflow]
related: [rdm, rdm-holiday-and-weekend-ingestion, ratan-static-cashflow-currency-holiday, holiday-data-composite-duplicate-key, what-is-the-canonical-rdm-holiday-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# Holiday Calendar Event Model

The RDM holiday-calendar event model includes a center identifier, ISO currency and country codes, financial-center name, event date and year, day of week, event name, day type, file type, lifecycle state, and creation and modification timestamps.

The source sample includes:

```text
centerId
isoCurrencyCode
isoCountryCode
relatedFinancialCenter
eventYear
eventDate
eventDayOfWeek
eventName
dayType
fileType
entityState
createdTime
modifiedTime
```

The documented sample uses compact, non-ISO date and time representations. `eventDate` appears as `DDMMYYYY`, while audit timestamps appear as `DDMMYYYY HH:mm:ss`; a generated timestamp is explicitly marked `HKT`. Canonical field types, permitted values, timezone rules, and nullability are not defined.
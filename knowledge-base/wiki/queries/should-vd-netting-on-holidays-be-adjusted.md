---
type: query
title: Should VD Netting on Holidays Be Adjusted?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-auto-netting, settlement-calendar, value-date, holiday]
related: ["auto-netting-datetime-calculation", "business-calendar-relative-netting-time", "cashflow-auto-netting"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting.md"]
---
# Should VD Netting on Holidays Be Adjusted?

The currency-calendar examples establish that `VD-1` uses the relevant currency calendar, including CNY working weekends. They also show a GBP payment date that is a holiday remaining unchanged when the configured offset is `VD`.

The source does not define whether this behavior is intentional for all holiday and weekend value dates, or whether `VD` should sometimes be normalized to a currency working day.

A decision is needed for scheduler implementation, operational expectations, and acceptance testing.
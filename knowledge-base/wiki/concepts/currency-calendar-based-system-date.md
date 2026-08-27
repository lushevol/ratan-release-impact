---
type: concept
title: Currency-Calendar-Based System Date
tags: [cashflow, business-day, currency-calendar, swift-value-date]
related: [reinstated-from-failed-exception, payment-date-override, failed-cashflow-reprocessing]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md"]
---
# Currency-Calendar-Based System Date

For failed cashflow re-processing, **Current System Date** means the latest business day calculated according to the relevant currency calendar. It is not necessarily the literal calendar date on which the user performs the action.

The source gives examples in which the result differs by currency:

- For USD, a user action on Saturday 22 April results in a system date of Monday 24 April because Saturday and Sunday are non-working days.
- For CNY, the example treats Saturday 23 April as a working day and returns 23 April.

This indicates that business-day determination is currency-specific. The result is one of the permitted values for `Swift Value Date` in the [[reinstated-from-failed-exception]] workflow.

## Unresolved Calendar Definition

The requirement does not identify:

- The authoritative currency-calendar service.
- Holiday-calendar ownership or version.
- Timezone and end-of-day cutoffs.
- Treatment of holidays and regional non-working days.
- Whether the calculation is based on currency, settlement location, account, or another attribute.

The term **Current System Date** should therefore be treated as a business label pending confirmation of the authoritative calculation rule.
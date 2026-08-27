---
type: query
title: What Is the Authoritative Timezone Rule for Cash Settlement DateTime Fields?
tags: [open-question, timezone, utc, datetime, cash-settlement]
related: [cash-settlement-home-page, utc-local-time-display-toggle, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--46-9--myq5fx, currency-calendar-based-system-date]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244054-Bug - UTC   Local ccy toggle doesnt work.md"]
---
# What Is the Authoritative Timezone Rule for Cash Settlement DateTime Fields?

## Question

What timezone should the Cash Settlement Home Page use for “local” display, and which DateTime fields must change when the UTC/local control is activated?

## Known evidence

Bug `9244054` states that clicking the UTC button does not change DateTime-related fields correspondingly. It requires the button to display the correct datetime, but does not define the local timezone, field inventory, conversion ownership, or persistence behavior.

## Decisions needed

The owning team should establish:

1. Whether “local” means browser timezone, user-profile timezone, business timezone, or server timezone.
2. Whether timestamps are stored canonically in UTC.
3. Whether conversion occurs in the frontend or backend.
4. Which fields are in scope.
5. Whether the control affects timestamps only, or also currency and business-date values.
6. Whether the selected mode persists across refreshes, navigation, or sessions.
7. The required format and timezone indicator.
8. The expected handling of null, date-only, timezone-less, and daylight-saving-sensitive values.

## Why this matters

The terms “local ccy” and “UTC/local time” are inconsistent in the source. Currency-calendar dates and payment dates must not be conflated with timezone conversion. The authoritative rule is required before the defect can be implemented and verified reliably.

## Related evidence

- [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--46-9--myq5fx]]
- [[entities/cash-settlement-home-page]]
- [[concepts/utc-local-time-display-toggle]]
- [[concepts/currency-calendar-based-system-date]]
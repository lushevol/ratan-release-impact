---
type: concept
title: UTC/Local Time Display Toggle
tags: [timezone, utc, datetime, user-interface, cash-settlement]
related: [cash-settlement-home-page, what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-ktlo-requirement--46-9--myq5fx]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244054-Bug - UTC   Local ccy toggle doesnt work.md"]
---
# UTC/Local Time Display Toggle

A UTC/local time display toggle is a UI control that changes how timestamp values are rendered without necessarily changing the underlying stored value.

In the reported Cash Settlement Home Page defect, activating the UTC control does not update the related DateTime fields. The intended behavior is timezone-aware presentation of all fields within the control's defined scope.

## Required behavior

A well-defined toggle should specify:

- The selected display mode and its default.
- The authoritative meaning of “local.”
- The complete set of controlled DateTime fields.
- The conversion source and target timezones.
- The display format and whether a timezone indicator is shown.
- Behavior for null, date-only, and timezone-less values.
- Behavior during refresh, sorting, filtering, pagination, and navigation.
- Persistence scope for the selected mode.

Selecting UTC should render every in-scope timestamp in UTC. Selecting local time should render those timestamps in the defined local timezone. The fields should update together and without a page refresh.

## Boundary conditions

Timezone display logic should be tested for:

- Values close to midnight and dates that cross calendar boundaries.
- Daylight-saving-time transitions where applicable.
- Positive and negative UTC offsets.
- Null or incomplete timestamp values.
- Data refresh and re-rendering after the control changes.

## Scope distinction

This concept concerns timestamp presentation. It should not be assumed to govern business dates, currency-calendar system dates, payment-date overrides, or backend settlement calculations without additional evidence.
---
type: source
title: "9244054 — UTC/Local Time Toggle Defect"
tags: [cash-settlement, functional-requirement, ktlo, bug, timezone, datetime]
related: [cash-settlement-home-page, utc-local-time-display-toggle, what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244054-Bug - UTC   Local ccy toggle doesnt work.md"]
authors: []
year: 2025
url: ""
venue: ""
---
# 9244054 — UTC/Local Time Toggle Defect

## Summary

This source reports a defect in the UTC control on the [[entities/cash-settlement-home-page]]. Clicking the control does not update DateTime-related fields to the expected time representation.

The source title refers to a “UTC Local ccy” toggle, while the body describes UTC and DateTime behavior. The intended scope should therefore be confirmed before implementation or closure.

## Reported behavior

The UTC button is shown in a highlighted area of the Cash Settlement Home Page. When the button is clicked, the affected DateTime fields do not change correspondingly.

## Expected behavior

The control should be functional. When the UTC mode is selected, every in-scope DateTime field should display the correct UTC value. If the control supports both modes, selecting local time should display values in the defined local timezone.

All affected fields should update consistently without requiring a page refresh.

## Source context

> The UTC button in the red box below doesn't work, when click this button, the DateTime type related fields doesn't change correspondently.
>
> So we need to effective the button, when click this button, the DateTime type related fields should change to the right datetime.

The source references the following image:

`attachments/image-2025-7-4_17-15-53.png`

## Evidence limitations

The report does not define:

- The exact control type or default mode.
- The meaning of “local” timezone.
- The complete set of affected fields.
- Whether timestamps are stored in UTC and converted at presentation time.
- Whether the setting persists across navigation, refresh, or sessions.
- The behavior for null, date-only, or timezone-less values.
- Display format, daylight-saving-time handling, or date-boundary behavior.
- Whether the issue affects backend data or only UI presentation.

No SQL DDL, API signature, configuration, schema, or structured table is included in the source.

## Recommended acceptance criteria

1. The control exposes a clearly defined UTC/local selected state.
2. Selecting UTC updates every in-scope DateTime field to UTC.
3. Selecting local time updates every in-scope DateTime field to the authoritative local timezone.
4. All affected fields update immediately and consistently.
5. The selected mode remains consistent during sorting, filtering, pagination, and data refresh.
6. Date-boundary and daylight-saving-time behavior is defined and tested where applicable.
7. Null and timezone-less values have explicitly defined behavior.
8. Automated tests cover representative timestamps, including values near midnight and timezone-offset changes.
9. The control label is corrected if “ccy” is a typographical error.

## Related pages

- [[entities/cash-settlement-home-page]]
- [[concepts/utc-local-time-display-toggle]]
- [[queries/what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]]
- [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--22-functional-requiremen--1ya5f39]]
---
type: concept
title: Auto Netting Datetime Calculation
tags: [auto-netting, datetime, business-calendar, weekends, holidays, netting-static]
related: [cashflow-auto-netting, business-calendar-relative-netting-time, auto-netting-rule-management, manual-cashflow-netting, what-is-the-authoritative-auto-netting-cutoff-time-semantics]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Datetime Calculation.md"]
---

# Auto Netting Datetime Calculation

## Definition

Auto Netting Datetime Calculation determines when eligible cashflows are expected to be processed by the [[concepts/cashflow-auto-netting]] job. The calculation uses a payment or value date, an offset and time from Netting Static, and calendar-handling rules.

The source specifically discusses `VD-1 5AM`: one day before the payment date at 5:00 AM.

## Calendar policy issue

The reported example produces different dates for cashflows with the same payment date:

- XAU payment date `2025-11-12`: `2025-11-11 5:00`, because 2025-11-11 is a working day in the example.
- USD payment date `2025-11-12`: `2025-11-10 5:00`, because 2025-11-11 is a USD holiday in the example.

A proposed alternative is to skip weekends but not currency holidays. That would retain `2025-11-11 5:00` for USD. This is a proposal documented in the source, not a confirmed rule.

## Distinct dates

The following dates must not be conflated:

- **Calculated auto-netting datetime:** the configured target datetime for auto-netting.
- **Release date:** when the cashflow becomes available for processing.
- **Actual job execution time:** when the auto-netting job runs.
- **Manual processing date:** when Operations processes a cashflow outside the scheduled job.

The source shows a USD example in which the release date is `2025-11-10`, while the proposed no-holiday auto-netting datetime is `2025-11-11 5:00`. This indicates that release-date and auto-netting-date calculations may use different calendar semantics.

## Late-arriving cashflows

Cashflows created after the calculated datetime can be processed in a later job, as illustrated by USD cashflows processed at `2025-11-10 7:30` after the initial `2025-11-10 5:00` job. The source does not define whether this is:

- the standard next-run behavior;
- a result of a configurable late-arrival policy;
- a manual-netting exception; or
- a recalculation to a future datetime.

The job's boundary for cashflows created exactly at, after, or during execution remains unspecified.

## Operational consequence of holidays

Retaining a holiday as the calculated datetime is only sufficient if the organization defines what happens when the scheduled job does not run on that holiday. The source records a manual fallback: Operations may manually net cashflows if the calculated datetime falls on an Operations vacation day.

This creates an unresolved dependency between calendar calculation and job availability. The system must distinguish the target datetime from the availability of an automated processing run.

## Configuration considerations

The source recommends configuring a later netting datetime when cashflows are likely to arrive after the current configured time. This is an operational mitigation rather than a complete late-arrival rule. A robust specification should define:

- the owner and scope of the configuration;
- whether it applies globally, per currency, product, or netting rule;
- eligibility at the cutoff boundary;
- behavior when a job is skipped;
- interaction with release dates; and
- audit and operational monitoring requirements.

## Evidence status

The XAU/USD discrepancy and the example timelines are concrete source evidence. The weekend-only policy and the manual-versus-automatic late-arrival options remain unresolved design proposals.

See [[comparisons/auto-netting-holiday-handling-options]] for the alternatives documented by the source.
---
type: concept
title: Release Cutoff Configuration
created: 2026-08-22
updated: 2026-08-23
tags: [settlement, cutoff, static-data, release-control, release, razor, timezone]
related: [entity-branch-onboarding, vietnam-ifc-branch, dev-team, ops-team, razor, manual-entity-go-live-static-data-controls, fmid-country-time-zone-resolution, what-are-the-authoritative-razor-release-cutoff-values-for-qatar-tanzania-and-bangladesh, ratan, manual-entity-go-live-readiness, what-are-the-final-qatar-release-cutoff-and-ebbs-configurations]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md"]
---
# Release Cutoff Configuration

Release cutoff configuration defines the time after which settlement release is restricted or handled differently for a specific legal entity and currency. It also defines the date-shifting rule, applicable timezone, and source of truth used to govern settlement release.

For manual-entity cashflows, release-cutoff configuration determines when a cashflow may be released and which business-day shift applies.

A documented intended value does not demonstrate that it has been loaded into [[ratan]] or validated in a settlement flow.

## Control Model

According to the Vietnam branch onboarding source, release cutoffs are defined at legal-entity-and-currency granularity. Operations must provide reviewed and approved values, and the [[dev-team]] deploys them to production under a Change Request.

According to the manual-entity go-live checklist, `VD-1BD` is specified with explicit UTC cutoff times for most entities.

## Required Information

Based on the Vietnam branch onboarding source, a deployable cutoff record should identify:

- Legal entity or branch identity.
- Currency.
- Cutoff time.
- Time zone and calendar.
- Effective date.
- Operational treatment after cutoff.
- Reviewer and approver.
- Production deployment reference.

## Entity- and Source-Specific Requirements

### Vietnam IFC Branch

The Vietnam branch onboarding source requires cutoff configuration for the [[vietnam-ifc-branch]] but does not provide the currencies, cutoff values, time zones, or approval evidence.

### Manual-Entity Checklist

The manual-entity go-live checklist identifies Qatar, Tanzania, and Bangladesh as exceptions. Their Currency, Shifter, Time, and Timezone values must be obtained from [[razor]], rather than from explicit checklist values.

That checklist does not include the Razor values or evidence that they were configured.

### Tranche 2 Values

The Tranche 2 checklist records the following intended release-cutoff values:

| Entity | Cutoff time | Shifter |
|---|---:|---|
| Bahrain | `15:00 UTC` | `VD-1BD` |
| Uganda | `15:00 UTC` | `VD-1BD` |
| Ghana | `15:00 UTC` | `VD-1BD` |
| Nigeria | `17:00 UTC` | `VD-1BD` |

The Tranche 2 checklist states that Qatar has no effective values in that checklist. Qatar's currency, shifter, time, and timezone are intended to come from [[razor]].

The Tranche 2 values are documented intended values; the source does not establish that they were loaded into [[ratan]] or validated through a settlement flow.
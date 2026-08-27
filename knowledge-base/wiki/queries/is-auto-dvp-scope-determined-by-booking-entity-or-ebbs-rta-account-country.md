---
type: query
title: Is Auto DVP Scope Determined by Booking Entity or EBBS RTA Account Country?
created: 2026-08-23
updated: 2026-08-23
tags: [dvp, scope, booking-entity, ebbs, country]
related: [auto-dvp, auto-dvp-pilot-scope, ebbs-rta-notification]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Is Auto DVP Scope Determined by Booking Entity or EBBS RTA Account Country?

The pilot is expressed as a booking-entity list, while CorporateFinancial RTA country code is stated to identify the account country. The required scope dimension controls both event subscription and cashflow eligibility.

Confirm whether the rule is booking entity, RTA account country, or a conjunction of both, and publish a machine-readable configuration list for all included China branches.
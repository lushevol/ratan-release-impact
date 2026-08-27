---
type: concept
title: RATAN Settlement Contact Routing
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, settlements, operations, escalation, fmcodes, fmids]
related: [ratan, pss, gbs-settlements-east, gbs-settlements-west, in-country-ops, clearing-ops, what-is-the-current-korea-settlement-onboarding-and-contact-routing-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Settlements Ops Contacts.md"]
---
# RATAN Settlement Contact Routing

RATAN settlement contact routing assigns operational contacts by settlement profile, using `COUNTRY`, `FMCODE`, and `FMID` as routing keys.

## Scope Boundary

The contact directory applies only to teams with Settlement profiles. It must not be treated as an enterprise-wide RATAN support or ownership directory.

For wider issues, PSS is instructed to raise an incident ticket and communicate with all RATAN users. The source does not identify the incident system, severity criteria, distribution list, response ownership, or service-level expectations.

## Routing Dimensions

The source organizes contacts across these functional columns:

- [[gbs-settlements-east]]
- [[gbs-settlements-west]]
- [[in-country-ops]]
- [[clearing-ops]]

Country alone is not a sufficient routing key: multiple countries have several `FMCODE`/`FMID` profiles with different contact assignments.

## Clearing Routing Is Conditional

Clearing Ops contacts are assigned only to explicitly listed profiles. For example, China Clearing Ops routing is limited to `SCB CN CHO*CHO` / FMID `400899993`; it must not be inferred for every China profile or every settlement profile.

## Limitations

A blank contact cell has no defined meaning in the source. It may indicate missing data, exclusion, unsupported scope, or another process, but the source does not say which.

The contradictory Korea entries for `SCB SEOUL*SEL` / FMID `10036645` require validation before they are used for operational routing. See [[what-is-the-current-korea-settlement-onboarding-and-contact-routing-status]].
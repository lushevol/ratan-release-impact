---
type: query
title: What Is the Impact and Remediation Status of CA PV-Check Bypass?
tags: [ratan, ca-control, pv-check, remediation, open-question]
related: [pv-check-bypass-risk, ratanone-ca-control-service, ratan-operational-observability]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# What Is the Impact and Remediation Status of CA PV-Check Bypass?

## Question

Which trades were affected by the `event_reason varchar(25)` constraint, did their major versions skip PV checking, and were they retrospectively revalidated?

## Evidence

The value `REMAINING_PARTY_FULL_NOVATION` is 29 characters, while the database field allows 25 characters. The source states that the resulting defect causes the trade major version to skip PV checking.

## Required resolution evidence

- The affected-trade population and time range.
- Confirmation that the schema or application fix was deployed.
- Results of retrospective PV checks.
- Any corrected trades, downstream notifications, or control exceptions.
- Owner, release identifier, deployment date, and post-deployment monitoring results.

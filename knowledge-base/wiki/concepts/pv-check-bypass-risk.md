---
type: concept
title: PV-Check Bypass Risk
tags: [ratan, pv-check, ca-control, schema-constraint, data-integrity, control-risk]
related: [ratanone-ca-control-service, what-is-the-impact-and-remediation-status-of-ca-pv-check-bypass, ratan-operational-observability]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# PV-Check Bypass Risk

PV-check bypass risk occurs when a CA-control event cannot be persisted because its event reason exceeds the database column length, causing the trade major version to skip PV checking.

The source provides the following evidence:

```text
ERROR: value too long for type character varying(25)
```

```text
event_reason at max of 25 characters
REMAINING_PARTY_FULL_NOVATION
```

`REMAINING_PARTY_FULL_NOVATION` is 29 characters, exceeding the `event_reason varchar(25)` definition. The source attributes the defect to `ratanone-ca-control-service` and explicitly states:

```text
The impact is this major version of trade will skip PV check.
```

This is a material control-impacting defect and should not be grouped with routine “no impact/ignore” alerts. Remediation requires identifying affected trades, determining whether PV checks were skipped, and recording retrospective validation.

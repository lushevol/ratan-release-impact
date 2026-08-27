---
type: query
title: What Is the Authoritative OLA Monitoring Owner Between Murex and Ratan?
created: 2026-08-24
updated: 2026-08-24
tags: [ola, monitoring, murex, ratan, operations]
related: [cash-settlement-ola-break-monitoring, murex, itrs, ratan-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# What Is the Authoritative OLA Monitoring Owner Between Murex and Ratan?

The source calls Murex real-time ITRS monitoring the preferred control for Murex-to-Ratan missing cashflows, while assigning RATAN PSS a second-level control based on groups pending for more than five minutes.

The operational model needs to establish:

- the accountable owner for the primary alert;
- the expected handoff and acknowledgement SLA between Murex PSS and RATAN PSS;
- the authoritative definition of a missing cashflow;
- whether group-level monitoring is only an escalation safety net; and
- how duplicate alerts and duplicate replay requests are prevented.
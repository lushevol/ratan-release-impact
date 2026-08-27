---
type: query
title: What Is the Approved Indonesia RDM API Schedule and Data-Freshness SLA?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, scheduling, data-freshness, indonesia, control-m, holiday-calendar]
related: [rdm, rdm-api-based-holiday-compensation, ratan-indonesia-onshoring-2026, indonesia-environment-readiness-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/RDM API call for compensation.md"]
---
# What Is the Approved Indonesia RDM API Schedule and Data-Freshness SLA?

The source states that RDM calls CoppClark at 08:00 HK and provides data after 09:00 HK. It also records Indonesia Control-M execution “After 8am IST” and a temporary Indonesia holiday-data action before 18:00 IST. These timings do not define a clearly compatible operating schedule.

## Questions to Resolve

- What time zone and trigger time are approved for Indonesia synchronization?
- What is the latest acceptable source-data availability time for each operational day?
- Which Indonesia time zone governs service-level commitments where WIB, WITA, and WIT differ?
- What retry window, escalation path, and manual fallback apply if RDM data is late or unavailable?
- Does the future scheduler replacing Control-M preserve the same timing, authorization, audit, and alerting behavior?

## Evidence

Currency-holiday freshness directly affects downstream settlement cutoff-date calculation. The schedule must therefore be approved as a business-day control, not merely a batch-job configuration.
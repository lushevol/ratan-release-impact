---
type: query
title: What Caused Inter-Entity Netting Coverage to Drop in June and August 2026?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, auto-netting, incident-analysis, coverage, settlement-day-2]
related: [inter-entity-netting-coverage-metrics, auto-netting-rule-check, auto-netting-static-go-live-sequencing, netting-rule-change-cashflow-refresh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter entity Netting - Volume Tracker.md"]
---
# What Caused Inter-Entity Netting Coverage to Drop in June and August 2026?

The volume tracker identifies two periods of materially lower reported in-scope netting coverage.

## Observed Periods

From 22 to 25 June 2026, reported `Netted vs in scope` was 1%, 17%, 12%, and 24%, before returning to 99% on 26 June.

After the 30 July 2026 observation of 99.80% in-scope coverage, subsequent rows report 83%, 87%, 74%, 82%, 77%, and 73%. The dates on the final three rows require confirmation because the source uses inconsistent formats.

## Evidence Needed

Investigate whether either period is explained by:

- netting-rule static configuration, activation, or deployment status;
- batch or job execution failures;
- upstream cashflow availability or data-quality issues;
- eligibility-rule changes or threshold handling;
- entity-pair coverage, exception populations, or unmatched cashflows;
- post-rule-change refresh behavior.

The tracker records UK vs SG and UK vs Dubai rule-creation events on 31 July 2026, immediately before the later decline. This is temporal proximity only and does not demonstrate causation. Root-cause evidence should include job logs, configuration history, exception reporting, and entity-pair-level volume data.

See [[inter-entity-netting-coverage-metrics]] for metric interpretation and [[auto-netting-static-go-live-sequencing]] for related rollout context.
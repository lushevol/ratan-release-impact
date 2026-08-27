---
type: concept
title: Auto-Netting Job Time
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, job-time, value-date, shifter, lifecycle, scheduling]
related: [auto-netting-rule-configuration, lifecycle-service, controlm, what-is-the-canonical-auto-netting-job-schedule-and-timezone, what-is-the-auto-netting-hint-and-pending-auto-netting-status-transition]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# Auto-Netting Job Time

Auto-netting job time (`jobTime`) is the deferred-processing time calculated by [[lifecycle-service]] after an auto-netting eligibility request:

```text
jobTime = VD + Shifter
```

`VD` is provided alongside the configured shifter when the rule-check hint applies. The design adds `job_time` to SCBML history and uses job time as part of the auto-netting group key.

The scheduled job groups eligible cashflows by booking entity, currency, counterparty, value date, and job time. Before `jobTime`, a group is not processed. At or after `jobTime`, a group with more than one cashflow is sent to netting; a single-cashflow group is processed through [[single-cashflow-auto-netting-exception]].

The source does not define timezone, value-date calendar behavior, date rollover, daylight-saving handling, or the relationship between Static Service datetime calculation and Lifecycle Service calculation.
---
type: query
title: What Is the Authoritative Murex-RATAN Publication and Monitoring Window?
tags: [murex-211, ratan, fmrp, publication-window, monitoring, open-question]
related: [murex-211, ratan, fmrp-cashflow-publication-lifecycle, murex-ratan-hybrid-batch-and-realtime-processing, lien-cashflow-monitoring-workaround]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document.md"]
---
# What Is the Authoritative Murex-RATAN Publication and Monitoring Window?

The DOI contains two different horizons:

- RATAN-eligible payments and automatic future-value-date publication are described as covering nine days.
- The LIEN monitoring query restricts payment value dates to the current Murex processing date through seven days later.

The source does not explain whether the seven-day LIEN window is an intentionally narrower operational monitoring period, a legacy filter, or an inconsistency.

The same DOI also describes the batch schedule as “110 payments on 00:00–17:00 GMT from Monday to Friday every 15min.” The meaning of “110 payments” and the current validity of this schedule after the SG, IN, and KL migration revision are not established.

## Questions to resolve

1. Is nine days the authoritative publication horizon?
2. Is seven days the intended LIEN monitoring horizon?
3. Does the LIEN query omit eligible payments that require monitoring?
4. What does “110 payments” mean: a batch identifier, capacity, or transcription error?
5. Is the documented schedule still current for all migrated regions?

Until resolved, the nine-day eligibility rule, the seven-day LIEN query, and the batch wording should remain separately documented rather than normalized into one global rule.
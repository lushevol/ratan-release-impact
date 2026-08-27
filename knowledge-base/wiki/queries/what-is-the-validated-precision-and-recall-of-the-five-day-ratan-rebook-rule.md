---
type: query
title: What Is the Validated Precision and Recall of the Five-Day Ratan Rebook Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, rebook-exception, false-positive, false-negative, validation]
related: [ratan, rebook-exception, payment-date-proximity-matching, amendment-driven-cashflow-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# What Is the Validated Precision and Recall of the Five-Day Ratan Rebook Rule?

Ratan reduced its payment-date proximity threshold from 15 days to 5 days on 2026-05-30 to reduce rebook exceptions. The source reports lower post-deployment exception volume, but it does not measure whether retained exceptions are genuine amendment rebooks or whether genuine rebooks are now missed.

## Evidence needed

- A labelled sample of amendment-driven and unrelated new cashflows.
- Counts of true positives, false positives, false negatives, and true negatives for both thresholds.
- A defined observation period and separate analysis for Murex and [[stella]].
- Operations validation outcomes for rebook exceptions.
- A documented baseline for the expected approximately 40% volume reduction.

The outcome should distinguish an operational volume reduction from validated improvement in matching accuracy.
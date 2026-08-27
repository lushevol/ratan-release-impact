---
type: concept
title: PRE/POST Performance and Regression Testing
created: 2026-08-24
updated: 2026-08-24
tags: [performance-testing, regression-testing, controlled-comparison, cash-settlement, murex-2-11]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1aw0oef, was-the-msrb-pss-concern-formally-resolved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 MSRB Evidence.md"]
---
# PRE/POST Performance and Regression Testing

PRE/POST performance and regression testing compares a baseline state with a changed state. Using the same dataset in both runs helps isolate the effect of the change from differences in input volume or composition.

## Required evidence

A conclusive comparison should identify:

- the exact PRE and POST software, configuration, schema, and operational states;
- dataset provenance, volume, composition, and whether it represents production use;
- environment capacity and concurrent workload;
- runtime, throughput, error rate, resource-use, and data-growth measurements;
- functional regression cases and their expected outcomes;
- acceptance thresholds and an accountable approval decision.

## Application to CN Settlement

The source register identifies a same-dataset PRE/POST test workbook for CN Settlement and [[murex-211|Murex 2.11]] cashflow integration. It does not reproduce the test design, measurements, thresholds, or result. Consequently, it cannot alone demonstrate the absence of a performance or functional regression.

See [[was-the-msrb-pss-concern-formally-resolved|Was the MSRB/PSS Concern Formally Resolved?]] for the unresolved acceptance question.
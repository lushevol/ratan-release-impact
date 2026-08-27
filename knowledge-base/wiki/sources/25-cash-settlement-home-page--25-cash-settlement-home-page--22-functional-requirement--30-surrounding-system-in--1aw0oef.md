---
type: source
title: CN Settlement - Murex 2.11 MSRB Evidence
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cn-settlement, murex-2-11, msrb, performance-testing, regression-testing, evidence-register]
related: [murex-211, cash-settlement-home-page, pre-post-performance-regression-testing, staging-purge-job-performance, cash-settlement-inbound-outbound-message-validation, was-the-msrb-pss-concern-formally-resolved, what-are-init-sntr-and-stpdoc-entry-table]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 MSRB Evidence.md"]
authors: []
year: 0
url: ""
venue: ""
---
# CN Settlement - Murex 2.11 MSRB Evidence

This source is an evidence register for a stated PSS concern associated with MSRB in the CN Settlement–[[murex-211|Murex 2.11]] cashflow-integration context.

It indexes five Excel workbooks but does not include their underlying results, test environments, acceptance thresholds, approvals, message payloads, or operational metrics. It must therefore be treated as a record of available evidence, not proof that the concern was resolved.

## Evidence inventory

1. **Performance and regression tests — PRE and POST using the same dataset**
   - Attachment: [Performance&Regression 0428.xlsx](attachments/Performance&Regression%200428.xlsx)
   - The stated design supports [[pre-post-performance-regression-testing|controlled PRE/POST performance and regression testing]] by holding the dataset constant.

2. **Performance and regression tests — POST-CN-Payment database-size comparison**
   - Attachment: [Performance&Regression 0419.xlsx](attachments/Performance&Regression%200419.xlsx)
   - Covers database-size differences for `INIT-SNTR` and `STPDOC_ENTRY_TABLE` following CN Payment processing.

3. **New task and formula summary**
   - Attachment: [New Task&Formula Summary.xlsx](attachments/New%20Task&Formula%20Summary.xlsx)
   - Identifies new tasks and formulas, although this source provides neither their definitions nor their impacts.

4. **Staging purge execution**
   - Attachment: [Staging Purge.xlsx](attachments/Staging%20Purge.xlsx)
   - Intended to provide purge-job running-time and performance evidence, relevant to [[staging-purge-job-performance|staging purge job performance]].

5. **Inbound and outbound messages**
   - Attachment: [InOutbound message_1012.xlsx](attachments/InOutbound%20message_1012.xlsx)
   - Intended to provide integration-message evidence, relevant to [[cash-settlement-inbound-outbound-message-validation|cash settlement inbound and outbound message validation]].

## Evidence limitations

The Markdown source does not state:

- the PRE and POST system states, dataset content, environment, or production representativeness;
- test timings, throughput, error rates, resource consumption, or pass/fail criteria;
- the size values or acceptable-growth rationale for `INIT-SNTR` and `STPDOC_ENTRY_TABLE`;
- the new tasks or formulas and their functional or operational effects;
- staging purge volume, batch-window target, retries, or failure handling;
- message types, payload fields, acknowledgements, rejection cases, or reconciliation results;
- a conclusion, acceptance decision, or formal PSS/MSRB sign-off.

The approval status is tracked by [[was-the-msrb-pss-concern-formally-resolved|Was the MSRB/PSS Concern Formally Resolved?]]. The ownership and meaning of the database objects are tracked by [[what-are-init-sntr-and-stpdoc-entry-table|What Are INIT-SNTR and STPDOC_ENTRY_TABLE?]].

## Context

This evidence register supplements [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1r9fh58|Surrounding System Integration]] and concerns the [[cash-settlement-home-page|Cash Settlement Home Page]] integration landscape. It does not establish a relationship to Vostro SSI processing.
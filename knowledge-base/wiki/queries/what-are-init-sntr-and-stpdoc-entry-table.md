---
type: query
title: What Are INIT-SNTR and STPDOC_ENTRY_TABLE?
created: 2026-08-24
updated: 2026-08-24
tags: [database, init-sntr, stpdoc-entry-table, cn-payment, data-growth]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--1aw0oef, pre-post-performance-regression-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 MSRB Evidence.md"]
---
# What Are INIT-SNTR and STPDOC_ENTRY_TABLE?

## Question

What systems, schemas, functional processes, and retention rules own `INIT-SNTR` and `STPDOC_ENTRY_TABLE`, and what database growth is expected after CN Payment processing?

## Known evidence

The source register identifies `INIT-SNTR` and `STPDOC_ENTRY_TABLE` as the objects used in a POST-CN-Payment database-size comparison. It does not provide size values, schema definitions, ownership, retention behavior, or an assessment of whether the differences were acceptable.

## Evidence needed

- database platform, schema, and object definitions;
- object owners and consuming applications;
- CN Payment write, update, and purge behavior;
- PRE and POST size measurements with volume context;
- expected growth model and capacity thresholds;
- indexes, retention policies, and purge responsibilities;
- approval of the observed database-growth outcome.
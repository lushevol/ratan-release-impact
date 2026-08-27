---
type: query
title: How Are Cashflow Amendments Correlated and Discarded?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, amendment, correlation, open-question]
related: [cashflow-amendment-supersession, stella, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# How Are Cashflow Amendments Correlated and Discarded?

The functional demo requires an amendment to be displayed while the corresponding `New` cashflow is discarded. It does not define the correlation key or persistence semantics.

Clarification is needed on:

- the field or composite identifier defining the same cashflow;
- whether discarded records are deleted, archived, or marked superseded;
- processing of multiple amendments; and
- handling of amendments received before, after, or independently of the original `New`.
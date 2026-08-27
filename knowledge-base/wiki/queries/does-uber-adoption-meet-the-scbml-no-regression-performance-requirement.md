---
type: query
title: Does Uber Adoption Meet the SCBML No-Regression Performance Requirement?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, scbml, performance-regression, acceptance]
related: [uber, scbml, uber-scbml-performance-regression-testing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--19101up, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1isntku]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/PT result for UBER.md"]
---
# Does Uber Adoption Meet the SCBML No-Regression Performance Requirement?

## Status

Open.

## Evidence available

A Round 1 mixed-workload Settlement STP run without Message Bridge reports:

- Average: `00:00:03.401777`
- Maximum: `00:00:14.553234`
- Minimum: `00:00:01.474934`
- Total: `13737`

## Evidence needed

Obtain a matched SCBML-only baseline, define the timing boundary and acceptance threshold, and compare latency distributions, throughput, failure rate, and resource use against an Uber-enabled run. Confirm whether the production path includes Message Bridge.

The current source does not establish the required no-regression result.
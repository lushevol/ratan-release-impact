---
type: query
title: Does Netting Service Meet Peak Murex Volume and Retry Resilience Requirements?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, murex, capacity, retry-resilience, endurance-testing]
related: [netting-service, murex, netting-service-performance-testing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--22-netting-service-design--24-netti--1598489, what-are-the-netting-service-performance-slos-and-test-conditions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Netting performance test.md"]
---
# Does Netting Service Meet Peak Murex Volume and Retry Resilience Requirements?

The source shows successful tests at 1,996, 2,000, and 3,400 items and provides nine historical Murex reference rows ranging from 1,250 to 1,960 items. It does not establish whether those rows represent peak production demand or whether the 3,400-item case is a required capacity target.

## Questions

- What workload unit does the historical Murex `Netting amount` represent: a batch, operation, daily aggregate, or another measure?
- What historical period, selection criteria, and percentile define expected and peak Murex workload?
- Is 3,400 items the required peak-capacity target, a stress case, or an arbitrary test volume?
- What completion deadline must [[netting-service]] meet at normal and peak volumes?
- What concurrent Netting, Un-net, withdrawal, and dependent-system workloads must be supported?
- What retry count, failure modes, recovery conditions, and duration are required to demonstrate withdrawal retry resilience?
- Should the scenario-specific increase in Un-net duration be reproduced and investigated before acceptance?

## Current Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--22-netting-service-design--24-netti--1598489]] documents a single successful withdrawal retry operation lasting 64 seconds. This is insufficient to demonstrate endurance or recovery resilience without repeated and failure-oriented testing.
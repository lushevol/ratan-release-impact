---
type: query
title: What Is the Authoritative Bulk Exception Batch Size?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, bulk-processing, performance, capacity]
related: [backend-batch-partitioning, bulk-exception-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design.md"]
---
# What Is the Authoritative Bulk Exception Batch Size?

The source reports the best result for 1,000 logical cashflows when partitioned into 20 backend batches of 50, but it does not establish 50 as a supported or universally optimal batch size.

Confirm:

- The maximum logical request size.
- The default and maximum backend execution batch size.
- Whether 50 is a production setting, a test configuration, or a proposal.
- The number and capacity of live instances assumed by the test.
- Cost metric units, measurement method, repetition count, and acceptance criteria.
- Behavior when an execution batch fails or is only partially successful.

Related source: [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--11yr784]].
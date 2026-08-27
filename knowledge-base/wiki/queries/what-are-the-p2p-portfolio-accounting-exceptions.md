---
type: query
title: What Are the P2P Portfolio Accounting Exceptions?
created: 2026-08-23
updated: 2026-08-23
tags: [p2p, accounting, settlement-exceptions, murex-2-11]
related: [pre-trade-settlement-accounting-exceptions, murex-2-11-cn-derivative-settlement, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# What Are the P2P Portfolio Accounting Exceptions?

The source reports that some portfolios described as `P2P` generate neither trade nor settlement accounting. The exception is said to occur in pre-trade processing and not to appear in the payment queue.

The following remain unknown:

- The meaning and scope of `P2P`.
- The triggering condition and root cause.
- Whether payment creation always fails as a consequence.
- The responsible upstream system and remediation owner.
- The monitoring control required to detect these failures before settlement deadlines.
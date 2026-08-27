---
type: concept
title: Pre-Trade Settlement Accounting Exceptions
created: 2026-08-23
updated: 2026-08-23
tags: [settlement-exceptions, accounting, payment-queue, p2p, cn-settlement]
related: [murex-2-11, murex-2-11-cn-derivative-settlement, ssi-data-quality-for-swift-generation, what-are-the-p2p-portfolio-accounting-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Pre-Trade Settlement Accounting Exceptions

Pre-trade settlement accounting exceptions are failures that occur before payment-queue processing and may prevent a payment from being created.

The CN Settlement Ops session reported that certain portfolios referred to as `P2P` do not generate trade or settlement accounting. These exceptions are not reflected in the payment queue.

## Distinct Exception Classes

1. **Payment-stage SSI exceptions** — missing Vostro or Nostro SSI, which was identified as the main business exception for Murex 2.11 CN derivative settlement.
2. **Upstream accounting failures** — pre-trade failures that prevent trade or settlement accounting and therefore may prevent payment-queue visibility.

Controls for payment queues alone cannot detect the second class. The source does not define `P2P`, the root cause, or the remediation owner.
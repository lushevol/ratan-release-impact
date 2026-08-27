---
type: query
title: Which RATAN Distributed Lock Ownership Model Is Approved?
created: 2026-08-24
updated: 2026-08-24
tags: [RATANONE, distributed-locking, architecture, open-question]
related: [ratan-distributed-lock-ownership, cross-service-lock-validation, redisson, resource-lock-manager, resource-lock]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Which RATAN Distributed Lock Ownership Model Is Approved?

The source presents two proposal variants without clearly recording an approved choice:

1. Require client validation and enhance lock propagation to pass the process identity.
2. Do not perform client validation because processing without a valid lock is unsafe.

The document also states that the lock owner should control creation, extension, renewal, retry, and release, while existing flows distribute those responsibilities across Orchestration, Lifecycle, Netting, NSTP, SSI, and Swift.

## Evidence to resolve

The approval record should define:

- The authoritative lock identity.
- Whether ownership can transfer between services.
- Whether clients may renew or only validate.
- Behavior for expired or invalid propagated identities.
- All-or-nothing semantics for multi-key acquisition.
- Acquisition, renewal, validation, and release error contracts.
- The selected implementation for batches exceeding 5,000 payments.

Until these points are confirmed, the source supports a design direction but not an accepted architectural decision.

---
type: concept
title: Rule Sync Idempotency and Version Ordering
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, idempotency, ordering, retry, rule-sync]
related: [ratan-global-rule-synchronization, ratanone-rule-service, ratan-gdc, ratan-indonesia, what-is-the-canonical-ratan-rule-sync-message-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# Rule Sync Idempotency and Version Ordering

The proposed rule synchronization design uses a request ID, rule version, and parent-rule histories to manage retries and out-of-order delivery.

For a given rule, every synchronization event has a unique `request_id`. Retried events reuse that ID and overwrite the prior synchronization content. Producer responses with a mismatched request ID are to be ignored.

When a newer rule update supersedes earlier parent histories, the earlier synchronization events are marked `IGNORE` so they are not retried. Update and control events carry the latest parent histories, which are expected to be `DEAD`.

The design does not specify consumer-side idempotency storage, duplicate detection, ordering keys, transaction boundaries, or the terminal-state semantics of `IGNORE`. Consequently, its stated no-loss, no-repeat, and no-disorder guarantee is not yet substantiated by an implementable contract.
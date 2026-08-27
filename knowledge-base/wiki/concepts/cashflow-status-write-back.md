---
type: concept
title: Cashflow Status Write-Back
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-lifecycle, status-synchronization, backward-workflow]
related: [backward-workflow-design, razor, cash-settlement-platform, ratan-cashflow-lifecycle-service, stella, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Backward Workflow Design.md"]
---
# Cashflow Status Write-Back

Cashflow status write-back is the backward workflow in which a settlement outcome from [[razor]] is returned to Ratan, applied to the relevant cashflow records, and synchronized to downstream systems.

## Workflow

```text
Razor → Ratan → Adaptor → Murex2.11
                 └──────→ STELLA
```

The source explicitly assigns Ratan responsibility for updating cashflow status and synchronizing the result to STELLA or Murex2.11.

## Statuses

Razor is documented as sending `ACK/NACK`, `RELEASED`, and `SETTLED`. The payload examples support only `RELEASED` and `SETTLED`. The source does not define whether `ACK/NACK` is an acknowledgement, a business outcome, or a third category of cashflow status.

No authoritative transition sequence is provided. In particular, the source does not establish whether `ACK → RELEASED → SETTLED` is mandatory, whether `NACK` terminates processing, or whether statuses may arrive out of order.

## Ownership

Ratan is the documented state-management layer. The specific Ratan service that performs the update is not identified. The scope is also not established as RATAN GDC, RATAN Indonesia, or a shared platform workflow.

## Unresolved Contract Questions

The workflow requires decisions about idempotency, duplicate and stale messages, retries, downstream failure handling, correlation, and synchronous versus asynchronous synchronization. These issues are tracked in [[what-is-the-authoritative-ratan-backward-workflow-message-contract]].

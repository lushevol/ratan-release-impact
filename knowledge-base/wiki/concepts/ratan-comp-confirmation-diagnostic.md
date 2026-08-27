---
type: concept
title: RATAN COMP Confirmation Diagnostic
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, confirmation, pending-affirmation, cashflow, sql, troubleshooting]
related: [ratan-murex-kr-mt-to-mx-interface, ratan-murex-kr-exception-recovery, ratan-cashflow-lifecycle-service]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# RATAN COMP Confirmation Diagnostic

## Documented use

The source recommends checking RATAN trade state when a cashflow has failed or been suppressed as a `Pending Affirmation` exception and was not processed automatically. The check looks for a row with the supplied trade ID and `trade_state='COMP'`.

```sql
select trade_id,trade_state from ratan_cashflow_group_management_service.ratan_trade where trade_id ='*trade id*' and trade_state='COMP'.
```

The source states that a null result indicates that no `COMP` message was received by RATAN.

## Interpretation boundary

The query is a useful operational diagnostic, but the source does not define whether `COMP` means confirmation received, trade completion, or another business state. It also does not document retention, processing latency, duplicate rows, alternate states, or whether a missing row can result from persistence or replication behavior.

Therefore, a null result should be treated as a documented investigation signal rather than definitive proof of non-receipt until the `ratan_trade` lifecycle and storage semantics are confirmed.

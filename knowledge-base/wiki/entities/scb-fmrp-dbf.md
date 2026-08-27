---
type: entity
title: SCB_FMRP_DBF
created: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
tags: ["database-table", "fmrp", "murex-211", "cashflow-status", "cash-settlement", "database", "staging-table", "cashflow-integration"]
related: ["fmrp", "murex-211", "fmrp-murex-cashflow-status-synchronization", "ratan-murex-211-cashflow-integration", "fmrp-cashflow-status-synchronization", "ratan-cashflow-acknowledgement-and-release-processing", "ratan", "murex-ratan-bidirectional-cashflow-integration", "murex-ratan-cashflow-reconciliation"]
updated: 2026-08-23
---

# SCB_FMRP_DBF

`SCB_FMRP_DBF` is the Murex-side FMRP integration tracking table used by the Murex 2.11 FMRP settlement workflow to correlate Murex cashflows with FMRP and RATAN processing. The technical-design source describes it as a Murex staging and integration-audit table for eligible FMRP cashflows sent to [[ratan]]. It records Murex flow and status data, RATAN identifiers, net-resultant identifiers, and lifecycle timestamps.

The table is referenced by the January 2023 workflow configuration and is inserted into as `MUREXDB.SCB_FMRP_DBF`.

## Evidenced fields

### Fields described by the workflow sources

| Field | Role evidenced by the workflow sources |
|---|---|
| `M_FLOW_ID` | Murex payment-flow or cashflow identifier; used as a lookup key. |
| `M_STATUS` | FMRP integration or processing state, including `INIT`, `SENT`, `CANC`, and legacy `MATH`. |
| `M_RATAN_ID` | RATAN response or external-source identifier; newly inserted records use `0`. |
| `M_INS_DATETIME` | Insertion timestamp. |
| `M_REC_DATETIME` | RATAN response or inbound-acknowledgement receipt timestamp. |

### Fields and data types listed by the technical-design source

The technical-design source lists the following table layout:

```text
SCB_FMRP_DBF

M_FLOW_ID        numeric(10,0)  murex cashflow id
M_STATUS         char(4)        murex cashflow status INIT/SENT/MATH/CANC
M_RATAN_ID       char(12)       Ratan cashflow id
M_RATAN_NET_ID   char(12)       Ratan net resultant id when cashflow got net in Ratan, otherwise value 0
M_INS_DATETIME   datetime       cashflow record insertion timestamp
M_ACK_DATETIME   datetime       murex receive Ratan ACK message timestamp
M_RLS_DATETIME   datetime       murex receive Ratan RELEASE message timestamp
M_PUB_DATETIME   datetime       murex send out message timestamp
```

The technical-design field list therefore identifies `M_RATAN_NET_ID` as the RATAN net-resultant identifier, with value `0` when the cashflow was not netted in RATAN. It also distinguishes acknowledgement, release, and publication timestamps as `M_ACK_DATETIME`, `M_RLS_DATETIME`, and `M_PUB_DATETIME`.

The workflow sources instead document `M_REC_DATETIME` as the inbound acknowledgement or RATAN response receipt timestamp. The sources do not establish whether `M_REC_DATETIME` and `M_ACK_DATETIME` are the same deployed column, different columns from different design versions, or terminology for the same timestamp.

## Workflow operations

The workflow sources describe status-dependent lookups and updates against `SCB_FMRP_DBF` for outbound publication, cancellation, replay, acknowledgement, and release processing:

- Records are counted by flow ID and status.
- New records are inserted with status `SENT`, RATAN ID `0`, and a database insertion timestamp.
- `INIT` records are changed to `SENT` before publication.
- `SENT` records are changed to `CANC` for cancellation.
- The legacy acknowledgement implementation updates a matching record to `MATH`.
- The generated-version source describes released records as being changed to `MATH`.
- RATAN identifiers and receipt timestamps are stored after acknowledgement.

The technical-design source separately specifies the table statuses as `INIT`, `SENT`, `MATH`, and `CANC`, and describes the table as supporting the outbound and inbound lifecycle of eligible FMRP cashflows sent to RATAN.

## Status-code discrepancy

The technical-design source lists `MATH` as a valid status but elsewhere references `MACH`. The canonical code remains unresolved; see [[is-math-or-mach-the-canonical-scb-fmrp-dbf-status-code]].

The workflow sources also identify `MATH` as the legacy acknowledgement status and as the status used for released records in the generated-version account. These workflow statements do not resolve the technical-design source's `MATH`/`MACH` inconsistency.

## Maintenance and schema limitations

The technical-design source specifies that Control M runs a monthly purge. It does not define the purge's retention duration or any archival obligations.

Neither the workflow sources nor the technical-design source provides complete deployed DDL. The technical-design source specifically does not define primary keys, indexes, foreign keys, nullability, retention duration, or archival obligations.

The generated-version source states that operational uniqueness behavior should be verified against the deployed database schema. The existing-version source further notes that the documented count-then-insert pattern does not demonstrate protection against concurrent duplicate processing. Neither source provides locking strategy or transaction boundaries.
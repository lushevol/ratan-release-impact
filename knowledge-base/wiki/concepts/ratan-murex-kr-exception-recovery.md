---
type: concept
title: RATAN-Murex KR Exception Recovery
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, murex-kr, exception-management, message-replay, reconciliation, manual-fallback]
related: [ratan-murex-kr-mt-to-mx-interface, ratan-operational-resilience-plans, oscar, ssdr-51507, enisis]
sources: ["RATAN/RATAN -Interfaces/Ratan and Murex KR 50216.md"]
---
# RATAN-Murex KR Exception Recovery

## Purpose

The documented recovery approach separates failures by processing boundary: inbound delivery to RATAN, invalid Murex data, RATAN MX generation, downstream SFTP delivery to ENISIS, and missing confirmation messages.

## Recovery actions

| Failure scenario | Documented detection or signal | Recovery action |
| --- | --- | --- |
| Murex sends messages but RATAN does not receive them | Murex exception email to Korea FMO | Investigate with the PSS or development team; manually draft in ENISIS or OSCAR if automated recovery is unavailable |
| RATAN Swift exception caused by invalid Murex data | No ACK returned to Murex and Murex exception email | Investigate the source data; use manual drafting if the payment cannot be resumed |
| RATAN Swift-generation exception | RATAN MX exception blotter | Correct static data or restore the unavailable service, then replay the message; use manual drafting if replay fails |
| RATAN sends a message but ENISIS does not receive it | Comparison of the Murex payment report from SSDR with ENISIS MX extraction | Identify missing or failed payments and manually draft them in ENISIS or OSCAR |
| Missing confirmation for a `Pending Affirmation` cashflow | Query for `trade_state='COMP'` | Investigate whether the related confirmation was received |

## Replay

Replay from the RATAN MX exception blotter is documented for messages affected by incorrect static data or a temporarily unavailable service. Replay retriggers the MT-to-MX conversion after the underlying issue is corrected.

The source does not establish:

- Which exception classes are eligible for replay.
- Whether replay is idempotent.
- How duplicate MX messages are prevented.
- What audit record is created.
- Who authorizes replay.
- Whether downstream delivery is automatically reattempted.

## Manual fallback

When automated recovery is not possible, Korea FMO may manually draft the MX message in ENISIS or draft the payment in OSCAR. The source does not define approval, segregation-of-duties, reconciliation, or evidence-retention controls for this fallback.

## Reconciliation

For downstream delivery discrepancies, Murex provides a payment report through SSDR. Korea FMO downloads the report, extracts ENISIS messages by source system, and compares the two manually. The source does not identify which system is authoritative when the records differ.

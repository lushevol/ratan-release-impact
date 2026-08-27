---
type: project
title: Cashflow Migration
status: planned
owner: ""
start_date: 2023-09-02
target_date: 2023-09-11
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, migration, Murex, Ratan, Razor, cutover]
related: [cashflow-migration-readiness, murex-ratan-migration-reconciliation, static-data-readiness, expected-ratan-to-razor-accounting-break]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# Cashflow Migration

## Scope

The project concerns the migration of Cash Settlement Home Page cashflow processing from Murex 2.11 into Ratan, with downstream processing through Razor, EBBS, PSGL, TLM, FMSRE, AMH, and Aspire.

## Planned Cutover

The source describes the following planned sequence:

- 2–3 September: Murex, Ratan, and Razor technical go-live.
- 2–3 September: Murex begins publishing cashflows to Ratan, with value date on 11 September.
- 4–8 September: Controlled real-time reconciliation of Murex 2.11 against Ratan, followed by Razor accounting, EBBS/PSGL processing, and TLM EOD and reconciliation.
- 8 September: Ratan early-releases payments to Razor, FMSRE, and AMH.
- 9–10 September: Aspire release and go/no-go decision.
- 11 September: Formal business go-live and first Aspire EOD.

The source does not state the year for these September dates. The project is therefore represented as a planned sequence, not as a confirmed historical execution.

## Key Readiness Dependencies

Key dependencies include Vostro and SSI+ migration, SSI stamping UAT, Razor Swift-generation testing, Murex reversal/new-cashflow matching, Murex event exception handling, Stella event handling, and downstream reconciliation.

## Risks and Gaps

The source provides no rollback plan, rollback triggers, go/no-go outcome, UAT results, or execution evidence. The project status should be updated only when corroborating material confirms completion or cancellation.
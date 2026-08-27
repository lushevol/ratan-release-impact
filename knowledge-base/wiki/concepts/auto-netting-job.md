---
type: concept
title: Auto-Netting Job
created: 2026-08-23
updated: 2026-08-23
tags: [auto-netting, cash-settlement, cashflows, migration-testing]
related: [korea-migration-performance-testing, murex-korea, lien-aware-netting-and-auto-unnetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Performance Testing Plan.md"]
---
# Auto-Netting Job

## Definition

An auto-netting job is a settlement-processing step that automatically nets eligible cashflows after migrated data has been reconciled, analyzed, and processed.

In the Korea migration test plan, the job is run once for each of three EOD dump cycles. Cashflows remaining in the `waiting` state are then reprocessed before SWIFT messages are compared.

## Documented Use

The source specifies the following sequence for each cycle:

1. Process the selected EOD dump.
2. Run the auto-netting job.
3. Reprocess `waiting` cashflows.
4. Compare SWIFT messages for the applicable payment cohort.

## Unknown Rules

The source does not define:

- Which cashflows are eligible for netting.
- Whether netting is performed by currency, account, value date, or another grouping.
- Exclusions or failure handling.
- Whether the job is idempotent.
- How netting affects payment counts or SWIFT messages.
- The relationship between the generic job and lien-aware netting.

Therefore, this page should not be used as evidence for the rules in [[concepts/lien-aware-netting-and-auto-unnetting]].

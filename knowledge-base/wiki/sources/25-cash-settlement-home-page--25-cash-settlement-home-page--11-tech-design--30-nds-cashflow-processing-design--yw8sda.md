---
type: source
title: NDS Cashflow Processing Design
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [cash-settlement, cashflow, nds, netting, nstp, scbml]
related: [nds-cashflow-processing, nd-parent-trade-metadata, nstp-and-ndirs-rule-routing, ratan-mxg-cashflow-adaptor, what-is-the-authoritative-nds-cashflow-processing-state-machine, what-are-the-nid-and-nd-parent-typology-validation-rules, what-are-the-scheduled-netting-scan-idempotency-and-locking-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# NDS Cashflow Processing Design

This technical design records proposed changes across netting, cashflow lifecycle, rule evaluation, MXML-to-SCBML mapping, and cash-settlement orchestration for NDS cashflow processing. The document does not define the expansion of “NDS”, detailed processing algorithms, state transitions, or operational controls.

## Change Register

| SN | Module | Changes | Description |
| --- | --- | --- | --- |
| 1 | ratan-cash-settlement-netting-service | 1. Cron job to scan cashflow candidates and netting | Code change |
| 2 | ratan-cashflow-lifecycle-service | 1. Precheck refactoring, decouple data persistence and attribute stamping. | Code change Lifecycle stamping logic refer to design page: [Cashflow Lifecycle Stamping Logic - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/Cashflow+Lifecycle+Stamping+Logic) |
| 3 | ratan-rule-service | 1. Add a new rule to NSTP cashflows has non-NDIRS parent typology and NID exists 2. update existing rule on demand to bypass cashflows has NDIRS parent typology | DB change only |
| 4 | ratan-mxg-cashflow-adaptor | 1. Be able to map NID from MXML to SCBML for downstream processing. | Minor code change |
| 5 | ratan-cash-settlement-orchestration | 1. Add new node after Pre-check | Flow change |

## Data Modeling Change

| Logical model | Xpath | Description | Change Flag |
| --- | --- | --- | --- |
| Cashflow.ND_Parent_Trade_Id | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:NDParentTradeId | NID | Internal Adding |
| Cashflow.ND_Parent_Typology | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:NDParentTradeTypology | ND parent trade typology | Internal Adding |

## Recorded Processing Dependencies

The documented identifier propagation path is:

```text
MXML
  -> ratan-mxg-cashflow-adaptor
  -> SCBML
  -> downstream cashflow processing and rule evaluation
```

The design distinguishes cashflows with a non-NDIRS parent typology and an existing NID from cashflows whose parent typology is NDIRS. The latter must bypass an existing on-demand rule; the source does not define precedence among rules, NID validation, or the processing result of a matching rule.

The lifecycle-service change separates precheck refactoring from data persistence and attribute stamping. The linked Confluence lifecycle-stamping design, rather than this source, is the indicated reference for stamping logic.

## Boundaries and Unknowns

The source does not specify:

- The cron schedule, candidate-selection criteria, locking, retries, or idempotency for scheduled netting.
- The responsibility or failure behavior of the new orchestration node after Pre-check.
- Transaction boundaries or recovery behavior between persistence and attribute stamping.
- MXML field locations, NID validation, missing-NID treatment, or historical backfill.
- Whether the two internally added logical fields are exposed through APIs, events, or dynamic-query mappings.

See [[nds-cashflow-processing]], [[nd-parent-trade-metadata]], and [[nstp-and-ndirs-rule-routing]] for the documented scope and [[what-is-the-authoritative-nds-cashflow-processing-state-machine]] for unresolved flow semantics.
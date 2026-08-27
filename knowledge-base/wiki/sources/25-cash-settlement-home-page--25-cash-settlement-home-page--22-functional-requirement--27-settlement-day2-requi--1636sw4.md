---
type: source
title: Cashflow Splitting UAT for EBBS
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-splitting, EBBS, UAT, Settlement-Day-2, accounting]
related: [ebbs, ratan, cash-settlement-home-page, cashflow-splitting, cashflow-splitting-accounting-generation, ratan-accounting-service, uat-test-case, cashflow-auto-netting, cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For EBBS.md"]
---
# Cashflow Splitting UAT for EBBS

## Summary

This source records User Acceptance Testing for [[concepts/cashflow-splitting]] within the EBBS Settlement Day 2 scope. Six populated scenarios were marked **Pass** on 2025-11-11. The tests cover manual splitting of gross cashflows, automatic splitting of gross cashflows, and automatic distribution over a net resultant cashflow.

The evidence supports a scoped implementation rule: in the tested EBBS flow, partial release, `swift_suppress`, and child failure resulted in accounting information generation, while `cashflow_suppress` did not.

## Test results

| # | Test case | Test steps or input | Expected result | Tested data | Tested by | Result |
|---:|---|---|---|---|---|---|
| 1 | Split over gross cashflow; child cashflow partially released | Manual split; release one child | Generate accounting information | Parent `M00123889310`; child `S00000050000` | Li1, Johnny | Pass |
| 2 | `swift_suppress` one child | Generate accounting information | Generate accounting information | Parent `M00123889310`; child `S00000049998` | Li1, Johnny | Pass |
| 3 | `cashflow_suppress` one child | Do not generate accounting information | Do not generate accounting information | Parent `M00123889310`; child `S00000049999` | Li1, Johnny | Pass |
| 4 | Fail one child | Generate accounting information | Generate accounting information | Parent `M00123889310`; child `S00000050001` | Li1, Johnny | Pass |
| 5 | Split over gross cashflow; all child cashflows released | One parent cashflow; automatic split | All children released and accounting information generated | Parent `M01760959502`; children `S00000050019`, `S00000050020` | Li1, Johnny | Pass |
| 6 | Automatic distribution over a net resultant cashflow; all child cashflows released | Net plus automatic split case | All children released | `M01760959503`, `M01760959504`, `N00000050021`; children `S00000050022`, `S00000050023` | Li1, Johnny | Pass |

Rows 7–11 contain no executed test data or result. Rows 8 and 9 contain only the country labels `SG` and `UK`.

## Accounting validation

The source references `ratan_accounting_request_task_202511111213.csv` and provides the following SQL query against the RATAN accounting service:

```sql
select cashflow_id, business_version, minor_version, payment_date,trade_id ,country ,booking_entity_fmid,booking_entity_fmcode ,counterparty_fmid ,counterparty_fmcode,external_system_key,currency, request_info 
from ratan_cash_accounting_service.ratan_accounting_request_task
where cashflow_id in ('S00000050000','S00000049998','S00000049999','S00000050001','S00000050019','S00000050020','S00000050022','S00000050023')
```

The query examines `cashflow_id`, version fields, payment and trade identifiers, country, booking and counterparty identifiers, `external_system_key`, currency, and `request_info`.

The source does not include the CSV contents, query output, row counts, accounting payloads, amounts, currencies, or reconciliation totals. Therefore, the pass results document UAT outcomes but do not independently establish the exact accounting-request cardinality or payload correctness.

## Supported behavior

- A partially released child in a manually split gross cashflow generated accounting information.
- `swift_suppress` on one child did not prevent accounting information generation.
- `cashflow_suppress` on one child prevented accounting information generation.
- A failed child still generated accounting information in the tested scenario.
- Automatic splitting of a gross cashflow succeeded when all children were released.
- Automatic distribution over a net resultant cashflow succeeded when all children were released.

These findings are implementation-specific UAT evidence for EBBS. They should not be generalized to all suppression mechanisms, failure states, or netted cashflows without additional evidence.

## Evidence and limitations

Referenced evidence includes screenshots dated 2025-11-11 and the attachment `ratan_accounting_request_task_202511111213.csv`. The source contains a malformed or shifted scenario 2 row, inconsistent terminology such as “auto spit,” and ambiguous parent/child labeling in scenario 6. It does not define amount allocation, parent-child reconciliation, retries, duplicates, rollback, or partial-failure behavior.

---
---FILE: wiki/concepts/cashflow-splitting.md---
---
type: concept
title: Cashflow Splitting
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, splitting, EBBS, Settlement-Day-2, UAT]
related: [ebbs, ratan, cash-settlement-home-page, cashflow-splitting-accounting-generation, cashflow-aggregation, cashflow-auto-netting, uat-test-case]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For EBBS.md"]
---
# Cashflow Splitting

Cashflow splitting divides an original parent cashflow into one or more child cashflows. The child cashflows can then receive distinct lifecycle actions and outcomes while remaining associated with the original parent.

## Modes tested

The EBBS UAT evidence covers two modes:

- **Manual split:** A user splits a gross cashflow and applies different actions to individual children.
- **Automatic split or distribution:** The system distributes a gross cashflow or a net resultant cashflow into child cashflows.

The tested gross-cashflow scenarios used parent `M00123889310` for differentiated child outcomes and parent `M01760959502` for an all-children-released flow. The net-resultant scenario used `M01760959503`, `M01760959504`, and `N00000050021`, with children `S00000050022` and `S00000050023`.

## Child-level behavior

The UAT results show that child actions are not equivalent:

- Partial release generated accounting information.
- `swift_suppress` generated accounting information.
- `cashflow_suppress` did not generate accounting information.
- Child failure generated accounting information in the tested case.

This distinction belongs to [[concepts/cashflow-splitting-accounting-generation]]. It should not be merged with the broader [[concepts/murex-2-11-cashflow-suppression]] behavior or with every failure state described by [[concepts/ratan-fail-and-autofail-status-transitions]].

## Relationship to netting and aggregation

Automatic distribution over a net resultant cashflow is related to [[concepts/cashflow-auto-netting]], [[concepts/net-function]], and [[concepts/cashflow-aggregation]], but splitting is a separate operation. The UAT does not specify the netting calculation, allocation formula, or amount reconciliation between parent and child cashflows.

## Scope

The evidence is limited to six passing EBBS UAT scenarios dated 2025-11-11. It does not establish behavior for retries, duplicate events, rollback, partial processing, unsupported states, or the incomplete `SG` and `UK` rows.
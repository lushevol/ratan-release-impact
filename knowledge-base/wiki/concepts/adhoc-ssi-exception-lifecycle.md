---
type: concept
title: Adhoc SSI Exception Lifecycle
tags: [ssi, exception-management, adhoc-ssi, cashflow-state]
related: [ssi-stamping-service, adhoc-ssi-maker-checker-workflow, what-are-the-two-new-ssi-exception-categories, what-is-the-authoritative-adhoc-ssi-api-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# Adhoc SSI Exception Lifecycle

The source defines `ADHOC_SSI_EXCEPTION` as the named exception produced by Adhoc SSI actions, including cases where no SSI exception existed before the action.

## Evidenced transitions

| Trigger | Resulting exception status | Response code in illustrated example |
| --- | --- | --- |
| Successful Maker Adhoc SSI submission | `PENDING_VERIFICATION` | `SUCCESS` |
| Checker rejection of Adhoc SSI | `PENDING_OPERATOR` | `FILTERED` |

“Filtered” therefore cannot safely be interpreted as a technical failure without further contract definition: the rejection example uses it while reporting the expected business-state transition.

## Missing transitions

The source lists Checker approval but does not provide its request/response example, final exception status, or final cashflow status. It also says two new exception categories are added, although only `ADHOC_SSI_EXCEPTION` is named. [[what-are-the-two-new-ssi-exception-categories]] tracks this discrepancy.
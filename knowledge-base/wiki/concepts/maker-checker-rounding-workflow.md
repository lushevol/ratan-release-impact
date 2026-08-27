---
type: concept
title: Maker-Checker Rounding Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [maker-checker, segregation-of-duties, manual-rounding, workflow, cash-settlement]
related: [manual-rounding-amendment, camunda-task-bulk-amend-rounding-api, camunda]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# Maker-Checker Rounding Workflow

The maker-checker rounding workflow separates manual rounding submission from its review. A maker submits an `AmendRounding` request, and a checker later submits either `Approve` or `Reject` through the same endpoint.

## Documented lifecycle

```text
Maker: AmendRounding
        |
        +--> Checker: Approve
        |
        +--> Checker: Reject
```

The maker request contains the proposed amount and currency. The checker requests contain the cashflow identifier and version fields but do not repeat the proposed amount or currency.

The source labels the operations as maker and checker actions, but it does not specify:

- Whether the maker and checker must be different users.
- Which permissions are required for each action.
- Whether authorization is enforced by Camunda or another service.
- What state is created by the maker action.
- Whether rejection restores the previous amount or only closes the task.
- What downstream processing follows approval.

Accordingly, the workflow separation is documented, while segregation-of-duties enforcement and post-action semantics remain unverified.

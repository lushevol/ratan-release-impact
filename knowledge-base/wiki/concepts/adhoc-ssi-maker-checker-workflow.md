---
type: concept
title: Adhoc SSI Maker-Checker Workflow
tags: [ssi, maker-checker, cashflow, exception-management, camunda]
related: [ssi-stamping-service, adhoc-ssi-exception-lifecycle, ssi-stamping-message-contract, cashflow-blotter, cash-settlement-data-entitlement, bpmn-workflow-service-orchestration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# Adhoc SSI Maker-Checker Workflow

Adhoc SSI is a controlled manual settlement-instruction process initiated from a cashflow context. The source says a user selects “Adhoc SI” from a right-click menu on a `READY` cashflow in [[cashflow-blotter]].

## Documented path

1. A Maker submits Vostro and Nostro instruction data for a versioned cashflow.
2. The SSI Stamping Service returns `ADHOC_SSI_EXCEPTION` in `PENDING_VERIFICATION` after the illustrated successful submission.
3. A Checker may approve or reject the submitted instruction. The approval endpoint is listed but no approval sample or resulting status is supplied.
4. The illustrated Checker rejection produces `ADHOC_SSI_EXCEPTION` in `PENDING_OPERATOR`.

The source says that Adhoc SSI invokes the SSI API from Camunda for CN, implying orchestration through [[bpmn-workflow-service-orchestration]].

## Control gaps

Maker and Checker responsibilities imply segregation of duties, but the source does not state where role validation, entitlement, audit, or Maker-versus-Checker separation is enforced. This is an open integration point with [[cash-settlement-data-entitlement]].
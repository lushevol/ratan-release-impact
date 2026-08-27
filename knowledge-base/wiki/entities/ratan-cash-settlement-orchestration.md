---
type: entity
title: ratan-cash-settlement-orchestration
created: 2026-08-24
updated: 2026-08-25
tags: [cash-settlement, orchestration, irs, workflow, microservice, Camunda, ratan, retry, kafka, monitoring]
related: [irs-cashflow-processing, lifecycle-service, netting-service, rule-service, cash-settlement-platform, camunda, ratan-cashflow-lifecycle-service, ratan-cash-settlement-netting-service, process-in-publication-contract, automatic-un-netting-error-handling, ratanone, ratan-transient-failure-recovery, ratan-itrs-alert-triage, ebbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md", "RATAN/RATAN -Monitoring/RATAN ITRS Log.md"]
---
# ratan-cash-settlement-orchestration

`ratan-cash-settlement-orchestration` is an orchestration component named in the IRS cashflow-processing design. The Uber development-testing source separately describes it as an orchestration service referenced in an automatic un-netting failure record.

The RATAN ITRS log describes it as processing Camunda settlement workflows.

## IRS Subprocess Placement

The IRS cashflow-processing design marks as Done an IRS subprocess inserted after `1_2 CloseException&&SuppressionCheck` and before `1_3 NettingEligibleCheck`.

This establishes intended ordering only. That source does not specify invocation criteria, BPMN details, whether the subprocess bypasses or supplements generic netting eligibility, or runtime test evidence.

See [[irs-cashflow-processing]] and [[cash-settlement-service-landscape]].

## Automatic Un-netting Failure Record

According to the Uber development-testing source, `ratan-cash-settlement-orchestration` invoked `ratan-cash-settlement-netting-service` through the Camunda-oriented `autoUnNet` endpoint.

### Observed failure context

```text
ratan-cash-settlement-orchestration || STELLA.1755538990974.6b9cc4d8-5a42-4e02-8ef8-721306996a8c-1-1_1001 || Stella || RAZOR || null
```

The orchestration call reported no replay topic and received a “No static resource” response from `ratan-cash-settlement-netting-service`.

The same source records an “orchestration 1_1” Camunda modification as passed, but does not describe the change or its acceptance criteria.

See [[automatic-un-netting-error-handling]], [[ratan-cash-settlement-netting-service]], and [[camunda]].

## Transaction Failure Recovery

According to the RATAN ITRS log, when transaction setup fails with `CannotCreateTransactionException: Could not open JPA EntityManager for transaction`, the workflow does not commit its input-topic offset and retries until processing succeeds.

That source reports that cashflow `006988767280` was eventually processed successfully and had no confirmed business impact. The root cause and broader systemic impact remained unresolved. This is evidence of recovery for one cashflow, not proof that the underlying failure was fixed.

See [[ratan-transient-failure-recovery]].

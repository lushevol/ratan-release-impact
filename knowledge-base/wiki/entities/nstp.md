---
type: entity
title: NSTP
created: 2026-08-22
updated: 2026-08-23
tags: [nstp, settlement, exception-processing, business-rules, hard-blocker, cash-settlement, exception-queue, net-to-gross, workflow, retry, exception, maker-checker]
related: [sal-swap-agent-hard-blocker, nstp-hard-blocker-bulk-eligibility, business-rule-maintenance, ratan-rule-lifecycle-management, settlement-suppression-exceptions, ratan, net-to-gross-workflow, camunda, netting-service, cashflow-locking-and-retry-policy, nstp-maker-checker-processing, camunda-based-maker-checker-workflows, cash-settlement-exception-handling, canonical-nstp-maker-checker-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Self testing evdience.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Lock Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
---

# NSTP

NSTP is used as a settlement exception and rule-processing mechanism in Settlement Day 2 SAL hard-blocker scenarios. In the Netting requirement, NSTP is the exception queue to which Ratan Net-to-Gross requests from Netting Clients must be routed.

NSTP is also named as a participant in automatic retry for new cashflow workflow events. In the documented retry scenario, processing is keyed by `Cashflow Id` and retries until success.

A separate maker-checker redesign source describes NSTP as a Cash Settlement exception or process classification. Its proposed implementation concerns NSTP-related manual operations and does not establish that the proposal's workflow design is the current behavior.

> **Scope note:** The Cash Settlement Lock Process source does not define NSTP's responsibilities, message contract, retry implementation, or idempotency controls. The Netting requirement concerns Net-to-Gross requests and does not establish the destination of cashflows affected by automatic un-netting.

## Rules and hard blockers

The Settlement Day 2 hard-blocker evidence shows that NSTP rules are displayed in the Settlement NSTP Rules Blotter and can be configured with the following operational levels:

- `Maker Only`
- `Checker Only`
- `Maker Checker`

A hard-blocker rule produces the `Hard block Swap Agent` exception for qualifying `SWAP_AGENT` cashflows.

NSTP hard-blocker behavior is primarily a release and approval control. Same-payment-type netting may still create a resultant, while maker submission, checker approval, or bulk submission can be rejected. A non-hard-blocker NSTP rule remained creatable in the tested configuration.

## Proposed maker-checker workflow redesign

According to the proposed maker-checker redesign, NSTP-related manual operations should be orchestrated by [[camunda]] rather than embedded in business-service code.

For an NSTP cashflow, [[ratan-cash-settlement-orchestration]] is planned to modify `1_5_Nstp_Check.bpmn` to invoke an NSTP sub-workflow.

The proposal states that Camunda-originated calls are to update SCBML history to:

- `Pending_Operator`
- `NSTP_Release`

The redesign source does not define whether these values are complete NSTP lifecycle states, their valid predecessors, or their terminal semantics. See [[canonical-nstp-maker-checker-state-machine]].
---
type: query
title: What Is the Authoritative FMRP MQ Queue Ownership?
created: 2026-08-24
updated: 2026-08-24
tags: [query, mq, fmrp, mls, integration-ownership]
related: [fmrp-outbound-mq, fmrp-inbound-mq, fmrp-murex-211-settlement-workflow, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# What Is the Authoritative FMRP MQ Queue Ownership?

## Question

Are `GM.MXG.MLS.FEDS.UAT` and `GMPCI.MLS.MXG.RQSTIN` FMRP-owned queues, MLS-owned queues, or shared or legacy-named transport endpoints?

## Evidence

Both queue names contain `MLS`, while the workflow tasks and message descriptions identify the route as FMRP and RATAN integration. The source does not define application ownership.

## Verification needed

Confirm queue ownership, message consumers and producers, environment scope, and whether the queue names are retained for compatibility with an earlier MLS integration.
---
type: concept
title: Ratan SUSPENDED Cashflow Rule Filtering
tags: [cash-settlement, suspended-status, rule-evaluation, camunda, stp]
related: [ratan-rule-service, camunda, ratan-cashflow-lifecycle-service, fail-open-rule-service-evaluation, rule-semantic-compilation-risk, how-is-ratan-suspended-rule-conjunction-evaluated]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# Ratan SUSPENDED Cashflow Rule Filtering

Ratan SUSPENDED cashflow rule filtering determines whether an inbound SCBML or Uber cashflow carrying source status `SUSPENDED` should become `RATAN_SUSPENDED`.

A matching rule result requires the workflow to:

1. Persist the group message in `ratan_cashflow_group_message`.
2. Mark it as suspended, with the exact mapping between source `SUSPENDED`, group-message status, and lifecycle `RATAN_SUSPENDED` still requiring confirmation.
3. Stop subsequent workflow processing.
4. Suppress `GroupReadyEvent`.
5. Suppress STP publication.

A non-match continues the established processing path. The implemented interception point is after group-message processing in Camunda, not before inbound persistence in group-service handlers.

The active configured rule is the FX-replication rule `7444684846945615873333`; it targets `FMRPSTELLA` FX cashflows and excludes fee payment types.
---
type: concept
title: Rebook Cashflow Netting Exclusion
tags: [cashflow-auto-netting, rebook, netting-eligibility, inter-entity-netting, rule-management]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-eligibility-rules, released-resultant-amendment-handling, should-rebook-cashflows-be-excluded-from-all-auto-netting-rules]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Enhancement on Auto Netting.md"]
---
# Rebook Cashflow Netting Exclusion

Rebook cashflow netting exclusion is a proposed [[cashflow-auto-netting]] eligibility control that prevents cashflows associated with a rebooking event from matching auto-netting rules.

## Requirement

The source requires rebook cashflows to be excluded from auto-netting rule matching. It does not define the authoritative attribute or lineage evidence used to identify a rebook cashflow.

## Scope remains unresolved

The intended scope is explicitly TBC:

- exclusion only for inter-entity netting; or
- exclusion for other auto-netting rules as well.

This requirement must not be generalized to manual netting, pending netting, or every netting product without a confirmed decision.

## Design considerations

A rule implementation needs to define:

- whether rebook identification is held on the cashflow, parent trade, or event lineage;
- whether both sides of an inter-entity pair must be excluded;
- treatment of cashflows that were already netted before rebook status is identified; and
- audit evidence for an exclusion decision.

The eligibility control is separate from the lifecycle response to an amendment after resultant release; see [[released-resultant-amendment-handling]].
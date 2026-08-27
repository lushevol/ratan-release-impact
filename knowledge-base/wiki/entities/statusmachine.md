---
type: entity
title: statusmachine
tags: [cash-settlement, status-management, camunda, integration]
related: [camunda, nstp-maker-checker-processing, canonical-nstp-maker-checker-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# statusmachine

`statusmachine` is a component named in the proposed NSTP maker-checker implementation plan.

It is expected to expose an API for invocation by [[camunda]], with an estimate of 1. The source does not define the component’s canonical service name, ownership, API contract, statuses it controls, failure semantics, or whether the planned change was delivered.
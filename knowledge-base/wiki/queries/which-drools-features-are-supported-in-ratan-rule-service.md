---
type: query
title: Which Drools Features Are Supported in RATAN Rule Service?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, drools, feature-support, rule-authoring]
related: [ratan-rule-engine, drools, constrained-rule-authoring-grammar]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# Which Drools Features Are Supported in RATAN Rule Service?

## Question

Which Drools attributes, operators, dialects, agenda controls, timers, calendars, and rule groups are implemented, exposed in the UI, tested, and supported in production?

## Evidence

The source inventories broad Drools capabilities, including `salience`, `agenda-group`, `activation-group`, `timer`, `calendar`, and `MVEL`. It simultaneously proposes a narrower user-facing grammar that restricts top-level boolean expressions.

## Required resolution

A current feature matrix should distinguish generic Drools semantics from RATAN implementation, UI exposure, validation behavior, and production support.
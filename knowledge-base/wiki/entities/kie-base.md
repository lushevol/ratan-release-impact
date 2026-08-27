---
type: entity
title: KieBase
created: 2026-08-24
updated: 2026-08-24
tags: [drools, kie, compilation, rule-engine]
related: [drools, kie-session, kie-helper, dynamic-drl-compilation, rule-engine-session-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# KieBase

`KieBase` is the Drools repository of compiled knowledge definitions, including rules, processes, functions, and type models. It does not contain runtime facts; applications create [[kie-session|KieSession]] instances from it for runtime execution.

In the archived RATAN example, `KieHelper.build(config)` creates a `KieBase` after generated DRL has been added and verified. The source does not define compiled-base caching, atomic replacement, memory limits, or concurrent-read behavior.
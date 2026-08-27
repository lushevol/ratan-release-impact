---
type: entity
title: KieSession
created: 2026-08-24
updated: 2026-08-24
tags: [drools, kie, runtime, rule-engine]
related: [drools, kie-base, kie-helper, rule-engine-session-lifecycle, dynamic-drl-compilation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# KieSession

`KieSession` is the stateful Drools runtime context used to insert facts, set globals, execute processes, and fire matching rules. A session is created from a [[kie-base]] and contains runtime data rather than compiled rule definitions.

The source uses `setGlobal`, `insert`, and `fireAllRules`, then calls `dispose()` in a `finally` block. Explicit disposal is a lifecycle requirement to free resources and used memory.

The source does not determine whether sessions should be pooled, reused, cached, or created independently under concurrent load.
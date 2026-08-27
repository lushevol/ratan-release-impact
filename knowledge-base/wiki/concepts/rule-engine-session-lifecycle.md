---
type: concept
title: Rule-Engine Session Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [drools, kie, lifecycle, resource-management]
related: [drools, kie-base, kie-session, dynamic-drl-compilation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# Rule-Engine Session Lifecycle

The Drools KIE lifecycle separates compiled rule definitions from runtime execution state.

A [[kie-base|KieBase]] contains compiled rules, processes, functions, and type models without runtime facts. A [[kie-session|KieSession]] is created from that base and holds facts, globals, and runtime interaction with the rule engine.

Applications must call `KieSession.dispose()` when work is complete to release used memory and resources. The archived RATAN examples dispose sessions after `fireAllRules()`, including a `finally` block in the dynamic-compilation path.

The source does not establish lifecycle policies for session reuse, pooling, cache ownership, base sharing, or concurrent execution.
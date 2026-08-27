---
type: concept
title: Dynamic DRL Compilation
created: 2026-08-24
updated: 2026-08-24
tags: [drools, drl, runtime-compilation, rule-engine]
related: [drools, kie-helper, kie-base, kie-session, drools-rule-refresh, what-is-the-performance-and-concurrency-model-for-dynamic-drl-compilation, what-is-the-authoritative-suppression-rule-language-and-governance-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# Dynamic DRL Compilation

Dynamic DRL compilation is the process of producing DRL from runtime rule data, validating it, compiling it into a `KieBase`, opening a `KieSession`, inserting facts, and firing matching rules without restarting the host application.

The archived RATAN example follows this sequence:

1. Load configured suppression rules.
2. Merge them into a FreeMarker DRL template.
3. Add the generated DRL to `KieHelper`.
4. Verify the DRL and reject `WARNING` or `ERROR` messages.
5. Build a [[kie-base|KieBase]].
6. Create a [[kie-session|KieSession]].
7. Insert a `Map<String, Object>` fact, set a result-list global, and fire all rules.
8. Dispose the session.

This proves an implementation path, not production suitability. Rendering, verification, and compilation appear to occur per invocation in the example. Caching, asynchronous compilation, version activation, rollback, and safe concurrent replacement are unspecified.

Dynamic compilation should not be treated as equivalent to [[drools-rule-refresh|production-grade rule refresh]].
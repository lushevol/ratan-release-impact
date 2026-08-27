---
type: query
title: What Is the Performance and Concurrency Model for Dynamic DRL Compilation?
created: 2026-08-24
updated: 2026-08-24
tags: [drools, performance, concurrency, runtime-compilation]
related: [dynamic-drl-compilation, drools-rule-refresh, kie-helper, kie-base, kie-session]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# What Is the Performance and Concurrency Model for Dynamic DRL Compilation?

The archived `checkRules` example appears to load rules, render DRL, verify it, and build a `KieBase` during each invocation. The source explicitly warns that verification and compilation may be time-consuming but provides no measurements.

## Questions to resolve

- Are DRL generation, verification, and compilation request-time, event-time, or asynchronous refresh operations?
- Is a compiled `KieBase` cached and reused, and what invalidates it?
- How is a new rule version atomically activated while in-flight sessions finish?
- What are the latency, throughput, memory, compilation-frequency, and concurrency limits?
- What failure behavior applies when refresh or validation fails?
- Are sessions independently created per execution, pooled, or otherwise managed?
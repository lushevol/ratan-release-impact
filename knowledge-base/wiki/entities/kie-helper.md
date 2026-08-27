---
type: entity
title: KieHelper
created: 2026-08-24
updated: 2026-08-24
tags: [drools, kie, drl, runtime-compilation]
related: [drools, dynamic-drl-compilation, kie-base, kie-session, what-is-the-performance-and-concurrency-model-for-dynamic-drl-compilation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# KieHelper

`KieHelper` is a Drools helper API used by the archived RATAN example to add generated DRL content, validate it with `verify()`, and build a [[kie-base|KieBase]].

The example treats both `WARNING` and `ERROR` verification messages as fatal by throwing an exception. This is a stricter policy than rejecting syntax errors alone, but the source does not explain whether that policy is intentional or appropriate for deployment.

Its use in the example is central to [[dynamic-drl-compilation]]. The performance and concurrency suitability of building through `KieHelper` during request or event processing remains open.
---
type: entity
title: LiteFlow
created: 2026-08-24
updated: 2026-08-24
tags: [java, rule-engine, workflow-orchestration, spring-boot]
related: [business-rule-engines, rule-engine-vs-workflow-orchestration, drools-vs-easy-rules-vs-liteflow, what-is-the-boundary-between-drools-camunda-and-domain-services]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine.md"]
---
# LiteFlow

LiteFlow is a Java component-based rule-engine and flow-orchestration framework evaluated as an alternative to [[drools]]. The source describes Java `NodeComponent` implementations orchestrated through configurable chains supporting serial, parallel, conditional, nested, and switch-like execution.

## Capabilities described

The source states that LiteFlow integrates with Java and Spring Boot, supports several scripting languages, includes monitoring for time-consuming steps, supports external rule storage, and provides rule hot deployment or refresh. External stores named in the source include databases, Nacos, ZooKeeper, and etcd.

## Architectural characterization

The source considers LiteFlow more appropriate for complex business-flow orchestration than for separating business decisions from code, because component logic is commonly implemented in Java. This is an architectural interpretation, not a demonstrated Cash Settlement evaluation.

LiteFlow may overlap with existing [[camunda-based-maker-checker-workflows]]. The boundary between component flows, workflow orchestration, declarative decisions, and domain services remains unresolved.
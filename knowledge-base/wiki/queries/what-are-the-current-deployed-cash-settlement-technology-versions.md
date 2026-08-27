---
type: query
title: What Are the Current Deployed Cash Settlement Technology Versions?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, technology-stack, versions, camunda, postgresql, kafka, redis, open-question]
related: [cash-settlement-platform, camunda-7, kafka, postgresql, redis, what-is-the-approved-camunda-7-to-8-migration-strategy-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design.md"]
---
# What Are the Current Deployed Cash Settlement Technology Versions?

## Question

Which versions of the declared Cash Settlement Platform technologies are currently deployed and supported in each environment?

## Evidence

The source declares a baseline including Camunda engine 7.10.0, Kafka 2.5.0, PostgreSQL 12.x, Redis 6.2.6, Spring Boot 2.6.6, and ELK 8.1.0. It does not provide a date, environment, deployment evidence, or support status.

The Redis row is ambiguous: it states version `6.2.6` and also says “will update to 6.2.6.”

## Required resolution

Obtain environment-specific deployment manifests, runtime version evidence, and approved target versions for Camunda, Kafka, PostgreSQL, Redis, Spring Boot, Consul, and ELK. Reconcile Camunda runtime evidence with [[what-is-the-approved-camunda-7-to-8-migration-strategy-for-cash-settlement]].

Until then, the listed versions are design-baseline claims rather than verified production facts.
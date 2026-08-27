---
type: concept
title: Drools-Based NSTP Rule Evaluation
created: 2026-08-24
updated: 2026-08-24
tags: [drools, nstp, rete, rule-evaluation, archived-design]
related: [drools, cn-rule-service, nstp, multiple-cashflow-exception-handling, what-are-the-performance-and-resilience-contracts-for-special-nstp-rule-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# Drools-Based NSTP Rule Evaluation

The archived CN Rule Service proposal scopes a Drools proof of concept to NSTP rules.

It distinguishes common NSTP rules from special NSTP rules. Special rules retrieve information from an unspecified third-party service before determining whether the rule matches. A match is stated to generate an exception using `operation_level`, `exception_code`, and `exception_category`.

## Performance implication

The source characterizes Drools Rete matching as sequential. Its proposed mitigation is to retrieve remote data concurrently before sequential rule evaluation. Thread-pool sizing and rejection behavior are explicitly identified as items requiring performance testing.

The source suggests caller-runs as an alternative to abort rejection but supplies no workload data. Caller-runs adds backpressure by executing rejected work on submitting threads; it can also propagate saturation and request latency. It is not established as the correct production policy.

## Status

This is a proposed PoC design, not evidence that Drools is the current NSTP implementation or that the PoC met correctness, throughput, resilience, or operational acceptance criteria.
---
type: query
title: What Are the Performance and Resilience Contracts for Special NSTP Rule Dependencies?
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, third-party-service, performance, resilience, thread-pool]
related: [drools-based-nstp-rule-evaluation, cn-rule-service, drools, nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# What Are the Performance and Resilience Contracts for Special NSTP Rule Dependencies?

Special NSTP rules are described as calling an unnamed third-party service before a match decision. The archived source says remote retrieval can be prepared in parallel and that thread-pool configuration should be tested, but it defines no dependency contract.

## Questions

- Which external services and processors are invoked by special NSTP rules?
- What are their timeout, retry, circuit-breaker, concurrency, rate-limit, and fallback policies?
- What correctness behavior applies when dependency data is unavailable or stale?
- What throughput and latency targets govern parallel data preparation?
- Under overload, should tasks be rejected, caller-runs executed, queued, or shed?

## Evidence needed

Processor configuration, remote API contracts, service-level objectives, capacity limits, resilience configuration, and representative load-test results.
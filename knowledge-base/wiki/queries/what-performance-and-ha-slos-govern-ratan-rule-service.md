---
type: query
title: What Performance and HA SLOs Govern RATAN Rule Service?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, performance, high-availability, slos]
related: [ratan-rule-engine, ratan-rule-engine-v2-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# What Performance and HA SLOs Govern RATAN Rule Service?

## Question

What throughput, latency, concurrency, error-rate, capacity, availability, and failover objectives apply to the Rule Service?

## Evidence

The source records one two-thread, five-minute observation with seven settlement and NSTP rules, two filtered rules, and `436/s no errors`. It provides no latency percentiles, hardware, payload characteristics, rule complexity, capacity limits, or HA test results.

## Required resolution

A current performance and HA test plan should define representative workloads, success criteria, scaling behavior, failover behavior, and production SLOs.
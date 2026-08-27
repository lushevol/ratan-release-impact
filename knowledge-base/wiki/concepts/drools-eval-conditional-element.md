---
type: concept
title: Drools eval Conditional Element
created: 2026-08-24
updated: 2026-08-24
tags: [drools, drl, eval, rule-engine]
related: [drools, drl-pattern-constraints, should-drools-eval-perform-external-http-calls]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# Drools eval Conditional Element

The DRL `eval` conditional element is a catch-all condition that executes semantic code returning a primitive Boolean. It can use variables bound by preceding rule conditions and functions defined in the rule package.

The archived source demonstrates `eval(httpCall($c))`, where a function creates a Spring `RestTemplate`, invokes a remote HTTP endpoint, and returns whether the response identifies a loyal customer.

This demonstrates that external calls are technically possible inside rule evaluation. It does not endorse this as an architecture pattern. Network I/O in a matching condition can introduce latency, availability dependencies, nondeterminism, repeated-evaluation concerns, and unclear failure semantics. The example catches every exception and converts it to `false`, potentially masking operational failures.
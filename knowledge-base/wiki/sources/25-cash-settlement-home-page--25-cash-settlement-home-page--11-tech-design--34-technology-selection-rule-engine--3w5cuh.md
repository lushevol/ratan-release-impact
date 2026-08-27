---
type: source
title: Drools Implementation - CN Rule Service
created: 2026-08-24
updated: 2026-08-24
tags: [archived, rule-engine, drools, nstp, redis, kafka]
related: [cn-rule-service, ratan-rule-service-ratan-rule, drools, cached-rule-loading, drools-based-nstp-rule-evaluation, database-to-kafka-exception-event-reliability, what-is-the-current-cn-rule-service-rule-engine-and-rule-source, what-is-the-authoritative-cn-rule-cache-consistency-contract, what-do-operation-level-exception-code-and-exception-category-mean-in-cn-rules, how-are-cn-rule-exceptions-reliably-published-to-kafka, what-are-the-performance-and-resilience-contracts-for-special-nstp-rule-dependencies]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
authors: []
year: 2026
url: ""
venue: "Internal archived technical design"
---
# Drools Implementation - CN Rule Service

## Status and scope

This archived technical-design note proposes a Drools-based proof of concept for NSTP rule implementation in CN Rule Service. It does not confirm that Drools was adopted, that the PoC was completed, or that its performance and correctness were validated.

The document proposes loading rules from Redis rather than PostgreSQL, while noting that rule loading may not be the primary performance bottleneck. It identifies remote calls made by special NSTP rules as a potentially dominant latency dependency.

## Rule types

All listed CN rules are stated to be stored in `ratan_rule_service.ratan_rule`.

| Rule Name | Business Workflow | Rule Type | Rule Status | Comment |
| --- | --- | --- | --- | --- |
| IRS Rule | n/a | IRS | ADD_CONFIRMED DEL_PENDING | - Skip the rule checking if *Cashflow.Is_Cashflow_SettleAsGross* is true. - Call the remote service called ***CashflowService ***to determine if the cashflow is resultant released. |
| Suppression Rule | SETTLEMENT | SUPPRESSION | ADD_CONFIRMED DEL_PENDING | - Skip the rule checking if *Cashflow.Is_Cashflow_Unsuppress* is true. - The rest is same as the *ratanone_suppression_service *does. |
| Swift Suppression Rule | SETTLEMENT | SWIFT_SUPPRESSION | ADD_CONFIRMED DEL_PENDING | - Skip the rule checking if *Cashflow.Is_Cashflow_Swift_Unsuppress* is true. - The rest is same as the *ratanone_suppression_service *does. |
| Netting Rule | n/a | Netting | ADD_CONFIRMED DEL_PENDING | - Skip rule checking if *Cashflow.Is_Cashflow_SettleAsGross* is true. |
| *NSTP Rule* | SETTLEMENT | NSTP | ADD_CONFIRMED DEL_PENDING | - Two types of NSTP rule, one is common rule, the other is the special rule that will call the thirty-party service to determine whether the rule is matched. - Generated the exception according to the *operation_level*, *exception_code*, *exception_category*. |

The source does not define the semantics of `ADD_CONFIRMED DEL_PENDING`, individual predicates, Drools rule files, or the interface of the referenced third-party service.

## Rule storage changes

The document says that `ratan_rule_service.ratan_rule` replaces `ratanone.ratan_suppression_rule` as the store for all CN rules.

```text
Columns added in table ratan_rule_service.ratan_rule:
created_by, updated_by, operation_level, exception_code and exception_category.

Columns removed from table ratanone.ratan_suppression_rule:
creator, last_modifier, approver, approve_time, hierarchy and value_date.
```

The source identifies duplicate exception metadata in `ratan_rule_service.ratan_rule` and `ratan_rule_service.ratan_rule_exception`:

```text
operation_level, exception_code and exception_category
```

It does not provide DDL, data types, keys, constraints, nullability, or index definitions. The intended ownership and definition of `operation_level` remain unresolved.

The special-rule configuration table is described as follows:

```text
ratan_rule_service.ratan_special_rule_config:
business_workflow, rule_type, exception_code, exception_category, operation_level and processor.
```

## Proposed loading and execution approach

The proposal recommends a strategy-pattern abstraction so that rule loading can later change independently of rule evaluation. If Redis becomes the runtime rule source, PostgreSQL and Redis must remain consistent.

No source-of-truth model, cache versioning, TTL, invalidation method, cache warm-up process, stale-rule tolerance, or fallback behavior is specified. See [[cached-rule-loading]] and [[what-is-the-authoritative-cn-rule-cache-consistency-contract]].

The source characterizes Drools Rete matching as sequential and proposes parallel preparation of remotely retrieved data before rule evaluation. It recommends performance testing to tune thread-pool core size, maximum size, queue size, and rejection behavior. Its suggestion to use caller-runs rather than the default abort policy is unvalidated and requires end-to-end overload testing.

## Exception delivery risk

When an NSTP rule matches, the described flow persists an exception and then publishes exception information to Kafka. The source identifies a consistency gap if the database insert succeeds but Kafka publication fails. It points to the [Microservice Transactional Outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html) as a possible mitigation but records no adoption decision.

This concern relates to [[multiple-cashflow-exception-handling]], [[exception-operation-level]], and [[database-to-kafka-exception-event-reliability]].

## Related wiki context

The archived proposal extends [[nstp]] with a distinction between common rules and externally evaluated special rules. It also records a limited relation to [[cashflow-netting]]: Netting Rule checks are skipped when `Cashflow.Is_Cashflow_SettleAsGross` is true. It does not define the current netting state machine, maker-checker process, or an authoritative production architecture.
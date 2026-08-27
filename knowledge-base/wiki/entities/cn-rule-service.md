---
type: entity
title: CN Rule Service
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, cash-settlement, nstp, archived-design]
related: [ratan-rule-service-ratan-rule, drools, cached-rule-loading, drools-based-nstp-rule-evaluation, database-to-kafka-exception-event-reliability, nstp, cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]/Drools Implementation - CN Rule Service.md"]
---
# CN Rule Service

CN Rule Service is described in an archived design note as the component that loads and evaluates IRS, suppression, SWIFT suppression, netting, and NSTP rules.

## Proposed responsibilities

The note identifies `ratan_rule_service.ratan_rule` as the unified store for CN rules. Proposed behavior includes:

- skipping IRS and netting checks when `Cashflow.Is_Cashflow_SettleAsGross` is true;
- skipping suppression checks when `Cashflow.Is_Cashflow_Unsuppress` is true;
- skipping SWIFT suppression checks when `Cashflow.Is_Cashflow_Swift_Unsuppress` is true;
- using `CashflowService` to determine whether a cashflow is resultant released for IRS processing; and
- generating NSTP exceptions using `operation_level`, `exception_code`, and `exception_category` when a rule matches.

NSTP rules are described as either common rules or special rules that call an unspecified third-party service before deciding whether a match occurred.

## Proposed architecture

The archived proposal considers Redis-backed loading, PostgreSQL/Redis consistency controls, a strategy-pattern loading abstraction, and a Drools-based NSTP proof of concept. It also identifies reliable database-to-Kafka exception delivery as an unresolved concern.

## Status

This page records historical design evidence only. The source does not demonstrate the current rule engine, active rule source, completion of the Drools PoC, or production behavior. See [[what-is-the-current-cn-rule-service-rule-engine-and-rule-source]].
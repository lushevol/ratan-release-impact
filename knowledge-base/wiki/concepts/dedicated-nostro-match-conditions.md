---
type: concept
title: Dedicated Nostro Match Conditions
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, matching, rule-engine, drools, rfi, ssi]
related: [dedicated-nostro-stamping, nostro-stamping, ratan-cash-settlement-ssi-stamping-service, ratanone-static-data-service, ratanone-rule-service, what-is-the-authoritative-dedicated-nostro-stamping-architecture]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# Dedicated Nostro Match Conditions

A dedicated Nostro match condition is a configured predicate that determines whether a specialised Nostro configuration should be selected. In the documented RFI example, matching requires portfolio and currency.

The deprecated design considers two ownership models.

## Rule-Engine Evaluation

Under this model, a rule engine evaluates conditions and returns a matching rule or associated Nostro metadata. The documented rule type is `NOSTRO_STAMP`.

Potential benefits identified by the source include centralised condition management, richer matching capability, and reuse of business logic models. Candidate custom fields include:

```text
DEDICATED_NOSTRO_PORTFOLIO
DEDICATED_CURRENCY
```

These fields are intended to avoid product-specific trade-currency paths in rules.

The trade-off is an additional runtime dependency and possible compatibility, availability, and traffic concerns involving `ratanone-rule-service`.

## SSI-Service Evaluation

Under this model, `ratan-cash-settlement-ssi-stamping-service` evaluates the match condition directly.

The source identifies lower dependency and local operational ownership as advantages. However, the proposed initial condition capability is limited to simple operators such as `EQ` and `IN`, and could duplicate the rule engine's role and logic.

## Status

The source makes mutually competing arguments for the two models. It does not demonstrate which component currently owns condition evaluation. See [[what-is-the-authoritative-dedicated-nostro-stamping-architecture]].

## Design Constraint

For trade processing, matching needs contextual separation by `messageType`, `nostroType`, and `currencyTag`. A condition definition must therefore be interpreted in the context of a particular stamp action rather than only as a portfolio/currency predicate.
---
type: entity
title: RATAN One Rule Service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan-one, rule-service, trade-validation, archived]
related: [rule-service-performance-testing, drools, business-rule-engines, drools-rule-language, does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]
---
# RATAN One Rule Service

RATAN One Rule Service is the historical service subject of the archived [[rule-service-performance-testing]] record. In the documented scenario, a consumer trade service calls a validation API to verify a trade against configured rules.

## Historical API scenario

The test record identifies a validation endpoint at `/v1/rules/validate` and supplies a request with:

- `businessFlow`: `FX_REPLICATE`
- `ruleType`: `FILTERING`
- `scbml`: an SCBML/FpML-formatted FX Forward trade payload

The payload provides integration context involving [[stella]], Blade, and SABRE. It does not establish current integration ownership or behaviour.

## Rule-engine status

The source discusses [[drools]] as a candidate engine for suppression, validation, and entitlement rules. It does not confirm that the tested service used Drools, identify a Drools version, or document its KIE configuration, compilation approach, rule deployment model, or session lifecycle.

Accordingly, this entity must not be treated as proof of a confirmed Drools deployment.

## Performance evidence

The archived record reports zero JMeter errors in several 600-second trade-validation runs and latency growth as load increased. The record does not demonstrate a 60-user test, 12-hour endurance result, full workload representativeness, or validated six-instance fleet capacity.

The claimed support for 120 consumer applications remains unverified; see [[does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim]].
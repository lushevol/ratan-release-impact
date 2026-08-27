---
type: query
title: "What Are the Canonical executionFlag and needDryRun API Values?"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-engine, api-schema, enum, dry-run]
related: [ratan-rule-engine, ratan-rule-service-ratan-rule, action-oriented-rule-lifecycle-api, what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]
---
# What Are the Canonical executionFlag and needDryRun API Values?

The archived status-machine refactor proposal does not establish canonical rule-execution and dry-run field names or serialized values.

## Conflicting representations

The source uses all of the following `executionFlag` forms:

```text
EXECUTION
NOT_EXECUTION
NOT_EXECUTED
ExecutionFlag.EXECUTION
```

It uses both names for dry-run control:

```text
needDryRunFlag
needDryRun
```

The proposal states defaults of `EXECUTION` and `false`, respectively, but does not specify a formal JSON schema, enum definition, nullability behavior, backward compatibility, or validation errors.

## Evidence needed

Obtain the implemented DTO or JSON Schema, OpenAPI definition, persistence model, and consumer payloads. Confirm whether `needDryRunFlag` and `needDryRun` are aliases or distinct fields, and identify the exact serialized enum values accepted by [[ratan-rule-service-ratan-rule]].

This issue is part of the broader contract investigation in [[what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]].
---
type: concept
title: Rule Maintenance and Validation Pipeline
created: 2026-08-24
updated: 2026-08-24
tags: [rule-maintenance, validation, service-boundary, cash-settlement]
related: [ratanone-rule-service, ratan-rule-engine, special-rule-processing, scbml, ratan-special-rule-config-v2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# Rule Maintenance and Validation Pipeline

The proposed pipeline separates input transformation from rule evaluation.

## Maintenance

`ratanone-rule-service` directly maintains `NSTP`, netting, suppression, and Swift Suppression rules, including creation, deletion, status changes, and content updates.

## Validation

1. A type-specific rule invokes a domain service.
2. The domain service generates JSON from [[scbml]].
3. The JSON is sent to `ratanone-rule-service`.
4. The service returns a filtered result or a success response.

Special rules add preprocessing before the resulting JSON and rule information are sent to the service.

The source does not specify whether the flow is synchronous, its error model, transaction boundaries, or retry and idempotency behavior.
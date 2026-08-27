---
type: concept
title: Special Rule Processing
created: 2026-08-24
updated: 2026-08-24
tags: [special-rules, rule-engine, rule-content, cash-settlement]
related: [ratanone-rule-service, ratan-special-rule-config-v2, ratan-rule-mapping, rule-maintenance-and-validation-pipeline, nstp-exception-metadata]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# Special Rule Processing

Special rules are identified by `ruleCategory: "SPECIAL"` and receive additional domain-specific processing before evaluation by `ratanone-rule-service`.

Each special-rule configuration predefines a `rule_content` expression. The source example is:

```text
fmEntity__fmAccount__fmType matches "(?i)CORP"
```

The expression replaces the processor-oriented `fact_processor` field and is passed to the rule service with the processed JSON.

The design states that six rules generated from `ratan_special_rule_config` should be marked `is_special = true` in `ratan_rule_mapping`. The six rules are not named in the source, so the count should be treated as configuration-specific pending confirmation.
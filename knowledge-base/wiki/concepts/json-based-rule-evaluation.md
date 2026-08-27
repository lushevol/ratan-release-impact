---
type: concept
title: JSON-Based Rule Evaluation
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, json, scbml, migration, fact-model]
related: [ratan-rule-engine, domain-owned-rule-fact-enrichment, ratan-rule-engine-v2-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]/RATAN Rule Engine Overview.md"]
---
# JSON-Based Rule Evaluation

## Definition

JSON-based rule evaluation is the proposed RatanOne Rule Service v2 model in which callers provide JSON facts directly and the Rule Service evaluates them without internal SCBML conversion.

An illustrative request is:

```json
{
  "businessFlow": "STRATEGIC_SETTLEMENT",
  "ruleType": "NSTP",
  "message": {
    "logicFacts": {
      "Entity": {
        "Counterparty_Is_Internal": [
          "INTERNAL"
        ]
      }
    },
    "additionalFacts": {
      "fmEntity": {
        "fmAccount": {
          "fmType": "CORP"
        }
      }
    }
  }
}
```

## Architectural rationale

Direct JSON input is intended to:

- Keep the Rule Service lightweight.
- Allow domain-specific and custom facts such as `fmEntity.fmAccount.fmType`.
- Avoid maintaining internal XML/SCBML transformation logic.
- Move enrichment and transformation responsibility to consuming domain services.

## Migration considerations

The source proposes retaining v1 temporarily while consumers migrate to v2. It identifies uncertainty around custom facts when SCBML conversion is used and records limitations in `tl-model-client`, including inability to support cashflow parsing.

No authoritative JSON schema, typing model, result contract, error contract, or versioning policy is included.
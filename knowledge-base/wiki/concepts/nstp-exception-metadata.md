---
type: concept
title: NSTP Exception Metadata
created: 2026-08-24
updated: 2026-08-24
tags: [NSTP, exception-metadata, rule-engine, JSON]
related: [ratanone-rule-service, ratan-rule-engine, special-rule-processing, ratan-rule-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# NSTP Exception Metadata

NSTP exception metadata is UI-supplied information passed to `ratanone-rule-service` with a rule.

The source example represents `metaData` as a JSON object serialized inside a string:

```json
{
  "exceptions": [
    {
      "exceptionCode": "CORP CLIENT",
      "operationLevel": "MAKER_CHECKER",
      "exceptionCategory": "NSTP"
    }
  ]
}
```

Documented `operationLevel` values are `MAKER_ONLY`, `CHECKER_ONLY`, and `MAKER_CHECKER`. Documented `exceptionCategory` values include `NSTP`, `HIGH_RISK_NSTP`, and `OTHER`; `AFFIRMATION` and `BACK_VALUE` are identified as special-rule categories.

The source does not establish whether serialized JSON is the authoritative API representation, whether multiple exceptions are allowed, or how metadata is validated.
---
type: query
title: Which Drools Dialect and Version Support the Required Null Navigation?
created: 2026-08-24
updated: 2026-08-24
tags: [drools, mvel, drl, compatibility, null-safety]
related: [drools, drl-pattern-constraints, dynamic-drl-compilation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# Which Drools Dialect and Version Support the Required Null Navigation?

The generated DRL template explicitly declares `dialect "mvel"`, while the source identifies lack of null-safe bean-property navigation in MVEL as an open issue. The source does not state the evaluated Drools or MVEL version, nor does it document an alternative dialect or safe input-model strategy.

## Evidence needed

- Exact Drools, KIE, and MVEL versions.
- Reproducible tests for required nested-property and null-handling expressions.
- The authoritative dialect decision.
- Rule-authoring constraints or data-model conventions that avoid unsupported navigation.
- Version-specific validation of the documented DRL operator syntax.
---
type: concept
title: Korea Settlement Message Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, cashflow, eligibility, swift, settlement]
related: [ratan, enisis, korea-migration, ratan-enisis-fm-solace-integration, ratan-swift-message-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/RATAN to ENISIS.md"]
---
# Korea Settlement Message Eligibility

For the RATAN-to-ENISIS Korea route, the stated outbound settlement-message condition is:

```text
Cashflow Status in (RELEASED, SETTLED) and Settlement Mean='NOS'
```

The source labels this as existing SWIFT logic. It is evidence for the Korea migration route only; it does not define a universal RATAN cashflow-dispatch rule.

The source does not specify null treatment, handling of cashflow changes after dispatch, or whether the two conditions are implemented as a single conjunctive decision in all components.
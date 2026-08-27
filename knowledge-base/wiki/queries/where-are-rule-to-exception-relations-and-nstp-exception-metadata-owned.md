---
type: query
title: Where Are Rule-to-Exception Relations and NSTP Exception Metadata Owned?
created: 2026-08-24
updated: 2026-08-24
tags: [exceptions, nstp, rule-engine, ownership, traceability]
related: [ratan-rule-service, ratanone-rule-service, cn-rule-prevalidation, nstp-maker-checker-processing, exception-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Where Are Rule-to-Exception Relations and NSTP Exception Metadata Owned?

The archived design removes `exception_code` and `exception_category` from the target rule schema, removes legacy NSTP exception APIs, and states that Rule Service should not maintain exception-to-rule relationships.

At the same time, CN NSTP validation is said not to start when exceptions exist.

## Questions to resolve

- Which service owns rule-to-exception traceability after migration?
- Which service provides NSTP exception metadata and action data?
- What exception statuses prevent NSTP rule validation?
- How is the exception check performed, and what happens on dependency failure?
- How are audit and historical investigation supported across the Rule Service and [[exception-platform]]?

The source identifies a boundary decision but does not assign the replacement responsibility.
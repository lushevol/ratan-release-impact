---
type: query
title: What Is the Canonical NSTP Exception Platform and Publication Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [nstp, exception-management, integration, publication, open-question]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--35-ratan-rule-service-technical-desi--j5csbt, ratanone-rule-service, ratan-rule-engine, nstp-exception-metadata]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design.md"]
---
# What Is the Canonical NSTP Exception Platform and Publication Contract?

The design states that rule-match exceptions are published to an “exception platform,” while its use case says exceptions are published to “rep.” It does not confirm whether these names refer to the same destination.

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--35-ratan-rule-service-technical-desi--j5csbt]] states that every inbound message is checked against active NSTP rules and that matching rules generate externally published exceptions visible to users.

## Questions to resolve

- Are “exception platform” and `rep` the same system?
- Which service owns exception publication?
- What event or API schema carries the exception?
- What are the idempotency, ordering, retry, acknowledgement, and failure-handling requirements?
- Does publication occur synchronously with rule evaluation or asynchronously?
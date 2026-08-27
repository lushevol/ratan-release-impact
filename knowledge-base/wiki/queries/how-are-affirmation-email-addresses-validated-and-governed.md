---
type: query
title: How Are Derivative Settlement Affirmation Email Addresses Validated and Governed?
created: 2026-08-23
updated: 2026-08-23
tags: [email-routing, data-governance, contact-data, derivative-settlement, operational-risk]
related: [derivative-settlement-affirmation-email-routing, what-is-the-authoritative-affirmation-email-routing-key]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Cashflow Scope & Email Ids.md"]
---
# How Are Derivative Settlement Affirmation Email Addresses Validated and Governed?

The source provides external recipient addresses but does not define ownership or operational control for them. It also includes malformed or inconsistent email representations and individually named contacts.

## Questions to resolve

- Who owns the recipient configuration and approves changes?
- What syntax and domain validation occurs before activation?
- How are malformed addresses corrected and verified?
- Should shared distribution lists be preferred over named individuals?
- How are named recipient contacts reviewed for privacy, continuity, and access-control concerns?
- What periodic recertification is required?
- How are delivery failures retried, alerted, and remediated?
- Are recipients classified into To, CC, and BCC roles?

Until a governance and validation process is defined, recipient data should be treated as controlled operational reference data rather than self-validating configuration.

See [[derivative-settlement-affirmation-email-routing]].
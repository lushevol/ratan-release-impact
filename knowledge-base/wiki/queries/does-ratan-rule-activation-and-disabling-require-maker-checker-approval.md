---
type: query
title: Does RATAN Rule Activation and Disabling Require Maker/Checker Approval?
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, maker-checker, rule-activation, access-control]
related: [ratan-rule-lifecycle-management, business-rule-maintenance, maker-checker-settlement-control, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md"]
---
# Does RATAN Rule Activation and Disabling Require Maker/Checker Approval?

The source states that rules can be updated only through Maker/Checker control, but separately says that users with operate permission can immediately disable live rules or activate dry-run rules.

It is unclear whether activation and disabling:

- Are exempt from Maker/Checker approval.
- Require a separate authorization or emergency control.
- Are independently audited.
- Are inaccurately described in the guide.

An authoritative entitlement matrix and workflow specification are needed before treating these actions as compliant with the general approval process.

## Related evidence

- [[concepts/ratan-rule-lifecycle-management]]
- [[concepts/maker-checker-settlement-control]]
- [[concepts/business-rule-maintenance]]
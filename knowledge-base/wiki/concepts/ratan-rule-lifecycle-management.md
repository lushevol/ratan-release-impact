---
type: concept
title: RATAN Rule Lifecycle Management
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, rule-lifecycle, rule-engine, auditability]
related: [ratan, rule-service, business-rule-maintenance, maker-checker-settlement-control, fmo-post-trade-portal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md"]
---
# RATAN Rule Lifecycle Management

RATAN Rule Lifecycle Management is the set of operations and controls used to manage a rule from creation through approval, testing, activation, modification, disablement, deletion, review, and audit.

## Documented lifecycle operations

The RATAN Rule Blotter supports:

1. **Create** — A maker selects the business flow, defines field-value conditions, supplies a mandatory reason, and may add a comment.
2. **Dry run** — A rule is configured not to execute immediately, allowing unexpected configurations to be detected before live processing.
3. **Check** — A checker approves or rejects a submitted creation or update.
4. **Activate** — A user with operate permission can activate an existing dry-run rule; the source says this takes effect immediately.
5. **Disable** — A user with operate permission can disable an existing live rule with immediate effect.
6. **Update** — A maker changes conditions and supplies a reason; the update remains pending checker approval.
7. **Delete** — A maker can submit deletion of an existing cashflow suppression rule, subject to checker approval.
8. **History** — Users can inspect record-level and whole-rule histories.
9. **Export and filter** — Users can export rules and filter individual rule fields.

Different selected fields are treated as `AND` conditions. Grouped rules are supported for complex scenarios.

## Control ambiguities

The source says that rule makers and checkers should be different people for creation and updates, while its overview says that a checker can also perform maker actions. Immediate operate-permission actions also appear to bypass the general Maker/Checker process. The phrase “activate an existing dry run live rule” is unclear about the underlying state.

These ambiguities are tracked in:

- [[queries/does-ratan-rule-activation-and-disabling-require-maker-checker-approval]]
- [[queries/can-a-ratan-rule-checker-also-act-as-maker-under-segregation-of-duties-controls]]
- [[queries/what-is-the-ratan-dry-run-rule-state-model-and-activation-control]]

## Auditability

History views, export, mandatory reasons, and DOI recording provide documented evidence mechanisms. The source does not specify retention periods, immutable audit requirements, entitlement matrices, or audit-log ownership.

## Related pages

- [[entities/rule-service]]
- [[concepts/business-rule-maintenance]]
- [[concepts/maker-checker-settlement-control]]
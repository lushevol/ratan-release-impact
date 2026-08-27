---
type: concept
title: Auto-Netting Rule Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, lifecycle, maker-checker, rule-engine]
related: [auto-netting-rule-event-contract, auto-netting-rule-version-replacement, ratan, cashflow-manual-fail-maker-checker-control, maker-checker-ssi-control, what-is-the-authoritative-auto-netting-rule-action-contract, is-auto-netting-update-approval-atomic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Auto-Netting Rule Lifecycle

The documented `AUTO_NETTING` lifecycle applies to the `STRATEGIC_SETTLEMENT` business flow and separates maker actions from checker approval or rejection.

## States

- `ADD_PENDING`: a newly created rule awaiting checker action.
- `UPDATE_PENDING`: a proposed replacement rule awaiting checker action.
- `LIVE`: an operationally active rule.
- `DISABLED`: a rule removed from active use but represented as disabled.
- `DEAD`: a terminally removed rule, including rejected proposals and retired prior versions.

## Main Transitions

| Operation | Event sequence | Result |
| --- | --- | --- |
| Create | `SAVE` | A new rule enters `ADD_PENDING`. |
| Approve creation | `CONFIRM` | The rule becomes `LIVE`. |
| Reject creation | `REMOVE` | The rule becomes `DEAD`. |
| Initiate update | `CONFIRM` on old rule, then `SAVE` on new rule | The existing rule is represented as `LIVE`; the replacement enters `UPDATE_PENDING`. |
| Approve update | `REMOVE` old rule, then `CONFIRM` replacement | The old rule becomes `DEAD`; the replacement becomes `LIVE`. |
| Reject update | `REMOVE` replacement | The proposed replacement becomes `DEAD`. |
| Enable | `CONFIRM` | A rule becomes `LIVE`. |
| Disable | `REMOVE` | A rule becomes `DISABLED`. |
| Delete | `REMOVE` | A rule becomes `DEAD`. |

Disable and delete must remain separate operations: both use `REMOVE`, but their statuses and intended meanings differ.

The source documents the business sequence but does not establish authorization checks, atomicity, idempotency, retries, compensation, or the rule-evaluation policy during the update-approval window. See [[is-auto-netting-update-approval-atomic]].
---
type: query
title: What Is the Authoritative Auto-Netting Rule Action Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, rule-action, api-contract, ambiguity]
related: [auto-netting-rule-lifecycle, auto-netting-rule-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# What Is the Authoritative Auto-Netting Rule Action Contract?

The source contains conflicting approval-action representations.

The lifecycle matrix specifies `create_confirm` for creation approval and `update_confirm` for update approval. The supplied `CONFIRM` payloads for both workflows instead use:

```json
"rule_action": "confirm"
```

It also uses `CONFIRM` with `rule_action: "update"` to initiate an update on an existing LIVE rule, despite `CONFIRM` otherwise denoting activation.

## Questions to Resolve

- Is `confirm` the canonical approval value, or must callers send operation-specific values?
- Does the rule engine derive the operation from status and record linkage instead of `rule_action`?
- Is `CONFIRM` with `rule_action: "update"` a frontend-only instruction, a persisted event, or a documentation error?
- What validation and backward-compatibility rules apply to `rule_action` values?

Resolution is required before the UI, backend, and rule-event consumers can rely on a stable contract.
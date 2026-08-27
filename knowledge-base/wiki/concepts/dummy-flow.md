---
type: concept
title: Dummy Flow
created: 2026-08-25
updated: 2026-08-25
tags: [flow, configuration, settlement, change-management]
related: [chg1006933, configuration-removal, ratan, pre-cab-checklist]
sources: ["RATAN/RATAN -Release copy/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_06_20_CHG1006933_Ratan Settlement remove SG dummy flow config.md"]
---
# Dummy Flow

A dummy flow is a flow described as placeholder, synthetic, temporary, test-oriented, fallback, or otherwise non-standard. The term is used in the source filename in connection with [[chg1006933]], which proposes removal of an `SG` dummy-flow configuration from Ratan Settlement.

The available evidence does not define the flow's purpose. It may be a test route, temporary workaround, fallback path, inactive configuration, or an operationally used flow. No such interpretation should be treated as confirmed.

## Investigation requirements

Before removal, the change record should identify:

- The flow's functional purpose and lifecycle.
- The meaning of `SG`.
- Environments and settlement paths where it can be invoked.
- Upstream callers and downstream consumers.
- Conditions that activate the flow.
- Test coverage and expected behavior after removal.
- Rollback or reinstatement steps.

These details are especially relevant to [[configuration-removal]] and [[pre-cab-release-governance]].
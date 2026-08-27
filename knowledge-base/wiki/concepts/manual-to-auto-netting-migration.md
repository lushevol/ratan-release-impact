---
type: concept
title: Manual-to-Auto-Netting Migration
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, manual-processing, rule-management, migration, controls]
related: [cashflow-auto-netting, auto-netting-rule-management, auto-netting-static-go-live-sequencing, maker-checker-settlement-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Manual-to-Auto-Netting Migration

Manual-to-auto-netting migration is the controlled replacement or modification of existing manual netting rules with static auto-netting rules.

## Migration patterns

The source identifies several patterns:

- Disable an existing manual rule after a new auto-netting rule works as expected.
- Switch an existing manual rule to auto netting without changing its condition, as specified for FMO SG.
- Update an existing rule to narrow its scope before or alongside auto-netting activation.
- Retain manual processing where the technical team will not switch the rule; a user request is then required based on business requirements.

## Control risk

The source does not identify which manual rules were ultimately disabled, retained, or converted. It also does not provide a rollback sequence or prove that suppression coverage remained gap-free during migration. These details require operational confirmation before the procedure can be treated as a complete go-live record.
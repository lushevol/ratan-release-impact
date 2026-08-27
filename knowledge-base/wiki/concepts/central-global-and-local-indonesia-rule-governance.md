---
type: concept
title: Central Global and Local Indonesia Rule Governance
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-governance, indonesia, maker-checker]
related: [ratan-gdc, ratan-indonesia, ratan-global-rule-synchronization, ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment, when-do-maker-checker-approvals-trigger-ratan-global-rule-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# Central Global and Local Indonesia Rule Governance

The proposed governance model separates centrally governed Global rules from locally administered Indonesia-specific rules.

Global rules are governed in [[ratan-gdc]], automatically identified from the absence of Indonesia entity attributes, and replicated to [[ratan-indonesia]] as read-only records. Indonesia-specific rules are entered directly in RATAN Indonesia and contain the Indonesia FMID and FMCODE attributes by default.

The source requires maker/checker control for both GDC Global-rule changes and direct Indonesia entries. It does not define authorization roles, approval states, audit requirements, or whether replication occurs at submission, approval, activation, or another lifecycle transition.
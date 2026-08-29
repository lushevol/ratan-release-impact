---
type: concept
title: Auto-Netting Rule Configuration
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, rule-management, validation, cash-settlement]
related: [auto-netting-job-time, ratanone-rule-service, what-is-the-auto-netting-hint-and-pending-auto-netting-status-transition]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# Auto-Netting Rule Configuration

An auto-netting rule is a netting rule identified by `isAutoNetting`. The design reuses the netting-rule blotter and makes the following fields mandatory when auto-netting is selected:

- booking entity;
- currency; and
- shifter.

The shifter must support hour and minute values. Rules may include exclusion criteria.

ratanone rule service is intended to create, update, delete, validate, and deduplicate these rules. On a rule-check hint, it should return `VD+Shifter` for downstream lifecycle processing.

The design does not define the rule schema, duplicate identity, exclusion precedence, hint producer, or precedence against other netting rules. It also does not establish whether this design applies specifically to inter-entity, Murex-originated, or other cashflow populations.
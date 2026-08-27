---
type: query
title: What Is the Precedence Between NDIRS STP and Pending NDS Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, NDIRS, STP, netting, rule-precedence]
related: [ndirs, nds-fixing, pending-nds-netting, nds-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# What Is the Precedence Between NDIRS STP and Pending NDS Netting?

The requirement states that USD from NDS Fixing for ND IRS must be STP and excluded from netting. The generic solutioning rule places qualifying NDS Fixing cashflows into `WAITING` with `Pending NDS Netting` when the parent typology is not NDIRS.

The authoritative rule precedence, including behavior when parent typology is empty, is not documented. Confirm whether the NDIRS condition is an explicit exclusion evaluated before the generic NSTP rule.
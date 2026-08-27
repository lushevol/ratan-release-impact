---
type: query
title: What Is the Authoritative Pending-Netting Withdrawal Behavior?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, pending-netting, lifecycle, withdrawal, un-netting]
related: [netting-resultant-cashflow-lifecycle, cashflow-lifecycle-versioning, ratan-cashflow-lifecycle-state-machine, irs-resultant-cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting.md"]
---
# What Is the Authoritative Pending-Netting Withdrawal Behavior?

## Question

What should happen when a component cashflow is withdrawn while its resultant netting cashflow is pending?

## Evidence

The source states that a pending netting cashflow cannot be un-netted, manually or automatically, by withdrawing a component cashflow. It does not define whether the withdrawal is rejected, whether the pending resultant remains unchanged, or whether the resultant moves to an exception or remediation state.

## Required Resolution

The lifecycle specification should define:

- the canonical pending-netting state and sub-state;
- permitted and rejected withdrawal requests;
- behavior for manual and automatic withdrawal;
- treatment of component and resultant cashflows;
- audit and reconciliation requirements;
- recovery behavior if the component withdrawal has already been processed.

The restriction should remain a proposed requirement until the transition behavior is approved.
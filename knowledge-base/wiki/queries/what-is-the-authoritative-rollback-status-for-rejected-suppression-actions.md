---
type: query
title: What Is the Authoritative Rollback Status for Rejected Suppression Actions?
created: 2026-08-23
updated: 2026-08-23
tags: [suppression, maker-checker, rollback, cashflow-status]
related: [suppression-maker-checker-workflow, cashflow-status-lifecycle, cashflow-suppression, swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# What Is the Authoritative Rollback Status for Rejected Suppression Actions?

Checker rejection of Cashflow Suppression and Swift Suppression specifies “Rollback status” for the cashflow status, sub-status type, and sub-status.

The requirement does not define whether this means the immediately preceding state, the original state at Maker submission, or another calculated workflow state. The rule is especially unclear for a cashflow that was already `WAITING` with an unrelated sub-status.
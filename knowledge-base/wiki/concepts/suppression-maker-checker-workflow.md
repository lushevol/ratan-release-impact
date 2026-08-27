---
type: concept
title: Suppression Maker/Checker Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [maker-checker, cashflow, suppression, workflow, controls]
related: [cashflow-suppression, swift-suppression, suppression-rule-management, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# Suppression Maker/Checker Workflow

Manual Cashflow Suppression and Swift Suppression use dual control.

A Maker can initiate suppression from `PROJECTED`, `READY`, or a `WAITING` cashflow not already carrying a suppression-related sub-status. The cashflow enters `WAITING` with the applicable action type and `Pending Verification`.

A Checker approval changes the status to either `CASHFLOW SUPPRESSED` or `SWIFT SUPPRESSED`. An approved undo of either suppression type changes the cashflow to `QUEUED`. Rejection of an undo explicitly restores the relevant suppressed status.

The specified target for a rejected suppression request is only “Rollback status.” The requirement does not define how that status is calculated or restored, particularly for an originally `WAITING` cashflow. See [[what-is-the-authoritative-rollback-status-for-rejected-suppression-actions]].

Manual undo is unavailable beyond value date. See [[what-is-the-value-date-cutoff-and-exception-process-for-suppression-undo]].
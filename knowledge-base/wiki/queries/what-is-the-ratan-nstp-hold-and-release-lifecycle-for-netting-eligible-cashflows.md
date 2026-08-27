---
type: query
title: What Is the Ratan NSTP Hold and Release Lifecycle for Netting-Eligible Cashflows?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, nstp, netting, cashflow-lifecycle, settlement-ops]
related: [ratan, netting-eligibility-rules, manual-cashflow-netting, dvp-nstp, ratan-cashflow-lifecycle-state-machine, cashflow-hold-unhold]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Rules Static Data.md"]
---
# What Is the Ratan NSTP Hold and Release Lifecycle for Netting-Eligible Cashflows?

The source states that a cashflow eligible under a Netting eligibility rule is held as NSTP, after which [[settlement-ops]] manually performs netting. It does not identify the precise lifecycle state, sub-state, transition owner, or release behavior.

## Questions

- Which Ratan state and sub-state represent the documented NSTP hold?
- Is every eligibility-rule match automatically held, or can an operator override the hold?
- Which user action or system event releases a cashflow after manual netting?
- How are failed, rejected, cancelled, or partially completed manual-netting attempts handled?
- Does this NSTP use have the same meaning as the DVP context in [[dvp-nstp]]?
- What audit events and notifications are required for hold and release transitions?

## Evidence Needed

Review the authoritative [[ratan-cashflow-lifecycle-state-machine]], action eligibility rules, and operational procedures for [[manual-cashflow-netting]].
---
type: concept
title: Release-Cutoff Risk for Unhold
tags: [cashflow, unhold, release-cutoff, operational-risk, downstream-processing]
related: [held-cashflow-reinstatement, cash-settlement-home-page, adhoc-ssi-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Actions on Hold.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Release-Cutoff Risk for Unhold

Release-cutoff risk for `Unhold` is the risk that restoring a held cashflow to `READY` allows automatic downstream release when the release-cutoff job executes.

The requirement states that an operator may need to amend SSI, suppress the cashflow, or otherwise intervene before release. Direct `Unhold` does not provide that intervention point when the pre-hold state was `READY`.

## Specified mitigation

The [[cash-settlement-home-page]] must warn users that `Unhold` can auto-release payment to downstream and must explain that it restores the previous status: `QUEUED`, `WAITING`, or `READY`.

For cashflows requiring further intervention, the specified alternative is [[held-cashflow-reinstatement]] through **Send to WAITING**, which creates a `WAITING` state with a `Reinstate` exception.

## Scope caveat

This is a functional-requirement rule for the Cash Settlement Home Page. The source does not identify the release-cutoff job implementation, timing semantics, downstream system, or applicability across products and entities.
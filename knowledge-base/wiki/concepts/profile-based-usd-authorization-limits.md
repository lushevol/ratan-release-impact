---
type: concept
title: Profile-Based USD Authorization Limits
created: 2026-08-23
updated: 2026-08-23
tags: [authorization, usd-limits, ratan, cash-settlement, operational-risk, access-control]
related: [ratan, fmo-ops, high-value-exception-dependency, settle-as-gross-maker-checker-workflow, cashflow-usd-equivalent-authorization-calculation, profile-limit-static-data-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# Profile-Based USD Authorization Limits

## Definition

Profile-based USD authorization limits are static monetary thresholds assigned to operational profiles. Ratan compares a cashflow's USD-equivalent amount with the authority configured for the acting user before allowing verification or approval.

The objective is to align payment authority with operational seniority and reduce BAU operational risk.

## Proposed authority bands

The requirement proposes increasingly senior global checker profiles:

- `GBL_BOC_ST`: below USD 30 Million.
- `GBL_BO_ST`: below USD 100 Million.
- `GBL_BOL_ST`: below USD 1 Billion, with additional high-risk actions listed.
- `GBL_BOM_ST`: up to USD 4 Billion.

The exact inclusivity of the thresholds is unresolved. In particular, the source does not state who may approve exactly USD 30 million, USD 100 million, or USD 1 billion.

## High-risk actions

The high-value profile is stated to approve:

1. Adhoc Netting.
2. Amendment or cancellation after payment release.
3. Exceptions at or above USD 100 Mio.
4. CPN across FX and Deriv.

The requirement does not clarify whether these actions remain subject to the general monetary limit or whether profile 10 inherits all profile-9 high-risk entitlements.

## Enforcement

The source describes UI gating: show Submit/Approve when the user is authorized and hide it otherwise. UI gating alone is not sufficient. Ratan should enforce the same decision at the backend or API boundary to prevent direct-request bypass, race conditions, and stale UI state.

The distinction between maker submission and checker approval also requires confirmation.

## Data and audit requirements

The authorization decision should be reproducible and auditable. The source identifies `Profile`, `Currency`, `USDConverted`, and `Limit` as important fields for a Ratan-specific table, but does not define the schema or the rate and rounding metadata needed to reproduce a non-USD decision.

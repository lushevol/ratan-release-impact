---
type: source
title: Source: Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, cpn, un-netting, technical-design, draft]
related: [cpn-netting, force-gross-review, cpn-netting-reversal-cashflow, netting-resultant-cashflow-lifecycle, automatic-un-netting-on-trade-market-events, netting-withdrawal-timing, cashflow-netting, entities/stella, entities/cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN Technical Design Draft for Netting and Un-Netting

## Scope and status

This draft describes CPN netting and un-netting actions on cashflows, including ad-hoc netting, CPN netting, Force Gross, manual full-group un-netting, and automatic un-netting after Stella trade amendments or cancellations.

The document is evidence of intended workflow design rather than a confirmed production contract. It contains unresolved terminology, status, versioning, and Netting ID inconsistencies.

## Core workflow

The intended CPN workflow is:

1. Cashflows from stella or Murex 2.11 are sent to Payment Lake.
2. The CPN Eligibility Checking workflow identifies eligible cashflows and marks them with the `CPN Netting` sub-status type.
3. FMO Ops selects components from the cashflow blotter and performs CPN netting.
4. Selected components receive a Netting ID, move to `Netted`, and become invisible in the Cashflow Blotter.
5. CPN Service creates a resultant cashflow and stores it in Payment Lake.
6. Settlement Workflow routes the resultant to NSTP Release for `Netting Review`.
7. A checker approves the resultant, changing it to `Validated` with `Reviewed` sub-status.
8. The resultant may subsequently progress to `Released` and `Settled`.

The component lifecycle is separate from the resultant lifecycle. Netted components are filtered from subsequent settlement tasks, while the resultant is held for review.

## Supported action boundaries

| Cashflow Primary Status » | Projected/Queued | Pending | Validated | Released | Settled |
| --- | --- | --- | --- | --- | --- |
| Action ↓ |  |  |  |  |  |
| Ad-hoc NET on components | scenario 1 | NA | NA |  |  |
| CPN NET on components | NA | scenario 2 | NA | NA | NA |
| Force Gross on components | NA | scenario 3 | NA | NA | NA |
| UNNET on resultant | NA | scenario 4 | scenario 5 | NA | NA |
| AMENDMENT on components | NA | scenario 6 | scenario 7 |  |  |
| CANCELLATION on components | NA | scenario 8 | scenario 9 |  |  |
| Auto CPN NET | Out of Day 1 scope |  |  |  |  |
| NET of NET | Not supported; un-net the original netting first |  |  |  |  |
| Partial UNNET | Not supported; only full un-netting is supported |  |  |  |  |
| Incremental Amendment | Not supported; follow current production behavior |  |  |  |  |

Scenario 1 separately describes ad-hoc netting across a mixed set of `Projected`, `Queued`, `Pending`, and `Validated` components. This conflicts with the narrower summary matrix and requires clarification.

## Ad-hoc netting

Ad-hoc netting allows a user to select component cashflows from the Cashflow Blotter. The scenario includes:

- `Projected` cashflows with `CPN Netting` sub-status type.
- `Queued` cashflows with `CPN Netting` sub-status type.
- `Pending` cashflows marked `CPN Netting`.
- `Pending` cashflows with another sub-status.
- `Validated` cashflows.

After selection, all components move to `Netted`, receive the same Netting ID, and are hidden from the GUI. CPN Service creates a queued resultant, which Settlement Workflow later changes to `Pending` / `Netting Review`.

## CPN netting and review

For standard CPN netting, eligible components are initially `Pending` with `CPN Netting` sub-status type. The user can typically choose `Netting` or `Force Gross`.

After CPN netting:

- Components move from `Pending` to `Netted`.
- Components receive a Netting ID such as `N001`.
- Component versions are incremented.
- Murex-originated updates are written through CPN Service to Payment Lake.
- Stella-originated updates are propagated through `Stella -> TDS3 -> Payment Lake`.
- The resultant is created by CPN Service with source system `CPN`.
- The resultant moves from `Queued` to `Pending` / `Netting Review`.
- Checker approval changes it to `Validated` / `Reviewed`.

## Force Gross

Force Gross is a separate maker/checker path. A user may select some components for CPN netting and others for Force Gross in the same operation.

Force Gross components:

- Are excluded from the Netting ID and resultant.
- Move to `Pending`.
- Receive `Force Gross Review` sub-status type.
- Expose `Force Gross Approve/Reject`.
- Move to `Validated` / `Reviewed` after checker approval.

## Manual full-group un-netting

Manual un-netting is available on a resultant in `Pending` / `Netting Review` or `Validated` / `Reviewed`.

The maker initiates un-netting, changing the resultant to `Un-Net Review`. A checker can approve or reject the action. On approval:

- The complete netting group is restored; partial un-netting is unsupported.
- The resultant moves to `DEAD`.
- Components move from `Netted` to `Queued`.
- Component versions increase.
- Components return to Settlement Workflow.
- CPN Eligibility Checking runs again.
- Eligible components are marked `CPN Netting` and require manual netting again.

## Automatic un-netting after trade events

When a new version of a netted component arrives after a Stella trade amendment or cancellation, Settlement Workflow detects that the previous version belonged to a netting group.

If the resultant is not released or settled:

- CPN Service automatically un-nets the prior netting group.
- The old resultant moves to `Dead`.
- Unchanged components return to `Queued` and later re-enter CPN eligibility.
- The amended component receives a newer version and may re-enter eligibility.
- A cancelled component moves to `Dead`.
- The latest eligible components can be manually netted again.

If the resultant has been released:

- The original resultant remains `Released`.
- Components move from `Netted` to `Queued`.
- CPN creates a reversal cashflow.
- The reversal is sent to NSTP Release for manual operations intervention.
- The latest component versions re-enter CPN eligibility.

The document states that the same reversal path is intended for a settled resultant, but does not provide a separate settled-state example.

## Reversal cashflow contract shown in the draft

The following record is reproduced from the draft as the proposed reversal example:

| Description | Cashflow ID | Reversal Flag | Reversal ID | Netting ID | Source System | Cashflow Status | Cashflow Version | Cashflow Sub Status Type | Payment Lake Version | Comment |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- |
| Post CPN Netting | C105 | N |  | N001 | CPN | Released | 3 | NA | 4 |  |
| Cashflow Amendment | C106 | Y | C105 | N001 | CPN | Pending | 1 | NSTP Release | 1 | This is Reversal of C105 |

`C106` is intended to represent the reversal of `C105`. The draft further states that `C106` may later be used to generate an `MTx92` SWIFT message to cancel the original resultant.

The document does not define field types, nullability, uniqueness, idempotency, or whether `Reversal ID` must reference the immediately preceding resultant version.

## Unresolved design points

- The authoritative eligibility matrix for mixed-status ad-hoc netting is unclear.
- The cancellation scenario repeatedly uses amendment terminology.
- Settled-resultant behavior is described but not separately specified.
- Component sub-status values after manual un-netting are inconsistent between scenarios.
- It is unclear whether Netting ID values are historical, active, or both after un-netting.
- Cashflow version and Payment Lake version increments are not governed by a formal rule.
- The terminal meaning of `DEAD` is not defined.
- Automated eligibility identification is in scope, while automated CPN net execution is explicitly out of Day 1 scope; this distinction should be stated directly.
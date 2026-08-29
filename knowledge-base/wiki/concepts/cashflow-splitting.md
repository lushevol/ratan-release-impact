---
type: concept
title: Cashflow Splitting
created: 2026-08-22
updated: 2026-08-23
tags: [cashflow, splitting, settlement-operations, fmrp, settlement, nstp, exceptions, cashflow-splitting, ratan, cash-settlement, lifecycle, uat, accounting, netting, split, cashflows]
related: [ratan-cashflow-blotter, loaniq, cashflow-blotter-action-eligibility, cash-settlement-home-page, split-cashflow-netting-exclusion, pending-nds-netting, ratan-cashflow-lifecycle-state-machine, pending-confirmation-affirmation, ratan, cashflow-unsplit, split-amount-amendment, split-child-threshold-redistribution, split-cashflow-downstream-integration, cashflow-logical-model, netting-eligibility-rules, nostro-threshold-auto-splitting, split-child-processing-exclusions, split-cashflow-swift-annotation, ratan-cashflow-id-management, cashflow-lifecycle-versioning, netting-resultant-cashflow-lifecycle, is-manual-splitting-of-irs-aggregation-resultants-in-day-1-scope, split-cashflow-withdrawal-propagation, accounting-request-info-attachment, net-function, split-cashflow-dvp-handling, cashflow-lineage-and-amendment-correlation, netting-service, resultant-cashflow-generation, cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Cashflow Splitting

Cashflow splitting creates and handles child cashflows derived from an original parent or aggregate cashflow, allowing child amounts to be processed separately. The generated Cashflow Splitting source describes the children as collectively representing the original payment amount, supporting allocation to different client accounts or settlement instructions, and reducing manual-payment activity.

The FMRP cashflow-blotter source provides actions to split a cashflow, amend a split amount, and un-split a cashflow. The Cashflow Splitting UAT source describes splitting in Ratan as dividing an eligible parent cashflow into multiple child cashflows.

The ASPIRE UAT record distinguishes:

- manual splitting of gross cashflows;
- automatic splitting of gross cashflows; and
- automatic distribution following creation of a net-resultant cashflow.

## Netting-service design representation

The [[netting-service]] design represents splitting with the `SPLIT` action and stores component/resultant records in the same cashflow-operation model.

In the example from that design:

- resultant `N01` has amount `300` and status `SPLIT`;
- child `S01` has amount `150` and status `WAITING`; and
- child `S02` has amount `150` and status `WAITING`.

Both children have split ID `3333`.

The netting-service design does not specify:

- whether the original resultant is terminal;
- whether it remains linked to a netting ID;
- whether split outputs may later be re-netted;
- validation of amount conservation;
- permissible split counts;
- field derivation;
- authorization; or
- failure recovery.

These design statements concern the netting-service representation and are not generalized here as requirements for the Ratan cashflow-blotter split workflow.

## UAT evidence

The ASPIRE UAT record 25 cash settlement home page  25 cash settlement home page  22 functional requirement  27 settlement day2 requir  6za5lq records passing scenarios in HK, TW, and TH for:

- manual gross splitting followed by release, failure, or SWIFT suppression of individual children;
- automatic gross splitting followed by release of all children;
- netting followed by automatic distribution and release of all children; and
- parent withdrawal after gross splitting or net-resultant automatic distribution.

The ASPIRE UAT source reports expected accounting-information generation for several gross-split cases. It does not define the accounting event model or establish that all jurisdictions share the same accounting acceptance criteria.

## Manual split lifecycle

According to the generated Cashflow Splitting source, a user initiates **Split Cashflow** from the cashflow blotter. The preview starts with the original amount. When the user enters a valid lower amount, RATAN creates a residual child; further edits can create additional residual children.

After submission, that source specifies the following behavior:

- The parent moves to `SPLIT`.
- Children return to the normal processing flow in NSTP with a `Split Cashflow` exception.
- Each child identifier has an `S` prefix and length 12, for example `S00123456789`.
- The parent and children are linked through `Splitting Id`, which must be visible and queryable in the blotter.
- A user may select an eligible counterparty SI for a child.
- **Split With Affirmation** creates affirmed children without a pending-affirmation exception.
- Split and split-amend actions require a single user; no checker and no authorization limit are required for the action itself.

The Cashflow Splitting UAT source also states that the parent moves to `SPLIT`, generated children share the parent’s splitting ID, and the children remain traceable from the parent cashflow details.

According to that UAT source, children may be released independently after a split. A released child generates SWIFT and sends accounting successfully. The parent remains the split-group record and retains its relationship to the children.

## Lineage and identifier evidence

The ASPIRE UAT examples use `M...` values for parents, `N...` values for net-resultant cashflows, and `S...` values for children. This is observed test-data usage rather than a confirmed identifier or lineage specification. The ASPIRE UAT source does not supply an authoritative parent-child correlation key.

This ASPIRE UAT limitation is distinct from the generated Cashflow Splitting source and Cashflow Splitting UAT source, which respectively specify a `Splitting Id` linkage and state that generated children share the parent’s splitting ID.

The netting-service design’s example also uses `N01` for a resultant and `S01`/`S02` for split children, with split ID `3333`; it does not establish that these values are an authoritative identifier or lineage convention.

Split processing is related to cashflow lineage and amendment correlation and split cashflow dvp handling. The ASPIRE UAT evidence is not DVP-specific and does not prove DVP behavior.

## Eligibility and action criteria

### FMRP cashflow-blotter criteria

The cashflow-blotter action source specifies the following eligibility criteria:

| Action | Eligibility |
| --- | --- |
| Split Cashflow | Cashflow is `WAITING` or `READY`; Netting Id and Splitting Id are empty; event type is `New`; original trade source is not loaniq; and settlement method is not `UTIL`. |
| Amend Split Amount | Cashflow is `WAITING`; event type is `New`; an existing Splitting Id is present; and settlement method is not `UTIL`. |
| Un-Split Cashflow | Cashflow is `New`; an existing Splitting Id is present; Splitting Id is not `RELEASED` or `SETTLED`; and settlement method is not `UTIL`. |

> [!note]
> The cashflow-blotter action source inconsistently spells the Split Cashflow netting criterion as `Netting Is`. The canonical field name remains unresolved.

### UAT eligibility and exclusions

The Cashflow Splitting UAT source states that manual splitting is supported for eligible gross cashflows in `WAITING` or `READY`, including tested Murex and Stella cashflows.

That source states that manual splitting is not available for:

- BCS or LOANIQ cashflows;
- IRS aggregation resultant cashflows;
- netting resultant cashflows; or
- existing split-child cashflows.

The UAT exclusions are not fully expressed in the cashflow-blotter action criteria. In particular, the cashflow-blotter source explicitly excludes original trade source loaniq, whereas the UAT source additionally names BCS cashflows, IRS aggregation resultant cashflows, netting resultant cashflows, and existing split children.

The generated Cashflow Splitting source identifies a contradiction in its source material regarding manual-split eligibility for netting and IRS aggregation resultants. This issue is tracked by is manual splitting of irs aggregation resultants in day 1 scope.

## Amend and unsplit

### Amend split amount

The generated Cashflow Splitting source states that a split-child amount may be amended only while eligible children are in `WAITING`, and at least two children must be in that state. Users can adjust amounts but cannot add or remove children. An amended child receives both `Split Cashflow` and `Split Amend` NSTP exceptions.

For allocation changes, see split amount amendment.

### Unsplit

The generated Cashflow Splitting source states that unsplit can be selected from a parent or child, but succeeds only when no child is `RELEASED`, `SETTLED`, or `NETTED`. A successful unsplit marks every child `DEAD`, reinstates the parent in `WAITING`, and applies an `Un-Split` exception.

The FMRP cashflow-blotter action source instead specifies that **Un-Split Cashflow** requires a cashflow with event type `New`, an existing Splitting Id that is not `RELEASED` or `SETTLED`, and a settlement method other than `UTIL`.

For reversal of an unreleased split, see cashflow unsplit.

## Split-related state indicators and NSTP handling

The settlement-day static source defines the following indicators:

- A **split child cashflow** has a non-null and non-empty `Cashflow__Splitting_Id`.
- An **amended split amount** is identified by `Cashflow__Is_Split_Amend_Amount == true`.
- An **unsplit cashflow** is identified by `Cashflow__Is_Cashflow_Unsplit == true`.
- A **withdrawal on split** is identified by `Cashflow__Is_Withdrawal_On_Split == true`.

That source proposes four new exception codes for split-related states:

| State | Condition | Exception code | Operation level | Bulk eligible |
| --- | --- | --- | --- | --- |
| Split child cashflow | `Cashflow__Splitting_Id != null && Cashflow__Splitting_Id != ""` | `Split Cashflow` | `MAKER_CHECKER` | No |
| Amended split amount | `Cashflow__Is_Split_Amend_Amount == true` | `Split Amend` | `MAKER_CHECKER` | No |
| Unsplit cashflow | `Cashflow__Is_Cashflow_Unsplit == true` | `Un-Split` | `MAKER_CHECKER` | No |
| Withdrawal on split | `Cashflow__Is_Withdrawal_On_Split == true` | `Withdrawal on Split` | `MAKER_CHECKER` | No |

These NSTP rules indicate that split-related events require controlled manual handling rather than bulk processing.

The settlement-day static source does not define precedence or mutual exclusivity among the four NSTP rules. A cashflow may potentially satisfy more than one condition. Track this issue in what is the precedence between split nstp rules.

## External lifecycle behavior

According to the generated Cashflow Splitting source:

- `SPLIT`, withdrawal-to-`SPLIT`, and unsplit are written back to Stella, but not Murex.
- A child reaching `RELEASED`, or reaching `SETTLED` without `RELEASED`, has specified Murex write-back behavior.
- `SPLIT` does not create accounting and must not transition to `FAILED`.
- A withdrawal received while the parent is `SPLIT` branches by child release status: unreleased children are cancelled, while a released child causes the withdrawal to be held in `WAITING` for manual action.
- An upstream trade undo received during `SPLIT` moves the new event to `ERROR`.

## Withdrawal and lifecycle gaps

The ASPIRE UAT source does not define lifecycle transitions, event ordering, child eligibility after withdrawal, or consequences for previously released children. The withdrawal contract is tracked in what is the authoritative split child lifecycle after parent withdrawal.

This absence of definition in the ASPIRE UAT source does not override the generated Cashflow Splitting source’s stated behavior for withdrawal while the parent is `SPLIT`.

The netting-service design likewise does not define failure recovery for its splitting representation.

## Relationship to netting and other processing

The settlement-day static source documents a rule-specific exclusion: a split child is excluded from the pending NDS auto-netting rule when `Cashflow__Splitting_Id` is non-null or non-empty. See split cashflow netting exclusion. That source states that this rule-specific exclusion is not evidence of a universal prohibition on netting split cashflows.

Separately, the Cashflow Splitting UAT source states that split children are excluded from manual netting and bypass manual netting, automatic netting, IRS check conditions, and NDS auto-netting rules. It describes this as preventing already-segmented payment flows from being re-aggregated or re-evaluated by unrelated netting paths.

The generated Cashflow Splitting source states that split children are governed by split child processing exclusions.

The netting-service design does not specify whether split outputs may later be re-netted. This is an unresolved design statement specific to that source and should not be treated as overriding the rule-specific NDS exclusion or the broader UAT exclusions.

## Versioning and non-economic amendments

The generated Cashflow Splitting source states that non-economic amend events are ignored when split children have been released or settled, or when the cashflow has a manual touch point. Otherwise, RATAN processes the latest version.
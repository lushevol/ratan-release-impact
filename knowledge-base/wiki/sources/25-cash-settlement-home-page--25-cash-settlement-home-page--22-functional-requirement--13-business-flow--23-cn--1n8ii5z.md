---
type: source
title: CN Cash Settlement Flow
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, business-flow, functional-requirement, cashflow-lifecycle, netting]
related: [cn-cashflow-lifecycle, cpn-manual-netting-workflow, cashflow-maker-checker-sub-statuses, stella, blade, cpn, should-post-release-cn-cashflow-amendments-use-reversal-swift-or-cancellation, can-cpn-netting-resultant-cashflows-be-suppressed, why-does-cn-cashflow-undo-transition-from-dead-to-validated, what-are-the-authoritative-cn-cashflow-and-technical-version-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
authors: []
year: 0
url: ""
venue: ""
---
# CN Cash Settlement Flow

This functional requirement specifies the intended CN cashflow lifecycle for flows from [[stella|STELLA]], Murex, and Razor. It covers booking, VD-5 queueing, NSTP validation, CPN manual netting, suppression, amendment, undo, cancellation, and replacement cashflows.

The document defines a standard route of `PROJECTED → QUEUED → PENDING → VALIDATED → RELEASED → SETTLED → NOSTRO MATCHED`. Within this route, publishing a SWIFT message to [[amh|AMH]] leads to `RELEASED`, and `AMH ACKED` leads to `SETTLED`. These are source-specific CN-flow requirements and do not establish a universal AMH contract.

Murex cashflows are described as having only the event `NEW`; other changes are treated as incremental cashflows. The document does not define their identifiers, correlation method, payload, or state rules.

## Business Processing Flow

| Transaction Action | Cashflow 1 Original Status | Cashflow 1 Event | Cashflow 1 Status | Cashflow 2 Event | Cashflow 2 Status |
| --- | --- | --- | --- | --- | --- |
| Book trade | PROJECTED | NEW | PROJECTED | NA |
| QUEUED | QUEUED |
| Undo/Cancel trade | PROJECTED | WITHDRAWAL | PROJECTED |
| QUEUED | QUEUED |
| PENDING | PENDING |
| VALIDATED | VALIDATED |
| RELEASED | WITHDRAWAL + CANCELLED | CANCELLED |
| SETTLED | CANCELLED |
| NOSTRO MATCHED | CANCELLED |
| Update trade | PROJECTED | AMEND | QUEUED |
| QUEUED | QUEUED |
| PENDING | QUEUED |
| VALIDATED | QUEUED |
| RELEASED | WITHDRAWAL | CANCELLED | NEW | PROJECTED |
| SETTLED | CANCELLED |
| NOSTRO MATCHED | CANCELLED | QUEUED |

The source matrix is structurally malformed: its continuation rows do not consistently match the six declared columns. It must not be treated as an authoritative formal transition matrix until normalized and confirmed by the source owner.

## Transaction Booking

| | Cashflow ID | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| 3 | C01 | PENDING | NA | 2 | 2 | Intermediate status when sub status is "NA" |
| 4 | C01 | VALIDATED | NA | 3 | 3 | Auto validation passed |
| 5 | C01 | RELEASED | NA | 4 | 4 | SWIFT message published to AMH |
| 6 | C01 | SETTLED | NA | 5 | 5 | AMH ACKED |
| 7 | C01 | NOSTRO MATCHED | NA | 6 | 6 | |

## NSTP Release Case

| Cashflow ID | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- |
| C01 | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| C01 | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| C01 | PENDING | Pending_Validation_Maker | 2 | 2 | **Hit the NSTP rule, waiting for Manual verification** |
| C01 | PENDING | Pending_Validation_Checker | 2 | 3 | **Maker released the cashflow** |
| C01 | VALIDATED | NA | 3 | 4 | **Checker confirmed the releasing** |
| C01 | RELEASED | NA | 4 | 5 | SWIFT message published to AMH |
| C01 | SETTLED | NA | 5 | 6 | AMH ACKED |
| C01 | NOSTRO MATCHED | NA | 6 | 7 | |

## CPN Case

| | Cashflow ID | Source | Status | Netting Id | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | STELLA | PROJECTED | | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | STELLA | QUEUED | | NA | 1 | 1 | On VD-5, Receive QUEUED cashflow from STELLA |
| 3 | C01 | STELLA | PENDING | | Pending_Netting_Maker | 2 | 2 | CPN eligible, hold the cashflow for manual netting |
| 4 | C02 | MUREX | PROJECTED | | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 5 | C02 | MUREX | QUEUED | | NA | 1 | 1 | On VD-5, Move Murex cashflows from PROJECTED to QUEUED |
| 6 | C02 | MUREX | PENDING | | Pending_Netting_Maker | 2 | 2 | CPN eligible, hold the cashflow for manual netting |
| 7 | C01 | STELLA | NETTED | Net001 | NA | 3 | 3 | **Maker netted the cashflow C01 and C02** 1. **NETTED cashflow will be received from STELLA for C01** 2. **CS Platform need to move C02 to NETTED status** 3. **CS Platform generates C03 as netted cashflow** |
| 8 | C02 | MUREX | NETTED | Net001 | NA | 3 | 3 |
| 9 | C03 | CPN | QUEUED | Net001 | NA | 0 | 0 |
| 10 | C03 | CPN | PENDING | Net001 | Pending_Netting_Checker | 1 | 1 | Hold the netted cashflow for verification |
| 11 | C03 | CPN | VALIDATED | Net001 | NA | 2 | 2 | Continue the rest of the status update |

## Suppression Case

Doable for status:  [lyn question: doable for netting rresultant flow?]

1. PROJECTED
2. QUEUED
3. PENDING
4. VALIDATED

| | Cashflow ID | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| 3 | C01 | PENDING | NA | 2 | 2 | Intermediate status when sub status is "NA" |
| 4 | C01 | VALIDATED | NA | 3 | 3 | Auto validation passed |
| 5 | C01 | PENDING | Pending_Suppression_Checker | 4 | 4 | Maker manually suppress the cashflow |
| 6 | C01 | SUPPRESSED | NA | 5 | 5 | Checker confirmed the suppression |

## Transaction Amend/Undo on PROJECTED/QUEUED/PENDING/VALIDATED

| | Cashflow ID | Event | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | NEW | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | NEW | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| 3 | C01 | NEW | PENDING | NA | 2 | 2 | Intermediate status when sub status is "NA" |
| 4 | C01 | NEW | VALIDATED | NA | 3 | 3 | Auto validation passed |
| 5 | C01 | AMEND | PENDING | NA | 4 | 4 | **Transaction Update by FO from Blade, a withdraw will be consumed** |
| 6 | C01 | AMEND | VALIDATED | NA | 5 | 5 | |

| | Cashflow ID | Event | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | NEW | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | NEW | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| 3 | C01 | NEW | PENDING | NA | 2 | 2 | Intermediate status when sub status is "NA" |
| 4 | C01 | NEW | VALIDATED | NA | 3 | 3 | Auto validation passed |
| 5 | C01 | WITHDRAWAL | DEAD | NA | 4 | 4 | **Transaction Undo by FO from Blade, a withdraw will be consumed** |
| 6 | C01 | WITHDRAWAL | VALIDATED | NA | 5 | 5 | |

## Transaction Amend on RELEASED/SETTLED/NOSTRO MATCHED

Cashflow withdraw & new will only be consumed from STELLA, which means FO/MO amend a transaction to cancel the cashflow and generate a new cashflow.

Open questions:

1. When SWIFT already released, which one preferred from settlement ops: 1. Reversal SWIFT to be released 2. Cancellation

| | Cashflow ID | Event | Status | Sub-Status | Cashflow Version | Technical Version | Trigger point |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C01 | NEW | PROJECTED | NA | 0 | 0 | Flow from STELLA or Murex or Razor |
| 2 | C01 | NEW | QUEUED | NA | 1 | 1 | On VD-5, 1. Receive QUEUED cashflow from STELLA 2. Move Murex cashflows from PROJECTED to QUEUED |
| 3 | C01 | NEW | PENDING | NA | 2 | 2 | Intermediate status when sub status is "NA" |
| 4 | C01 | NEW | VALIDATED | NA | 3 | 3 | Auto validation passed |
| 5 | C01 | NEW | RELEASED | NA | 4 | 4 | |
| 6 | C01 | WITHDRAWAL | CANCELLED | NA | 4 | 4 | **Transaction Amend by MO from Blade, a withdraw&new will be consumed** |
| 7 | C02 | NEW | QUEUED | NA | 0 | 0 | |
| 8 | C02 | NEW | PENDING | Pending_Linked_Withdrawal_Done | 1 | 1 | Hold until the withdrawal done |
| 9 | C02 | NEW | VALIDATED | NA | 2 | 2 | **Auto validation passed** **Withdrawal done** |
| 10 | C02 | NEW | RELEASED | NA | 3 | 3 | SWIFT message published to AMH |
| 11 | C02 | NEW | SETTLED | NA | 4 | 4 | AMH ACKED |
| 12 | C02 | NEW | NOSTRO MATCHED | NA | 5 | 5 | |

## Known Gaps

- The `DEAD → VALIDATED` transition in the undo example requires clarification.
- It is not confirmed whether a CPN resultant cashflow can be suppressed.
- The required operational response to an amendment after SWIFT release remains undecided: reversal SWIFT or cancellation.
- The table groups `RELEASED`, `SETTLED`, and `NOSTRO MATCHED`, but illustrates the withdrawal-and-replacement process only from `RELEASED`.
- Cashflow-version and technical-version increment rules are not specified universally.
---

---FILE: wiki/entities/stella.md---
---
type: entity
title: STELLA
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, upstream-system, cashflow]
related: [cn-cashflow-lifecycle, cpn-manual-netting-workflow, cashflow-maker-checker-sub-statuses, blade]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# STELLA

STELLA is an upstream cashflow source in the CN cash-settlement flow.

The source specifies that STELLA supplies `QUEUED` cashflows on VD-5. For CPN manual netting, STELLA supplies the `NETTED` update for its constituent cashflow. For post-release amendments, only STELLA supplies the withdrawal-and-new cashflow pair.

These statements describe the CN functional flow only and do not define STELLA behavior in other settlement routes.
---

---FILE: wiki/entities/blade.md---
---
type: entity
title: Blade
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, transaction-interface, front-office, middle-office]
related: [cn-cashflow-lifecycle, cashflow-maker-checker-sub-statuses, should-post-release-cn-cashflow-amendments-use-reversal-swift-or-cancellation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# Blade

Blade is the FO/MO transaction interface named as the trigger for cashflow amendments and undo actions in the CN cash-settlement flow.

An FO transaction update triggers the early-lifecycle amend scenario. An FO undo triggers a withdrawal scenario. An MO amendment after release triggers consumption of a STELLA withdrawal-and-new pair, cancellation of the original cashflow, and creation of a linked replacement cashflow.
---

---FILE: wiki/entities/cpn.md---
---
type: entity
title: CPN
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, netting, cashflow-source]
related: [cpn-manual-netting-workflow, cashflow-maker-checker-sub-statuses, can-cpn-netting-resultant-cashflows-be-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# CPN

CPN is the source/category assigned to a resultant cashflow generated by the CS Platform during CN manual netting.

A CPN resultant begins at `QUEUED` with a `Netting Id`, enters `PENDING / Pending_Netting_Checker` for verification, and becomes `VALIDATED` after checker processing. The source does not explicitly define the resultant's lifecycle after validation or whether it may be suppressed.
---

---FILE: wiki/concepts/cn-cashflow-lifecycle.md---
---
type: concept
title: CN Cashflow Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, cashflow, lifecycle, swift, amh]
related: [cashflow-maker-checker-sub-statuses, cpn-manual-netting-workflow, swift-status-lifecycle-and-reconciliation, source-system-based-nstp, stella, blade, amh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# CN Cashflow Lifecycle

The CN functional requirement defines the standard cashflow business-status progression:

`PROJECTED → QUEUED → PENDING → VALIDATED → RELEASED → SETTLED → NOSTRO MATCHED`

## Entry and release

- A flow from STELLA, Murex, or Razor is initially `PROJECTED`.
- On VD-5, STELLA `QUEUED` cashflows are received and Murex cashflows move from `PROJECTED` to `QUEUED`.
- `PENDING` is the intermediate state where the sub-status is `NA` in the standard flow.
- Automatic validation moves a cashflow to `VALIDATED`.
- SWIFT publication to [[amh|AMH]] moves a cashflow to `RELEASED`.
- `AMH ACKED` moves a cashflow to `SETTLED`.
- `NOSTRO MATCHED` follows settlement.

## Versions

The model distinguishes a business-facing `Cashflow Version` from a `Technical Version`. Standard automatic lifecycle progression increments both counters together. In NSTP maker-checker processing, the technical counter increments when the maker releases the flow while the cashflow counter remains unchanged until checker validation.

The source does not establish whether that distinction applies consistently to netting, suppression, cancellation, or all manual actions. This remains tracked in [[what-are-the-authoritative-cn-cashflow-and-technical-version-rules]].

## Amendments and replacement

Before release, amendments and withdrawals are illustrated as changes to the existing cashflow. After release, the flow is cancellation plus replacement: the original is cancelled and the new cashflow remains in `Pending_Linked_Withdrawal_Done` until the withdrawal completes.

The source does not fully establish whether the same treatment is allowed after `SETTLED` or `NOSTRO MATCHED`.
---

---FILE: wiki/concepts/cpn-manual-netting-workflow.md---
---
type: concept
title: CPN Manual Netting Workflow
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, cpn, manual-netting, maker-checker]
related: [cn-cashflow-lifecycle, cashflow-maker-checker-sub-statuses, cpn, stella, auto-netting-job, lien-aware-netting-and-auto-unnetting, can-cpn-netting-resultant-cashflows-be-suppressed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# CPN Manual Netting Workflow

CPN manual netting is a CN-specific multi-cashflow workflow. It must not be conflated with the mechanisms documented in [[auto-netting-job]] or [[lien-aware-netting-and-auto-unnetting]].

## Constituent flows

CPN-eligible constituent cashflows from STELLA and Murex move to:

`PENDING / Pending_Netting_Maker`

When the maker nets the constituent cashflows:

1. STELLA supplies a `NETTED` update for its constituent flow.
2. The CS Platform moves the Murex constituent flow to `NETTED`.
3. Both flows share a `Netting Id`.
4. The CS Platform generates a new resultant cashflow whose source is [[cpn|CPN]].

## Resultant flow

The CPN resultant enters `QUEUED` at cashflow and technical version `0`, retaining the `Netting Id`. It then enters:

`PENDING / Pending_Netting_Checker → VALIDATED`

The requirement only says to continue the remaining status updates after validation; it does not explicitly specify the resultant's later release, settlement, and reconciliation behavior.

Whether suppression is allowed for a CPN resultant is an unresolved source question tracked in [[can-cpn-netting-resultant-cashflows-be-suppressed]].
---

---FILE: wiki/concepts/cashflow-maker-checker-sub-statuses.md---
---
type: concept
title: Cashflow Maker-Checker Sub-Statuses
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, maker-checker, validation, netting, suppression]
related: [cn-cashflow-lifecycle, cpn-manual-netting-workflow, source-system-based-nstp, should-post-release-cn-cashflow-amendments-use-reversal-swift-or-cancellation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# Cashflow Maker-Checker Sub-Statuses

The CN cashflow flow uses the `PENDING` business status with specialized sub-statuses to expose manual-control dependencies.

## Validation controls

For an NSTP-eligible cashflow, the route is:

`Pending_Validation_Maker → Pending_Validation_Checker → VALIDATED`

The maker release increments only `Technical Version` in the illustrated case. Checker confirmation moves the business status to `VALIDATED` and increments both business and technical versions relative to the maker stage.

## Netting controls

CPN-eligible constituent cashflows are held at:

`Pending_Netting_Maker`

The generated CPN resultant is held for verification at:

`Pending_Netting_Checker`

## Suppression controls

A maker manually suppresses an otherwise `VALIDATED` cashflow by moving it to:

`PENDING / Pending_Suppression_Checker`

Checker confirmation moves it to `SUPPRESSED`.

## Linked withdrawal dependency

A replacement cashflow generated following a post-release amendment is held at:

`PENDING / Pending_Linked_Withdrawal_Done`

It may move to `VALIDATED` only after both automatic validation and completion of the linked withdrawal.

The source does not define universal version-counter rules for every sub-status transition.
---

---FILE: wiki/queries/should-post-release-cn-cashflow-amendments-use-reversal-swift-or-cancellation.md---
---
type: query
title: Should Post-Release CN Cashflow Amendments Use Reversal SWIFT or Cancellation?
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, amendment, swift, cancellation, reversal, decision-needed]
related: [cn-cashflow-lifecycle, cashflow-maker-checker-sub-statuses, stella, blade, amh, swift-status-lifecycle-and-reconciliation, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# Should Post-Release CN Cashflow Amendments Use Reversal SWIFT or Cancellation?

## Question

When an amendment is received after a CN cashflow has reached `RELEASED` and its SWIFT message has been published, should the operational response be a reversal SWIFT message or cancellation?

## Evidence

The source explicitly asks [[settlement-ops|Settlement Ops]] to choose between releasing a reversal SWIFT and cancellation. Its illustrated workflow cancels the released original cashflow and creates a replacement that waits for linked-withdrawal completion.

## Why it matters

The decision affects payment risk, message reconciliation, operational workload, and the replacement cashflow's release timing. The document does not establish whether the same procedure is valid after `SETTLED` or `NOSTRO MATCHED`.

## Needed resolution

Settlement Ops should define the approved disposition by original status (`RELEASED`, `SETTLED`, and `NOSTRO MATCHED`), including message, accounting, reconciliation, and audit requirements.
---

---FILE: wiki/queries/can-cpn-netting-resultant-cashflows-be-suppressed.md---
---
type: query
title: Can CPN Netting Resultant Cashflows Be Suppressed?
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, cpn, netting, suppression, open-question]
related: [cpn-manual-netting-workflow, cashflow-maker-checker-sub-statuses, cpn, cn-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# Can CPN Netting Resultant Cashflows Be Suppressed?

## Question

Is manual suppression supported for a CPN netting resultant cashflow?

## Evidence

The suppression section explicitly asks whether suppression is possible for a “netting rresultant flow.” It lists `PROJECTED`, `QUEUED`, `PENDING`, and `VALIDATED` as statuses where suppression is doable, but the worked scenario only performs maker suppression from `VALIDATED`.

A CPN resultant reaches `VALIDATED` after `Pending_Netting_Checker`, which makes the scope ambiguity material.

## Needed resolution

Confirm eligibility by cashflow source and status, including whether a CPN resultant can enter `Pending_Suppression_Checker` and how suppression affects its constituent cashflows and `Netting Id`.
---

---FILE: wiki/queries/why-does-cn-cashflow-undo-transition-from-dead-to-validated.md---
---
type: query
title: Why Does CN Cashflow Undo Transition from DEAD to VALIDATED?
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, undo, withdrawal, dead, validated, data-quality]
related: [cn-cashflow-lifecycle, blade, cashflow-maker-checker-sub-statuses]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# Why Does CN Cashflow Undo Transition from DEAD to VALIDATED?

## Question

Does the illustrated undo transition from `DEAD` to `VALIDATED`, retaining the `WITHDRAWAL` event and the same cashflow identifier, represent an intended rule or a documentation defect?

## Evidence

In the pre-release undo scenario, a Blade-triggered withdrawal moves the cashflow to `DEAD` at version 4, followed by `VALIDATED` at version 5. No trigger, replacement identifier, or explanatory rule is supplied for the latter transition.

## Needed resolution

Confirm the valid terminal and recovery behavior for withdrawn cashflows. If revalidation represents a replacement cashflow, define its identifier, event type, linkage, and versioning semantics.
---

---FILE: wiki/queries/what-are-the-authoritative-cn-cashflow-and-technical-version-rules.md---
---
type: query
title: What Are the Authoritative CN Cashflow and Technical Version Rules?
created: 2026-08-23
updated: 2026-08-23
tags: [cn, cash-settlement, versioning, maker-checker, netting, suppression, open-question]
related: [cn-cashflow-lifecycle, cashflow-maker-checker-sub-statuses, cpn-manual-netting-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Business Flow/CN Cash Settlement Flow.md"]
---
# What Are the Authoritative CN Cashflow and Technical Version Rules?

## Question

What are the authoritative increment rules for `Cashflow Version` and `Technical Version` across CN cashflow processing?

## Evidence

The standard lifecycle increments both version counters together. The NSTP scenario separates them: a maker action advances `Technical Version` while retaining the same `Cashflow Version`; checker validation then advances the cashflow version.

The source gives examples for netting, suppression, amendment, withdrawal, cancellation, and replacement, but does not state a common rule that explains all cases.

## Needed resolution

Define a transition-level version policy for automatic processing, maker actions, checker actions, netting constituents, CPN resultants, suppression, amendments, withdrawals, cancellation, and replacement cashflows.
---

---FILE: wiki/log.md---
## 2026-08-23 ingest | CN Cash Settlement Flow

- Ingested the CN cash-settlement functional flow, including lifecycle, maker-checker, CPN netting, and amendment-control requirements.
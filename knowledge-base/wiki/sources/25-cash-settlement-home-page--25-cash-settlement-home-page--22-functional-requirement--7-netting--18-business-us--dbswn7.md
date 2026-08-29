---
type: source
title: Cash Settlement Home Page Bilateral Netting Business User Case
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, bilateral-netting, functional-requirement, acceptance-criteria]
related: [bilateral-netting, bilateral-netting-eligibility, netting-resultant-cashflow-lifecycle, netting-withdrawal-timing, netting-exception-recovery, netting-static-blotter, ccil, cashflow-blotter, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Cash Settlement Home Page Bilateral Netting Business User Case

## Scope

This functional requirement defines manual bilateral netting in the Cash Settlement Home Page. It covers eligibility rules, resultant cashflow creation, maker-checker processing, manual and automatic un-netting, withdrawal timing, and recovery from selected exception states.

The source includes acceptance criteria and case notes. Referenced screenshots are preserved as source references, but their contents are not machine-readable in the source text.

## Core workflow

A user creates a live manual netting rule in the [[netting-static-blotter]], selects eligible cashflows in the cashflow blotter, and submits the netting operation. Component cashflows initially have:

- `state = 'WAITING'`
- `cashflow sub state type = 'Pending Netting'`

After successful processing, components become `NETTED` and a resultant cashflow is generated with:

- `Affirmation status = 'Affirmed'`
- Correct amount
- `Payment type = 'Bilateral Netting'`
- `NSTP process complete (MAKER_CHECKER)`

The resultant cashflow is then released from [[ratan]] by Ops.

## Acceptance criteria

| AC-NO | Function / scenario | Expected result |
|---|---|---|
| `AC-Settlement-Manual Netting-001` | Generic bilateral netting | A live manual rule permits eligible C1/C2 cashflows to become `NETTED`; N1 is generated with affirmed status, correct amount, bilateral-netting payment type, and completed maker-checker NSTP; N1 is released from Ratan. |
| `AC-Settlement-Manual Netting-002` | Guaranteed CCIL bilateral netting | Cashflows with `Settlement Method = CCIL` and `Counterparty FMID=400021949` are netted into an affirmed bilateral-netting resultant with completed maker-checker NSTP. |
| `AC-Settlement-Manual Netting-003` | Manual un-net | Selecting `Un-Net Cashflow` displays component details. Selecting `Un-Net all Cashflow` changes N1 to `DEAD` and restores C1/C2 to `WAITING / Pending Netting`. |
| `AC-Settlement-Manual Netting-004` | Different netting key | Netting is rejected when booking entity, counterparty, value date, or currency differs. |
| `AC-Settlement-Manual Netting-005` | Released or settled status | Netting is rejected for cashflows in `Released` or `Settled` state. |
| `AC-Settlement-Manual Netting-006` | Withdrawal before netting | C1 becomes `CANCELLED`; C2/C3 can be netted into N1, which is released from Ratan. |
| `AC-Settlement-Manual Netting-007` | Withdrawal after netting while resultant is not final | The system automatically un-nets N1 and marks it `DEAD`; C1 becomes `CANCELLED`; C2/C3 return to `WAITING / Pending Netting`; C2/C3 can be netted into N2, which is released from Ratan. |
| `AC-Settlement-Manual Netting-008` | Withdrawal after resultant is settled or released | N1 remains `SETTLED` or `RELEASED`; C1 is `WAITING`; C2 remains `NETTED`. |
| ~~`AC-Settlement-Manual Netting-008`~~ | ~~Manual netting refresh — disable or update existing rule~~ | ~~Struck through and marked `Confirm`; not an active acceptance criterion.~~ |
| `AC-Settlement-Manual Netting-009` | Pending Netting — Manual Fail-Reinstate | C1 transitions from `FAIL / NA` to `WAITING / Pending Netting`; C1/C2/C3 can then be netted into N1, which is released from Ratan. |
| `AC-Settlement-Manual Netting-010` | Pending Netting — Settle As Gross | C1 becomes `WAITING / Pending Exception` with `Settlement Method='Gross'`; C2/C3 can be netted into N1. |
| `AC-Settlement-Manual Netting-011` | Pending Netting — Hold/Unhold | C1/C2/C3 transition to `Hold / NA` and then return to `WAITING / Pending Netting`; they can subsequently be netted. |
| `AC-Settlement-Manual Netting-012` | Pending Netting — Swift Suppression | Rejection of Swift Suppression returns C1/C2/C3 from `WAITING / Swift Suppression` to `WAITING / Pending Netting`; they can subsequently be netted. |
| `AC-Settlement-Manual Netting-013` | Pending Netting — Suppress Cashflow | Rejection of Cashflow Suppression returns C1/C2/C3 from `WAITING / Cashflow Suppression` to `WAITING / Pending Netting`; they can subsequently be netted. |

## Validation message

For mismatched eligibility attributes, the source specifies:

> `Validation failed ,Cash flow selected are not eligible for netting as either the same booking entity, counterparty,value date,currency`

For released or settled selected cashflows, it specifies:

> `Validation failed ,Netting is not allowed on 'Released'/'Settled' cashflow.`

## Case notes

The source includes the following identifiers:

```text
N00000003228,M01750907483,M01750907477
```

One case note records withdrawal of:

```text
M01750907477
```

A second case note describes a `READY + Pending Ack` scenario, a released resultant cashflow, and withdrawal of one component cashflow.

## Limitations and unresolved points

The source does not define:

- The formula for determining the “correct” resultant amount.
- Whether `RELEASED` and `SETTLED` have identical financial finality.
- The accounting or reversal treatment when a component is withdrawn after the resultant is released or settled.
- Audit, authorization, or lineage details for automatic un-netting.
- Whether `Counterparty FMID=400021949` is mandatory for all CCIL netting.
- The behavior when a live netting rule is disabled or updated after cashflows enter `Pending Netting`.

The duplicate `AC-Settlement-Manual Netting-008` identifier should be corrected in the acceptance suite.

## Related pages

- [[bilateral-netting]]
- [[bilateral-netting-eligibility]]
- [[netting-resultant-cashflow-lifecycle]]
- [[netting-withdrawal-timing]]
- [[netting-exception-recovery]]
- manual and automatic netting un netting
- what happens when a component is withdrawn after resultant settlement
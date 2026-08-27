---
type: concept
title: Cashflow Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, netting, settlement, cash-settlement, cashflows, aggregation]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--7-netting--18-business-us--b1wlmm, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--26-n--18p25vy, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity, netting-service, resultant-cashflow-generation, netting-eligibility, cashflow-unnetting, maker-checker-netting, irs-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Cashflow Netting

Cashflow netting is a settlement-processing capability that may offset eligible obligations into a net payment or resultant cashflow. The technical design describes it as combining eligible component cashflows into an aggregate resultant cashflow.

## Documented Technical Design

According to the Netting Service technical design:

- Component amounts are summed to produce an aggregate resultant cashflow.
- Components are marked `NETTED`.
- Components may move from `Pending`, `Validated`, `Queued`, or `Projected` to `Netted`.
- A resultant cashflow is generated after netting, with the Definition of Done specifying an initial status of `Queued`.
- Netting operations are grouped using a netting identifier.
- Netting requires validation, maker/checker approval, eligibility checks, and status write-back to STELLA.

### Example Aggregations

The examples in the technical design include:

| Component | Amount |
|---|---:|
| `C01` | `100` |
| `C02` | `200` |
| `C03` | `400` |

The documented resultants are:

- `300` for `C01 + C02`
- `700` for `C01 + C02 + C03`

The technical design distinguishes IRS aggregation from bilateral netting. Their eligibility and lifecycle rules should therefore not be assumed to be identical.

## Evidence Boundary

The available Functional Requirement source is named as a Netting business-user-case requirement, but its body is unavailable. That source does not establish the following for this capability:

- eligibility criteria or grouping keys;
- whether netting is manual, automatic, scheduled, or event-driven;
- permitted cashflow statuses;
- cross-currency, counterparty, or settlement-date constraints;
- original-to-resultant identity and lineage;
- netting, un-netting, reversal, or re-netting transitions;
- authorization, maker/checker, audit, accounting, reconciliation, or exception controls.

The technical design documents validation, maker/checker approval, eligibility checks, status write-back to STELLA, component statuses, and resultant status as described above. It does not resolve every aspect of the broader lifecycle or control model.

The deprecated [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--26-n--18p25vy]] reference may contain historical requirements, but it is not validated by the Functional Requirement source.

## Unresolved Design Questions

The technical design leaves the authoritative state machine, partial-success behavior, idempotency rules, and concurrency controls unresolved. See [[what-is-the-authoritative-netting-state-machine]].

[[what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]] tracks the canonical status terminology and identity model for netting-related cashflows.
---
type: concept
title: TIS Cashflow Eligibility Rules
tags: [tis, cashflow, eligibility, settlement, reversal, fmid]
related: [tis, withdrawal-cashflow-query-exclusion, ratan-accounting-status-lifecycle, authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TIS.md"]
---
# TIS Cashflow Eligibility Rules

The RATAN–TIS interface source states an intended set of cashflow criteria for [[tis|TIS]] consumption:

| Criterion | Exact stated value |
|---|---|
| Cashflow status | `'Released' or 'Settled' cashflow` |
| Settlement means | `STTL_MEANS = NOX` |
| Reversal condition | `No reversal event` |
| Entity scope | `FMID: 10036645` |

## Interpretation limits

The source presents these items as a scope list but does not define their executable semantics. In particular, it does not confirm:

- whether all four criteria are mandatory conjunctive predicates;
- the authoritative system, table, or event stream for status, `STTL_MEANS`, reversal, and FMID;
- the legal entity or business unit represented by `FMID: 10036645`;
- the exact event or field that determines whether a reversal has occurred.

The stated withdrawal exclusion describes withdrawals as `Settled` with a `Reversed/Reversal` flag. This suggests that the no-reversal condition may exclude withdrawals even though `Settled` is otherwise listed as eligible, but that conclusion is an inference rather than a formal rule.

These are a TIS-specific consumer scope, not evidence of a RATAN-wide lifecycle definition. Related lifecycle ownership remains open in [[authoritative-cashflow-lifecycle-and-system-owners-2026-08-24-104403]].
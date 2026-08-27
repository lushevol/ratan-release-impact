---
type: concept
title: Netting Withdrawal Timing
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, netting, withdrawal, cancellation, settlement-finality]
related: [bilateral-netting, netting-resultant-cashflow-lifecycle, what-happens-when-a-component-is-withdrawn-after-resultant-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Netting Withdrawal Timing

The effect of withdrawing a component depends on when the withdrawal occurs relative to netting and resultant finality.

## Before netting

When C1 is withdrawn before netting:

```text
C1: CANCELLED
C2, C3: remain eligible and become NETTED
N1: generated as a Bilateral Netting resultant
```

The resultant is subsequently released from [[ratan]].

## After netting but before release or settlement

When C1 is withdrawn while N1 is neither `SETTLED` nor `RELEASED`:

```text
N1: DEAD
C1: CANCELLED
C2, C3: WAITING / Pending Netting
```

C2 and C3 can be netted again to create N2, which is released from Ratan.

## After release or settlement

When C1 is withdrawn after N1 becomes `SETTLED` or `RELEASED`:

```text
N1: remains SETTLED or RELEASED
C1: WAITING
C2: NETTED
```

The source does not state whether the resultant is financially adjusted, reversed, or replaced. It also does not explain how the component relationship is represented in audit history.

## Operational significance

The transition before finality is an automatic un-netting rule. The transition after finality is a separate behavior and should not be generalized without resolving the associated accounting and lineage questions.
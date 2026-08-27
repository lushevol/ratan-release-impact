---
type: concept
title: Cashflow Netting and Un-Netting State Transitions
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, netting, un-netting, settlement-status, ratan, withdrawal, resultant]
related: [ratan, cashflow-blotter, lien-aware-netting-and-auto-unnetting, what-are-the-netting-eligibility-and-netting-id-rules-for-cn-cashflows, cashflow-netting-and-un-netting, cashflow-withdrawal-and-new, cashflow-event-versioning, fmsre]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 17.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Cashflow Events Control Draft 1.md"]
---
# Cashflow Netting and Un-Netting State Transitions

The Sprint 17 CN settlement cases define the expected non-lien netting and GUI un-netting lifecycle in [[ratan]]. A deprecated cashflow-events draft separately proposes withdrawal-driven automatic un-netting behavior, including branches based on whether the resultant remains in Ratan.

## Netting

According to the Sprint 17 CN settlement cases, when netting is initiated from [[cashflow-blotter]]:

- each component cashflow must move to `Netted`;
- a resultant cashflow must be created as `Queued`;
- the resultant amount must equal the sum of component cashflow amounts;
- components and resultant must have the same Netting ID.

## GUI Un-Netting

According to the Sprint 17 CN settlement cases, when un-netting is performed through the GUI:

- each component cashflow must return to `Queued`;
- the resultant cashflow must move to `Dead`.

Moving the resultant to `Dead`, rather than deleting it, preserves an operational trace of the netting reversal.

## Withdrawal-Driven Automatic Un-Netting Proposal

The deprecated cashflow-events draft extends the netting model with withdrawal-driven automatic un-netting. These proposed flows are distinct from the Sprint 17 GUI un-netting criteria.

### Component Withdrawal

For a netting set containing components `C101`, `C102`, and `C103` and resultant `N101`, the deprecated draft proposes that withdrawal of `C101` produces:

```text
C101: PROJECTED -> CANCELLED
C102: PROJECTED -> QUEUED -> WAITING -> NETTED -> QUEUED -> WAITING
C103: PROJECTED -> QUEUED -> WAITING -> NETTED -> QUEUED -> WAITING
```

Under this proposal, the surviving components return to a pre-netting processing state.

### Resultant Remains in Ratan

If `N101` remains in Ratan, the deprecated draft proposes:

```text
N101: QUEUED -> WAITING -> DEAD
```

This closes the resultant lifecycle while the surviving components are reprocessed.

### Resultant Outside Ratan

If the resultant is outside Ratan, the deprecated draft proposes a different branch:

- Ratan generates a withdrawal event for `N101` with an updated business version.
- Operations checks the status in [[fmsre]].
- Operations may manually release the resultant.
- `MT192`/`MT202` may be required.
- Replacement or surviving cashflows may remain in NSTP while reversal processing is pending.

These steps are not confirmed current operational requirements. The draft does not define “outside Ratan,” which may refer to multiple operational conditions.

## Scope Boundaries and Open Questions

The Sprint 17 source does not mention liens. Its criteria are related to, but do not redefine, [[lien-aware-netting-and-auto-unnetting]]. It also does not define netting eligibility, signed amount treatment, Netting ID generation, concurrency, or atomicity.

The deprecated draft does not resolve the authoritative netting arithmetic, sign convention, resultant correlation, partial processing behavior, or financial treatment of a resultant that has already been released or settled.
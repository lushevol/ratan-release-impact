---
type: concept
title: Settlements BRP Prioritization
created: 2026-08-22
updated: 2026-08-22
tags: [BRP, prioritization, settlements, MoSCoW, delivery-risk, portfolio-management]
related: [settlements-brp-prioritization, strategic-cash-settlements, uk-strategic-cash-settlements-rollout, auto-netting-rule-check]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md"]
---
# Settlements BRP Prioritization

Settlements BRP prioritization is a portfolio-management view for ranking Strategic Cash Settlements backlog items against business priority, delivery risk, backlog state, definition of done, and delivery timing.

The source tracker uses MoSCoW-like values: `M` for Must, `S` for Should, `?` for unresolved priority, `N` in one apparent not-committed row, and blank values where classification is absent or cannot be reconstructed. It also uses an `At Risk` field and a DoD indicator, but does not define their timing or semantics.

## Use in the source

The tracker combines:

- delivery streams such as UK Go Live, UK Phase 2, Prime Migration, and Drop 4 LNBR;
- systems including RATAN, Murex 2.11, FMSGW, and Stella;
- ADO identifiers and backlog status;
- deliverables and comments;
- release dates, pending work, scope questions, and capacity constraints.

## Interpretation

This is a planning and status artifact, not a normalized delivery database. The rendered table contains rows that appear shifted relative to the header. Historical risk, current risk, and post-delivery risk are not distinguished. A `DoD = Y` value and a release comment provide reported completion evidence, but do not substitute for release records or UAT evidence.

The UK portfolio is the principal focus and combines operational controls—such as payment filtering, cashflow suppression, timing windows, fixing flags, and rollback—with strategic settlement capabilities. [[settlement-day-2]] and [[cashflow-netting-renetting]] provide related operational context.

## Open governance questions

The authoritative meaning of `At Risk`, `N`, blank MoSCoW values, and `DoD = Y` should be confirmed. The tracker should also be reconciled with ADO and release records before it is used for delivery reporting.
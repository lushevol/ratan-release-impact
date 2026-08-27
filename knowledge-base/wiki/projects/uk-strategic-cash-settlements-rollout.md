---
type: project
title: UK Strategic Cash Settlements Rollout
status: active
owner: ""
start_date: 2024-01-01
target_date: 2025-01-31
created: 2026-08-22
updated: 2026-08-22
tags: [UK, strategic-cash-settlements, RATAN, Murex, FMSGW, rollout]
related: [settlements-brp-prioritization, ratan, murex, settlement-day-2, waiting-fixing-flag, uk-cnh-ebbs-currency-preservation, automated-settlement-rollback, settlement-suppression-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md"]
---
# UK Strategic Cash Settlements Rollout

## Scope

The rollout covers UK go-live and January Phase 2 work across RATAN, Murex 2.11, and FMSGW. Scope includes Green Zone timing, BIC static data, cash-local-agent account prefixes, CNH preservation in eBBS, FMCODE reporting, Waiting Fixing Flag handling, zero-amount suppression, UK NDS exclusion from auto-netting, CPN retention, payment filtering, rollback, RFR, Swap Agent, LIEN, and pending-fixing processing.

## Reported status

The tracker reports several UK items as released, including BIC normalization, cash-local-agent prefixes, and CNH handling. Other items were in analysis, pending, or planned for January 2025. The UK Vostro SI requirement and MAIN BIC logic were marked as descoped; the Vostro SI item followed 12 failures during two weeks of data testing.

## Dependencies and risks

Murex 2.11 and FMSGW are named for upstream or UAT activities. RATAN is the strategic settlement platform. LIEN processing requires a TDS3 dependency. The tracker does not identify dependency owners or resolution dates.

The repeated `At Risk = Y` values show portfolio exposure, but the tracker does not clarify whether risk was historical, current, or unresolved at publication.

## Success evidence

The source provides release comments and planned dates, but no consolidated UAT evidence, production metrics, rollback test results, or validated evidence for the claimed “1 FTE Save from Ops side.”
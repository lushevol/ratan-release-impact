---
type: query
title: Is EBBS Feeding EOD by Entity, Realtime per Payment, or Both?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, ebbs, eod, realtime, accounting]
related: [ebbs, entity-based-eod-feeding, single-payment-realtime-accounting-feeding, cashflow-accounting-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Is EBBS Feeding EOD by Entity, Realtime per Payment, or Both?

## Question

Should EBBS receive accounting data through entity-based end-of-day feeds, single-payment realtime feeds, or both?

## Evidence

The function breakdown describes EOD integration and EOD feeding. A separate section titled `EBBS feeding approach` lists both an EOD approach by entity and realtime feeding by single payment.

## Resolution Needed

The design must identify whether the approaches are alternatives or complementary, define their applicability by payment population, and specify precedence, fallback, acknowledgement, retry, and reconciliation behavior.

---
type: concept
title: Waiting Fixing Flag
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, fixing, payment-status, RATAN, Murex, UK]
related: [ratan, murex, settlement-day-2, uk-strategic-cash-settlements-rollout]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md"]
---
# Waiting Fixing Flag

The Waiting Fixing Flag is a settlement-processing state used when payment or rate fixing is not complete. In the source tracker, it appears in UK go-live, realtime processing, and the January strategic cash-settlement scope.

The planned behavior includes handling the flag for UK go-live and realtime processing, and updating the Pending Fixing Flag value to `X`. The source does not define the complete state machine, ownership, transition triggers, or downstream message contract.

## Operational purpose

The flag is intended to prevent settlement processing from treating a payment as ready before the required fixing event has completed. It therefore relates to payment-status control, netting eligibility, and downstream publication.

The tracker identifies this capability across both [[entities/murex]] and [[entities/ratan]], but does not establish which system is authoritative for setting or clearing the flag.
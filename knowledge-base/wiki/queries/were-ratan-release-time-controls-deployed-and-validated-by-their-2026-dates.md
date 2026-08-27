---
type: query
title: Were RATAN Release-Time Controls Deployed and Validated by Their 2026 Dates?
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, control-assurance, release-cutoff, production-validation]
related: [ratan, cash-settlement-release-cutoff-controls, release-time-cashflow-status-gating, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--11-2026-design--40-ops-allowed-actio--pckrjd]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/OPS Allowed Actions Post Pending Release.md"]
---
# Were RATAN Release-Time Controls Deployed and Validated by Their 2026 Dates?

## Question

Were the timing control due by 2026-01-17 and the status-check control due by 2026-01-31 deployed to production, tested, and independently validated on or before their stated dates?

## Ambiguity

The source describes the controls with completed language while also assigning future target dates. It also describes the netting and splitting strategic fix as “done” by Jan 2026, despite the duplicate-payment incident occurring on 13 Jan 2026.

## Evidence needed

- Approved change records and production deployment timestamps.
- Requirements and implementation evidence for both controls.
- Concurrent-action and end-to-end downstream-dispatch test results.
- Post-deployment monitoring, exception records, and control-attestation evidence.
- Confirmation of whether the two controls were separate releases.

Until this evidence is available, the source supports control intent but not confirmed production effectiveness.
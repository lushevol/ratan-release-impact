---
type: query
title: Does CCIL Netting Require FMID 400021949?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ccil, bilateral-netting, counterparty-static-data]
related: [ccil, bilateral-netting-eligibility, bilateral-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/01 Bilateral Netting.md"]
---
# Does CCIL Netting Require FMID 400021949?

The guaranteed CCIL acceptance criterion uses both:

```text
Settlement Method = CCIL
Counterparty FMID = 400021949
```

The source does not state whether this FMID is a universal CCIL-netting requirement, a test-specific counterparty identifier, or an additional rule condition.

## Required clarification

Confirm the authoritative eligibility matrix for CCIL bilateral netting, including whether other counterparties or FMIDs may participate and whether the FMID is maintained in the [[netting-static-blotter]].
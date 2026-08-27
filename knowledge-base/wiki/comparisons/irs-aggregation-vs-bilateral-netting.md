---
type: comparison
title: IRS Aggregation vs Bilateral Netting
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, IRS, bilateral-netting]
related: [cashflow-netting, resultant-cashflow-generation, netting-service, irs-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# IRS Aggregation vs Bilateral Netting

The source presents IRS aggregation and bilateral netting as separate process scenarios. It provides examples but does not establish that they share identical eligibility, status, or resultant-generation rules.

| Aspect | IRS aggregation | Bilateral netting |
| --- | --- | --- |
| Component records | `C01` and `C02` are shown as `NETTED` | `C01`, `C02`, and `C03` are shown as `NETTED` |
| Component amount | `100 + 200` | `100 + 200 + 400` |
| Resultant amount | `300` | `700` |
| Resultant example | `N01`, payment type `IRS`, status `WAITING` | `N02`, status `WAITING`; `N01` is `DEAD` |
| Netting identifier | `1111` | `2222` |
| Additional behavior | IRS-specific aggregation example | Includes a fee cashflow and a prior dead resultant |

Both examples support amount aggregation and component/resultant grouping. The differing records and statuses show why IRS and bilateral netting should remain separate subjects until the authoritative contract confirms common semantics.
---
type: concept
title: Currency Rounding Static Data
created: 2026-08-24
updated: 2026-08-24
tags: [static-data, currency, rounding, precision, cashflow]
related: [automated-cashflow-rounding, ratan, what-is-the-authoritative-cashflow-rounding-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md"]
---
# Currency Rounding Static Data

Currency rounding static data maps `Cashflow.Payment_Currency` to a rounding precision and rounding type. It is the configuration input for [[automated-cashflow-rounding]].

The imported matrix supports `NO DECIMAL`, `1 DECIMAL`, `2 DECIMAL`, and `3 DECIMAL` precision. Most entries use `Round Off`. The explicit `Round Down` exceptions are:

```text
CLP | NO DECIMAL | Round Down
JPY | NO DECIMAL | Round Down
KRO | NO DECIMAL | Round Down
```

The authoritative full matrix is retained in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--64-round--10xd1dk]].

## Data-governance gaps

The source does not identify the matrix owner, version, effective date, validation rules, uniqueness rules, or audit process. Its codes include non-standard and internal-looking values, so the matrix must be treated as application configuration rather than inferred from ISO 4217 conventions.
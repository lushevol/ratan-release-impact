---
type: concept
title: Net Function
tags: [cashflow, netting, settlement, business-semantics]
related: [irs-cashflow-aggregation, interest-rate-swap, cash-settlement-home-page]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Net Function

The Net function allows users to merge different cashflows.

For IRS settlement, the current system uses Net to combine two separately received IRS legs. The source states that this works functionally but is semantically misleading: Net implies a user-initiated merger of unrelated cashflows, while IRS leg combination is a settlement-specific requirement.

The proposed [[irs-cashflow-aggregation]] function is intended to preserve this distinction. The source does not identify whether Net remains available for the IRS legs after Aggregation is introduced.
---
type: concept
title: Split-Child Processing Exclusions
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, netting, exclusions, duplicate-payment-prevention, irs]
related: [cashflow-splitting, cross-rule-netting-isolation, cashflow-auto-netting, nds-auto-netting, nds-duplicate-payment-prevention, irs-resultant-cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# Split-Child Processing Exclusions

A cashflow produced by splitting is insulated from processes that could aggregate, re-net, or duplicate its payment treatment.

Split children:
- May be automatically split again.
- Must not be manually split again.
- Must not match an auto-netting rule.
- Must not be manually netted.
- Must not undergo IRS checks.
- Must not enter NDS auto netting.

These controls extend [[cross-rule-netting-isolation]] to the split-child lifecycle. They are intended to preserve the settlement allocation chosen during splitting and to prevent duplicate or incompatible processing paths.
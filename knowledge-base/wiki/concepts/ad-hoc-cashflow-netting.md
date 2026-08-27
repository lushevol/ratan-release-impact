---
type: concept
title: Ad Hoc Cashflow Netting
created: 2026-08-22
updated: 2026-08-22
tags: [netting, un-netting, cashflow, maker-checker]
related: [bic-netting, ccs-auto-netting, netting-over-netting, cross-product-netting, cashflow-exception-handling, stella, mxcash]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# Ad Hoc Cashflow Netting

Ad hoc cashflow netting is a user-controlled process that groups eligible cashflows and generates a resultant cashflow rather than relying only on automated netting.

For FMRP strategy netting, eligible component cashflows must not be settled or released and must have a blank Netting Id. RATAN calculates the amount and direction, marks component cashflows as `Netted`, creates a resultant `QUEUED` cashflow, and creates a `Net Cashflow` exception for checker review.

If subsequent market events affect netted components, RATAN is expected to un-net them, hold the affected cashflow as NSTP, and generate a `Previously Netted` exception. The BCS model separates un-net initiation and verification, and excludes auto-netting rows from maker-initiated ad hoc netting.

FMRP routes netting actions according to BIC-net flags, CCIL settlement method, FMID, booking entity, and blank splitting identifiers. The current status of the struck-through Hong Kong booking-entity exclusion is unresolved.
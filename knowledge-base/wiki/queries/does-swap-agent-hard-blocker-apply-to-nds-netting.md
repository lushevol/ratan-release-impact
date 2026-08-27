---
type: query
title: "Does the SWAP_AGENT Hard Blocker Apply to NDS Netting?"
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, hard-blocker, nds, netting, endpoint-scope]
related: [swap-agent-coupon-interim-mtm-hard-blocker, nds-auto-netting, nds-netting-key, ratan-cash-settlement-netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md"]
---
# Does the SWAP_AGENT Hard Blocker Apply to NDS Netting?

The design explicitly lists BIC, CCIL, and bilateral netting endpoints as affected, then leaves an unresolved reference to `/v1/cashflows/nds/netting`.

Confirm whether NDS netting must enforce the same `SWAP_AGENT` payment-type validation and resultant hard-blocker propagation. If it does, identify the equivalent request fields, validation point, and release-control behavior.
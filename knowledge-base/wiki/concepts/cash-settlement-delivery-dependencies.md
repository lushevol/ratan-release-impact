---
type: concept
title: Cash Settlement Delivery Dependencies
tags: [cash-settlement, dependencies, integration, delivery-plan, 2024]
related: [cash-settlement, auto-netting, stella, murex-2-11, ebbs, emdi, tdsx, fm-swift-gateway, razor]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# Cash Settlement Delivery Dependencies

Cash settlement delivery depends on coordinated behavior across trade-data, market-event, netting, accounting, SWIFT, SSI, and operational-control systems.

The 2024 source assigns distinct responsibilities:

- [[entities/stella]]: market events, fixing cashflows, FMRP/non-FMRP indicators, DVP indicators, settlement method, and payment-schedule-related behavior.
- [[entities/murex-2-11]]: CCIL, suppression, IRS fixing/floating, lien, and clearing indicators or rules.
- [[entities/ebbs]]: accounting feeding, EOD scheduling, Solace connectivity, UAT, and EOD running.
- EMDI: Solace connections with EBBS/FM Swift Gateway and consumption of Murex 2.11 trades.
- TDS2/TDSX: TDSX API delivery for Drop2/Drop3.
- FM Swift Gateway and Razor/FMSGW: SWIFT generation and NACK handling.
- SCI: inter-entity, counterparty Murex Code, CCIL, BIC, and domicile-client dependencies.

The source reports several items as `Closed`, some as `Not Required` and `CLOSED`, and others with blank status. These labels should remain distinct because the document does not define their operational meaning.
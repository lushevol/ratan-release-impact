---
type: concept
title: Utilization Pilot
tags: [utilization-pilot, fmrp, fxu, cash-settlement, migration]
related: [fmrp, fxu, cash-settlement, auto-netting]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes.md"]
---
# Utilization Pilot

The utilization pilot is the Nepal/Saudi/Egypt workstream described for 2024 cash settlement. It uses [[entities/fmrp]] with [[entities/fxu]] integration and includes product support, Swift Generation, Accounting Generation, and Drop2/Drop3 events.

Its functional scope includes market-event processing, fixing/floating netting, CCIL Netting, splitting, settlement method, DVP NSTP, inherited-on-netting behavior, lien-driven NSTP, STP/NSTP, LMS Feeding, and SSI stamping.

The source reports delivery dependencies but does not provide independent production evidence. In particular, Inter Entity Netting, CFI Code query enhancement, and Omgeo Alert SSI are unchecked.
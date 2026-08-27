---
type: query
title: Should Primary Nostro Lookup Use CCY Pair?
created: 2026-08-23
updated: 2026-08-23
tags: [query, primary-Nostro, SSI-stamping, CCY-Pair]
related: [primary-nostro-fallback, ssi-stamping-service, ccy-pair-based-nostro-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Compatibility design for multiple entities.md"]
---
# Should Primary Nostro Lookup Use CCY Pair?

The proposal uses `CCY Pair` for primary Nostro lookup when Vostro data is missing or multiple. The source identifies this as an open question requiring confirmation of the static-data query contract.

Resolution should specify whether the pair is a supported key, what happens when it is absent, and how multiple or zero results are handled.
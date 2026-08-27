---
type: entity
title: Nostro Static Data
tags: [nostro, static-data, settlement-instructions, swift]
related: [ratan, murex, ssi-plus, static-data-readiness, nostro-static-data-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Murex and Ratan Swift Difference Review.md"]
---
# Nostro Static Data

Nostro static data comprises configured Nostro accounts, agent BICs, account numbers, and routing values used during SWIFT generation. The review repeatedly identifies Nostro data as the cause of apparent differences between Murex replay output and RATAN output.

Examples include MT202 field 53A and MT210 field 52A differences. The Tranche 1 review records populations of 951 MT210 field 52A differences as “Nostro file updated,” while other high-volume differences were still assigned to SSI-data checking.

A note that the Nostro file was updated is not sufficient evidence of resolution. The affected records require effective-date confirmation and replay validation under [[concepts/nostro-static-data-governance]].
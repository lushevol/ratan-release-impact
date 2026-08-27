---
type: query
title: Which Murex Payment Reports Move to Razor or RATAN and Remain for Precious Metals?
created: 2026-08-22
updated: 2026-08-22
tags: [reporting, razor, ratan, murex, precious-metals, accounting]
related: [razor, murex-to-ratan-cashflow-integration, ebbs-settlement-accounting, murex-cashflow-migration-to-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Which Murex Payment Reports Move to Razor or RATAN and Remain for Precious Metals?

The source identifies reports affected by the Murex `SNTR/RLSR` end statuses and proposes a mixed target-state model:

- EBBS and Aspire settlement-accounting reports are expected to move to [[razor]].
- CRRS and CCRS feeds are expected from RATAN EOD, combining RATAN ONE non-precious-metal data with Murex precious-metal data.
- Some FMMIS reports are expected from RATAN ONE.
- TLM continuity and China applicability remain explicitly questioned.
- One weekly report has no recorded user downloads.

A formal inventory is needed to establish, for each report, its target owner, data source, precious-metal treatment, consumer, retention requirement, and decommission decision.
---
type: query
title: How Should RATAN Handle Empty ND Parent Typology?
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, TDS3, NDS, data-quality, enrichment]
related: [tds3, nds-auto-netting, nds-fixing, pending-nds-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# How Should RATAN Handle Empty ND Parent Typology?

RATAN may receive an empty `ND_Parent_Typology` when TDS3 has not yet received the corresponding Murex data.

The source does not define whether RATAN should retry enrichment, hold the cashflow, route it to STP, include it in netting, or create a separate exception. A fail-safe policy is needed because incorrectly treating an unknown parent typology as eligible could bypass the NDIRS-specific STP rule or include an unsuitable payment in a resultant.
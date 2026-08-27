---
type: query
title: Which Inter-Entity Mapping Static Is Authoritative?
created: 2026-08-22
updated: 2026-08-22
tags: [inter-entity-netting, mapping-static, configuration, governance]
related: [counterparty-mapping-static, inter-entity-cashflow-pre-match, 26-auto-netting-page-md-files--135-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-se--634gz8]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Which Inter-Entity Mapping Static Is Authoritative?

The source presents an original counterparty mapping table and a confirmed deployment table with omitted mappings. It describes six excluded rows, but comparison identifies five:

- `10075222` / `SCB LONDON*LDN`
- `400040044` / `SC IRTW TWOIRO*TPE`
- `400037927` / `SC IRTW TWNDF*TPE`
- `400037876` / `SC IRGB HKSWAP*LDN`
- `400037877` / `SC IRGB IROTRAD*LDN`

Confirm the live backend static, the approved version, and whether each omitted mapping is intentionally outside Phase 1. This is a correctness dependency for [[inter-entity-cashflow-pre-match]].
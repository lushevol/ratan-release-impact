---
type: entity
title: NDS
created: 2026-08-22
updated: 2026-08-22
tags: [NDS, product-typology, cash-settlement, netting]
related: [nds-auto-netting, nds-fixing, ndirs, nds-netting-key, ratan, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/NDS Auto Netting.md"]
---
# NDS

NDS is a product typology within the scope of the RATAN auto-netting requirement.

NDS cashflows are component cashflows when they satisfy the configured eligibility rules. They are expected to enter `WAITING` status with the `Pending NDS Netting` NSTP exception until RATAN combines them with eligible NDS Fixing cashflows sharing the same [[concepts/nds-netting-key]].

The requirement moves ownership of NDS netting from Murex 2.11 to RATAN. NDS cashflows are also used as the source of the CFI Code on the net resultant.
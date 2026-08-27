---
type: concept
title: Netting Client Configuration
tags: [cash-settlement, netting, client-configuration, batch-processing]
related: [cadm, netting-set-affirmation, ratan-s2bng-netting-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Story Board.md"]
created: 2026-08-23
updated: 2026-08-23
---
# Netting Client Configuration

Ratan and S2BNG require client-level configuration of netting eligibility at product, lowest CFI-code, and instrument-currency level.

The solution must also support automatic batch netting at a configured date and client-specific netting-script timing keyed by FMID or LEI.

The source does not define configuration ownership, validation, effective dating, precedence, or whether product-level configuration qualifies the requirement to use the same CFI-code product in a netting set.
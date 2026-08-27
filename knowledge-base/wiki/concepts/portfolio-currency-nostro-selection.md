---
type: concept
title: Portfolio-and-Currency Nostro Selection
created: 2026-08-23
updated: 2026-08-23
tags: [rfi, portfolio, currency, nostro, ssi]
related: [dedicated-nostro-stamping, ratan-cash-settlement-ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# Portfolio-and-Currency Nostro Selection

Portfolio-and-currency Nostro selection is the RFI-specific lookup method. It selects a dedicated Nostro using the cashflow or trade portfolio and currency, without settlement means, settlement account, or Vostro data.

The rule is leg-specific. For an RFI portfolio USD/KOR trade, only the KOR leg uses dedicated selection; the USD leg follows normal selection. The document also uses `KRO` in places, so the canonical currency code must be confirmed before configuration or implementation.

Portfolio extraction from XML is not finalized for every product. Trade stamping is not currently committed because portfolio paths may be absent or ambiguous.
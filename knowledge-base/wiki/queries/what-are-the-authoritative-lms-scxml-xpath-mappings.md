---
type: query
title: What Are the Authoritative LMS SCBML XPath Mappings?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, scbml, xpath, integration, data-mapping]
related: [lms, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# What Are the Authoritative LMS SCBML XPath Mappings?

The published LMS mapping contains defects and inconsistencies that should be reconciled before implementation or automated validation.

## Issues to resolve

- Several XPath values contain Markdown links embedded inside string literals.
- `legalEntityId` is inconsistently associated with `LEID` and `FMID`.
- `receiverPartyReference` is represented inconsistently as an element value and an attribute.
- `payerPartyReference` uses `href="party1"` in the XML template, but the active mapping does not consistently preserve that distinction.
- `SCB_Nostro_Account_Type` appears in the eligibility logic but not visibly in the XML payload.
- The active mapping and the struck-through historical “Detail Fields Mapping” contain different fields and mandatory flags.
- Amendment fields such as `cancelledCashflowId` and `cancelledCashflowStatus` need an explicit event-specific contract.

The source summary at [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--30-surrounding-system-in--15olx7l]] preserves the published template and active mapping for reconciliation.
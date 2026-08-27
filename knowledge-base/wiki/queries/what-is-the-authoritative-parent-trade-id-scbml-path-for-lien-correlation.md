---
type: query
title: What Is the Authoritative Parent Trade ID SCBML Path for Lien Correlation?
created: 2026-08-23
updated: 2026-08-23
tags: [scbml, parent-trade-id, tds3, murex, lien]
related: [ratan, tds3, murex, trade-lien-notification-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# What Is the Authoritative Parent Trade ID SCBML Path for Lien Correlation?

The source defines original trade ID as the correlation contract between Murex cashflows and TDS3 trades:

- Cashflow: `Parent_Trade_Id`
- Trade: `Trade_Id`

However, the supplied `Parent_Trade_Id` SCBML path is truncated or malformed, including rendered Markdown URL text inside an XPath-like expression. It cannot safely be implemented as written.

Confirmation is needed for the exact SCBML path, complete `linkIdScheme` value, identifier cardinality, and correlation behavior for novation, cancel/reissue, and other trade-event forms.
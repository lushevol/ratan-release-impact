---
type: query
title: Does AMH ACK Mean Final Settlement or SWIFT Network Acceptance?
tags: [amh, swift, settlement-status, acknowledgement]
related: [amh, fmsre, cashflow-status-lifecycle, cash-settlement-platform]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/SFMRP - Cash Settlement Platform Integration（Deprecated）.md"]
---
# Does AMH ACK Mean Final Settlement or SWIFT Network Acceptance?

The deprecated integration source transitions a payment from `RELEASED` to `SETTLED` after [[amh]] sends an ACK following routing to the SWIFT network.

Confirm whether this acknowledgement represents technical acceptance, SWIFT network delivery, recipient-bank acceptance, or final financial settlement. The distinction affects terminal-state semantics, operational controls, reversals, and reconciliation.
---
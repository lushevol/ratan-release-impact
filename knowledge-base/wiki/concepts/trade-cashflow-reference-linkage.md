---
type: concept
title: Trade-Cashflow Reference Linkage
tags: [trade, cashflow, linkage, Reference-ID, reconciliation, STP]
related: [cdu, ratan, scbml, cashflow-reference-consistency-validation, trade-confirmation-driven-cashflow-stp, cashflow-amendment-supersession]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md"]
---
# Trade-Cashflow Reference Linkage

Trade-cashflow reference linkage is the proposed mechanism for identifying whether a cashflow corresponds to the trade state confirmed by [[cdu]].

The design introduces a Reference ID that is persisted in trade and cashflow [[scbml]] messages. The Reference ID changes when an economic trade update affects cashflows and remains unchanged for status transitions and non-economic changes. Fixing-event cashflows inherit the Reference ID from their parent trade.

This provides a direct business-linkage check in place of relying solely on Trade ID, Tracking Version, or Event ID. The source presents the mechanism as a proposal in a deprecated document; its implementation and current authority are unverified.
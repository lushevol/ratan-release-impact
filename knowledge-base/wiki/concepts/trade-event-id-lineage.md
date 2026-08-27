---
type: concept
title: Trade Event ID Lineage
tags: [trade, Event-ID, event-lineage, cashflow, SCBML]
related: [scbml, trade-cashflow-reference-linkage, trade-economic-versus-non-economic-update, cashflow-amendment-supersession]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/CDU Trade Confirmation Notification & Cashflow.md"]
---
# Trade Event ID Lineage

Trade Event ID Lineage describes how Event ID and Event Version relate trade events to subsequent processing records.

The source gives two behaviors:

- For an economic trade update, Event ID can remain unchanged while Event Version changes and new cashflow versions are generated.
- For a non-economic amendment, Event ID can change even when the cashflow relationship is not the primary economic concern.

One Event ID can therefore map to multiple cashflows or cashflow versions. Event ID is useful as lineage metadata but is not sufficient by itself to establish that a cashflow is the current valid cashflow for STP. The proposed Reference ID is intended to provide the direct trade-to-cashflow linkage check.
---
type: concept
title: ND Parent Trade Metadata
tags: [cashflow, nid, ndirs, parent-trade, scbml, data-model]
related: [nds-cashflow-processing, nstp-and-ndirs-rule-routing, ratan-mxg-cashflow-adaptor, scbml, centralized-cashflow-field-mapping-governance, dynamic-cashflow-query-field-mapping, what-are-the-nid-and-nd-parent-typology-validation-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NDS Cashflow Processing Design.md"]
created: 2026-08-24
updated: 2026-08-24
---
# ND Parent Trade Metadata

ND parent trade metadata consists of two logical cashflow fields added internally to support downstream processing and rule evaluation.

## Logical Fields

| Logical model | Xpath | Description | Change Flag |
| --- | --- | --- | --- |
| Cashflow.ND_Parent_Trade_Id | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:NDParentTradeId | NID | Internal Adding |
| Cashflow.ND_Parent_Typology | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:cashflow/scb:NDParentTradeTypology | ND parent trade typology | Internal Adding |

NID is mapped from MXML to [[scbml]] by [[ratan-mxg-cashflow-adaptor]]. The parent typology distinguishes `NDIRS` from non-`NDIRS` cashflows for [[nstp-and-ndirs-rule-routing]].

“Internal Adding” identifies the change as an internal data-model addition. The source does not establish external message-contract exposure, query availability, source-of-truth ownership, or validation semantics.

See [[what-are-the-nid-and-nd-parent-typology-validation-rules]] for unresolved missing, blank, malformed, and historical-data cases.
---
type: concept
title: CDUPS SSI Stamping Integration
created: 2026-08-23
updated: 2026-08-23
tags: [cdups, ssi-stamping, cashflow, exception-handling, solace]
related: [cdups, cdu, ssi-stamping-service, latest-cashflow-ssi-result, uber-message-ssi-stamping, solace, ssi-exception-state-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# CDUPS SSI Stamping Integration

The CDUPS integration provides client-document generation with current SSI-stamping outcomes from RATAN. Its key requirement is visibility of the latest cashflow-level result, including changes caused by Vostro refresh, Nostro refresh, fixing notices, trade events, and approved ad-hoc remediation.

The source describes a call-based interaction for refresh and remediation scenarios rather than proactive publication. Separately, the trade-booking flow describes sending a response to CDUPS through Solace. This likely represents a distinction between event-triggered re-stamping and a response to a CDUPS query, but the document does not make that distinction explicit.

Exception handling between CDUPS and RATAN is required, but the source does not define exception states, payload fields, retries, recovery, ownership, or reconciliation. The recipient ambiguity between CDU and CDUPS also remains unresolved.
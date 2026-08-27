---
type: query
title: Are CDU and CDUPS Distinct Recipients for Stamped uber Messages?
created: 2026-08-23
updated: 2026-08-23
tags: [cdu, cdups, uber, ssi-stamping, integration]
related: [cdu, cdups, uber-message-ssi-stamping, cdups-ssi-stamping-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Are CDU and CDUPS Distinct Recipients for Stamped uber Messages?

The source names CDU as the recipient of a post-stamped `uber` message in the meeting notes, but describes delivery to CDUPS through Solace in the trade-booking flow.

This query requires confirmation of whether CDU and CDUPS are separate systems, whether one is upstream of the other, and which system owns consumption of the stamped message for client-document generation.
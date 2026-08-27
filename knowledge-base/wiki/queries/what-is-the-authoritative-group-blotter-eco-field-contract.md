---
type: query
title: What Is the Authoritative Group Blotter Eco Field Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [group-blotter, eco-fields, data-contract, open-question]
related: [group-blotter-eco-fields, group-blotter, cashflow-record, trade-record, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md"]
---
# What Is the Authoritative Group Blotter Eco Field Contract?

## Question

What are the authoritative source, schema, release status, and functional uses of the twelve fields listed for the 2026 Group Blotter?

## Known Evidence

The source identifies eight `Cashflow Record` fields and four `Trade Record` fields. It specifies release-dependent sourcing only for `Settlement_Method` and marks `Portfolio.Booking_Entity_Trade_Portfolio_Name` as to be released with RFI.

## Open Points

- Which fields are displayed in the Group Blotter, and which are backend-only?
- What are the data types, nullability rules, formats, and permissible values?
- What are the physical source systems and trade-to-cashflow join keys?
- Is `Settlement_Method` stored or derived in each release?
- What does “TB Released with Uber” mean operationally?
- What is the RFI identifier, release date, and validation status for `Portfolio.Booking_Entity_Trade_Portfolio_Name`?
- How is `LIEN_Monitoring` calculated, and does it affect workflow?
- Are `Contract_Typology`, `Linked_Package_Id`, and `Swap_Agent_Id` used for display, filtering, grouping, or downstream processing?

## Evidence Boundary

The field list is strong evidence for intended scope but does not prove implementation, production availability, data quality, user-interface behavior, or processing semantics. It should be resolved with an authoritative schema, API contract, release record, or validated test evidence.
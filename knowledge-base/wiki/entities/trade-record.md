---
type: entity
title: Trade Record
created: 2026-08-23
updated: 2026-08-23
tags: [trade, record, group-blotter, cash-settlement]
related: [group-blotter, group-blotter-eco-fields, trade-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Group Blotter Requirement.md"]
---
# Trade Record

## Group Blotter Fields

The 2026 Group Blotter requirements associate four fields with `Trade Record`:

- `LIEN_Monitoring`, labelled an Eco field.
- `Contract_Typology`, labelled a Special field.
- `Linked_Package_Id`, labelled a Special field.
- `Swap_Agent_Id`, labelled a Special field.

The source does not define the physical record schema, field types, nullability, ownership, or whether these fields are mandatory.

## Evidence Boundary

`LIEN_Monitoring` is connected to existing lien-related concepts, but the source does not state how it is calculated or whether it affects workflow. `Swap_Agent_Id` identifies a swap agent but does not establish any particular swap-agent settlement behavior.
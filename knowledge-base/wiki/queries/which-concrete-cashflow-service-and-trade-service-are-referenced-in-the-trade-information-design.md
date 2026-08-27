---
type: query
title: Which Concrete Cashflow Service and Trade Service Are Referenced in the Trade Information Design?
tags: [cash-settlement, service-ownership, trade-information, open-question]
related: [trade-information-sourcing-for-cash-settlement, ratan-cashflow-lifecycle-service, cashflow-group-management-service, ratan-cashflow-standardization-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Trade Information Tech Design.md"]
---
# Which Concrete Cashflow Service and Trade Service Are Referenced in the Trade Information Design?

## Question

Which deployed services are meant by the generic terms “Cashflow service” and “trade service” in the trade-information design?

## Evidence

Option 1 refers to a Cashflow service querying TDS3 through Data Ambassador on each cashflow event. Option 2 refers to the trade service currently used to consume all trades from TDS3. The source gives no service name, repository, owner, endpoint, topic, or deployment identifier.

Existing Cash Settlement pages such as [[ratan-cashflow-lifecycle-service]], [[cashflow-group-management-service]], and [[ratan-cashflow-standardization-service]] are potentially related, but the source does not establish that any of them is the referenced Cashflow service.

## Information Needed

Resolution requires service names, ownership, repository or deployment identifiers, integration interfaces, and confirmation of whether the services are shared or Cash Settlement-specific.

## Status

Open. Do not assign the generic responsibilities to an existing named service without corroborating evidence.

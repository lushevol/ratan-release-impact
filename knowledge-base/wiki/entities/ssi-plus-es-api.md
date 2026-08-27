---
type: entity
title: SSI+ ES API
created: 2026-08-23
updated: 2026-08-23
tags: [SSI-plus, API, Vostro, settlement-instructions, cash-settlement]
related: [ssi-plus, ssi, fmrp, ssi-stamping, vostro-ssi-best-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Vostro SSI Best Matching - UK Cashflow Migration.md"]
---
# SSI+ ES API

## Role

The SSI+ ES API is the source interface used during Vostro SSI stamping to retrieve possible settlement instructions. The requirement specifies one query per cashflow context, after which FMRP applies the best-matching logic to the returned candidates.

## Query Scope

The query may include:

- `BranchId_Murex3Id`, including a specific branch and `Global`
- `CFI_Code` patterns such as `SR****`, `*R****`, and `******`
- Currency
- Counterparty FMID
- Other SSI matching conditions

The source does not provide the endpoint, request or response schema, authentication details, timeout behavior, or error contract.

## Processing Boundary

SSI+ ES returns the candidate set. The selection order is applied after retrieval:

- BAU: product hierarchy, then branch and primary/secondary priority
- UK cashflow migration: branch versus Global, then product hierarchy, then primary/secondary priority

See [[concepts/vostro-ssi-best-matching]] for the conditional algorithms.
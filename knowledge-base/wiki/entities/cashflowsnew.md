---
type: entity
title: cashflowsNew
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, query-service, cashflow, api-operation]
related: [query-service, cash-settlement-query-service-graphql-read-model, cashflow-query-response-null-semantics, why-does-cashflowsnew-response-not-match-the-cashflow-id-filter, what-authorization-and-masking-controls-govern-cashflowsnew-ssi-fields]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# cashflowsNew

`cashflowsNew` is an observed GraphQL read operation associated with the [[query-service]]. It returns a paginated composite cashflow result and permits clients to project nested cashflow, trade, provenance, entity, portfolio, settlement-instruction, and FMO-comment fields.

## Observed Inputs and Outputs

The documented example provides a `filter` array, `page: 0`, and `size: 5`. Its response includes `pageInfo` with `totalHits`, `pageNo`, `pageSize`, and `lastPage`, followed by `results`.

No authoritative behavior is documented for supported filter fields, operator combinations, sorting, maximum page size, or invalid inputs.

## Consumer Considerations

The operation's requested projection includes sensitive SSI account, routing, BIC, address, remittance, and sender-to-receiver data. The example does not document entitlement, masking, or audit controls. It also demonstrates inconsistent representations for absent data.

The supplied equality-filter example does not match its returned results. Consumers should not infer identifier uniqueness or filtering behavior until [[why-does-cashflowsnew-response-not-match-the-cashflow-id-filter]] is resolved.
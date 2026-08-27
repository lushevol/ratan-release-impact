---
type: query
title: Can JSONB Dynamic Cashflow Filtering Meet Query Service Performance and Security Requirements?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, jsonb, postgresql, query-performance, security, graphql]
related: [query-service, dynamic-cashflow-query-field-mapping, jsonb-expression-indexed-query-performance, postgresql-jsonb-expression-index-matching, what-authorization-and-masking-controls-govern-cashflowsnew-ssi-fields]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# Can JSONB Dynamic Cashflow Filtering Meet Query Service Performance and Security Requirements?

The source proposes that [[query-service]] query and index JSONB after eliminating local XPath mappings. It provides no concrete JSON paths, index definitions, operators, benchmarks, query plans, or authorization design.

## Questions to resolve

- Will JSONB replace flattened columns or coexist with the existing read model?
- Which JSONB operators, expression indexes, generated columns, and data types support required filters and sorts?
- What query-plan and benchmark evidence demonstrates acceptable latency at expected data volume and concurrency?
- How are dynamic field names and operators validated to prevent unsafe query construction?
- Which fields can callers filter or return?
- Where are entitlements and SSI masking enforced, particularly for account and beneficiary data?
- How are pagination, sorting, nulls, and type coercion defined consistently with GraphQL?

The mapping proposal alone is insufficient evidence that the JSONB approach is performant or secure.
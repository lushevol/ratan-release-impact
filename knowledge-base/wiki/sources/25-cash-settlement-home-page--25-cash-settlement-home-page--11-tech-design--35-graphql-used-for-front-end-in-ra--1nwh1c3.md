---
type: source
title: GraphQL Proposal for the RATAN Frontend
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [graphql, ratan, cash-settlement, cashflow, frontend-architecture]
related: [ratan, cash-settlement-platform, cash-settlement-query-service-graphql-read-model, cashflow-query-response-null-semantics, cashflow-notification-and-auto-refresh, cashflow-exception-read-model-enrichment, ssi-stamping-service, is-graphql-candidate-query-performance-within-sla, is-graphql-defer-supported-end-to-end-in-ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Proposal.md"]
---
# GraphQL Proposal for the RATAN Frontend

## Summary

This proposal describes using GraphQL as the frontend query and aggregation layer for [[entities/ratan]], initially for the Cashflow Settlement CN workflow and its Multi Exceptions feature. The design aggregates data previously obtained through multiple RESTful API calls, allowing the frontend to request related cashflow, exception, maker-input, affirmation, candidate SSI, and confirmation data through one GraphQL operation.

The source records the implementation as complete: the APIs were evaluated, REST resources were mapped to GraphQL schemas, the new schema was implemented and tested, user cases were tested, and the workflow was taken live with the frontend REST APIs phased out.

## Architectural Intent

The proposal identifies the following intended benefits:

- Unifying frontend query methods.
- Reducing browser and network request overhead.
- Allowing clients to select the fields they require.
- Aggregating data from multiple existing REST resources.
- Improving data validation and error handling.
- Supporting schema evolution and real-time updates.
- Reducing network traffic.

These are design objectives rather than universally demonstrated properties. In particular, the source does not provide security controls, query-complexity limits, field-level authorization rules, or evidence that GraphQL replaced the underlying backend REST dependencies.

## Performance Criteria

The source defines the following response-time guidance for individual API segments:

| API Segment Size | Recommended Response Time | Minor Response Time |
| --- | --- | --- |
| <= 500B | <= 200ms | <= 300ms |
| <= 1KB | <= 200ms | <= 300ms |
| <= 50KB | <= 500ms | <= 1000ms |
| <= 100kb | <= 1000ms | <= 1500ms |

The source attributes these targets to the following external reference:

[Hobo web-performance reference](https://www.hobo-web.co.uk/your-website-design-should-load-in-4-seconds/)

The document does not specify whether payload sizes are compressed, whether the timing includes the complete request lifecycle, or whether these values are internal service-level objectives.

## Client and Server Implementation

| Type | implement | Support Features | details |
| --- | --- | --- | --- |
| Client | Apollo-Client@3.7.13 | Query/Mutations/Subscription/@defer | [https://github.com/apollographql/apollo-client](https://github.com/apollographql/apollo-client) |
| Server | DGS@4.9.24 | Query/Mutations/Subscription | [https://github.com/netflix/dgs-framework](https://github.com/netflix/dgs-framework) |

The source lists `@defer` as a client capability but does not list it among the DGS server capabilities. End-to-end support therefore remains unresolved; see [[queries/is-graphql-defer-supported-end-to-end-in-ratan]].

## Cashflow Settlement CN Use Case

The primary use case is Multi Exceptions, a Cashflow Settlement CN feature that displays all exceptions while viewing cashflow details and supports bulk fixing. The source states that this workflow previously required approximately 2.5 seconds to complete through RESTful APIs.

The reported GraphQL result was:

- Loading time reduced from approximately 2.5 seconds to approximately 1 second.
- Initial request count reduced by 80%.
- Average simple-request response time below 0.5 seconds.
- Average full GraphQL request response time of 393ms.
- Partial-request response times generally between 220ms and 320ms.

The source also reports maximum times of 4.6 seconds for the full request and 9.6 seconds for candidate queries. These tail results exceed the stated response-time guidance and are the principal operational risk. The source suggests a possible 2-second timeout but does not establish that it was implemented or define its partial-response behavior.

## REST-to-GraphQL Mapping

| Definition | Schema | Type | Description | Restful Mapping | Restful Loading Speed (Office) (Latency/Resource Size) |
| --- | --- | --- | --- | --- | --- |
| Exception List | ratanException → Exception | New | Realtime exceptions in cashflow. | /v1/rep/exceptions/byEntity | 297ms/677B |
| Maker Input | ratanException → Exception → Stashing | New | User Generated Data which stashed for further usage. Like Maker Input. | - /v1/nstpException/actionData - /v2/stamping/query/makerInput | - 430ms/167B - 295ms/173B |
| Vostro Candidate List | ratanVostroCandidates → SSI Array | New | Available Vostro List | /v2/stamping/query/vostro | 990ms/3.9kB |
| Nostro Candidate List | ratanNostroCandidates → SSI Array | New | Available Nostro List | /v2/stamping/query/nostro | 433ms/708B |
| Affirmation MetaData | ratanAffirmation → AffirmationInfo | New | Affirmation Data | /v1/nstpException/metaData | |
| Back Value MetaData | cashflow → SSI → Swift_Payment_Date | New | Back Value Data | /v1/nstpException/metaData | |
| System Assigned SSI | cashflow → Settlement_Instruction → SSI | Existing | - Good Stamped SSI - Nostro Default when Vostro Exception | - /v2/stamping/cashflow/query/vostro - /v2/stamping/cashflow/query/nostro | - 356ms/2.0kB - 323ms/649B |
| Trade Confirmation Status | cashflow → Confirmation → Confirmation_Staus | Existing | Trade Confirmation Status | | |

`Confirmation_Staus` is preserved exactly as written in the source. The spelling should be checked against the deployed schema before being normalized.

The source refers to a suppression-field CSV attachment named `ratan_suppression_fields_v34.1.0.dev.csv`, but the attachment contents and complete query/result schemas are not present in the supplied document.

## Error Handling

For a partial failure, the source proposes preserving the expected response key or path while returning an “empty value” for fields that failed to resolve. The frontend should retry only the failed field paths rather than resending the complete GraphQL request.

The phrase “empty value” is not a complete GraphQL contract. It does not specify whether a failed field is represented as `null`, an empty list, an empty object, an omitted field, a custom error value, or a standard GraphQL `errors` entry with a `path`. This gap is related to [[concepts/cashflow-query-response-null-semantics]].

A full failure is associated with unavailable query services or poor network conditions. Retry count, backoff, timeout ownership, circuit breaking, observability, user-facing messages, and subscription reconnection behavior are not specified.

## Evidence and Limitations

The source provides concrete technology versions, field mappings, latency observations, and reported before-and-after results. However, the performance evidence lacks sample size, percentile statistics, workload characteristics, environment details, payload comparison, concurrency, and a reproducible test procedure. Referenced screenshots and the suppression-field CSV are also unavailable in the supplied text.

The source should therefore be treated as strong evidence of an implemented use case and moderate evidence for the reported average improvements, but not as proof of a general GraphQL-over-REST performance advantage.

## Open Questions

- What are the complete deployed query and result schemas?
- Is `ratan_suppression_fields_v34.1.0.dev.csv` authoritative?
- What causes the 9.6-second candidate-query maximum?
- Was the proposed 2-second timeout implemented?
- What exact null and error semantics apply to partial failures?
- Which REST endpoints were retired from the frontend, and which remain backend dependencies?
- Are GraphQL subscriptions used in production?
- Is Apollo Client `@defer` supported end to end with DGS `4.9.24`?
- What authorization, field-masking, query-depth, query-complexity, and request-limit controls are deployed?
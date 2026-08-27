---
type: entity
title: Postman
created: 2026-08-24
updated: 2026-08-24
tags: [postman, api-testing, performance-testing]
related: [graphql-vs-restful-cashflow-querying, graphql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# Postman

## Role in the source

Postman was used for single-request timing comparisons between the GraphQL and RESTful CN Cash Settlement cashflow query endpoints. Each request included timestamps for request preparation, data fetching, and response completion.

The source also reports concurrency and traffic tests, but does not identify the complete test harness or provide repeated-run statistics.
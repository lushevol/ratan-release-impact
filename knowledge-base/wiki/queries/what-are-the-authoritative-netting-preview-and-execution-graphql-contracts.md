---
type: query
title: What Are the Authoritative Netting Preview and Execution GraphQL Contracts?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, graphql, mutation, api-contract, ratan]
related: [ratan, what-is-the-authoritative-ratan-frontend-graphql-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/GraphQL Used For Front End In RATAN/GraphQL Schema Completion 2025.md"]
---
# What Are the Authoritative Netting Preview and Execution GraphQL Contracts?

## Question

What GraphQL inputs, outputs, validation, authorization, state-transition, idempotency, and failure semantics govern Netting Preview and Netting Execution in RATAN?

## Evidence

GraphQL Schema Completion 2025 classifies Netting Preview as a query and Netting Execution as a mutation. It supplies no GraphQL schema for either operation.

## Required clarification

An implementable contract needs request and response types, eligibility rules, business-date and scope semantics, preview-to-execution consistency, authorization and maker-checker controls where applicable, idempotency behavior, auditability, concurrency handling, status transitions, and partial or terminal failure behavior.
---
type: query
title: What Is the Authoritative EBBS Solace Feed and Acknowledgement Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, ebbs, solace, accounting-feed, acknowledgement, integration]
related: [ebbs, solace, message-bridge, accounting-service, solace-based-ebbs-acknowledgement-integration, accounting-file-delivery-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# What Is the Authoritative EBBS Solace Feed and Acknowledgement Contract?

## Question

What are the authoritative message, transport, and recovery contracts for the Ratan-to-EBBS accounting integration over Solace?

## Evidence

The technical-live plan expects Ratan to publish an accounting feed or mocked EBBS JSON to a Solace topic, EBBS to return an ACK, and Ratan to consume that ACK. It does not provide the topic names, schemas, headers, correlation identifiers, or operational behavior.

## Questions to Resolve

- Which Solace topics and credentials are used?
- Which service publishes and consumes each message?
- What schema and version must the accounting feed and mocked JSON satisfy?
- Which identifier correlates an EBBS ACK to the original feed and cashflow?
- How are ACK, NACK, timeout, retry, duplicate delivery, and out-of-order delivery handled?
- How are new and reversal postings represented and correlated?
- Does an ACK trigger an accounting update, and what is the authoritative update key?
- Must the mock payload be schema-compatible with the production Accounting Service output?

## Current Assessment

The source supports the existence of an expected ACK flow but does not establish the detailed contract. This query should remain open until the production interface specification, implementation contract, or signed test evidence is available.
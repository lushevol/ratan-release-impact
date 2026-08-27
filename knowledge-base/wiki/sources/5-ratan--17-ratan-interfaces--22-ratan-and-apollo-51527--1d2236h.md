---
type: source
title: RATAN and Apollo 51527 Interface
authors: []
year: 2026
url: ""
venue: ""
tags: [ratan, apollo, interface, trade-validation, business-rules]
related: [apollo-rule-engine, ratan, post-trade-detective-controls, trade-validation, what-is-the-authoritative-ratan-apollo-rule-engine-interface-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN and Apollo 51527.md"]
---
# RATAN and Apollo 51527 Interface

## Summary

This document describes a high-level integration between [[entities/ratan]] and [[entities/apollo-rule-engine]], identified by Application ID `51527`. RATAN calls the Apollo Rule Engine API to validate trades against business requirements, extracts the resulting rule response, and saves the response in an exception data store.

The stated business purposes are post-trade detective controls and regulatory compliance. The document is an incomplete interface-documentation template and does not establish a reviewed or authoritative technical contract.

## Source Context

The source notes that the subject was updated to “BPMS APP and Interface APP,” using “RATAN and TDS3” as an example. The relationship between that documentation convention and Apollo Rule Engine is not defined.

## Review Status

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| | | | | |

No review or publication metadata is populated.

## Description

> This integration establishes a connection between our system and Apollo Rule Engine (Application ID: 51527) to leverage their comprehensive business rule evaluation capabilities for post-trade detective controls and regulatory compliance.

## End-to-End Data Flow

```text
RATAN --(API)--> Apollo Rule Engine
```

The described flow is:

1. RATAN submits trade data to the Apollo Rule Engine API.
2. Apollo evaluates the trade against configured business rules.
3. RATAN extracts the rule response.
4. RATAN saves the response in an exception data store.

## Connection Details

No connection details are provided. The source does not specify environments, network paths, endpoint URLs, authentication, authorization, timeout settings, or retry behavior.

## Interface Specification

No API operations, request schema, response schema, rule identifiers, error codes, or versioning information are provided.

## Interface Team Contact

No interface team or support contact is identified.

## OLA

No operational-level agreement is provided. The source mentions that an application self-OLA consolidation link may be added, but no link is present.

## Other Useful Documents

No related documents are identified in the source.

## Known Issues

No known issues are documented. The following information remains unspecified:

- The identity and ownership of the exception data store
- Failure, timeout, retry, and duplicate-submission behavior
- Rule versioning and audit requirements
- The relationship between Apollo Rule Engine and [[entities/ratan-rule-service]]
- Whether Apollo participates in the canonical NSTP exception publication path

## Troubleshooting

No troubleshooting steps are provided. The source does not identify where interface failures should be checked or which team owns operational investigation.

## Evidence and Limitations

The document supports the existence of an intended RATAN-to-Apollo integration and its high-level business purpose. It does not provide evidence that the interface has been implemented, reviewed, published, or placed into production.

The source does not establish that Apollo Rule Engine:

- Replaces or is the same component as `ratan-rule-service`
- Publishes NSTP exceptions
- Uses the same rule model or API as other RATAN rule services
- Participates in cash-settlement rule filtering
- Owns the exception state machine

See [[queries/what-is-the-authoritative-ratan-apollo-rule-engine-interface-contract]] for the unresolved interface and ownership questions.
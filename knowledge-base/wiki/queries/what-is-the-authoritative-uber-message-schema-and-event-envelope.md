---
type: query
title: What Is the Authoritative Uber Message Schema and Event Envelope?
created: 2026-08-24
updated: 2026-08-24
tags: [uber-message, schema, event-envelope, protocol-buffers]
related: [uber-message, full-state-event-attributed-messaging, cashflow-sequence-and-count-completeness-control, fixing-schedule-cashflow-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# What Is the Authoritative Uber Message Schema and Event Envelope?

## Question

What are the authoritative fields, message boundaries, and serialization rules for the proposed Uber message?

## Evidence

[[uber-message]] is expected to carry a full parent-trade snapshot and event-specific publication attribution. The source mentions Protocol Buffers, sequence identifiers, a generation timestamp, and `Trade ID + Asof Time` retrieval, but supplies no schema or API contract.

## Required resolution

Confirm the producer, consumers, envelope structure, snapshot and event sections, identifiers, timestamps, version fields, Protocol Buffers usage, sequence/count semantics, error representation, and query response model.
---
type: concept
title: Ratan-LMS Action-to-Event Mapping
created: 2026-08-24
updated: 2026-08-24
tags: [action-event-mapping, ratan, lms, integration, cash-settlement]
related: [ratan, lms, surrounding-system-integration, lms-event-contract, what-is-the-authoritative-ratan-to-lms-action-and-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan Action and LMS Event Matrix.md"]
---
# Ratan-LMS Action-to-Event Mapping

## Definition

Ratan-LMS action-to-event mapping is the integration abstraction that associates an application action or state transition in [[entities/ratan|Ratan]] with an event exchanged with [[entities/lms|LMS]].

The referenced source appears to document this mapping through an Excel matrix, but the available extract does not expose the matrix rows or establish any authoritative mapping.

## Contract dimensions

A complete mapping should identify, for each action and event:

- the initiating actor or system;
- the trigger and preconditions;
- the action or lifecycle state;
- the event name and direction;
- payload fields and schema version;
- correlation and idempotency identifiers;
- delivery, retry, ordering, and acknowledgement behavior;
- failure, reconciliation, and audit handling;
- owning system and effective version.

These dimensions are requirements for workbook review, not facts established by the available source.

## Evidence boundary

The filename supports the existence and apparent purpose of an action-to-event matrix. It does not support claims about individual Ratan actions, LMS events, service ownership, or implementation semantics. Those claims remain open in [[queries/what-is-the-authoritative-ratan-to-lms-action-and-event-contract|What Is the Authoritative Ratan-to-LMS Action and Event Contract?]].
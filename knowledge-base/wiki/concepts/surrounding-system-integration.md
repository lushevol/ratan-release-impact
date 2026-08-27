---
type: concept
title: Surrounding-System Integration
created: 2026-08-24
updated: 2026-08-24
tags: [surrounding-system, integration, cash-settlement, system-boundaries]
related: [cash-settlement-home-page, ratan, lms, ratan-lms-action-event-mapping, lms-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan Action and LMS Event Matrix.md"]
---
# Surrounding-System Integration

## Definition

Surrounding-system integration describes the interactions, event exchanges, and responsibility boundaries between the Cash Settlement application area and adjacent systems. In this source context, the named systems are [[entities/ratan|Ratan]] and [[entities/lms|LMS]].

## Relevance to Cash Settlement

The source is stored under the Cash Settlement Home Page functional requirements for surrounding-system integration. Its referenced workbook appears intended to document how Ratan actions relate to LMS events.

The available source does not establish:

- which system initiates each interaction;
- whether exchanges are commands, notifications, or acknowledgements;
- the service or team responsible for processing;
- payload, transport, delivery, or recovery rules;
- the relationship to individual Ratan microservices.

## Documentation requirement

The integration boundary should be documented from the workbook and corroborating implementation sources. Event rows should remain attached to their exact action, system direction, ownership, and lifecycle context rather than being generalized across Ratan services.
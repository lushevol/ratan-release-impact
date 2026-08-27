---
type: concept
title: RATAN-LMS Entity Filter Removal
tags: [ratan, lms, cashflow-feed, eligibility, entity-filter]
related: [ratan, lms, manual-entity-lms-reference-data-feed, has-lms-confirmed-all-entity-ratan-feed-compatibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/LMS - Remove the entity filter in LMS feed.md"]
created: 2026-08-23
updated: 2026-08-23
---
# RATAN-LMS Entity Filter Removal

RATAN is required to remove the booking-entity-list check that previously governed whether a cashflow message was sent to LMS. The intended post-change rule is that [[ratan]] sends cashflow messages for all entities to [[lms]].

## Scope boundary

The change concerns feed eligibility only. The source explicitly states that the outbound SCBML 4.0 `CashflowData` message template remains unchanged. It does not establish changes to payload fields, XPath mappings, message version, error handling, retries, or reconciliation.

## Responsibility boundary

The recorded rationale is that LMS will handle entity treatment on its side. This is an intended responsibility allocation, not evidence that LMS acceptance, routing, prefixing, exception handling, or capacity has been validated.

The proposed LMS prefix handling for RATAN and other source systems remains unconfirmed. See [[has-lms-confirmed-all-entity-ratan-feed-compatibility]].

This requirement broadens the related [[manual-entity-lms-reference-data-feed]] context from manual-entity coverage to all-entity cashflow eligibility.
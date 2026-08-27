---
type: concept
title: Manual-Entity LMS Reference-Data Feed
created: 2026-08-23
updated: 2026-08-23
tags: [manual-entities, LMS, reference-data, settlement, onboarding]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/019 Feed Manual Entities to LMS.md"]
---
# Manual-Entity LMS Reference-Data Feed

## Definition

The manual-entity LMS reference-data feed is the intended transfer of manual-entity identification and branch data to [[lms]] so that the entities can be represented in a downstream settlement platform.

In the source, the reference-data population consists of 13 records with FMID, country code, FMCODE, and branch code. The source does not define the technical implementation of the feed.

## Source-Supported Scope

The roster spans 12 country codes and contains two separate Sri Lankan records. It includes both numeric and alphabetic branch-code values, including `UG` for `SCB UGANDA*KAM` and `QA` for `SCB DOHA*DOH`.

This concept extends [[manual-entity-settlement-onboarding]] with a concrete cross-country roster and supports [[manual-entity-settlement-enablement]] by identifying records expected to be available downstream.

## Undefined Contract Elements

The source does not specify:

- The publishing system or operational owner.
- Whether the feed uses an API, file, message, or another transport.
- The authoritative payload schema and field mapping.
- Mandatory versus optional fields.
- Validation rules for FMID, country code, FMCODE, or branch code.
- Acceptance responses, reconciliation, retry, idempotency, or synchronization behavior.
- UAT execution status or approval criteria.

The shared term LMS does not establish that this feed uses the same contract as [[cross-border-debit-lms-feed-contract]].
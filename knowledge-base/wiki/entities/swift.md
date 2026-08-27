---
type: entity
title: SWIFT
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall.md", "RATAN/RATAN -Core Function copy/RATAN-Settlement  6_SWIFT.md"]
tags: ["swift", "financial-messaging", "cash-settlement", "korea", "settlement", "bic", "static-data"]
related: ["korea", "korea-swift-mx-message-generation", "swift-mt-mx-integration", "ratan-settlement", "strategic-fm-list-swift-generation-control", "ratan-swift-reference-and-correspondent-derivation", "manual-entity-swift-mx-bifurcation", "swift-generation", "ratan", "5-ratan--25-ratan-core-function-copy--23-ratan-settlement-6swift--1r9j1mr"]
updated: 2026-08-24
---

# SWIFT

## Role in the sources

SWIFT is the financial-messaging domain for Korea entity configuration and settlement-message generation. The Korea Migration Functional Analysis identifies entity-level values for FMID, sender BIC, Field 53 BIC, Field 58 BIC, receiver BIC, and branch-code mapping.

For manual entities, the Go Live Checklist states that SWIFT-message generation depends on controlled static data for sender BIC, Field 53 BIC and currency, Field 58 BIC, country, branch, and FMID.

The RATAN Settlement source names SWIFT as its subject. Its filename places SWIFT in the context of RATAN Settlement, but the available source evidence does not establish whether SWIFT refers to a network integration, a message standard, a gateway, or a broader outbound-processing capability.

## Message scenarios and customization

The Korea Migration Functional Analysis references Flip MT202 and MT604/605 message scenarios. It asks whether Korea requires customized MT/MX behavior, but does not provide message specifications or confirm that customization is required.

The Go Live Checklist does not validate generated message output and does not reproduce the linked MX eligibility criteria.

## Configuration boundary

The Korea Migration Functional Analysis presents the listed fields as checklist requirements, with several explicitly marked mandatory for each entity. It does not provide actual values, applicable flows, validation rules, or implementation status.

The Go Live Checklist specifies required static-data categories for manual-entity SWIFT-message generation, but does not establish the corresponding message-output validation.

## RATAN source evidence boundary

The RATAN Settlement source does not provide verifiable details about message formats, message types, transport protocols, endpoints, validation rules, operational ownership, or settlement-workflow behavior. These details must not be inferred from the filename alone.

The related concept [[swift-generation]] captures the broader idea of producing SWIFT-format settlement messages. The exact relationship between that concept and SWIFT as named in the RATAN Settlement source requires review of the source body.

## Related pages

This page complements [[korea-swift-mx-message-generation]] and [[swift-mt-mx-integration]].
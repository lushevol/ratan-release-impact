---
type: query
title: Is the Korea SWIFT Static Data Complete?
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, SWIFT, static-data, settlement-message-routing]
related: [korea-static-settlement-configuration, seoul, korea-swift-mx-message-generation, swift-mt-mx-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/Static date summary.md"]
---
# Is the Korea SWIFT Static Data Complete?

## Question

Are the blank Field 53 BIC, Field 53 currency, and Field 58 BIC values intentional for SEOUL, or do they indicate incomplete SWIFT static data?

## Evidence

The source specifies sender BIC `SCBLKRSEXXX` for SEOUL FMID `10036645`. Field 53 BIC, Field 53 currency, and Field 58 BIC are blank. It also states that no BIC-netting rule is needed in RATAN for Korea.

The absence of a BIC-netting rule does not by itself establish that all blank SWIFT fields are intentionally omitted.

## Required resolution

Confirm the expected MT/MX message behavior for each blank field, including whether the fields are omitted, derived dynamically, or populated by another static-data source. Record the responsible owner and production validation evidence.
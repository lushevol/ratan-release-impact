---
type: entity
title: HKCS
created: 2026-08-23
updated: 2026-08-23
tags: [HKCS, HK-Commodity-Settlement, settlement, gold]
related: [scb-hk, hau, xau, hkcs-ratan-cis-api-integration, mt604-mt605-hau-message-customization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# HKCS

## Role

HKCS (HK Commodity Settlement) is the initiative under which SCB HK is expected to become a Gold Clearing Agent. Deals will be booked in SCB HK books, with gold represented as `HAU` rather than `XAU`.

## Scope

The source describes HKCS-specific changes to:

- Gold booking and settlement processing.
- RATAN MT604 / MT605 SWIFT customization.
- Nostro and Vostro static data.
- Approval limits and rounding.
- RATAN, CIS, LMS, MDS, and potential RDM impacts.

The source records requirements and confirmations, not implementation or go-live evidence.

## Source Reference

The linked ADO work item is [14724643](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14724643).
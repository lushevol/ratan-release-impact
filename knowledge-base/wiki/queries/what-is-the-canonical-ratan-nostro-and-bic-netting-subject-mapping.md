---
type: query
title: What Is the Canonical RATAN Nostro and BIC Netting Subject Mapping?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, ratan-one, authorization, static-data, bic-netting, nostro]
related: [ratan, ratan-subject-to-tile-authorization, ccil-non-guaranteed-client-static-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/How to apply for RATAN ONE access.md"]
---
# What Is the Canonical RATAN Nostro and BIC Netting Subject Mapping?

## Question

Does `RATAN_NOSTRO_BLOTTER` intentionally authorize both the `Static - Nostro Static` and `Static - BIC Netting Static` tiles, or should BIC Netting Static have a distinct request-subject identifier?

## Evidence

The access guide lists `RATAN_NOSTRO_BLOTTER` twice with different tile mappings. No explanatory note, alternate identifier, or role-to-subject permission matrix is provided.

## Why it matters

An incorrect subject identifier can result in missing access, over-broad access, or incorrect access-request routing for static-data functions.

## Resolution needed

Obtain the authoritative ServiceNow subject catalogue or RATAN ONE entitlement configuration, then confirm:

- whether one subject deliberately maps to both tiles;
- the canonical subject for BIC Netting Static if it is distinct; and
- whether existing access requests need remediation.
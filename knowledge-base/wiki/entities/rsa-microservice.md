---
type: entity
title: RSA microservice
tags: [ratan, stella, microservice, trade-validation, affirmation]
related: [ratan, fmrp-stella, trade-validation, ratan-fmrp-stella-interface]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# RSA microservice

## Role

The RSA microservice is described as the secure integration gateway between RATAN and Stella for:

- Trade validation.
- Trade rejection.
- Trade affirmation.

The source does not expand the acronym **RSA**.

## Scope boundary

The source separately identifies the Ratan Stella Ambassador for trade-lock status retrieval. It does not establish whether RSA and Ratan Stella Ambassador are separate deployments, logical components of one gateway, or overlapping services.

The API methods, security controls, channel behavior, and failure handling are not specified.

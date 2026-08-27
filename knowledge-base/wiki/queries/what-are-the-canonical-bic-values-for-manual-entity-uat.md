---
type: query
title: What Are the Canonical BIC Values for Manual-Entity UAT?
created: 2026-08-23
updated: 2026-08-23
tags: [bic, static-data, manual-entity-settlement, uat, routing]
related: [manual-entity-settlement-onboarding, mts-downstream-settlement-validation, scpay-settlement-routing, bahrain-scb-bahrai-man-gbs, qatar-scb-doha, scb-nigeria-lag-gbs, ghana-scb-ghana-acc-gbs, uganda-scb-uganda-kam-gbs]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/Manual entity (NG GH QA BH UG) testing with ISO.md"]
---
# What Are the Canonical BIC Values for Manual-Entity UAT?

The UAT log contains apparent BIC-length and branch-format inconsistencies, including `SCBLUS33XXX` versus `SCBLUS33XXXX`, `SCBLBHBMXXX` versus `SCBLBHBMAXXX`, and `SCBLBHBMXXXX`.

Establish authoritative sender and receiver BIC values for each country, message route, and environment. Validate whether the values are source transcription errors, intended branch identifiers, or configuration differences that could affect routing and downstream correlation.
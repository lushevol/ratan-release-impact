---
type: entity
title: KeyStore
created: 2026-08-23
updated: 2026-08-23
tags: [KeyStore, EBBS, EOD-testing, static-data]
related: [ebbs, razor, ratan, settlement-integration-static-data-readiness, static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis.md"]
---
# KeyStore

## Role

KeyStore was an operational testing and static-data dependency for EOD settlement processing.

## Q4 2023 activities

Carrie coordinated KeyStore-related work, including:

- Preparing UAT for EOD1 in November and EOD2 and EDO3 in January 2024.
- Receiving EBBS account mappings from RAZOR.
- Aligning test cases and test approach with the product owner and RAZOR team.
- Sending EOD1 test data to RAZOR on 2023-11-17 using HK cashflow data settled from production with payment date `20231016`.
- Reviewing nostro records that could not be found in EBBS.

On 2023-11-24, one EBBS mapping remained pending from the program team. The source does not identify the final authoritative mapping owner.
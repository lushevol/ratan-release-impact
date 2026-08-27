---
type: query
title: What Is the Canonical BIC for HKCS HAU SWIFT and Nostro Configuration?
created: 2026-08-23
updated: 2026-08-23
tags: [HKCS, HAU, BIC, SWIFT, RATAN, Nostro, configuration]
related: [hkcs, hau, ratan, mt604-mt605-hau-message-customization, hau-gold-settlement-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# What Is the Canonical BIC for HKCS HAU SWIFT and Nostro Configuration?

## Question

Which BIC is authoritative for the HKCS HAU flow?

## Conflicting Values

- Requirement Detail 3.1 specifies `BKCHHKHHGSI` as the SWIFT receiver.
- Requirement Detail 5 specifies `BKCHCHKHHGSI` as the Nostro Agent.

The source does not resolve whether one value is a typographical error, whether the values serve different roles, or which value should be used in RATAN and Nostro configuration.

## Required Resolution

Confirm the canonical receiver and Nostro-agent identifiers with the responsible operations, static-data, and SWIFT owners before configuration or deployment. The second value should also be checked for format validity because it appears longer than a standard 11-character BIC.
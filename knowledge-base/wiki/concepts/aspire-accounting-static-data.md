---
type: concept
title: Aspire Accounting Static Data
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, payment-accounting, bridge-account, psgl]
related: [aspire-payment-accounting, ratan, what-is-the-authoritative-ratan-aspire-static-data-source-and-change-governance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Aspire Accounting Static Data

Aspire accounting depends on entity FMIDs, country and PSGL mappings, branch codes, bridge accounts, and Nostro-account data. These values determine posting account selection and PSGL reference construction.

The supplied mappings cover BANGKOK, TAIPEI, OBU TAIPEI, SCS HK, NEWYORK, and JERSEY_BR. HONGKONG values are visibly struck through and must be treated as excluded. The SCS HK bridge-account mapping includes a struck-through value and a replacement value; Jersey is named `Jersey` in one mapping and `JERSEY_BR` in others.

The source does not identify an authoritative runtime source, owner, effective dates, approval workflow, or validation controls. These omissions create a financial-control risk and are tracked in [[what-is-the-authoritative-ratan-aspire-static-data-source-and-change-governance]].
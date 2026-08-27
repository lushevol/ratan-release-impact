---
type: entity
title: Indonesia/Jakarta Entity
created: 2026-08-22
updated: 2026-08-22
tags: [Indonesia, Jakarta, entity, branch, cash-settlement, onboarding]
related: [entity-branch-onboarding, cash-settlement, cash-settlement-2025-roadmap, indonesia-entity-onboarding-checklist, murex, fmrp, ratan, razor, lms, nds-auto-netting, ebbs, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2026 Indonesia Instance.md"]
---

# Indonesia/Jakarta Entity

## Overview

The Indonesia/Jakarta entity is the new entity instance covered by the [[indonesia-entity-onboarding-checklist]]. The source frames its onboarding as a coordinated extension of cash-settlement, routing, messaging, accounting, static-data, and operational processes.

The source does not establish the entity's official legal name, branch identifier, FMID, SWIFT BICs, accounting parameters, or final routing destination. These values must be confirmed before configuration is treated as complete.

## Systems and controls affected

The onboarding checklist identifies dependencies involving:

- [[murex]] cash migration through the H2 Adaptor batch solution.
- [[fmrp]] post-MO validation and cash-settlement processing.
- [[lms]] entity-filtered feed configuration.
- [[ratan]] SWIFT and accounting handling.
- [[razor]] strategic-flow routing.
- [[nds-auto-netting]] blacklist configuration.
- [[ebbs]] branch and transaction-type accounting setup.
- [[cashflow-blotter]] and dashboard branch dropdowns.
- SWIFT message generation, including sender, receiver, Field 53, Field 58, FMID, and branch mappings.
- Nostro/Vostro static data and branch-specific SSI setup.

## Configuration status

The checklist records firewall access for users in the new location as done. Other mandatory configuration values and ownership assignments are incomplete or absent. In particular, the source leaves routing scope, blacklist values, post-MO validation, and Indonesia-specific SWIFT and accounting values unresolved.

## Related investigation

Open scope questions are tracked in [[what-is-the-final-indonesia-routing-and-blacklist-scope]] and [[is-post-mo-validation-required-after-fmrp-migration]].

---
type: concept
title: Entity and Branch Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [onboarding, cash-settlement, configuration, implementation]
related: [vietnam-ifc-branch, fmrp, ratan, standard-settlement-instructions, ssi-stamping, nostro-static-management, release-cutoff-configuration, maker-checker-segregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# Entity and Branch Onboarding

Entity and branch onboarding is the coordinated setup of a new organizational identity across booking, settlement, messaging, accounting, user interfaces, security, testing, and downstream systems.

## Identity Model

Before implementation, stakeholders must distinguish among:

- Legal entity.
- Branch.
- Booking entity.
- FM entity.
- FMID.
- Accounting branch.
- SWIFT identity.

A source may use these terms interchangeably even though systems can model them differently. The [[vietnam-ifc-branch]] proposal illustrates this risk by describing a new branch and a new FMID or entity under [[scb-singapore]].

## Core Workstreams

### Scope and Routing

Confirm in-scope source systems, products, currencies, and workflows. Configure entity whitelists, cashflow suppression, and routing to the appropriate settlement or message platform.

### SWIFT

Obtain and configure the booking-entity FMID, sender BIC, Field 53 BIC, Field 58 BIC, receiver BIC, branch code, and any local message-template requirements.

### Settlement Accounting

Configure branch codes, transaction codes, bridge accounts, currency mappings, accounting suppression, and messaging dependencies. Standard onboarding may still require reusable platform development.

### Settlement Instructions and Static Data

Confirm [[ssi-stamping]], the applicable [[ssi-selection-hierarchy]], branch-specific SSI behavior, [[nostro-static-management]], Vostro requirements, and currency release cutoffs.

### Rules

Configure cashflow suppression, SWIFT suppression, NSTP, auto-debit, netting, BIC netting, shared Nostros, and internal-counterparty handling.

### User Interfaces and Access

Add the identity to application dropdowns and query functions. Configure firewall access and application or data entitlements separately.

### Testing and Release

Define SIT, regression, UAT, CPT, release preparation, sign-off authorities, and rollback arrangements. Person-day estimates do not replace dependency planning or acceptance criteria.

### Downstream Systems

Confirm reporting, ledger, liquidity, data, and management-information requirements. A checklist item marked “not required” should not override explicit unresolved integration dependencies.

## Deployment Patterns

High-volume static data and rules can be initialized with scripts deployed under a Change Request. Lower-volume or BAU changes can be maintained through a GUI under [[maker-checker-segregation]].

Copying another market’s settings is not sufficient. FMIDs, BICs, accounts, cutoffs, currencies, regulatory behavior, and downstream requirements must be approved for the exact entity being onboarded.
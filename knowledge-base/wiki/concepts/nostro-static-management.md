---
type: concept
title: Nostro Static Management
created: 2026-08-22
updated: 2026-08-22
tags: [nostro, static-data, settlement, operations]
related: [entity-branch-onboarding, standard-settlement-instructions, maker-checker-segregation, vietnam-ifc-branch, dev-team, ops-team]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# Nostro Static Management

Nostro static management controls bank-owned settlement-account data at legal-entity-and-currency granularity.

## Initialization Patterns

### Scripted Bulk Initialization

For projects requiring hundreds of rows, Settlement Ops provides reviewed static data in the `WMSUS.xlsx` format. The technical team then deploys the data to production by database script under a Change Request.

### GUI Maintenance

For lower-volume or BAU changes, the RTS team manually maintains the data through a GUI. Creation and approval require [[maker-checker-segregation]].

The source does not define the precise volume threshold separating these patterns.

## Onboarding Requirements

A new entity requires confirmed:

- Legal-entity identity.
- Currency.
- Nostro account.
- Account ownership and operational status.
- Any sharing arrangement with another entity.
- Review and approval evidence.
- Deployment owner and method.

Vostro static setup is distinct. In some cases, Vostro data can drive Nostro assignment, and over-account clients may require branch-specific [[standard-settlement-instructions]].
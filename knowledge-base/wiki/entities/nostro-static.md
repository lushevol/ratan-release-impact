---
type: entity
title: Nostro static
created: 2026-08-23
updated: 2026-08-24
tags: [nostro, static-data, notifications, ssi-stamping, cash-settlement, ratan, ui]
related: [ssi-stamping-service, ratan, cdups, vostro-nostro-ssi-selection, ratan-ui-dropdown-data-source, nostro-configuration, static-data-service, static-configuration-management, canonical-dropdown-data-source]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Nostro Static

## Notification role

According to the functional-requirement source, Nostro static is identified as the source of Nostro refresh notifications. When a refresh occurs, [[ratan]] identifies affected trades and the [[ssi-stamping-service]] re-stamps Nostro values and associated cashflow results.

That source does not identify the implementing system, interface, notification schema, ownership, or delivery protocol for Nostro static.

## UI and configuration role

According to the technical-design source, Nostro Static is a UI or configuration surface listed in the dropdown inventory. The document identifies a Quick Search control but does not provide a Topic value or data-source mapping for the row.

## Relationship to Nostro Configuration

The technical-design source suggests a relationship to [[nostro-configuration]] based on the name, but does not establish that relationship as an implementation fact. It also does not establish that [[static-data-service]] or [[ratan-static-data-service]] owns the control.

## Open validation

For the Quick Search control described in the technical-design source, the following require confirmation:

- Business field
- Option-set semantics
- Authoritative owner
- Serving API
- Refresh behavior
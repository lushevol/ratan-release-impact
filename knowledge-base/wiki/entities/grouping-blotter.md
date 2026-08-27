---
type: entity
title: Grouping Blotter
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UI - Indonesia/Indonesia.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
tags: ["user-interface", "cashflow", "grouping", "settlement", "cash-settlement", "indonesia", "microfrontend", "ratan", "ui"]
related: ["cashflow-blotter", "fxo", "cashflow-status-handling", "cashflow-status-and-substate-model", "cash-settlement-platform", "indonesia-ui-microfrontend-isolation", "ratan-ui-dropdown-data-source", "cashflow-dropdown-consistency", "ui-dropdown-data-source-governance"]
updated: 2026-08-24
---

# Grouping Blotter

The Grouping Blotter is a Cash Settlement user-interface surface named in the FXO onboarding checklist. The Indonesia UI design describes it as a Cash Settlement UI module with an Indonesia-specific navigation target.

The [[ratan-ui-dropdown-data-source]] inventory also lists Grouping Blotter as a Cash Settlement UI surface.

## Indonesia UI Navigation

According to the Indonesia-specific source design, `Dashboard[ID]` status cards should support opening `Grouping Blotter[ID]`.

The Indonesia-specific source design does not define:

- The URL.
- Route parameters.
- Authorization checks.
- The implementation boundary for the Indonesia module.

## Quick Search Controls

According to the [[ratan-ui-dropdown-data-source]] inventory, Grouping Blotter has Quick Search controls for:

- Booking Entity.
- Cashflow State.
- Cashflow Sub State.
- Cashflow Sub State Type.
- Group Status.

The inventory table structure leaves some topic associations implicit.

## Data-Source Governance

The Ratan UI dropdown-data-source document does not specify current or authoritative data sources for the Grouping Blotter controls.

Booking Entity and status-related selectors should be evaluated for semantic consistency with corresponding controls in [[cashflow-blotter]] and [[dashboard]].

The following remain open under [[ui-dropdown-data-source-governance]]:

- Authoritative owner.
- Serving API.
- Entitlement behavior.
- Refresh policy.

## FX Cashflow Requirements

According to the FXO onboarding checklist, FX cashflows for spot, forward, and swap transactions should:

- Appear in `SUSPENDED` status.
- Bypass MO validation.

The checklist spells the status as both `SUSPENED` and `SUSPENDED`; this page uses the normalized `SUSPENDED` form.

These requirements are specific to the named FX flows and should not be applied automatically to unrelated products. See [[cashflow-status-handling]] and [[fxo]].

## Unresolved Behavior

The FXO onboarding checklist does not specify:

- Why these cashflows are suspended.
- Which actor or event releases them.
- Whether MO validation bypass applies before or after grouping.
- How failures and exceptions are presented.
- Whether the behavior applies to all entities and branches.

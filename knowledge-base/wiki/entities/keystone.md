---
type: entity
title: Keystone
created: 2026-08-22
updated: 2026-08-23
tags: ["Keystone", "Hong-Kong", "accounting", "Nostro", "suspense", "system", "settlement", "account-mapping", "uat", "cash-settlement", "bcs", "data-refresh", "integration", "payment-accounting", "migration", "transition", "dependency", "delivery-planning"]
related: ["ebbs", "aspire", "settlement-accounting", "f2b", "bcs", "razor", "nostro-account-mapping", "production-data-refresh-for-uat", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-2023-q4-analysis--19-k--gr3d2u", "keystone-nostro-account-mapping", "what-was-the-approved-disposition-of-four-unmapped-hk-keystone-nostro-accounts", "payment-accounting-flow", "nostro-account-scope", "nostro-centralization", "nostro-stamping"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# Keystone

## Context and identity

The November 2023 supporting notes identify Keystone—also rendered as **KeyStone**—as the system or project context for activity concerning Hong Kong (HK) BCS data preparation, Nostro-account mapping, and a script under test. The activity involved data intended to be sent to [[razor]].

Separately, the Payment Accounting source uses Keystone as the transition boundary between two payment-accounting ownership models. That source does not define Keystone as a product, system, migration event, configuration change, or date.

The Nostro centralization source lists `Keystone` as an overlapping requirement and records a plan for Keystone to go live in February 2026. That source does not provide a dependency direction, interface relationship, replacement relationship, or sequencing decision. The February 2026 date is historical relative to the current wiki ingest date and should not be treated as a current delivery commitment without confirmation.

The available sources do not define:

- Keystone's architecture, ownership, expansion, or authoritative product name.
- The expansion or ownership of BCS.
- Interface specifications.
- Keystone's broader functional scope.
- Keystone's exact relationship to the wider Cash Settlement Home Page estate.
- Whether the Payment Accounting transition is determined by trade date, payment date, migration date, cashflow version, or another criterion.

> [!warning]
> Keystone is not confirmed to be the same system as [[keystore]]. The names must remain distinct unless corroborating evidence establishes their identity.

Further routing and migration rules require confirmation before the Payment Accounting transition boundary can be used as an implementation contract.

## Payment-accounting ownership transition

According to the Payment Accounting source, before Keystone:

- Aspire owns all HK, TW, and TH Nostro accounts.
- eBBS owns all Nostro accounts for CN, SG, IN, MY, AG, and UK.

After Keystone, HK ownership is divided by Nostro account type:

- eBBS owns HK Main Nostro.
- Aspire owns HK Suspense.

According to that same source, eBBS retains its original six-market scope, while Aspire retains all TW and TH Nostro accounts.

## Accounting flow in the F2B onboarding checklist

Separately, the F2B onboarding checklist references Keystone through a Hong Kong accounting arrangement involving Nostro, over-account, and suspense feeds. According to that checklist:

- Nostro and over-account information is fed to EBBS.
- Suspense information is fed to Aspire.
- The checklist raises a broader move from an Aspire model to an EBBS model.
- It also raises the handling of historic cashflows and past-value events after cutover.

The checklist does not resolve whether Aspire remains required for specific accounting classes.

## Recorded HK BCS supporting activity

The Keystone/BCS-specific activity described in the November 2023 supporting notes was intended to:

- Load production data.
- Update Nostro information.
- Send data to [[razor]].

The same source reports that a script was being tested for loading production data and updating Nostro information. It records receipt of account-mapping logic, outstanding mapping confirmations, and four accounts for which no mapping could be found.

## Known status and evidence boundary

Account-mapping logic was available but still had outstanding confirmations. Four accounts could not be mapped and were accepted as an exception by Naresh and an Operations user. See [[account-mapping-exception]].

The available record supports an in-progress HK data-preparation and mapping dependency only. It does not establish:

- Completed UAT.
- Successful Razor delivery.
- Production deployment.
- Final mapping completeness.

## Boundaries

The November 2023 supporting notes support only the Keystone/BCS-specific activity described in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-2023-q4-analysis--19-k--gr3d2u]]. They do not establish a relationship between Keystone and RATAN, Murex, or other settlement systems.

The Payment Accounting source's ownership-transition description remains distinct from the November 2023 supporting activity and from the F2B onboarding checklist's feed arrangement. The available sources do not establish that these descriptions represent the same implementation, event, or cutover mechanism.

The Nostro centralization source's overlapping-requirement listing and February 2026 go-live plan are also distinct from the Payment Accounting ownership transition, the F2B feed arrangement, and the November 2023 HK BCS supporting activity. That source does not establish that its planned go-live date represents the same implementation, event, or cutover mechanism.
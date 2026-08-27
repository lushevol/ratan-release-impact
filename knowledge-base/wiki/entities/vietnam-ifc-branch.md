---
type: entity
title: Vietnam IFC Branch
created: 2026-08-22
updated: 2026-08-22
tags: [vietnam, branch, proposed-entity, cash-settlement]
related: [scb-singapore, scb-vietnam, fmrp, ratan, ebbs, lms, entity-branch-onboarding, is-the-vietnam-ifc-branch-part-of-scb-singapore]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# Vietnam IFC Branch

The Vietnam IFC Branch is a proposed new branch in Vietnam’s International Financial Centre. The source proposes that it be established as a branch of [[scb-singapore]], not as part of [[scb-vietnam]], in response to a request from the VN government and the strategy for the Vietnam market.

## Status

The branch model is a draft proposal, not a documented final decision. It should therefore be treated as proposed until legal, architecture, and governance approval is confirmed through [[is-the-vietnam-ifc-branch-part-of-scb-singapore]].

The source uses “branch,” “entity,” and “new FMID” terminology without defining whether these represent the same identity across legal, booking, FM, accounting, and messaging contexts.

## Proposed Processing Scope

- New FMID or entity identity under SCB Singapore.
- [[fmrp]] flow only.
- Standard [[entity-branch-onboarding]] without customized business features.
- Strategic trade [[ssi-stamping]].
- Routing to [[ratan]] or [[razor]] according to configured suppression and whitelist rules.

Legacy LOANIQ and BCS flows, Murex batch migration, Pending Fixing, and NDS Auto Netting appear as reference material rather than confirmed branch requirements.

## Required Configuration

The proposed branch requires confirmed values for:

- FMID and FM code.
- Sender, receiver, Field 53, and Field 58 BICs.
- Branch code.
- Supported currencies and ISO mappings.
- Nostro accounts.
- Currency release cutoffs.
- EBBS bridge accounts and transaction codes.
- Settlement and suppression rules.
- GUI dropdowns.
- Firewall access and data entitlements.

None of these authoritative values is supplied in the source.

## Systems

The core processing path involves [[fmrp]], [[stella]], TDS3, and [[ratan]]. Accounting integration involves [[ebbs]] and a new [[solace]] topic or queue. The branch must also be added to [[cashflow-blotter]] and Dashboard query dropdowns.

Participation in [[lms]] and changes to RATAN EOD, SSDR, CIS, and FMMIS remain unresolved.
---
type: concept
title: Cash Settlement Entity Onboarding
created: 2026-08-22
updated: 2026-08-23
tags: [cash-settlement, onboarding, booking-entity, static-data, operational-readiness, entity-onboarding, RATAN, configuration-management]
related: [scb-hefei, static-data-readiness, payment-and-cashflow-suppression-governance, nstp-exception-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--27yb0b, entity-level-static-data-consolidation, cash-settlement-service-landscape, cash-settlement-platform, static-data-service, cashflow-blotter, ratan-static-cashflow-nostro]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/China Hefei Branch Setup.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md"]
---

# Cash Settlement Entity Onboarding

## Definition

Cash settlement entity onboarding is the controlled process of introducing a new booking branch or legal entity into the configuration and static-data domains required for RATAN and related Cash Settlement services.

The process enables the entity across the systems, static data, rules, accounting arrangements, user interfaces, and tests needed to settle its transactions. It is cross-functional because the entity must be recognized consistently by data services, workflow, accounting, Swift processing, LMS, and user interfaces.

## Current process problem

The technical-design source describes onboarding as a fragmented sequence of manual updates covering:

- Rule Engine validation configuration.
- Nostro Static setup.
- Currency release-time configuration.
- LMS feed inclusion or exclusion.
- Swift sender and correspondent BIC data.
- Branch-code mapping.
- Settlement accounting mappings.
- Cashflow Blotter GUI availability.
- Workflow STP whitelist configuration.

The stated consequences are manual effort, risk of error, lack of systematic validation, dependence on change requests, and a minimum onboarding lead time of two weeks. The source provides a qualitative problem statement rather than measured onboarding metrics; error rates, touchpoint counts, and representative lead-time data remain to be established.

## Control areas

A complete onboarding assessment should cover the following areas:

1. **Entity identity and distribution** — Booking identifier, entity code, branch code, and downstream entity-list feeds.
2. **Message routing** — Sender BIC, correspondent BIC, SWIFT field mappings, message variants, and branch-specific exceptions.
3. **Release and currency configuration** — Inherited or new release schedules, time zones, currency release-time settings, and currency-code mappings.
4. **Settlement accounting** — Branch and transaction codes, bridge accounts, account ownership, settlement accounting mappings, and posting validation.
5. **Static settlement instructions** — Global versus branch-specific SSI scope, Nostro assignment, and downstream propagation.
6. **Business rules and workflow** — Rule Engine validation, suppression, NSTP behavior, netting, counterparty conditions, workflow STP whitelists, and rule-deployment evidence.
7. **LMS and downstream feeds** — Inclusion or exclusion from LMS feeds and propagation to consuming services.
8. **User-interface availability** — Branch visibility in operational lists, blotters, dashboards, and the Cashflow Blotter GUI.
9. **Operational acceptance** — Downstream assessment, UAT, regression testing, approvals, effective-date confirmation, and production evidence.

## Evidence standard

A completed configuration task is not equivalent to production readiness. For each control area, evidence should identify:

- Target environment.
- Effective date.
- Configuration owner.
- Approval.
- Test case.
- Expected result.
- Actual result.

Where a checklist states that no configuration is needed—such as “No NSTP” or no new currency mappings—the absence of a change should still be regression-tested. This distinguishes intentional inherited behavior from an unverified omission.

## Target operating model

The technical-design source proposes self-service onboarding through a consolidated entity-level configuration model. A successful operating model would need to define:

1. Required fields and composite keys.
2. Field ownership and system-of-record rules.
3. Validation before activation.
4. Authorization and approval controls.
5. Audit history and rollback.
6. Propagation to each consuming service.
7. Coordination with separate Nostro Static setup.
8. Migration from existing service-specific configuration.

The proposed model is intended to consolidate the fragmented service-specific updates while preserving the controls required by each consuming service.

## Important boundaries and open requirements

Self-service onboarding should not be interpreted as unrestricted direct editing. The technical-design source does not specify maker-checker controls, effective dates, or authorization boundaries; these remain open design requirements.

Nostro Static remains a separate mandatory onboarding dependency. The proposal therefore reduces fragmentation but does not eliminate the need to coordinate multiple configuration lifecycles.

The source also does not establish measured error rates, touchpoint counts, or representative onboarding metrics. Those metrics remain to be defined before the operational benefits of consolidation can be quantified.

## Related architecture

Entity onboarding is a cross-cutting concern within the [[cash-settlement-platform]] and [[cash-settlement-service-landscape]]. It depends on [[static-data-service]] for branch-code mapping and on [[cashflow-blotter]] for GUI entity availability.

The proposed consolidation is described in [[entity-level-static-data-consolidation]]. The onboarding model also relates to [[ratan-static-cashflow-nostro]] through the separate Nostro Static dependency.

## Hefei example

The [[scb-hefei]] checklist illustrates the operational-readiness pattern. It includes defined SWIFT and EBBS branch mappings, but has unresolved bridge-account approval, an SSI-scope risk involving [[murex-211]], and no recorded UAT or regression results.

This example demonstrates why entity recognition and configuration completion must be assessed separately from evidence of approval, testing, and production readiness.
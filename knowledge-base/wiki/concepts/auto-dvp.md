---
type: concept
title: Auto DVP
created: 2026-08-23
updated: 2026-08-25
tags: [dvp, settlement-automation, cashflow, ratan, automation, release-onboarding, unresolved]
related: [ratan, ebbs, ebbs-rta-notification, receive-to-pay-cashflow-linkage, rta-cashflow-validation, dvp-nstp-exception-handling, auto-dvp-cashflow-cardinality, dvp-received-ui-indicator, chgxxx, ratan-new-onboarding-checklist-2026, ratan-onboarding-change-evidence, technical-go-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md", "RATAN/RATAN -Release copy/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_xx_xx_CHGXXX_Ratan Release - Auto DVP.md"]
---
# Auto DVP

## Functional definition

According to the functional requirements document `Auto DVP (eBBS).md`, Auto DVP is RATAN automation that closes an eligible pay cashflow's DVP exception after verified settlement of its linked receive cashflow.

The initial design is safety-first. A receipt event alone is insufficient: RATAN must pass all of the following checks before closing an exception:

- Event filtering.
- Product and scope eligibility.
- RTA-to-receive validation.
- Source-specific linkage.
- Pay status.
- Exact exception-code matching.
- Relationship-cardinality validation.

The successful action is limited to DVP exception closure and a `DVP Received` UI indicator. Auto DVP does not itself define an accounting action or authorize release of unrelated cashflows.

## Day 1 boundaries

For Day 1, the functional requirements define these boundaries:

- **Upstream source:** EBBS only.
- **Eligible event:** Receive-side `CorporateFinancial` RTA with `CreditDebitFlag=D`.
- **Eligible products:** Configured CCS Murex and Stella taxonomies.
- **Eligible exception codes:** Exact `DVP Strategy` or `DVP`.
- **Manual fallback:** Unmatched, invalid, ambiguous, withdrawn, failed, or excluded cases are handled manually.

Future design should allow configuration expansion to more countries, products, cross-border debit, external-bank accounts, and MT910 sources.

## Release-plan and onboarding context

The separate release-plan/onboarding document `2026_xx_xx_CHGXXX_Ratan Release - Auto DVP.md` provides naming and document-context evidence, but does not independently define the functional behavior described above.

In that document:

- `Auto DVP` is the named subject in the filename.
- The term appears in the [[ratan-new-onboarding-checklist-2026]] and the 2026 release-planning hierarchy.
- It is associated by filename with [[chgxxx]], whose identifier is also unresolved.

The release-plan/onboarding document does not establish whether Auto DVP is a RATAN service, integration, workflow, automation pattern, or business capability beyond the functional definition supplied by the separate requirements document.

Based solely on that release-plan/onboarding document, no claims can be made about:

- Functional behavior or business purpose.
- Interfaces, dependencies, or affected RATAN components.
- Deployment, testing, approval, or go-live status.
- Ownership or operational support.
- Whether `Auto DVP` is a stable product name or a temporary project label.

## Classification and evidence guidance

Keep Auto DVP separate from the placeholder change request [[chgxxx]]. A future source should classify Auto DVP as an entity if it is a named system or product, or retain it as a concept if it describes a workflow, method, or capability.

A reliable release and implementation definition requires the document body or an authoritative technical or release reference that explains the acronym, scope, implementation, owner, and onboarding requirements.
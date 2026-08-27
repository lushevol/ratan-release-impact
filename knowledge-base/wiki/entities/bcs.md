---
type: entity
title: BCS
created: 2026-08-23
updated: 2026-08-23
tags: ["settlement", "routing", "cash-settlement", "system", "identifier", "keystone", "nostro-account", "cashflow-flow", "legacy-flow", "ratan", "BCS", "Stella", "RAZOR", "settlement-process", "workflow", "Camunda"]
related: ["2025-tranche2-entity-onboarding", "cashflow-suppression", "razor", "ratan", "keystone", "nostro-account-mapping", "25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-2023-q4-analysis--19-k--gr3d2u", "fmsgw", "ratan-high-value-payment-control", "cashflow-affirmation-automation", "stella", "source-stack-flow-name-propagation", "lms", "ratan-camunda-starter", "camunda"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Platform - Co-development Guideline.md"]
---

# BCS

The available sources use BCS in multiple contexts and do not support a single synthesized definition.

- The onboarding and Keystone-supporting sources use BCS in a Keystone and nostro-account-mapping correspondence subject, without defining its precise expansion, ownership, interfaces, or overall role.
- The RATAN high-value-payment-control source characterizes BCS as a legacy cashflow flow within that source's scope.
- The LMS-feed source characterizes BCS as a settlement process associated with the `BCSSTELLA` stack-flow value.
- The co-development-guideline source describes BCS as a settlement project whose workflow was used as evidence for the [[ratan-camunda-starter|Ratan Camunda Starter]].

These source-specific characterizations must not be treated as a single definition of BCS.

## Keystone and nostro-account mapping context

The onboarding and Keystone-supporting sources use BCS in the correspondence subject `HK KeyStone BCS - Nostro account mapping`.

Those sources associate BCS with [[keystone]] and a nostro-account-mapping activity, but provide no further definition. BCS's role must not be inferred from that correspondence subject alone.

## LMS feed and Stella route

According to the LMS-feed source, BCS is the settlement process associated with the `BCSSTELLA` stack-flow value.

- The documented route is `BCSSTELLA → Stella`.
- [[razor|RAZOR]] is identified as the Swift/accounting system.
- Under the source's confirmed Proposal 1, the LMS source value for this route remains `STELLA`.
- The documented Tag20 prefix is `EQ`.
- The trade original source system is `TBC`.
- The source does not define a netting-resultant stack value for this route.

## RATAN high-value payment-control scope

According to the RATAN high-value-payment-control source, BCS is a legacy cashflow flow in scope for authorization and downstream-routing changes. This characterization applies specifically to the RATAN source and does not establish that BCS is the same type of entity or process implied by the Keystone correspondence, LMS-feed route, or co-development-guideline workflow example.

Its solution is deliberately narrower than the solutions described for [[fmrp]] and [[loaniq]]:

- A High Value exception in cashflow detail will not be built.
- USD-equivalent display in the Cashflow Blotter will not be built.
- Blotter and custom-filter capabilities based on cashflow thresholds will not be built.
- Authorization-limit controls are required for NSTP checker approval and failed-cashflow-release checker approval.
- An authorization-limit check for the single-level update-affirmation-status action was confirmed on 2026-08-13.

The RATAN source also states that BCS uses the same general STP/NSTP and user-attribution approach as FMRP, while noting that the exact actions and values remain unconfirmed. Its statement that NSTP applies where a cashflow has user manual touch must not be treated as equivalent to the FMRP exception-closure rule. See [[what-is-the-final-stpflag-and-lastuser-contract-between-ratan-and-fmsgw]].

## Camunda workflow evidence

According to the co-development-guideline source, BCS is a settlement project used as evidence for the [[ratan-camunda-starter|Ratan Camunda Starter]].

- The starter was demonstrated with a BCS settlement workflow.
- The meeting record states that the workflow had already been proven by the BCS project.
- This evidence supports reuse of applicable workflow patterns.

The co-development-guideline source does not establish that BCS and China Settlement have identical business requirements or operational constraints.
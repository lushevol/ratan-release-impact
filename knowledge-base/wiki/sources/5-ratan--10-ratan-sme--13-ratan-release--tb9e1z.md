---
type: source
title: RATAN Release Governance Process
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, release-governance, early-engagement, pre-cab, change-management]
related: [ratan, early-engagement, existing-flow-and-feature-change, hotfix-change-governance, pre-cab-release-governance, change-description-quality, authoritative-ratan-weekly-release-governance-calendar, ratan-hotfix-approval-and-release-plan-requirements]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
authors: []
year: 0
url: ""
venue: Internal process document
---
# RATAN Release Governance Process

This internal document describes the intended RATAN change-review and release-governance process agreed with each squad's change manager. It defines separate handling for NewOnboarding, ExistingFlow&Feature, and Hotfix changes, followed by a weekly Pre-CAB approval sequence.

The document is operational guidance rather than a fully controlled policy record: it identifies no owner, version, approval date, review cadence, or evidence of adoption. It must not be treated as proof that any individual `CHG` record completed the required controls.

## Change paths

### NewOnboarding

New features or interfaces identified through the end-of-quarter BRP require early awareness by the [[pss-manager]] and [[sme]]. Engagement must occur before VAT, and the TDA process must be followed.

The following Confluence resources are mandatory review materials during the change-review meeting:

1. [RATAN -Interfaces - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-Interfaces)
2. [RATAN -Core Function - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-Core+Function)
3. [New interface feature onboarding checklist - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/New+interface+feature+onboarding+checklist)

See [[early-engagement]] and [[new-onboarding-checklist]].

### ExistingFlow&Feature

A scheduled Thursday change-review meeting reviews changes planned for the next coming weekend. Required review inputs are:

- Business or issue background and technical details.
- The Pre-CAB checklist, including assessment of whether it needs updating.
- The RATAN Interfaces and RATAN Core Function Confluence pages.
- A valid, specific, and complete change description in [[snow]]; generic or missing descriptions are not acceptable.

See [[existing-flow-and-feature-change]], [[pre-cab-checklist]], and [[change-description-quality]].

### Hotfix change

For a hotfix, PSS must receive the business impact, urgency, and RCA. The document does not define emergency approval authority, rollback controls, emergency CAB treatment, or post-implementation review.

See [[hotfix-change-governance]].

## Pre-CAB engagement sequence

For the coming weekend release:

1. Pre-CAB is scheduled every Wednesday.
2. All concerns raised during Early Engagement must be closed.
3. All working items must be approved by the [[product-owner]] and [[tso]].
4. The [[sme]] gives first-level change approval by end of day Wednesday.
5. The Pre-CAB result is sent to [[jane]] for second-level change approval and work-item approval by 10 AM Thursday.

The document does not clarify whether PO and TSO approval precedes SME approval in all cases, whether Jane's work-item approval duplicates or supersedes PO/TSO approval, or where each approval is recorded.

## Release Plan gap

The source ends with a `Release Plan` heading but contains no plan content, template, ownership, deployment steps, rollback requirements, communications approach, validation activities, or post-release monitoring requirements.

## Open governance questions

- The intended weekly calendar remains ambiguous: the Thursday review is stated to cover the next coming weekend, whereas Pre-CAB occurs on Wednesday for the coming weekend. See [[authoritative-ratan-weekly-release-governance-calendar]].
- BRP, VAT, TDA, PSS, and TSO are not defined in the source.
- The source does not establish hotfix approval or release-plan controls. See [[ratan-hotfix-approval-and-release-plan-requirements]].
---

---FILE: wiki/entities/ratan.md---
---
type: entity
title: RATAN
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, settlement, release-governance]
related: [early-engagement, existing-flow-and-feature-change, hotfix-change-governance, pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# RATAN

RATAN is the system or programme governed by the release process documented in [[5-ratan--10-ratan-sme--13-ratan-release--tb9e1z]].

The documented process differentiates new interface or feature onboarding, changes to existing flows or features, and hotfixes. It requires early engagement, defined review artefacts, Pre-CAB readiness, and a staged approval sequence for weekend releases.

The source references RATAN Interfaces and RATAN Core Function documentation hosted in Confluence. It does not establish product ownership, technical architecture, or the expanded meaning of RATAN.
---

---FILE: wiki/entities/snow.md---
---
type: entity
title: SNOW
created: 2026-08-25
updated: 2026-08-25
tags: [snow, change-management, change-records]
related: [change-description-quality, existing-flow-and-feature-change]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# SNOW

SNOW is the change-record system referenced by the RATAN release-governance process.

For ExistingFlow&Feature changes, the change description in SNOW must be valid, specific, and complete. The process explicitly rejects overly generic or missing descriptions.

The source does not expand SNOW or confirm whether it refers to ServiceNow. It also does not specify whether approvals are recorded in SNOW.
---

---FILE: wiki/stakeholders/pss-manager.md---
---
type: stakeholder
title: PSS Manager
created: 2026-08-25
updated: 2026-08-25
tags: [pss, stakeholder, early-engagement, ratan]
related: [early-engagement, new-onboarding-checklist, hotfix-change-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# PSS Manager

The PSS manager is a required early-engagement stakeholder for RATAN NewOnboarding work. The role must be kept aware when a new feature or interface is defined through end-of-quarter BRP, before VAT.

For hotfix changes, PSS must receive the business impact, urgency, and RCA.

The source does not define PSS, identify an individual holder of the role, or state how acknowledgement and engagement are evidenced.
---

---FILE: wiki/stakeholders/sme.md---
---
type: stakeholder
title: SME
created: 2026-08-25
updated: 2026-08-25
tags: [sme, stakeholder, approval, ratan]
related: [early-engagement, pre-cab-release-governance, new-onboarding-checklist]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# SME

The SME participates in early engagement for RATAN NewOnboarding work and provides first-level change approval for the Pre-CAB process by end of day Wednesday.

The document states that all work items also require approval by the [[product-owner]] and [[tso]], but does not establish the exact ordering, delegation rules, or system of record for these approvals.
---

---FILE: wiki/stakeholders/product-owner.md---
---
type: stakeholder
title: Product Owner
created: 2026-08-25
updated: 2026-08-25
tags: [product-owner, po, stakeholder, approval]
related: [pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Product Owner

The Product Owner (PO) must approve all working items before progression through the RATAN Pre-CAB approval process.

The source does not identify the Product Owner, define approval criteria, or clarify whether PO approval must occur before SME first-level approval.
---

---FILE: wiki/stakeholders/tso.md---
---
type: stakeholder
title: TSO
created: 2026-08-25
updated: 2026-08-25
tags: [tso, stakeholder, approval, ratan]
related: [pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# TSO

TSO approval is required for all working items in the RATAN Pre-CAB process.

The source does not expand TSO, identify its accountable holder, or define whether its approval is independent of, or sequenced with, PO, SME, and Jane approvals.
---

---FILE: wiki/stakeholders/jane.md---
---
type: stakeholder
title: Jane
created: 2026-08-25
updated: 2026-08-25
tags: [jane, stakeholder, approval, pre-cab]
related: [pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Jane

Jane receives the RATAN Pre-CAB result by 10 AM Thursday for second-level change approval and work-item approval.

The source provides no surname, organisational role, delegation arrangement, or clarification of whether Jane's work-item approval duplicates or supersedes PO and TSO approval.
---

---FILE: wiki/concepts/early-engagement.md---
---
type: concept
title: Early Engagement
created: 2026-08-25
updated: 2026-08-25
tags: [early-engagement, change-governance, ratan, release-management]
related: [ratan, new-onboarding-checklist, existing-flow-and-feature-change, hotfix-change-governance, pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Early Engagement

Early Engagement is the upstream RATAN governance stage used to surface scope, impact, documentation, and review needs before Pre-CAB.

## Change-type-specific expectations

- **NewOnboarding:** Inform the [[pss-manager]] and [[sme]] when a feature or interface is defined through end-of-quarter BRP; engage them before VAT and follow the TDA process. Review RATAN Interfaces, RATAN Core Function, and the new interface feature onboarding checklist.
- **ExistingFlow&Feature:** Present business or issue background and technical details at the scheduled Thursday review. Review the Pre-CAB checklist and relevant RATAN Confluence documentation, and ensure the [[snow]] record has a specific and complete description.
- **Hotfix:** Provide PSS with business impact, urgency, and RCA.

## Pre-CAB closure gate

All concerns raised during Early Engagement must be closed before Pre-CAB. The source does not define the closure criteria, accountable verifier, required evidence, or escalation path for unresolved concerns.
---

---FILE: wiki/concepts/existing-flow-and-feature-change.md---
---
type: concept
title: Existing Flow and Feature Change
created: 2026-08-25
updated: 2026-08-25
tags: [existing-flow, feature-change, change-review, ratan]
related: [early-engagement, pre-cab-checklist, change-description-quality, pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Existing Flow and Feature Change

An ExistingFlow&Feature change is a RATAN change affecting an existing flow or feature. The documented process subjects these changes to a scheduled Thursday change-review meeting for changes planned for the next coming weekend.

## Required review inputs

- Business or issue background.
- Technical details.
- Review of the Pre-CAB checklist, including whether updates are needed.
- Review of RATAN Interfaces and RATAN Core Function documentation in Confluence.
- A valid, specific, and complete change description in [[snow]].

The source does not define eligibility boundaries between this change type and NewOnboarding, nor does it resolve the apparent timing ambiguity between Thursday review and Wednesday Pre-CAB. See [[authoritative-ratan-weekly-release-governance-calendar]].
---

---FILE: wiki/concepts/hotfix-change-governance.md---
---
type: concept
title: Hotfix Change Governance
created: 2026-08-25
updated: 2026-08-25
tags: [hotfix, change-governance, rca, ratan]
related: [early-engagement, ratan-hotfix-approval-and-release-plan-requirements]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Hotfix Change Governance

For a RATAN hotfix change, PSS must receive:

- Business impact.
- Urgency.
- RCA.

This is the full set of hotfix-specific controls stated in the source. It does not identify emergency approval authority, emergency CAB requirements, release timing, implementation evidence, rollback expectations, or post-implementation review requirements.

These missing controls are tracked in [[ratan-hotfix-approval-and-release-plan-requirements]].
---

---FILE: wiki/concepts/change-description-quality.md---
---
type: concept
title: Change Description Quality
created: 2026-08-25
updated: 2026-08-25
tags: [change-management, documentation-quality, snow, ratan]
related: [snow, existing-flow-and-feature-change, pre-cab-release-governance]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# Change Description Quality

For RATAN ExistingFlow&Feature changes, the change description in [[snow]] must be valid, specific, and complete. The release process explicitly says to avoid descriptions that are overly common or have missing information.

This requirement is a documentation quality control within change review. The source does not define an acceptance checklist, required fields, reviewer, or enforcement mechanism.
---

---FILE: wiki/queries/authoritative-ratan-weekly-release-governance-calendar.md---
---
type: query
title: What Is the Authoritative RATAN Weekly Release Governance Calendar?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, release-calendar, pre-cab, change-review]
related: [early-engagement, existing-flow-and-feature-change, pre-cab-release-governance, 5-ratan--10-ratan-sme--13-ratan-release--tb9e1z]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# What Is the Authoritative RATAN Weekly Release Governance Calendar?

## Question

How should the Thursday ExistingFlow&Feature review, Wednesday Pre-CAB meeting, Thursday 10 AM second-level approval, and intended weekend release be sequenced?

## Evidence

[[5-ratan--10-ratan-sme--13-ratan-release--tb9e1z]] states that:

- Thursday change review covers changes planned for the next coming weekend.
- Wednesday Pre-CAB is for the coming weekend release.
- SME first-level approval is due by end of day Wednesday.
- Jane receives the Pre-CAB result by 10 AM Thursday for second-level approval.

## Why this remains open

The wording can describe a review cycle preparing the following week's release, or overlapping release cycles. The document does not supply a calendar example, cut-off rule, or exception treatment.

## Needed evidence

- An approved RATAN release calendar with named release weekends.
- Meeting invitations or operating procedures identifying the release cycle each governance meeting supports.
- Evidence of handling when an item misses the Wednesday or Thursday deadline.
---

---FILE: wiki/queries/ratan-hotfix-approval-and-release-plan-requirements.md---
---
type: query
title: What Are the RATAN Hotfix Approval and Release Plan Requirements?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, hotfix, release-plan, change-governance]
related: [hotfix-change-governance, pre-cab-release-governance, 5-ratan--10-ratan-sme--13-ratan-release--tb9e1z]
sources: ["RATAN/RATAN -SME/RATAN Release.md"]
---
# What Are the RATAN Hotfix Approval and Release Plan Requirements?

## Question

What approval, implementation, rollback, communication, validation, and retrospective controls apply to RATAN hotfixes and planned releases?

## Evidence

[[5-ratan--10-ratan-sme--13-ratan-release--tb9e1z]] requires hotfixes to provide PSS with business impact, urgency, and RCA. Its terminal `Release Plan` section contains no further content.

## Gaps to resolve

- Emergency approval authority and emergency CAB requirements.
- Required risk assessment and implementation evidence.
- Rollback decision criteria, ownership, and tested procedure.
- Release communications and stakeholder notification.
- Post-deployment validation and monitoring.
- Post-implementation review requirements.
- Release-plan template, owner, and minimum required content.

## Needed evidence

- Approved emergency-change or hotfix procedure.
- RATAN release-plan template and completed examples.
- CAB or change-management standards governing emergency releases.
---

---FILE: wiki/log.md---
## 2026-08-25 ingest | RATAN Release Governance Process

- Ingested RATAN release-governance guidance covering early engagement, differentiated change paths, Pre-CAB approvals, SNOW description quality, and the undefined Release Plan section.
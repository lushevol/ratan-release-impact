---
type: concept
title: NAMS Nostro Account-Opening Workflow
tags: [nams, nostro, account-opening, workflow, static-data, approvals]
related: [nams, nostro-centralization, nostro-notification-and-refresh, nostro-static-data-migration, network-manager, nm-coe, what-is-the-nams-nostro-static-data-publishing-contract, what-is-the-nams-nostro-account-reuse-and-duplicate-prevention-rule]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# NAMS Nostro Account-Opening Workflow

## Definition

The NAMS Nostro account-opening workflow is the standardized process for initiating, approving, and setting up a Nostro account for an SCB entity. The source describes NAMS as the golden inventory for SCB and subsidiary Cash and Securities Nostro account details.

The documented lifecycle has three high-level stages:

1. Initiation.
2. Approval.
3. Account Opening or setup.

After submission, NAMS generates a case reference that the requestor must track until closure.

## Workflow inputs

The requestor identifies the account using:

- SCB Entity.
- Business Type.
- Currency.
- Provider Country.

The SCB Entity should be checked using **Name + Country + LEID**. If the entity is ambiguous, the relevant market’s [[stakeholders/network-manager]] should confirm the selection.

Business Type determines whether the request is for a Cash/Correspondent account or a securities account. The guide directs requestors to consult DOI for security-account business types.

## Existing-account reuse check

NAMS displays available Nostro accounts for the selected SCB Entity and currency in the relevant country. The requestor may select an existing account or choose **CREATE NEW**.

This is a user-facing reuse check. The source does not establish:

- The complete search key.
- Reuse eligibility criteria.
- A strict database uniqueness constraint.
- Whether duplicate creation is technically prevented.
- The approval treatment for exceptions.

These questions are tracked in [[queries/what-is-the-nams-nostro-account-reuse-and-duplicate-prevention-rule]].

## Account setup and governance

The request includes transaction-volume expectations, regulatory-purpose status, SSI classification, business ownership, reconciliation ownership, target balance, and business justification.

The requestor must explain why an existing account cannot be used. This justification supports subsequent approval rather than merely documenting a technical configuration value.

Service-provider selection is governed by the Network Manager. Existing providers may be selected; a missing provider may be proposed after consultation with the Network Manager, who has final authority on agent selection.

## Team and TP System routing

The guide states that Team and TP System selections are important because they trigger approvals and set up the account in the respective TP systems. However, it does not identify the available TP Systems, provide a routing matrix, or document the technical handoff.

No direct integration with [[entities/ssi-plus]], [[entities/ratan]], [[entities/keystone]], or [[entities/tlm]] should be inferred from this statement alone.

## Relationship to centralized Nostro data

The workflow supports [[concepts/nostro-centralization]] by placing account opening and amendment under a controlled NAMS process. The guide also states that NAMS publishes account static data to banking infrastructure.

The publication mechanism, consumer authority, event or batch contract, and refresh semantics are not documented. These are open questions in [[queries/what-is-the-nams-nostro-static-data-publishing-contract]].

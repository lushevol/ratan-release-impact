---
type: concept
title: Ratan Inter-Entity Netting Operational Readiness
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, operational-readiness, release-governance, resilience, monitoring]
related: [ratan, inter-entity-netting, chg0988640, inter-entity-netting-spot-rate-retrieval, is-inter-entity-netting-housekeeping-implemented-or-out-of-scope]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md"]
---

# Ratan Inter-Entity Netting Operational Readiness

## Overview

Operational readiness for the CHG0988640 release is assessed through a BPMS onboarding questionnaire. The checklist covers business scope, architecture, resilience, automation, monitoring, support, documentation, and change management for the extension of [[concepts/inter-entity-netting]] in [[entities/ratan]].

The document records intended controls and asserted completion, but many responses rely on “Follow RATAN current process” or placeholders rather than named runbooks, test artifacts, monitoring identifiers, owners, and approval dates.

## Release-specific commitments

The source states the following release-specific operating assumptions:

- Java 17, Spring Boot, and PostgreSQL on VM infrastructure.
- ADO CI/CD as the deployment mechanism.
- Active-passive DR with DNS-based switchover and no code change.
- 24x5 support coverage.
- ITRS coverage for services, APIs, GUI, and components.
- JSON logging for Splunk ingestion.
- CPU, memory, disk, and database capacity alerts at 70%.
- Three automatic retries for the new FMRP interface.
- Production file permissions of `640`.

These claims should be treated as commitments to verify for this release, not as platform-wide facts about all RATAN functionality.

## Readiness gaps

The source identifies or implies several gaps:

1. The new FMRP endpoint is a development/UAT URL rather than an evidenced production endpoint.
2. The cron scheduler timezone is unspecified.
3. The Phase 1 legal-entity pair list is ambiguous and appears to contain a duplicate.
4. Housekeeping is marked `NO`, while other sections claim all key operations are automated and that ASRM contains housekeeping details.
5. Naming conventions for code, Control-M, and folders are marked non-compliant without a dispensation or remediation plan.
6. The approval table is blank and the document retains placeholder owner and update fields.
7. Required resilience and release-test evidence is not attached or identified.

The housekeeping issue is tracked in [[queries/is-inter-entity-netting-housekeeping-implemented-or-out-of-scope]]. Scope normalization is tracked in [[queries/what-is-the-authoritative-chg0988640-phase-1-entity-pair-list]].

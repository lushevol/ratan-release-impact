---
type: source
title: "Ratan Inter-Entity Netting Operational Readiness Questionnaire (CHG0988640)"
authors: []
year: 2026
url: ""
venue: "BPMS New Feature Onboarding Operational Readiness Questionnaire"
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, inter-entity-netting, operational-readiness, release-management, CHG0988640]
related: [ratan, inter-entity-netting, inter-entity-netting-spot-rate-retrieval, ratan-inter-entity-netting-operational-readiness, chg0988640, fmrp, what-is-the-confirmed-day-1-entity-scope-for-inter-entity-netting, what-is-the-canonical-auto-netting-job-schedule-and-timezone]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan New Onboarding Checklist 2026/2026_05_30_CHG0988640_Inter Entity Netting.md"]
---

# Ratan Inter-Entity Netting Operational Readiness Questionnaire

## Source identity

This operational-readiness questionnaire covers the production onboarding of [[concepts/inter-entity-netting]] for [[entities/ratan]]. It identifies the release as Change Request `CHG0988640`, dated 30 May 2026, with Nick as DEV Owner/Lead and Jane as PSS contact.

The document is a release and onboarding checklist rather than a detailed functional or technical design. It frequently records asserted completion or reliance on the existing RATAN process without attaching test artifacts, named approvals, monitoring identifiers, or directly verifiable implementation evidence. Its evidence strength is therefore moderate to low for many controls.

The functional and architectural authority cited by the questionnaire is the [Inter Entity Netting Design](https://confluence.global.standardchartered.com/display/DSP/Inter+Entity+Netting). Related ADO work items are [12475532](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12475532), “Inter Entity Netting Development,” and [13374067](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13374067), “Inter Entity Netting - Withdrawal Event Handling.”

## Business scope and operating assumptions

The existing auto-netting function was already in production without inter-entity netting. This release introduces a new interface to obtain spot rates and adds inter-entity netting for internal users. No new users are introduced, and the stated product or asset scope is all products/assets.

| Metric | Source value |
|---|---|
| Average volume | `Avg 2k/day` |
| Peak volume | `Peak 1.5k/hour` |
| Business hours | `08:00 - 18:00 GMT` |
| Peak period | `09:00 - 12:00 GMT` |
| Release frequency | `Single` |
| Next upgrade | `NO` |
| Support coverage | `24x5` |

The source describes the rollout as Phase 1 followed by phased onboarding of the remaining entities. The supplied Phase 1 text is preserved below exactly as provided:

```text
SCB HONGKON*HKG||SCB LONDON*LDN
SCB LONDON*LDN||SCB TAIPOBU*TPE / SCB TAIPEI*TPE
SCB LONDON*LDN||SCB SG LTDACU*SIN / SCB SG LTD*SIN
SCB CN CHO*CHO||SCB HONGKON*HKG
SCB LONDON*LDN||STAN CHART AG*FRA
SCB LONDON*LDN||SCB SG LTDACU*SIN / SCB SG LTD*SIN
SCB DUBAI*DUB /SCB DUBAI DFC*DUB ||SCB LONDON*LDN
```

This list contains ambiguous aliases and an apparent duplicate London–Singapore pairing. It should not be treated as canonical configuration until validated against the functional design and the authoritative rule or static-data source. See [[queries/what-is-the-authoritative-chg0988640-phase-1-entity-pair-list]] and [[queries/what-is-the-confirmed-day-1-entity-scope-for-inter-entity-netting]].

## New spot-rate interface

The explicitly identified new integration is a spot-rate fetch interface for the official end-of-day USD rate:

```text
https://sabre-dev-cloud-global.uk.standardchartered.com/fmrp-fx-fxcs/uat/rate/{date}/OFFICIAL_EOD/USD
```

The questionnaire describes this as real-time, invoked by an inter cron task, with the following expression:

```text
0 0 1 * * TUE-SAT
```

The scheduler timezone is not stated. Although business hours are expressed in GMT, that does not establish that the cron expression is interpreted in GMT. The endpoint also contains `dev` and `/uat/`, so the document does not demonstrate that a production endpoint has been configured. Authentication, certificates, timeout, retry interval, idempotency, rate-date semantics, fallback behavior, and ownership are not specified. See [[concepts/inter-entity-netting-spot-rate-retrieval]], [[entities/fmrp]], and [[queries/is-the-chg0988640-fmrp-spot-rate-endpoint-production-ready]].

## Technology and registration

| Field | Value |
|---|---|
| Technology stack | `Java 17, Spring Boot, PostgreSQL` |
| Infrastructure | `VM` |
| CMDB | `Yes - ID: Ratan-51358` |
| ServiceNow | `Yes - ID: Ratan-51358` |
| ADO | `Yes - Project: FMQPR-51358` |
| Logging | `INFO, WARN, ERROR Configured`; JSON for Splunk ingestion |
| DR topology | `Active-Passive Configured` |
| DR switchover | `DNS Based, No Code Change Needed` |
| Retry behavior | `Auto Retry 3 times, the interface error will output error log` |
| Production file permissions | `640` |
| Certificate warning | `30 days prior` |
| ITRS privilege ID | `ITRS_ID_123` |

The source reports that code naming, Control-M naming, and folder naming do not follow standard conventions. It also states that no third-party vendor is used and that no new error codes are introduced.

## Resilience and exception-handling assertions

The questionnaire claims the following controls:

- Delivery is guaranteed through the API response.
- ACK/NACK is implemented at protocol level.
- Requests are validated against NFR and schema requirements before sending.
- The new interface retries automatically three times, then writes an error log.
- Existing RATAN processes handle infrastructure issues, single-message failures, technical recovery, and data-issue routing.
- All writes are atomic or transactional.
- No in-flight data is lost during graceful shutdown.
- Production and DR use an active-passive configuration.
- DNS-based DR switchover requires no code change.
- File download and re-download handling is not introduced by this release.

The checklist states that test evidence must be provided for each resilience checkpoint, but the supplied document does not identify the relevant test cases, artifacts, results, owners, or approval dates.

## Automation, monitoring, and support

The source claims that:

- ADO CI/CD is the deployment mechanism.
- ADO scripts support full-service and individual-service start/stop.
- DR switchover is available through a control-dashboard button.
- Server patching is automated through Ansible/ADO.
- Server reboot is automated through a change request.
- ITRS monitors all components, services, APIs, and GUI.
- Real-time interface connectivity uses heartbeat checks.
- Database, MQ, Kafka, network, disk, filesystem, query, and session health are monitored.
- CPU, memory, disk, and database thresholds are set at 70%.
- Trade volume, processing latency, intermediate-status trades, and MQ/Kafka queue depth are monitored.
- Certificate expiry alerts are set 30 days before expiry.
- BAU support is defined as 24x5.
- Production secrets are vaulted in Hashicorp and access is integrated with OneCert and MFA.
- PSS read-only access is available with file permissions set to `640`.

The monitoring assertions do not provide ITRS probe names, dashboard links, alert names, escalation routes, or incident-test evidence.

## Documentation and change-management evidence

The document asserts completion or availability of OLA, SLA, capacity planning, service recovery, application restore, backup certification, test-environment specification, ASRM, BRD, operational runbook, DASH onboarding, functional/regression/performance/DR/UAT/AIG sign-offs, implementation and rollback plans, scheduling, and PSS booking.

The supplied copy retains multiple placeholders, including:

- Blank DEV Lead and PSS Manager approval rows.
- `Last Updated: [Insert Date]`.
- `Owner: [Insert Name]`.
- `PSS SPOC: Name: XXX]`.
- `[Security Matrix ready]`.
- `[All Sign-offs Attached]`.
- `[Approved]`, `[Included]`, and `[Signed off]` statements without attached artifacts.

The source also contains an internal tension around housekeeping. Section 3.10 says `Housekeeping: NO`, `CRISP: NO`, and `ASRM: NO`, while Section 4.5 says all key operations are automated and Section 7.7 says housekeeping details were provided in ASRM. Section 3.11 additionally claims zero manual BAU tasks. This is tracked in [[queries/is-inter-entity-netting-housekeeping-implemented-or-out-of-scope]].

## Assessment

The questionnaire is useful evidence of the intended operational model and release commitments, especially the FMRP dependency, Phase 1 rollout, ADO deployment, active-passive DNS DR, 24x5 support, and monitoring thresholds. It is not sufficient on its own to verify production readiness. The most material unresolved items are the production FMRP endpoint and its failure semantics, the scheduler timezone, the normalized entity-pair matrix, the housekeeping contradiction, standards non-compliance, and the absence of named approval and test artifacts.

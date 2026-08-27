---
type: entity
title: ratan-rule-service
created: 2026-08-22
updated: 2026-08-25
tags: [ratan, rules, fmrp-uber, korea, microservice, nstp, exceptions, hard-blocker, rule-service, backend-service, cash-settlement, service, cn-rules, legacy, rule-engine, drools, api, optimistic-locking, jdbc, monitoring]
related: [ratan, chg1016055, fmrp-uber, rule-engine-trade-attributes, ratan-cash-settlement-netting, ratan-one, rule-service, swap-agent-coupon-interim-mtm-hard-blocker, auto-netting-rule-management, hard-blocker-exception, cashflow-suppression-rule, hard-blocker-go-live-checklist, ratanone-rule-service, rule-service-consolidation, cn-rule-prevalidation, ratan-suspended-cashflow-rule-filtering, fail-open-rule-service-evaluation, rule-semantic-compilation-risk, ratanone-settlement-orchestration-service, how-is-ratan-suspended-rule-conjunction-evaluated, what-is-the-ratan-suspended-rule-service-api-contract, ratanone, ratan-itrs-alert-triage, ratan-transient-failure-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md", "RATAN/RATAN -Monitoring/RATAN ITRS Log.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived/Rule Service Migration.md"]
---

# ratan-rule-service

## Overview

`ratan-rule-service` is a RATAN service that manages rule configuration and evaluation inputs and evaluates configurable Ratan rules.

The hard-blocker tech-design source describes it as managing rule exceptions and NSTP submit and approve processing for Ratan cashflows. The hard-blocker go-live-checklist source identifies it as a required Ratan back-end service.

The monitoring source additionally describes the service as handling rule-related operations, including closing affirmation exceptions through:

```text
POST /v1/nstpException/closeAffirm/...
```

Separately, the archived Rule Service Migration source identifies `ratan-rule-service` as the legacy service owning CN rules. That source proposes migrating those rules into [[ratanone-rule-service]]. It does not establish whether the service has been retired or migrated.

## Scope and Responsibilities

### Release-plan scope

The release-plan source lists the following scope:

- Add ten [[fmrp-uber]] fields for rule checks.
- Add fields for rule configuration.
- Add Korea confirmation upload support.
- Remediate recorded vulnerabilities.

### Archived CN-rule migration scope

The archived migration source identifies the following legacy service areas:

- Rule-maintenance APIs.
- Exception APIs.
- Profile Limitation APIs.
- Fields APIs.
- Frontend Validation Rule APIs.

That source proposes:

- Removing exception APIs and exception-to-rule relationships from the Rule Service.
- Moving Fields toward static data service ownership.
- Moving frontend Validation Rules toward static data service ownership.
- Migrating CN rules into [[ratanone-rule-service]].

The archived migration source also states that CN validation has category-specific preconditions, including:

- Third-party data for Special Rules.
- Exception checks before NSTP validation.

These migration and CN-validation statements are specific to the archived migration source and are separate from the release-plan scope.

## Suspended-Rule Filtering

The suspended-rule-filter tech-design source extends `ratan-rule-service` with the `RATAN_SUSPENDED` rule type and the following endpoint:

```text
POST /v1/ratanSuspendedRule/check
```

According to that source, the suspension filter uses rule-engine record `7444684846945615873333`, stored in `ratanone_rule_service.ratan_rule_engine` with status `LIVE`.

The same source states that the Camunda-based [[ratanone-settlement-orchestration-service]] calls the service after group-message processing. It further specifies that the caller handles timeout, unavailable-service, and unexpected-error outcomes fail-open; see [[fail-open-rule-service-evaluation]].

The suspended-rule-filter source leaves the API contract and the aggregation of Drools `matchedRules` unspecified. See [[what-is-the-ratan-suspended-rule-service-api-contract]] and [[how-is-ratan-suspended-rule-conjunction-evaluated]].

## Hard-Blocker and NSTP Processing

According to the hard-blocker tech-design source, the `SWAP_AGENT` hard-blocker design:

- Adds `HARD_BLOCKER` to `ExceptionCategory`.
- Checks for that category in `ExceptionServiceImpl` before allowing `/submit` or `/approve`.
- Prevents release from Ratan when a matching hard-blocker exception exists.

The acceptance scenarios in that source state that a matching hard-blocker exception does not prohibit every non-release operational action.

The hard-blocker tech-design source describes `ratan-rule-service` as a downstream enforcement layer:

1. Pre-netting validation is performed by [[ratan-cash-settlement-netting-service]].
2. Markers are exposed by [[ratanone-rule-service]].
3. The rule service applies downstream hard-blocker enforcement during submit and approve processing.

The archived migration source separately states that CN validation performs exception checks before NSTP validation. This is a CN-rule migration statement and should not be treated as a general replacement for the hard-blocker processing sequence above.

## Versions and Deployment Artifacts

The release-plan source specifies the following release artifact:

- Deployment step: `5`
- Branch: `release/v3.1.8`
- Package: `3.1.8-20260720.3`
- Pipeline run: `20260720.3`
- Owners: Yonghua Li and Chen Yang
- Rollback: recorded as existing

Separately, the hard-blocker go-live-checklist source specifies the following required deployment version:

| Service | Version |
| --- | --- |
| `ratan-rule-service` | `2.2.4.5` |

The go-live-checklist source does not provide deployment evidence, runtime status, ownership, or rollback instructions for this service. Its related database validation concerns suppression-field configuration and activated versions.

The release-plan artifact and the go-live-checklist version are reported separately because the sources provide different version details.

## Production Verification

The release-plan source specifies that PIT checks ten rule-engine records by ID:

- `7457997868871385088`
- `7457997381321293824`
- `7466305984159481856`
- `7482680514733842432`
- `7455188317088448512`
- `7457606136212160512`
- `7480462423639629824`
- `7455181677777846272`
- `7457602179788111872`
- `7457602978320678912`

The same release-plan source includes a separate rule-version UI check. Its textual result fields are not populated.

## Monitoring and Observed Failures

The monitoring source records an `OptimisticLockingFailureException` during close-affirm requests. According to that source:

- The root cause was identified.
- A fix was planned for the next release.
- The event was classified as having no business impact.
- No release identifier, deployment date, or post-release alert verification was recorded.

The monitoring source also records that the lifecycle service received an HTTP `500` response containing:

```text
Could not open JDBC Connection for transaction
```

That source does not confirm whether the JDBC-connection failure recovered.
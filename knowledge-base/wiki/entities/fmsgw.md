---
type: entity
title: FMSGW
created: 2026-08-22
updated: 2026-08-25
tags: [FMSGW, gateway, cash-settlement, UAT, UK, Prime, FM-Swift-Gateway, messaging, settlement-status, regression, swift, messaging-gateway, cashflow, settlement, message-gateway, payment-routing, queue-management, fm-settlement, ratan, solace, ratan-settlement, ratan-fmsgw-settlement-messaging]
related: [settlements-brp-prioritization, uk-strategic-cash-settlements-rollout, prime-trade-migration, ratan, strategic-settlements-platform, murex-cashflow-status-lifecycle, ratan-one, uber-regression-testing, regression-failure-triage, fmsgw-deletion-driven-cashflow-settlement, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--198hh9i, ratan-high-value-payment-control, stp-nstp-and-last-user-message-contract, high-value-payment-queue, high-value-payment-approval-queue, swift, solace, ratan-settlement, ratan-fmsgw-settlement-messaging, what-is-the-authoritative-ratan-fmsgw-interface-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md", "Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow status sync with FMSGW deletion.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md", "RATAN/RATAN -Interfaces/Ratan and FMSGW 54949.md"]
---

# FMSGW

## Identity and role

The Strategic Cash Settlements source identifies FMSGW as **FM Swift Gateway** and describes it as an external integration associated with [[ratan]].

The interface source for **Ratan and FMSGW 54949** identifies FMSGW as the recipient of RATAN-generated SWIFT settlement messages. Its documented logical path is:

```text
[[entities/ratan|RATAN]] → [[entities/solace|Solace]] → FMSGW
```

The Settlement Day2 cashflow-status synchronization requirement describes FMSGW as the downstream SWIFT messaging gateway in the documented Ratan flow. Ratan sends generated SWIFT messages to FMSGW and uses returned downstream status information to determine whether an interim `RELEASED` cashflow can become `SETTLED`.

The High Value Payment Control - RATAN requirement describes FMSGW as the downstream message gateway that receives settlement-message attributes from [[ratan]] and routes payment messages to processing queues.

FMSGW is also described in the RATANONE regression record as a messaging or gateway component appearing in the regression suite.

The 54949 interface source does not define whether FMSGW functions as a settlement gateway, onward-routing component, or settlement processor. It also does not define FMSGW ownership or the formal expansion of the acronym. The Strategic Cash Settlements source separately identifies the expansion **FM Swift Gateway**.

## 54949 message scope

According to the Ratan and FMSGW 54949 source, FMSGW receives two documented categories of real-time feed from RATAN:

- SWIFT MT messages
- SWIFT MX messages

That source records country coverage for both feeds, but does not specify individual message types, MX business messages, products, currencies, or legal entities.

The documented high-level integration relationship is therefore RATAN-generated SWIFT settlement messaging delivered through Solace to FMSGW. The 54949 source does not establish a more detailed message or processing scope.

## Settlements BRP tracker

The Settlements BRP tracker identifies FMSGW as a system or delivery stream supporting:

- Germany and UK UAT and release work
- Prime FIT/UAT support
- Roadmap activity

The tracker also lists a **FMSGW Roadmap** item for rolling out **RAZOR ALM**, noted as not part of SFMRP funding.

These tracker entries do not define FMSGW’s gateway interfaces, ownership, or processing responsibilities.

## Cash-settlement messaging and status

According to the Strategic Cash Settlements source:

- Acknowledgement and negative-acknowledgement notifications can reduce dependency on email from FMSRE or FMSGW.
- FM Swift Gateway status is one of the sources of cashflow sub-statuses.

According to the Settlement Day2 cashflow-status synchronization requirement, FMSGW participates in the Ratan cashflow-status synchronization flow. Returned downstream status information is used to determine whether an interim `RELEASED` cashflow can become `SETTLED`.

### FMSGW deletion and settlement

For the scoped deletion-related flow documented in the Settlement Day2 requirement, `FMSGW Deleted` is one member of the terminal-status allowlist.

In MT103/202 COV processing, both component messages must return an allowed status before Ratan settles the associated cashflow. See [[fmsgw-deletion-driven-cashflow-settlement]].

## High-value payment control

According to the High Value Payment Control - RATAN requirement, FMSGW is expected to distribute payment messages by payment-amount threshold to queues with differing approval requirements.

RATAN must supply routing-relevant STP/NSTP status and user attribution. The requirement leaves the final `stpFlag` and `lastUser` contract pending confirmation.

The source does not define:

- Numerical payment-amount thresholds
- Queue names
- Approval bands
- The final mapping between RATAN authorization profiles and FMSGW queues

See [[ratan-high-value-payment-control]] and [[what-is-the-final-stpflag-and-lastuser-contract-between-ratan-and-fmsgw]].

## RATANONE regression observation

The RATANONE regression suite exercised FMSGW through the `CN-API-FmsgwDeletion` cases within the amendment, error, rounding, and manual-settlement package.

The regression record reports a manual `202` response where the script expected `103Cov`. The item was classified as a likely script or expectation issue rather than established evidence of a FMSGW product defect. The associated case and API-log evidence should be reviewed before assigning release impact.

## Interface evidence and limitations

The 54949 interface source names Solace as the transport but provides no details for:

- Topics, queues, or endpoints
- Authentication
- Schemas
- Acknowledgements
- Retry behavior
- Dead-letter handling
- Sequencing
- Duplication handling
- Monitoring
- Recovery

It should therefore be treated as evidence for a high-level integration relationship rather than as the authoritative FMSGW interface contract. See [[ratan-fmsgw-settlement-messaging]] and [[what-is-the-authoritative-ratan-fmsgw-interface-contract]].

The Strategic Cash Settlements source does not specify the message contract, ownership, or production status.

The Settlement Day2 cashflow-status synchronization requirement documents the scoped Ratan synchronization and deletion-related settlement behavior described above, but does not by itself establish broader FMSGW ownership or production status.

The High Value Payment Control - RATAN requirement does not define the numerical routing thresholds, queue names, approval bands, final authorization-profile-to-queue mapping, or final `stpFlag` and `lastUser` contract.

The RATANONE regression record likewise does not establish that the reported response mismatch was caused by a FMSGW product defect.
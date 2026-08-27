---
type: entity
title: CDUPS
created: 2026-08-22
updated: 2026-08-24
tags: [cdups, settlement-instructions, integration, xml, ssi, repository, fmrp, SSI-stamping, interface, system, confirmation, trade-settlement, client-documents, cashflow, email-distribution, settlement, UBER, upstream-system, trade-processing, trade-confirmation]
related: [korea, korea-ssi-onboarding, ssi-stamping, ssi-selection-hierarchy, fmrp, ratan, f2b-hk-tw-milestone-checklist, fmrp-prime-uk-uat-drop-2, f2b, stella, standard-settlement-instructions, ssi, trade-ssi-stamping, ssi-stamping-notification, fixing-notice-ssi-override, cdu, ssi-stamping-service, latest-cashflow-ssi-result, cdups-ssi-stamping-integration, solace, outbound-affirmation-email, email-distribution-audit, cashflow-affirmation-automation, uber, trade-level-ssi-stamping, product-agnostic-ssi-stamping, scbml, ssi-stamping-and-best-match, cashflow, tds3, fm-edmi, ratan-cdups-trade-confirmation-flow, ratan-cdups-econaffirm-acknowledgement, operational-level-agreement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - HK & TW.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/Trade SSI Stamping - Product templates.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Strategic SSI Stamping Design/SSI Stamping Implementation(SCBML).md", "RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md"]
---

# CDUPS

CDUPS, also written as **CDU PS** in interface identifiers, is referenced as a trade-confirmation, settlement-instruction, and client-document integration platform. The sources describe it in several integration roles. These roles are retained separately because the sources do not establish that every role belongs to the same interface direction or finalized architecture.

## Roles in the RATAN integration

The *Ratan and CDUPS 51512* source describes CDUPS as the trade-confirmation platform participating in the RATAN integration. According to that source, CDUPS:

- Calls RATAN for trade SSI stamping.
- Confirms Murex, BCS, and FMRP trades.
- Sends trade-confirmation events to TDS3 for Murex trades.
- Sends BCS trade-confirmation information directly to RATAN because TDS3 does not contain the relevant data.
- Calls [[stella]] for the FMRP path.
- Consumes `EconAffirm` status from RATAN and returns an ACK or NACK.
- Sends trade messages that [[cdu-is]] can consume.

That source states that routing and downstream behavior depend on the trade population; the Murex, BCS, and FMRP paths are distinct.

## Roles in SSI-stamping flows

### Upstream caller in the SCBML implementation

The *SSI Stamping Implementation (SCBML)* source describes CDUPS as the upstream caller for trade SSI stamping in the documented RATANONE flow:

1. CDUPS sends SCBML to the trade SSI-stamping API.
2. RATANONE parses the required trade information.
3. RATANONE applies shared SSI best-match logic.
4. RATANONE returns enriched SCBML to CDUPS.

That source does not specify CDUPS ownership, transport, endpoint details, authentication, or delivery and retry semantics.

### Downstream interface, recipient, or consumer in other flows

The F2B onboarding-checklist sources identify CDUPS as a downstream interface, recipient, or destination for trade SSI stamping. In these flows, stamped settlement instructions are sent to CDUPS through XML and product-based logic.

The *Trade SSI Stamping - Product templates* source describes CDUPS as the confirmation client in the [[fmrp]] flow. According to that source, CDUPS queries [[ratan]] for trade SSI-stamping confirmation.

The *Trade Cashflow SSI Stamping on Uber Message* source describes CDUPS as a consumer of RATAN's SSI-stamping capability for client-document generation.

The *Strategic SSI Stamping Design* describes CDUPS as an external stamping and integration system with which RATAN is intended to communicate using [[uber|UBER]].

## Trade SSI-stamping and confirmation behavior

According to the *Trade SSI Stamping - Product templates* source, CDUPS:

- Submits trade identity, version, temporal, entity, settlement, and leg data to the trade SSI-stamping service.
- Requests confirmation on an ad-hoc, call-based basis following relevant SSI or trade changes.
- Queries the latest cashflow SSI when a post-trade cashflow stamp may differ from the trade SSI.
- Retries RATAN `500` responses, timeouts, and no-response conditions using the same trade ID and major version.

The *Trade Cashflow SSI Stamping on Uber Message* source likewise states that CDUPS requires access to the current cashflow-level SSI result because a cashflow may have a different SSI from an earlier trade-level result. CDUPS is expected to query the latest result when required.

### Refresh and re-stamping

The *Trade SSI Stamping - Product templates* source does not describe CDUPS as a subscriber to automatic Vostro or Nostro refresh publications. Instead, it specifies selective response behavior driven by CDUPS calls.

The *Trade Cashflow SSI Stamping on Uber Message* source describes Vostro refresh, Nostro refresh, and approved Settlement Ops remediation as re-stamping triggers rather than normal proactive CDUPS notifications.

### Fixing Notice handling

The *Trade SSI Stamping - Product templates* source states that Fixing Notice handling provides CDUPS with the latest cashflow SSI result before the general SSI result. See [[fixing-notice-ssi-override]].

## RATAN request model and UBER integration

The *Strategic SSI Stamping Design* proposes a CDUPS request model containing:

- Trade identity
- Major version
- Trade date
- Booking entity FMID
- Counterparty FMID
- CFI
- Repeated currency references
- Repeated payer-party references

That source does not establish whether this proposed request model is the final external API contract.

### Uber-message delivery

The *Trade Cashflow SSI Stamping on Uber Message* source states that a post-stamped `uber` response may be sent to CDUPS through [[solace]].

However, that source also notes that another meeting note names [[cdu]] as the recipient. The distinction between CDUPS and CDU as the `uber` response recipient remains open.

## Interface identifiers

The *Ratan and CDUPS 51512* source identifies the following FM-EDMi JMS-JSON flows:

```text
v1/post-trade/51358-ratanone/cdups/json-1.0/ecoaffirm/pub

q-51358-cdups-ratanone-ack

[CDU PS] v1/post-trade/51512-cdups/ratanone/json-1.0/ack/pub
```

That source does not provide message schemas, authentication details, correlation rules, or a complete ACK/NACK reason contract.

## Onboarding, delivery, and validation

The onboarding-checklist sources specify XML and product-based trade SSI stamping to CDUPS. New products, entities, currencies, settlement methods, or SSI hierarchy changes may require updates to CDUPS mappings and validation of the XML payload.

Validation should identify or verify the following, as applicable to the onboarding flow:

- The stamped SSI
- The product association
- The correct CFI code
- The settlement method
- The applicable agent configuration
- Delivery through the required XML and product-based paths

The general F2B milestone onboarding source does not provide a field-level CDUPS schema or evidence that a particular change was implemented. The Prime Day 2 source defines its validation as a required scenario but supplies no execution evidence.

### Prime Day 2 product scope

The Prime Day 2 checklist specifically requires XML and product-based trade SSI stamping to CDUPS for:

- IRS
- CCS
- Loan Depo

### Korea cashflow migration

The Korea cashflow-migration checklist states that trade SSI stamping feeds CDUPS through XML and product-based logic. This is relevant to validating whether Korea’s SSI onboarding path and the `KRO`-to-`KRW` transformation reach downstream settlement-instruction processing correctly.

The Korea source does not specify:

- The CDUPS interface schema
- Korea-specific CDUPS changes

### HK/TW F2B onboarding

The HK/TW F2B onboarding checklist requires trade SSI stamping to CDUPS through both XML and product-based flows.

Testing should verify that:

- SSI is automatically attached for IRS, CCS, and Loan Depo.
- The correct CFI code is captured for each of those products.
- CDUPS receives the stamped SSI through the required XML and product-based paths.

The HK/TW source does not specify:

- CDUPS schemas
- Delivery acknowledgements
- Retry behavior
- Reconciliation controls

## Outbound cashflow-affirmation email distribution

According to the *Email Affirmation Automation Tech Design* source, CDUPS is an existing email-distribution capability proposed for reuse in the outbound cashflow-affirmation flow.

For this flow, RATAN is expected to submit affirmation-email requests to CDUPS through [[solace]]. The design requires auditability for both:

- Submission of the request to CDUPS
- CDUPS sending the email to the client

The design also requires a distribution acknowledgement or negative acknowledgement mechanism.

That source does not define:

- Recipient selection
- Message schema
- Acknowledgement payloads
- Retry behavior
- Idempotency
- Delivery confirmation
- Failure handling

See [[outbound-affirmation-email]], [[email-distribution-audit]], and [[what-is-the-cdups-affirmation-email-acknowledgement-contract]].

## Related systems and processes

CDUPS is referenced in the context of [[ssi-stamping]], [[stella]], [[fmrp]], and the broader [[entity-branch-onboarding]] process. It is also discussed alongside [[scbml]], shared SSI best-match processing, [[cashflow]], and the RATANONE integration through [[uber|UBER]].

The trade-confirmation interface source additionally places CDUPS in relation to TDS3, FM-EDMi, [[stella]], and [[cdu-is]]. These relationships apply to the trade-confirmation integration described in that source and should not be generalized to every SSI-stamping or cashflow flow.
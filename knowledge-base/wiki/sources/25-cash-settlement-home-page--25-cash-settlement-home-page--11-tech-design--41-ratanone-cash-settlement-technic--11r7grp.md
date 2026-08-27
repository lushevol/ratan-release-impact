---
type: source
title: Ratan Accounting Service with EBBS Technical Live
authors: []
year: 2024
url: ""
venue: "RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, accounting-service, ebbs, solace, technical-live, cpt]
related: [ratanone, accounting-service, ebbs, solace, message-bridge, technical-live-versus-business-live, accounting-file-delivery-acknowledgement, full-accounting-tech-live-vs-mocked-solace-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Ratan Accounting Service with EBBS Technical Live

## Summary

This document presents two alternative technical-live and CPT scopes for validating the integration between Ratan, the Ratan Accounting Service, EBBS, and Solace. It is a planning and progress record, not evidence that either option was formally approved or successfully completed.

Option 1 validates the complete accounting path: Ratan payment processing, accounting-feed generation and publication, Solace integration, EBBS acknowledgement, and an accounting update on the originating cashflow.

Option 2 validates a narrower messaging path. Ratan publishes a mocked EBBS JSON feed directly to a Solace topic, EBBS returns an acknowledgement, and Ratan consumes the acknowledgement. This option does not demonstrate that the Accounting Service can generate a valid feed from an actual payment or that the acknowledgement produces an accounting update.

## Original Plan

| | Option 1 Ratan/EBBS tech live together | Option 2 Ratan tech live on Solace integration only |
| --- | --- | --- |
| Details | Ratan to tech go live accounting service. Then the front to back processing could be verified, such as Ratan processing, Solace integration and EBBS setup 1. Lifecycle service 2. Accounting Service 3. Static Data service 4. Message bridge 5. Query service 6. Service Properties 7. Static 1. Nostro 2. Static (transaction/bridge) 3. Rules (keep production version, no change) | Ratan tech go live the integration with Solace only, and mock dummy ebbs feed to verify solace integration and EBBS setup only 1. Message bridge 2. Service Properties |
| CPT plan | 1. Ratan to mock a dummy payment with cashflow id CPTCF0000001, trade id, CPTTRADE0001 for IN entity, with a back value date 2. User manual fail the payment 3. Expectation 1. Ratan generate & publish accounting feed to EBBS 2. EBBS ACK back to Ratan 3. Accounting update on the dummy cashflow | 1. Ratan to mock a dummy EBBS feed (json) directly and publish to the solace topic 1. CFID: 00 2. Trade id: 00 2. Post new and reversal 3. Expect EBBS ACK back and Ratan consume the ACK |
| CPT condition | Amount < 0.001 2024-05-27 check with Karthick whether amount is OK Entity FMID for IN | |
| Progress | 2024-05-24 Deployed on UAT 2024-05-27 Regression in progress | |
| | | |

## Option 1: Ratan and EBBS Technical Live Together

The first option includes the Lifecycle Service, Accounting Service, Static Data Service, Message Bridge, Query Service, Service Properties, Nostro static data, transaction and bridge static data, and the existing production rule version without changes.

The proposed CPT flow is:

1. Ratan mocks a payment for the IN entity using cashflow ID `CPTCF0000001`, trade ID `CPTTRADE0001`, and a back value date.
2. A user manually fails the payment.
3. Ratan generates and publishes an accounting feed to EBBS.
4. EBBS returns an ACK to Ratan.
5. The originating dummy cashflow receives an accounting update.

The recorded condition was `Amount < 0.001`. On 2024-05-27, the document still required confirmation with Karthick that the amount was acceptable, and the applicable entity FMID for IN was not specified.

The progress record states that the option was deployed on UAT on 2024-05-24 and that regression was in progress on 2024-05-27. No test results, ACK payloads, accounting-update evidence, or sign-off are included.

## Option 2: Ratan and Solace Integration Only

The second option limits the technical live to the Message Bridge and Service Properties. Ratan directly mocks an EBBS JSON feed and publishes it to the Solace topic.

The proposed mock feed contains:

- `CFID: 00`
- `Trade id: 00`
- A new posting
- A reversal posting

The expected result is that EBBS acknowledges the feed and Ratan consumes the ACK. The document does not identify the publisher component, production schema compatibility requirements, topic or header contract, ACK correlation key, or the accounting consequence of the reversal.

## Evidence Boundaries

The document establishes the proposed scope and the stated UAT/regression status. It does not establish:

- Formal approval of either option
- Successful completion of regression
- Production or business go-live
- The authoritative IN entity FMID
- Whether `Amount < 0.001` is a valid acceptance condition
- The accounting-feed and ACK schemas
- Retry, timeout, duplicate, NACK, or reversal-processing semantics

## Related Context

The plan is related to [[concepts/technical-live-versus-business-live]], [[concepts/accounting-file-delivery-acknowledgement]], and [[concepts/static-configuration-management]]. It is also relevant to [[entities/ebbs]] and [[entities/accounting-service]]. Its EBBS/Solace scope should not be generalized to Aspire or FileIT operating assumptions documented elsewhere.
---
type: entity
title: Solace
created: 2026-08-22
updated: 2026-08-24
tags: ["messaging", "integration", "accounting", "Solace", "trade-confirmation", "Murex", "payment-accounting", "transport", "trade-data", "murex-211", "tds3", "ratan", "message-broker", "queueing", "cash-settlement", "performance", "ebbs", "ratanone", "cdups", "event-driven-integration"]
related: ["vietnam-ifc-branch", "ebbs", "ratan", "settlement-accounting", "cdu-lake", "cashflow-migration-readiness", "ebbs-payment-accounting-integration", "cdups", "outbound-affirmation-email", "cashflow-affirmation-automation", "tds3", "murex-211", "what-is-the-authoritative-tds3-to-ratan-solace-topic-contract", "what-is-the-cdups-affirmation-email-acknowledgement-contract", "solace-queue-splitting-for-asset-class-workloads", "queue-throughput-metric-definition", "25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--30-s--3u93uv", "ratanone", "accounting-service", "message-bridge", "solace-based-ebbs-acknowledgement-integration", "fm-edmi", "ratan-interface-architecture", "ratan-ebbs-accounting-feed", "what-is-the-canonical-ratan-to-ebbs-interface-contract"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/solace queue split PT for Uber.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md", "RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md", "RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
---

# Solace

Solace is a messaging technology referenced by the source documents for payment-accounting integration, trade-confirmation and cashflow processing, affirmation-email integration, an Uber staging performance test, and RATAN-CDUPS trade flows.

## Payment accounting

### Ratan and EBBS transport

The *Cash Settlement - EBBS Accounting* functional-requirement source specifies Solace as messaging middleware for real-time transport between [[ratan]] and [[ebbs]]. It establishes Solace as the intended transport for JSON accounting messages.

The `RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md` source similarly describes the intended real-time accounting-feed route as:

```text
Ratan →Central solace ->Ebbs
```

According to that source, Solace is an intermediary transport in [[ratan-ebbs-accounting-feed]], rather than the accounting-message producer or consumer.

Separately, the *Tech Live of Ratan - Accounting Service with EBBS* technical-live plan identifies Solace as the messaging transport in both proposed Ratan technical-live options for accounting integration with [[ebbs]]:

- **Option 1:** Ratan publishes an accounting feed through the Solace integration and receives an EBBS ACK through the Ratan integration path.
- **Option 2:** Ratan directly publishes a mocked EBBS JSON feed to a Solace topic. EBBS is expected to acknowledge the feed, and Ratan is expected to consume the ACK.

#### Undocumented interface and broker configuration

The *Cash Settlement - EBBS Accounting* functional-requirement source does not define delivery guarantees, queue configuration, ordering, dead-letter behavior, or operational monitoring.

The technical-live source does not specify the Solace topic, message headers, schema version, credentials, correlation key, delivery guarantees, retry policy, timeout, duplicate handling, or NACK behavior. These details are tracked by [[what-is-the-authoritative-ebbs-solace-feed-and-acknowledgement-contract]].

The `RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md` source additionally does not identify the Solace environment, broker deployment, topic, queue, subscription, authentication mechanism, access-control model, delivery guarantee, retry behavior, or dead-letter process. That source states that these details must not be inferred from Solace's presence alone. See [[what-is-the-canonical-ratan-to-ebbs-interface-contract]] for the required contract clarification.

### Vietnam IFC branch accounting integration

The Vietnam entity-onboarding source identifies Solace as the messaging technology required for accounting integration for the proposed [[vietnam-ifc-branch]].

That source anticipates:

- A new Solace topic or queue.
- Adaptation of the accounting service so the new entity can generate [[ebbs]] accounting.

This work is treated as mandatory `Config/Dev` activity.

The source does not provide the topic or queue name, message contract, ownership, capacity requirements, security configuration, deployment sequence, or testing criteria.

## RATAN-CDUPS trade-flow summary

The `RATAN/RATAN -Interfaces/Ratan and CDUPS 51512.md` source names Solace as the messaging transport in its end-to-end summary for RATAN-CDUPS trade flows:

```text
CDUPS →Solace →Ratan (trade confirmation)
Ratan →Solace →CDUPS (trade info)
```

The same source's detailed interface specification names [[fm-edmi]] with JMS-JSON instead. It does not clarify whether Solace is the underlying broker, a logical transport label, or an alternative to FM-EDMi. Accordingly, the RATAN-CDUPS summary and the detailed FM-EDMi specification are retained as separate source claims rather than synthesized into a single interface contract.

## Trade confirmation and cashflow STP

The *Trade Confirmation & Cashflow STP* functional requirement names Solace as the topic transport through which [[ratan]] consumes Murex 2.11 trade SCBML supplied by [[tds3]].

That requirement lists product-specific publication and replay topic families for:

- Commodity
- Credit
- ForeignExchange
- InterestRate
- Cash

The requirement does not establish the environment, subscription ownership, ACLs, replay behavior, or whether the listed topology is deployed and current.

See [[what-is-the-authoritative-tds3-to-ratan-solace-topic-contract]] for validation of the operational contract.

## Cashflow migration readiness

The cashflow-migration-readiness source identifies Solace as a potential publication destination for Murex 2.11 trade-confirmation status from [[cdu-lake]].

This source records an effort assessment rather than a confirmed implementation. It provides no topic, message contract, ownership, delivery guarantee, or UAT result.

## Affirmation-email integration

The email-affirmation-automation technical-design source names Solace as the required connection protocol for the proposed RATAN-to-[[cdups]] affirmation-email integration.

That source records the transport choice but provides no topic, queue, schema, acknowledgement envelope, timeout, retry policy, dead-letter handling, or idempotency contract. See [[outbound-affirmation-email]] and [[what-is-the-cdups-affirmation-email-acknowledgement-contract]].

## Uber staging performance test

The *solace queue split PT for Uber* technical-design source describes Solace as the message-queueing platform used by an Uber staging performance test.

The documented test partitions inbound workload into these queues:

- `fx-other-msg`
- `fx-spot-msg`
- `equity-msg`
- `cash-msg`
- `com-msg`
- `interestrate-msg`
- `loan-msg`
- `credit-msg`

The performance-test source does not document queue configuration, consumer counts, delivery guarantees, retention settings, or the intended production topology.

See [[solace-queue-splitting-for-asset-class-workloads]] and [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--30-s--3u93uv]].
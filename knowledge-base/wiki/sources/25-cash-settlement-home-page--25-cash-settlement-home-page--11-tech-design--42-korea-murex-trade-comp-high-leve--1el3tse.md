---
type: source
title: Korea Murex Trade COMP High Level Solution
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, murex, korea, trade-confirmation, comp, integration, tactical-design]
related: [murex-korea, trade-confirmation-driven-payment-stp, mxml-trade-confirmation-event-integration, what-is-the-approved-murex-korea-to-ratan-comp-integration-and-retirement-plan, what-are-the-mxml-comp-event-contract-and-processing-semantics-for-ratan, murex, ratan, tds3, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP High Level Solution.md"]
---
# Korea Murex Trade COMP High Level Solution

## Summary

This design records options for supplying Korea Murex trade-confirmation (`COMP`) status to [[ratan]]. The stated business requirement is that payment STP depends on trade confirmation: without `COMP`, payments remain pending for manual Korea OPS affirmation. Korea OPS considers automated `COMP`-driven processing necessary for business go-live because manual processing capacity is limited.

The document describes two ruled-out options and a third, tactical option whose detailed design remains in progress. It does not state that the current option has been approved, implemented, tested, or put into production.

## Solution evolution

### Solution 1: Murex Korea through Murex GDC and TDS3

The initial proposal was to extend the existing Murex Korea to Murex GDC flow, which carried `VALD`, so that it also published `COMP`. [[ratan]] would then receive confirmation status through existing Murex GDC–[[tds3]] and TDS3–RATAN integrations.

Expected benefits were strategic sourcing through Trade Lake and reuse of existing downstream connections.

This solution was rejected by Murex PSS. The document states that both Murex and RATAN had completed development that must now be reverted. It does not explain the rejection rationale or define rollback scope, ownership, or schedule.

### Solution 2: direct SCBML over IBM MQ

The second option proposed a direct Murex Korea to RATAN integration using IBM MQ, with Murex Korea publishing trade [[scbml]].

Expected benefits included removing the Murex Korea–Murex GDC integration, avoiding a tactical RATAN build, simplifying integration testing, and enabling straightforward removal when a Murex Korea to TDS3 flow became available.

This option was ruled out because the evaluated Murex Korea flow could not generate SCBML. This is a scoped feasibility constraint; the document does not establish that SCBML generation is unavailable in every Murex deployment or configuration.

### Solution 3: direct MXML over IBM MQ

The current possible solution is for [[murex-korea]] to publish trade MXML directly to RATAN over a new IBM MQ integration. RATAN would require customization to process `COMP` events.

The proposed direct feed is expected to reduce Murex Korea–Murex GDC development and integration-test complexity. It is explicitly characterized as tactical: it will be removed eventually, requires additional delivery support, and creates removal debt that needs funding and a clear retirement plan.

Detailed design is in progress.

## Design implications

The proposed feed requires a defined MXML event contract and operational processing rules before it can be safely implemented. The document does not specify:

- MXML schema or version;
- trade identifiers and mapping to RATAN records;
- precise `COMP` status semantics;
- IBM MQ topology, queues, security, or delivery guarantees;
- duplicate, ordering, missing-event, replay, and idempotency handling;
- error states, reconciliation, monitoring, or alerting;
- approval, implementation, and go-live dates;
- the retirement trigger, owner, funding, and delivery plan for the tactical integration.

These gaps are tracked in [[what-are-the-mxml-comp-event-contract-and-processing-semantics-for-ratan]] and [[what-is-the-approved-murex-korea-to-ratan-comp-integration-and-retirement-plan]].
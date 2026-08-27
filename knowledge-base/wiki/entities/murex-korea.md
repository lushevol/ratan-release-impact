---
type: entity
title: Murex Korea
created: 2026-08-22
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/COMP status to drive STP process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Korea OLA and other release related DOCs.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Performance Testing Plan.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP High Level Solution.md"]
tags: ["murex", "korea", "source-system", "cash-settlement", "cashflow-migration", "comp", "integration", "trading-system", "migration", "korea-migration", "test-environment", "trade-processing"]
related: ["murex", "murex-2-11", "korea", "ratan-settlement", "ratan-settlement-korea", "tds3", "ratan-cashflow-lifecycle-service", "korea-direct-comp-driven-stp", "mxml", "scbml", "ratan", "korea-ratan-settlement-migration", "korea-murex-ratan-interface-readiness", "korea-migration-performance-testing", "trade-confirmation-driven-payment-stp", "mxml-trade-confirmation-event-integration"]
---
# Murex Korea

Murex Korea is the Korea-specific regional Murex source environment described in the cash-settlement migration requirements. It is also the regional Murex trade source discussed in the Korea trade-confirmation integration design.

The migration documentation identifies Murex Korea as the origin of Korea payment and trade MQ traffic sent to [[ratan]], and as the source or preparation environment for end-of-day (EOD) dumps used in Korea cash-settlement migration testing and performance testing.

## Korea cash-settlement migration and performance-testing scope

The Korea migration sources identify three EOD dumps dated 15, 16, and 18 June 2026. Each dump is pushed, reconciled, analyzed, and processed through auto netting, reprocessing of `waiting` cashflows, and SWIFT-message comparison in [[ratan-settlement]].

The end-to-end testing source states that the three dumps were pushed through reconciliation, auto netting, waiting-cashflow reprocessing, and SWIFT comparison. Murex Korea was used as the comparison baseline for SWIFT output. That source identifies differences in UETR generation, static data, and user-entered fields.

The performance-testing-plan source does not establish whether the dumps were successfully prepared or processed. It also does not provide performance results, reconciliation outcomes, message-comparison results, or migration approval.

This evidence applies only to the documented Korea migration test scope. It must not be generalized to other Murex deployments or versions without separate validation, including [[murex]] globally.

## COMP-driven payment STP integration

### Migration requirements

For the cashflow-migration scenario, the migration requirements expect Murex Korea to send trade messages containing `COMP` directly to RATAN because [[tds3]] cannot supply that status for Korea cashflows.

The source identifies Murex Korea as an upstream-status substitute for this migration scenario. It does not establish that direct integration applies to non-Korea entities, all products, or all RATAN processing flows.

Murex Korea supplies values from MXML for the intended SCBML message, including:

- Validation level
- Event action
- Entity
- Trade identifier
- Product taxonomy components

See [[korea-direct-comp-driven-stp]] and [[scbml]] for related integration context.

### Trade-confirmation integration design

The separate trade-confirmation integration design states that Murex Korea was not publishing trade `COMP` status for [[ratan]] to consume. According to that source, this prevented confirmation-driven payment STP and left payments pending manual operations affirmation.

That design evaluated and rejected a strategic route through Murex GDC and [[tds3]]. It also ruled out a direct SCBML route because the evaluated Murex Korea flow could not generate [[scbml]]. The remaining candidate is a direct MXML-over-IBM-MQ feed to RATAN, with RATAN-specific `COMP` processing. The candidate is tactical and remains in detailed design.

The design source does not establish Murex Korea's general ability or inability to generate SCBML outside the evaluated proposal.

These design statements describe the evaluated trade-confirmation integration proposal and should not be treated as a general claim about every Murex Korea flow or product.

## Interface readiness items

The Korea OLA and release-related documentation records the following unresolved items for Murex Korea's payment and trade MQ interface to [[ratan]]:

- MQ information and channel confirmation
- COMP trade volume
- COMP trade-message format and sample
- Monitoring arrangements

For COMP trades, the expected acknowledgement behavior is explicitly recorded as no ACK.
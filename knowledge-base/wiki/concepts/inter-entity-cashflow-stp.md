---
type: concept
title: Inter-Entity Cashflow STP
tags: [cash-settlement, settlement-day-2, STP, inter-entity, Murex, MX]
related: [murex-2-11, murex, internal-counterparty-exception-bypass, settlement-day-2, manual-entity-swift-mx-bifurcation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# Inter-Entity Cashflow STP

Inter-entity cashflow STP is the proposed automated processing of cashflows between entities without routing eligible flows through manual exception handling.

In the documented requirement, the scope is specifically:

- inter-entity cashflows from [[murex-2-11]];
- MX cashflows only;
- processing associated with SCB counterparty cashflows in Azure DevOps Story 6473009.

## Evidence and limits

The source records a functional objective, not a verified implementation. It provides no workflow, acceptance criteria, system ownership, field mapping, test evidence, or operational-readiness confirmation.

The MX-only statement applies to this Murex 2.11 inter-entity STP use case. It must not be generalized to all Murex cashflows, all inter-entity cashflows, or the broader SWIFT/MX processing model described by [[manual-entity-swift-mx-bifurcation]].

Whether non-MX or SWIFT inter-entity cashflows are unsupported, manually processed, or covered by another requirement remains unresolved. See [[is-inter-entity-stp-limited-to-murex-211-mx-cashflows]].
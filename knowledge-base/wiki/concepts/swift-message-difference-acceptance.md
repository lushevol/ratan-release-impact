---
type: concept
title: SWIFT Message Difference Acceptance
tags: [swift, reconciliation, controls, settlement-instructions, migration]
related: [reconciliation, swift-mt-mx-integration, korea-swift-mx-message-generation, korea-ssi-onboarding, ssi-plus, murex-korea, ratan-settlement]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md"]
---
# SWIFT Message Difference Acceptance

SWIFT message difference acceptance is a controlled reconciliation practice for documenting, assessing, approving, and retaining deviations between a source-system payment message and a target-system payment message.

## Required controls

Each accepted difference should state:

- the exact message fields and affected flow population;
- the source of the difference, such as product behavior, user input, static data, or a target-system limitation;
- whether payment routing, beneficiary data, regulatory reporting, or reconciliation is affected;
- the accountable approver and acceptance date;
- the country, product, currency, and release scope;
- whether the acceptance is temporary, permanent, or subject to remediation.

## Korea migration evidence

The Korea migration test records accepted differences in UETR/tag 121, `:32A:` decimal precision, `:52A:`, `:53A:`, `:57A:` BIC length, `:58A:` account presence, and `:72:` content. The document marks each sample as closed, but it does not identify an approver for the SSI+-to-Murex Vostro variance or establish a reusable approval standard.

These findings apply only to the cited [[murex-korea]] and [[ratan-settlement]] comparison flows. They should not be treated as globally accepted SWIFT behavior without documented scope and ownership.
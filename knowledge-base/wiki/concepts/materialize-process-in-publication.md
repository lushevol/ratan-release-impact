---
type: concept
title: Materialize Process-In Publication
created: 2026-08-24
updated: 2026-08-24
tags: [Materialize, cashflow-lifecycle, process-in, event-publication]
related: [process-in-topic, process-in-publication-contract, ratan-cashflow-lifecycle-service, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# Materialize Process-In Publication

Materialize process-in publication is the unresolved design question of whether a Materialize lifecycle action must publish an event to the `process-in` topic.

For `C07810140013`, the testing notes record a Materialize action error and state that lifecycle needs to determine whether publication is required. The action error and the publication requirement are separate questions: diagnosing the runtime failure does not establish the intended event contract.

Until the contract is accepted, Materialize should not be assumed to have the same process-in behavior as SettleAsGross or Swift unsuppression.
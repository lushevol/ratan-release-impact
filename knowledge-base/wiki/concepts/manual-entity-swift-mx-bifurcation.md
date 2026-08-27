---
type: concept
title: Manual-Entity SWIFT and MX Bifurcation
created: 2026-08-23
updated: 2026-08-23
tags: [swift, iso-20022, mx, manual-entities, settlement]
related: [ratan, manual-entity-swift-mx-bifurcation, cashflow-suppression-and-swift-generation, is-kenya-mx-eligibility-using-the-correct-sender-bic-prefix, is-uganda-confirmed-for-all-mx-generation, what-is-the-authoritative-manual-entity-mx-go-live-schedule, does-sri-lanka-ratan-or-cms-own-pacs009-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# Manual-Entity SWIFT and MX Bifurcation

Manual-entity SWIFT and MX bifurcation is RATAN's country- and entity-specific selection between legacy MT output and ISO 20022 output.

## Message selection

Eligible payment types are MT103, MT202, and MT202COV:

- MT103 maps to `pacs.008`.
- MT202 and MT202COV map to `pacs.009`.
- Cancellation uses `camt.056` only when the original message was MX.
- `MT192` is eligible for cancellation of an MT103-originated payment.
- `MT292` is eligible for cancellation of an MT202 or MT202COV-originated payment.

Selection conditions vary by sender BIC prefix and, for some entities, receiver BIC, Nostro static BIC, or settlement-account conditions. The conditions must remain entity-specific rather than becoming a generalized global rule.

## Rollout patterns

Vietnam, Bangladesh, Sri Lanka, Pakistan, and Zambia use MT for internal flows and MX for external flows. Bahrain, Ghana, Kenya, Nigeria, Qatar, Tanzania, and the stated Uganda target use MX for internal and external flows.

SLATE ONE LLC*DOH, FMID `401081696`, is excluded because its cashflows are suppressed. This exception does not apply to Qatar FMID `300010782`.

## Controls and open questions

Kenya's current documented condition uses Tanzania's `SCBLTZ` sender prefix rather than the expected Kenya prefix, making the configuration unsafe to implement without confirmation. Uganda's all-to-MX decision remains pending. The source also supplies incomplete ISO go-live dates and a Sri Lanka ownership ambiguity between RATAN and CMS.

See [[is-kenya-mx-eligibility-using-the-correct-sender-bic-prefix]], [[is-uganda-confirmed-for-all-mx-generation]], and [[what-is-the-authoritative-manual-entity-mx-go-live-schedule]].
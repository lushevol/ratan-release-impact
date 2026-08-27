---
type: concept
title: Precious-Metal Currency Classification
created: 2026-08-23
updated: 2026-08-23
tags: [precious-metals, currency, swift, mt604, mt605, mt692]
related: [new-currency-onboarding-static-data-readiness, murex-2-11, ratan, precious-metal-cashflow-vostro-requirement, what-is-the-authoritative-change-control-for-pm-and-iso-currency-mappings]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# Precious-Metal Currency Classification

RATAN uses a hardcoded PM currency list to identify whether a currency is precious metal. A positive classification drives generation of MT604, MT605, and MT692.

Murex 2.11 colleagues provided the stated list, while its reference documentation is maintained in the FMRP Swift Generation Confluence document. This division between hardcoded implementation and externally maintained reference documentation creates a configuration-governance dependency.

This concept concerns message-generation classification only. It does not establish a general Vostro or receive-cashflow rule; [[precious-metal-cashflow-vostro-requirement]] remains a separate requirement unless corroborating evidence connects the rules.

The source does not provide PM currency members or the detailed conditions for each SWIFT message type.
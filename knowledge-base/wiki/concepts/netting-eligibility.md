---
type: concept
title: Netting Eligibility
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, validation, eligibility]
related: [netting-service, cashflow-netting, maker-checker-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Netting Eligibility

Netting eligibility is the check that determines whether a cashflow may participate in a proposed netting operation.

The DoD requires an eligibility interface and requires the Netting Service to update the cashflow sub-status based on the check. The source does not define the eligibility predicates, the sub-status values, or whether eligibility is evaluated independently for each component or for the entire request.

Potentially relevant inputs visible in the design include cashflow status, payment type, amount, currency, entity, payment date, settlement method, source system, and cashflow version. These are observations from the data model, not confirmed eligibility rules.

The design also leaves unresolved how mixed eligibility is handled when some components pass and others fail. This should be specified together with validation, maker/checker approval, idempotency, and concurrency behavior.
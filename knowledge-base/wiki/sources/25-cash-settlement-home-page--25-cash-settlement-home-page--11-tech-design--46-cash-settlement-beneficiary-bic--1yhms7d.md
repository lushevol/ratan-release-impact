---
type: source
title: Cash Settlement Beneficiary BIC Netting Design
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, beneficiary-bic, netting, technical-design, service-scope]
related: [beneficiary-bic-netting, what-is-the-authoritative-beneficiary-bic-netting-model, what-static-data-changes-are-required-in-rule-service-for-beneficiary-bic-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Beneficiary BIC Netting Design.md"]
---
# Cash Settlement Beneficiary BIC Netting Design

## Summary

This source is a short service-change inventory for Cash Settlement Beneficiary BIC Netting. It identifies six affected areas: Front End, Netting service, Lifecycle service, Static data service, Query service, and Rule service. The Rule service is explicitly limited to static-data changes.

The document does not define the netting behavior, data ownership, interfaces, schemas, routing rules, validation rules, migration approach, or acceptance criteria. The identities of the generic service names are also not established.

## Stated Service Scope

The source content is preserved below:

```text
Service Change:

Front End

Netting service

Lifecycle service

Static data service

Query service

Rule service(only static data)
```

## Evidence and Boundaries

The source supports the conclusion that Beneficiary BIC Netting has cross-service implementation scope. It does not establish that Beneficiary BIC is a netting key, an eligibility constraint, a routing attribute, or an enrichment field.

The parenthetical “only static data” establishes a responsibility boundary for the Rule service, but does not clarify whether that scope covers storage, validation, configuration, enrichment, distribution, or reference-data synchronization.

The generic service labels cannot be safely mapped to existing named services such as [[ratanone-rule-service]], [[51358-ratanone-static-data-service]], [[ratan-cashflow-lifecycle-service]], [[51358-ratanone-query-service]], or [[51358-ratan-cash-settlement-query-service]] without additional evidence.

## Missing Design Detail

The source leaves the following unresolved:

- The role of Beneficiary BIC in netting.
- The authoritative source and owner of Beneficiary BIC.
- Netting grouping, exclusion, and segregation keys.
- Handling of missing, invalid, inactive, amended, or conflicting BIC values.
- Propagation between the listed services.
- API, database, event-contract, audit, migration, reconciliation, and testing changes.
- The deployment, region, or Cash Settlement implementation to which the design applies.

See [[beneficiary-bic-netting]] and [[what-is-the-authoritative-beneficiary-bic-netting-model]] for the resulting knowledge boundary and open questions.
---
type: source
title: Cash Settlement Accounting and Reconciliation Functional Requirement
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, accounting, reconciliation, functional-requirement, implementation-estimate]
related: [ebbs, aspire, bcdf, bridge-account, cashflow-accounting-stamping, entity-based-eod-feeding, single-payment-realtime-accounting-feeding, cashflow-accounting-eligibility, accounting-feed-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Accounting & Recon.md"]
---

# Cash Settlement Accounting and Reconciliation Functional Requirement

## Summary

This functional requirement describes preliminary accounting and reconciliation integration for the Cash Settlement Home Page. The scope covers accounting-entry generation and feed integration for two regional domains:

- **Aspire:** Hong Kong and Taiwan.
- **EBBS:** United Kingdom, Singapore, and India.

The proposed accounting-feed format is **BCDF**. Both accounting implementations depend on [[cashflow-accounting-stamping]], in which cashflows are associated with underlying static data before accounting entries are generated.

The document is an implementation-sizing note rather than a finalized interface specification. Cashflow eligibility, BCDF details, reconciliation behavior, and the relationship between end-of-day and realtime EBBS feeding remain unresolved.

## Function Breakdown

The source table is reproduced below. Its `Bridge Account` and `Sum` rows appear structurally malformed, so the estimates should be validated before being treated as an approved work breakdown.

```text
| Function Type | Function Name | New building | Effort Estimation | Comment |
| --- | --- | --- | --- | --- |
| Static Data | EBBS Account | N | NA | |
| Bridge Account | Y | Analysis: 8 Dev & Test: 12 UI : TBD | |
| Aspire Accounting (HK/TW) | Accounting Entries generation | Y | Analysis: 16 Dev & Test: 12 | 1. Accounting stamping ( cashflow VS underlying static data) 2. File format is BCDF, TBC the cashflows eligible for accounting feeding |
| Integration - EOD | Y | Analysis: 8 Dev & Test: 8 DevOps & Test: 12 | 1. EOD schedule by entity 2. Feeding data by BCDF file |
| EBBS Accounting(UK,SG/IN) | Accounting Entries generation -EOD | Y | Analysis: 16 Dev & Test: 12 | 1. Accounting stamping ( cashflow VS underlying static data) 2. File format is BCDF, TBC the cashflows eligible for accounting feeding |
| Integration - EOD Feeding | Y | Analysis: 8 Dev & Test: 8 DevOps & Test: 12 | 1. EOD schedule by entity 2. Feeding data by BCDF file |
| Sum | Analysis: 56 Dev & Testing: 76 | |
```

## New-Build Scope

The source marks the following areas as requiring new build:

- [[bridge-account]]
- Aspire accounting-entry generation
- End-of-day integration
- EBBS accounting-entry generation for UK, Singapore, and India
- End-of-day feeding integration

`Static Data — EBBS Account` is marked as not requiring new build. This does not establish that the data is complete or ready for accounting stamping.

## Integration Constraints

The source specifies BCDF for:

- Aspire accounting-entry generation.
- EBBS accounting-entry generation.
- End-of-day integration.
- End-of-day feeding.

No BCDF schema, version, record types, file naming convention, delivery mechanism, acknowledgement behavior, retry policy, security control, or error-handling contract is provided.

The end-of-day integration is described as being scheduled by entity and transmitting data through BCDF files. The source does not identify the systems that own scheduling, file creation, delivery, or acknowledgement.

## EBBS Feeding Approaches

The source lists two possible [[ebbs]] feeding approaches:

```text
# EBBS feeding approach

- EOD approach by entity
- Realtime feeding by single payment
```

It is unresolved whether these are alternatives, complementary modes, or modes assigned to different payment populations. The document does not identify a preferred approach.

## Effort Estimate

The reported total is:

- **Analysis:** 56
- **Development and testing:** 76
- **UI:** TBD for the Bridge Account item.
- **DevOps and testing:** 12 appears in the integration rows.

The document does not state whether the DevOps effort is included in the reported development-and-testing total. It also provides no staffing assumptions, estimation units, dependencies, confidence range, or delivery commitment.

## Open Requirements

The following requirements remain undefined:

1. Which cashflows are eligible for Aspire and EBBS accounting feeds?
2. What accounting attributes are required for cashflow-to-static-data stamping?
3. What is the authoritative BCDF schema and delivery contract?
4. What is the purpose and ownership of the [[bridge-account]]?
5. Does EBBS support both entity-based end-of-day and single-payment realtime feeding?
6. Which reconciliation keys, tolerances, outputs, and exception workflows are required?
7. Which system owns the underlying static data used for accounting stamping?

The source title includes reconciliation, but the body does not define matching, break management, replay, or settlement-to-accounting verification behavior. Existing patterns such as [[swift-message-reconciliation]] should not be assumed to apply without additional evidence.

## Evidence and Limitations

The source provides direct evidence for the regional split, new-build indicators, BCDF as the proposed format, the stated effort estimates, and the two listed EBBS feeding approaches. It does not establish final architecture, production schedules, accounting schemas, eligibility rules, or acceptance criteria.

This page should therefore be treated as a preliminary requirement summary and sizing record.

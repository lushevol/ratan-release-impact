---
type: concept
title: SGO SSI Replication
created: 2026-08-23
updated: 2026-08-23
tags: [SGO, SGD, SSI, replication, ES, static-data, cashflow]
related: [es-static-data-layer, ssi-id-persistence-and-edit-provenance, ssi-selection-as-non-adhoc-ssi, ssi-selection-provenance-and-ad-hoc-classification, nostro-stamping, ratan, what-is-the-authoritative-sgo-ssi-amendment-propagation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/FMRP SGO Testing.md"]
---
# SGO SSI Replication

## Definition

SGO SSI replication is the process of creating `SGO` Settlement Instruction records in the `ES` layer from existing `SGD` SSI records. Replicated identifiers use an `_SGO` suffix, such as `47726687_SGO`.

The process is a distinct lifecycle path rather than merely a display-name variation. It must preserve applicable SSI attributes, selection scope, effective-date behavior, and settlement-account mapping for SGO cashflows.

## Go-live behavior

For the 27 September 2025 go-live, existing SGD SSIs were planned to be replicated as SGO records in `ES`. The source states that no notification would be sent to `RATAN` because there were no SGO cashflows in production at that time.

This notification behavior is conditional on the deployment assumption and should not be generalized to later replication activity.

## Observed behavior

Testing showed that:

- Existing SGO cashflows could receive replicated `_SGO` SSIs.
- Newly created SGO cashflows could auto-attach the replicated SSI.
- Deleting an SGO SSI caused the affected cashflow to trigger `Missing Vostro`.
- Global and Singapore-country scoping was intended to apply consistently across SGD and SGO records.
- An SGO update event could be received without the associated SGO cashflow reflecting the amended SSI value.

The last observation is an unresolved defect in [[what-is-the-authoritative-sgo-ssi-amendment-propagation-contract]] and must not be merged with the successful SGD amendment result.

## Identifier relationship

```text
SGD SSI: 47726687
SGO SSI: 47726687_SGO
```

Future-effective records may use the corresponding `_ED` and `_SGO_ED` suffixes before transitioning to live identifiers; see [[ssi-effective-date-transition]].

## Boundaries

SGO replication does not prove that:

- Every production SGD SSI was successfully replicated.
- SGO amendment propagation is equivalent to SGD amendment propagation.
- Initial notification-free replication remains valid after production contains SGO cashflows.
- The entire FMRP SGO test matrix received formal sign-off.

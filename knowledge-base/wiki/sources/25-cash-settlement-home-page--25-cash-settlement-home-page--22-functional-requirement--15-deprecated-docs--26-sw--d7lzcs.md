---
type: source
title: "Swift Suppression — Deprecated Functional Requirement"
authors: []
year: ""
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, swift-suppression, deprecated, functional-requirement]
related: [swift-suppression, cashflow-suppression, suppression-maker-checker-workflow, suppression-rule-management, cash-settlement-home-page, amh, cashflow-blotter, deprecated-functional-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Swift Suppression -deleted.md"]
---
# Swift Suppression — Deprecated Functional Requirement

## Source status

This source is identified by the filename `Swift Suppression -deleted.md` and is located in the `Deprecated docs` directory. The document content was unavailable during ingest, so no functional requirements, schemas, workflows, interfaces, or acceptance criteria can be reliably extracted.

The filename supports only a historical classification of the document as a deleted or deprecated requirement concerning [[concepts/swift-suppression]]. It should not be treated as an authoritative current specification.

## Related wiki coverage

The subject is connected to the existing suppression knowledge cluster:

- [[concepts/swift-suppression]]
- [[concepts/cashflow-suppression]]
- [[concepts/suppression-maker-checker-workflow]]
- [[concepts/suppression-rule-management]]
- [[entities/amh]]
- [[entities/cashflow-blotter]]
- [[concepts/deprecated-functional-requirements]]

Existing open questions address whether payment suppression is equivalent to SWIFT suppression, post-value-date processing, suppression-rule precedence, rollback after rejected actions, and suppression undo cutoffs. This source cannot resolve those questions without its contents.

## Evidence limitations

No source body, tables, diagrams, SQL DDL, schema definitions, API signatures, configuration, or structured data were available. The following subjects therefore remain unverified:

- The processing stage affected by suppression.
- Trigger, eligibility, and exclusion rules.
- Maker/checker permissions and state transitions.
- Undo, rollback, rejection, and post-value-date behavior.
- Integration responsibilities involving `AMH`, Cashflow Blotter, or other systems.
- Any document that superseded this requirement.

## Recommended use

Use this page for historical traceability only. If the deleted document is recovered, compare its requirements with the current suppression concepts and related queries before incorporating any rules into authoritative documentation.
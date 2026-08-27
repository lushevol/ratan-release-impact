---
type: concept
title: SSI Selection Provenance and Ad Hoc Classification
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, settlement-instructions, provenance, adhoc-ssi, settlement-amendment, uat]
related: [fmo-post-trade-portal, field-70-72-customization-and-reference-id, cashflow-amendment-maker-checker-control, pre-adhoc-error-and-adhoc-ssi-exception-lifecycle, what-is-the-authoritative-reference-id-and-ssi-id-contract-for-field-70-72-customization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/SSI selection not treat as adhoc SSI - UAT.md"]
---
# SSI Selection Provenance and Ad Hoc Classification

SSI selection provenance distinguishes settlement values selected from an available SSI from values manually entered or manually amended in the [[fmo-post-trade-portal]]. Identical visible settlement values do not by themselves restore or establish the provenance of an SSI selection.

## UAT-supported UI rules

The UAT source indicates the following for ordinary settlement-detail fields:

- Selecting an available SSI, with no subsequent settlement-detail edit, populates SSI ID.
- Manual entry without selecting an SSI leaves SSI ID blank.
- Amending a field other than SWIFT field 70 or 72 clears SSI ID.
- Reverting that field to its original value does not restore SSI ID.
- Explicitly re-selecting the available SSI restores SSI ID.

Observed non-70/72 examples include account number, settlement means, Address 2, and field 58 address.

This is an irreversible provenance rule at the UI level: reversion restores values, but not the recorded association with the SSI. The special treatment of fields 70 and 72 is documented separately in [[field-70-72-customization-and-reference-id]].

## Maker/checker implication

The source reports that a checker cannot approve by manually entering details that match an SSI selected by the maker. The checker receives a validation error and must select the available SSI. This confirms that the workflow validates selection provenance rather than merely comparing settlement-detail values; see [[cashflow-amendment-maker-checker-control]].

## Boundary of evidence

Blank SSI ID is a UI indicator of manual or ad hoc settlement details in this UAT evidence. It is not proof of a backend ad hoc lifecycle transition, exception record, or database state. The relationship to `PRE_ADHOC_ERROR` and `ADHOC_SSI_EXCEPTION` remains unconfirmed by this source; see [[pre-adhoc-error-and-adhoc-ssi-exception-lifecycle]].
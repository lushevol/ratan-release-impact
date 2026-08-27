---
type: concept
title: SSI Selection as Non-Ad Hoc SSI
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, settlement-instruction, cash-settlement, ad-hoc-SSI]
related: [ssi-id-persistence-and-edit-provenance, 70-72-customization-highlighting, ssi-reference-id-display, nostro-stamping, ssi-stamping-behavior-differences, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# SSI Selection as Non-Ad Hoc SSI

## Definition

Selecting an available SSI in the Cash Settlement Home Page is a recognized SSI selection, not a manually entered ad hoc SSI. The selected record has an SSI ID that should be retained when the user submits without changes.

This distinction applies to user selection of an available settlement instruction. It does not make manually entered SSI values equivalent to a selected static-data record.

## Behavior

- A selected SSI receives or retains its SSI ID.
- A selection without subsequent edits preserves the selected SSI identity.
- A selection followed only by 70/72 customization preserves the SSI ID.
- A selection followed by an edit to another field removes the SSI ID.
- Restoring a changed field to its original value does not undo the manual-edit event.
- Explicitly selecting the SI again can repopulate the SSI ID.

## Provenance

The system should distinguish at least four input origins:

1. System auto-stamped SSI.
2. Maker-selected available SSI.
3. Manually entered SSI values.
4. Checker-entered values during review.

Two inputs with identical visible values may have different business meaning when their provenance differs. In particular, checker re-entry of values selected by the maker must not be treated as confirmation of the maker's selection.

## Operational relevance

An SSI ID absent from RATAN may be considered unused by SSI+. Correctly recognizing selected SSIs therefore reduces the risk of inappropriate cleanup and preserves lineage for downstream SWIFT processing.

The concept extends [[concepts/nostro-stamping]] and should be considered alongside [[concepts/ssi-id-persistence-and-edit-provenance]].
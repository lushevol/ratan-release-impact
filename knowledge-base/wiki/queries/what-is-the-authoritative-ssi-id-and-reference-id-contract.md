---
type: query
title: What Is the Authoritative SSI ID and Reference ID Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, Reference-ID, open-question, maker-checker, cash-settlement]
related: [ssi-reference-id-display, ssi-id-persistence-and-edit-provenance, ssi-selection-as-non-adhoc-ssi, 70-72-customization-highlighting, ratan, ssi-plus, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# What Is the Authoritative SSI ID and Reference ID Contract?

## Question

What are the authoritative persistence, lifecycle, and display rules for SSI ID and `Reference ID` when an SSI is auto-stamped, selected by a maker, manually entered, edited, restored, submitted, or approved by a checker?

## Evidence from the requirement

The requirement establishes that:

- Selecting an available SSI should populate the SSI ID.
- Editing only 70/72 should preserve the SSI ID and show a customization marker.
- Editing another field should remove the SSI ID, even when the value is restored.
- `Reference ID` may display the corresponding SSI ID after selected-SSI or auto-stamped-SSI processing.
- Checker visibility differs between maker-selected and system auto-stamped SSI.
- Scenario 16 contains conflicting statements about whether `Reference ID` is shown for a checker reviewing a maker-selected SSI with 70/72 changes.

## Resolution needed

The owning team should document:

- Whether SSI ID and `Reference ID` are separate persisted values.
- The authoritative system and write timing, including RATAN persistence.
- Whether `Reference ID` represents historical lineage or a current operational identifier.
- Role- and provenance-based visibility rules.
- The validation error and comparison contract for checker re-entry.
- The behavior after 70/72 restoration and after non-70/72 restoration.
- The exact definition of SWIFT fields 70/72 across supported message types.

The answer should be reconciled with [[concepts/ssi-reference-id-display]] and [[concepts/ssi-id-persistence-and-edit-provenance]].
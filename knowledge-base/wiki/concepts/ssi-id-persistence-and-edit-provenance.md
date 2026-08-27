---
type: concept
title: SSI ID Persistence and Edit Provenance
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, edit-provenance, state-management, cashflow, maker-checker]
related: [ssi-selection-as-non-adhoc-ssi, 70-72-customization-highlighting, ssi-reference-id-display, cashflow-versioning, maker-checker-rounding-workflow, nostro-stamping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# SSI ID Persistence and Edit Provenance

## Purpose

SSI ID validity depends on how the SSI was obtained and which fields the user changed. The system must track edit provenance rather than infer validity solely from final field equality.

## Persistence rules

| Event | SSI ID result |
| --- | --- |
| Select an available SSI and submit without edits | Populate or preserve the selected SSI ID |
| Select an available SSI and edit only 70/72 | Preserve the SSI ID |
| Edit a field other than 70/72 | Remove the SSI ID |
| Edit a non-70/72 field and restore its original value | Keep the SSI ID removed |
| Edit 70/72 and restore its original value | Preserve the SSI ID and retain the 70/72 customization marker |
| Manually enter SSI values without selecting an available SSI | Keep the SSI ID blank |
| Explicitly select the SI again | Repopulate the SSI ID for the newly confirmed selection |

## Required state dimensions

A robust implementation should track independently:

- The source of the SSI data.
- The selected SSI record and its SSI ID.
- Whether a non-70/72 field has been edited.
- Whether 70/72 has been edited.
- Whether a field was edited and later restored.
- Whether the current values were entered by the maker or checker.
- The workflow stage and approval status.

## State interpretation

The selected SSI remains authoritative when there is no disqualifying non-70/72 edit. A 70/72 edit is treated as payment-detail customization rather than replacement of the SSI identity. Any other manual edit invalidates the selected SSI identity, even if the final values happen to match the original SSI.

This is an interaction-history rule. A snapshot comparison at submission time cannot reliably implement it.

## Maker-checker implications

When a maker selects an SSI, a checker manually entering the same visible values is a distinct input event and must produce a validation error where required by the workflow. The checker view must preserve the distinction between a system auto-stamped SSI and a maker-selected SSI.

The model should be coordinated with [[concepts/cashflow-versioning]] and the existing [[concepts/maker-checker-rounding-workflow]] without assuming that SSI edits follow rounding-specific behavior.
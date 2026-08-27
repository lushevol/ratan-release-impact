---
type: concept
title: SSI Reference ID Display
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, reference-ID, UI, cash-settlement, maker-checker]
related: [ssi-selection-as-non-adhoc-ssi, ssi-id-persistence-and-edit-provenance, 70-72-customization-highlighting, cash-settlement-home-page, ratan, ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# SSI Reference ID Display

## Purpose

The `Reference ID` field makes the corresponding SSI ID visible in selected workflow scenarios, particularly when the main SSI ID display is empty or when the UI needs to distinguish a reference to the original system-stamped instruction from the current operational SSI state.

## Expected display behavior

- For a system auto-stamped SSI, `Reference ID` displays the stamped SSI ID where specified.
- After a selected SSI is customized only in 70/72, the SSI ID remains valid and `Reference ID` may display the corresponding SSI ID.
- For a maker-selected SSI opened by a checker, the checker should not automatically see the maker's SSI ID in the same manner as a system auto-stamped SSI.
- In the maker-selected 70/72 checker scenario, the source gives conflicting instructions about whether `Reference ID` is shown.
- After a non-70/72 edit invalidates an auto-stamped SSI, the source states that the checker view should not show `Reference ID`.

## Semantic distinction

The requirement does not establish whether `Reference ID` is:

- a separately persisted business field;
- a historical reference to the SSI used for stamping or selection;
- a role-specific presentation of SSI ID; or
- a display alias rendered from another persisted value.

Until this is resolved, implementations should not assume that an empty SSI ID and a populated `Reference ID` have identical operational semantics.

## Open contract

The authoritative contract must define:

1. The persistence source and lifecycle of `Reference ID`.
2. Whether it is written at selection, submission, or approval.
3. Visibility by maker/checker role.
4. Visibility by system-stamped versus maker-selected provenance.
5. Behavior after non-70/72 edits.
6. Behavior after 70/72 edits and subsequent restoration.

This concept is linked to [[queries/what-is-the-authoritative-ssi-id-and-reference-id-contract]].
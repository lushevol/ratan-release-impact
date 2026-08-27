---
type: source
title: SSI Selection Not Treated as Ad Hoc SSI
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13438079"
venue: Functional requirement
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, SSI, SWIFT, maker-checker, functional-requirement]
related: [cash-settlement-home-page, ssi-selection-as-non-adhoc-ssi, ssi-id-persistence-and-edit-provenance, 70-72-customization-highlighting, ssi-reference-id-display, what-is-the-authoritative-ssi-id-and-reference-id-contract, ratan, ssi-plus]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# SSI Selection Not Treated as Ad Hoc SSI

## Source context

This functional requirement changes SSI handling in the Cash Settlement Home Page. A user selecting an available SSI should be treated as selecting a recognized SSI rather than entering an ad hoc SSI.

The requirement also defines special treatment for SWIFT fields 70/72. These fields may contain payment-specific details, including invoice numbers and ultimate-beneficiary information, while the selected SSI account remains valid. Incorrect 70/72 content can cause payment failure when one account is shared by multiple funds.

SSI+ reviews unused SSI records. An SSI ID not stored in RATAN is treated as unused, which makes correct SSI ID persistence an operational data-governance concern.

## ADO

Work item: [13438079](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/13438079)

## AS-IS behavior

- A system auto-stamped SI has a populated SSI ID.
- A manually entered Vostro SI has a blank SSI ID.
- A user-selected available SI has a blank SSI ID, regardless of whether values are changed.
- Approving a cashflow while the Vostro SSI is in edit mode can leave the SSI ID blank.
- 70/72 field values are not included in dual-blind validation.

## TO-BE behavior

- Selecting an available SI and submitting without changes sets the SSI ID to the selected SI ID.
- Selecting an available SI and changing only 70/72 preserves the SSI ID.
- A 70/72 customization indicator is shown only when an SSI ID exists and the user has changed 70/72.
- Selecting an available SI and changing a field other than 70/72 removes the SSI ID.
- Changing a field and restoring its original value still removes the SSI ID unless the user explicitly selects the SI again.
- If a maker selects an available SI and a checker manually enters the same visible values, the system treats the inputs as different and displays a validation error.
- A checker does not see the SSI ID selected by the maker in the same way as a system auto-stamped SSI.
- Approving a cashflow with a Vostro SI in edit mode does not affect the SSI ID when the user makes no SI update.
- A `Reference ID` field displays the corresponding SSI ID in specified maker and checker scenarios.

## Consolidated behavior

| Initial state | User action | SSI ID outcome | 70/72 indicator |
| --- | --- | --- | --- |
| Auto-stamped SSI | Submit without changes | Populated | Not shown |
| Auto-stamped SSI | Change only 70/72 | Preserved | Shown |
| Auto-stamped SSI | Change another field | Removed | Not shown unless 70/72 was also changed |
| Auto-stamped SSI | Change and restore another field | Remains removed | Based on edit history |
| No stamped SSI | Manually enter SSI values | Blank | Not shown unless the applicable SSI-selection condition exists |
| No stamped SSI | Select available SSI without changes | Populated | Not shown |
| No stamped SSI | Select SSI and change only 70/72 | Populated | Shown |
| No stamped SSI | Select SSI and change another field | Removed | Not shown |
| Any relevant state | Change and restore 70/72 | Preserved | Remains shown |
| Maker selects SSI; checker re-enters the same values | Checker approval | Validation error | Provenance difference is retained |

## Business scenarios

1. Auto-stamped SI with a populated SSI ID.
2. Auto-stamped SI with a manually changed field other than 70/72; SSI ID is blank.
3. Auto-stamped SI with manually changed 70/72; SSI ID is populated and the 70/72 customized tag is shown. `Reference ID` displays the corresponding SSI ID.
4. Auto-stamped SI with a non-70/72 field changed and restored; SSI ID is blank until the user selects the SI again.
5. Auto-stamped SI selected without changes and submitted; SSI ID is populated.
6. Auto-stamped SI selected and 70/72 changed; SSI ID is populated and the customized tag is shown. `Reference ID` displays the corresponding SSI ID.
7. Auto-stamped SI selected, a non-70/72 field changed, and submitted; SSI ID is blank.
8. Auto-stamped SI selected, a non-70/72 field changed and restored; SSI ID is blank until the user selects the SI again.
9. Auto-stamped SI selected and a 70/72 field changed; SSI ID is populated and `Reference ID` displays the corresponding SSI ID.
10. No SSI stamped and SSI values manually entered; SSI ID is blank.
11. No SSI stamped, available SI selected without changes, and submitted; SSI ID is populated.
12. No SSI stamped, available SI selected, and 70/72 changed; SSI ID is populated and the customized tag is shown. `Reference ID` displays the corresponding SSI ID.
13. No SSI stamped, available SI selected, and a non-70/72 field changed; SSI ID is blank.
14. No SSI stamped, available SI selected, a non-70/72 field changed and restored; SSI ID is blank until the user selects the SI again.
15. Maker selects an available SI and checker manually enters the same values; approval produces a validation error.
16. Maker selects an available SI and modifies field 7072; the checker sees the 7072 highlight and auto-populated 7072 value, but the SSI ID is not auto-populated. The source contains conflicting statements about whether `Reference ID` is shown in this view.
17. Auto-stamped SI with maker-modified field 7072; the checker sees the 7072 highlight and value, the stamped SSI ID, and the stamped SSI ID in `Reference ID`.
18. Struck-through scenario concerning checker approval of an existing cashflow with pending manual ad hoc SSI; excluded from the active requirement.
19. SSI selected, field 7072 entered, and then restored to the SSI value; the 7072 field remains highlighted and `Reference ID` displays the stamped SSI ID.
20. Auto-stamped SI with only the 58A address changed; SSI ID is removed. The checker sees the system-stamped SSI display and the populated 58A address, but the final SSI ID remains blank and `Reference ID` is not shown.

## Implementation implications

The requirement requires separate tracking of:

- SSI provenance: system auto-stamped, maker-selected, manually entered, or checker-entered.
- The selected SSI identity.
- Manual edits to fields other than 70/72.
- Manual edits to fields 70/72.
- Edit history after a value is restored.
- Maker/checker input provenance.

Final-value comparison alone is insufficient. A change followed by restoration must remain observable in the relevant state. The implementation must also define when the selected SSI ID is persisted to RATAN and how SWIFT generation consumes a preserved SSI ID together with customized 70/72 content.

## Open questions

- Is `Reference ID` a persisted field, a historical lineage value, or a UI alias?
- When is a selected SSI ID written to RATAN: selection, submission, or approval?
- Does checker visibility depend on workflow role, SSI provenance, or both?
- What exact validation error applies when the checker re-enters maker-selected values?
- Are 70/72 changes included in dual-blind comparison or only highlighted?
- Does a 70/72 change create a new cashflow version?
- Should the terminology be `70/72`, `7072`, or separate SWIFT fields 70 and 72?
- How are blank, null, and restored 70/72 values distinguished?

## Related wiki pages

- [[concepts/ssi-selection-as-non-adhoc-ssi]]
- [[concepts/ssi-id-persistence-and-edit-provenance]]
- [[concepts/70-72-customization-highlighting]]
- [[concepts/ssi-reference-id-display]]
- [[concepts/nostro-stamping]]
- [[concepts/ssi-stamping-behavior-differences]]
- [[entities/ratan]]
- [[entities/ssi-plus]]
- [[entities/cash-settlement-home-page]]
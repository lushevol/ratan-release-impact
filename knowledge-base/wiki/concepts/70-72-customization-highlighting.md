---
type: concept
title: 70/72 Customization Highlighting
created: 2026-08-23
updated: 2026-08-23
tags: [SWIFT, 70-72, payment-details, SSI, maker-checker]
related: [ssi-selection-as-non-adhoc-ssi, ssi-id-persistence-and-edit-provenance, ssi-reference-id-display, outbound-property-propagation-to-swift-mt-mx, maker-checker-rounding-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI.md"]
---
# 70/72 Customization Highlighting

## Definition

70/72 customization is a user modification to SWIFT payment-detail fields after an SSI has been selected or auto-stamped. The modification does not invalidate the selected SSI ID, but it must remain visible as a customization for review and payment generation.

The source uses both `70/72` and `7072`; the implementation should establish a canonical terminology while preserving the underlying SWIFT field identifiers.

## Business rationale

Field 70/72 can carry payment-specific information such as invoice numbers or the ultimate beneficiary. A single beneficiary account may be shared by multiple funds, requiring field 70/72 to distinguish entities such as `Prudential Life Amundi Fund` and `Prudential Life Emerging Fund`.

Incorrect field 70/72 content may cause payment failure even when the settlement account and SSI remain correct.

## Rules

- Editing only 70/72 preserves the SSI ID.
- The 70/72 customized tag is shown when an SSI ID exists and 70/72 was edited.
- If no SSI ID exists, a 70/72 edit does not receive the special SSI customization highlight under this requirement.
- The highlight persists after 70/72 is changed back to its original value.
- The checker sees the 70/72 highlight and the relevant value in maker-checker scenarios.
- 70/72 content must be available to downstream SWIFT generation.

## Edit history

The highlight represents an edit event, not merely a difference between current and original values. Clearing or restoring the field does not remove the marker once the user has modified it during the relevant workflow.

The requirement therefore calls for event or provenance tracking in addition to final-value comparison. See [[concepts/ssi-id-persistence-and-edit-provenance]].
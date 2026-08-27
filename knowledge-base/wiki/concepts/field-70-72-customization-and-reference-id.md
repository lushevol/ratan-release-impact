---
type: concept
title: Field 70/72 Customization and Reference ID
created: 2026-08-23
updated: 2026-08-23
tags: [swift, field-70, field-72, reference-id, ssi, customization, uat]
related: [ssi-selection-provenance-and-ad-hoc-classification, fmo-post-trade-portal, scb-receive-cashflow-swift-stamping, what-is-the-authoritative-reference-id-and-ssi-id-contract-for-field-70-72-customization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SSI selection not treat as adhoc SSI/SSI selection not treat as adhoc SSI - UAT.md"]
---
# Field 70/72 Customization and Reference ID

In the SSI-selection UAT, SWIFT fields 70 and 72 receive different treatment from other settlement-detail fields. A change to either field creates a dedicated customization state rather than following the ordinary SSI-ID-clearing rule.

## Customization marker

The document states that changing field 70 or 72 displays the **Field 70/72 Customized** tag in cashflow details. The tag is expected to remain visible even if the user changes the field back to its original value.

This persistence means that the tag represents edit history or customization provenance, not only a current value difference.

## Identifier behaviour

The source contrasts historical behaviour with a proposed “After adding Reference ID” design:

- Historical expectation: SSI ID remains populated after field-70/72 customization.
- Reference ID expectation: SSI ID is blank and Reference ID is populated after field-70/72 customization.

The Reference ID requirement applies to auto-stamped and manually selected SSI cases. It is not verified: relevant scenarios have blank formal result fields and are marked for retest.

## Checker-specific uncertainty

The UAT records that checker views may not mirror maker identifier fields after field-70/72 changes:

- Where no SSI was initially stamped, the stated post-change design says the checker sees customized fields and the tag but neither an auto-populated SSI ID nor Reference ID.
- In the specific auto-stamped-SSI scenario, the stated checker Reference ID should represent the originally stamped SSI rather than the SSI subsequently selected by the maker.

The relationship between displayed settlement values, the selected SSI, the original auto-stamped SSI, and the Reference ID is not defined sufficiently to establish an audit model. This is tracked in [[what-is-the-authoritative-reference-id-and-ssi-id-contract-for-field-70-72-customization]].

This UAT is not SCB-specific. It should not be generalized as a requirement for [[scb-receive-cashflow-swift-stamping]] without additional evidence.
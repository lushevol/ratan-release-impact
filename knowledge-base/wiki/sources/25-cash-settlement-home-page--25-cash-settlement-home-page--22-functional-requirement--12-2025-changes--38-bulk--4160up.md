---
type: source
title: Bulk Manual STP for Group Blotter Test
authors: []
year: 2025
url: ""
venue: Internal functional test evidence
tags: [cash-settlement, group-blotter, manual-stp, functional-testing, 2025]
related: [group-blotter, bulk-manual-stp-for-group-blotter, group-major-version-completion-rules, trade-validation-gated-group-processing, what-are-the-authoritative-completion-rules-for-group-major-versions, what-does-na-mean-in-the-bulk-manual-stp-group-blotter-tests, when-does-is-trade-validated-propagate-bulk-manual-stp-to-related-group-versions, are-cases-4-4-and-5-2-complete-in-the-bulk-manual-stp-test-matrix]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# Bulk Manual STP for Group Blotter Test

This source is a functional test matrix for bulk manual STP in a group blotter within the [[cash-settlement-home-page]] domain. The matrix specifies expected outcomes but does not provide an explicit test execution status, tester, environment, pass/fail result, or implementation evidence. Screenshot filenames are retained as traceability references only.

The source is associated with [[ratan]] by folder and business-domain context, but RATAN is not explicitly named in the test matrix.

## Summary of Specified Behavior

- A selected pending cashflow can transition from `PENDING` to `END`.
- Bulk selection is tested at both group-major-version and individual-cashflow granularity.
- A group-major-version can remain `PENDING_TRADE_VALIDATION` after partial child processing.
- In selected scenarios, a parent group-major-version moves to `COMPLETED`.
- `is_trade_validated` appears to affect whether processing propagates from `T1_G2_V2` to `T1_G3_V3`.
- Several cases are incomplete or use `N/A` as the expected result, so they cannot establish behavior.

See [[bulk-manual-stp-for-group-blotter]], [[group-major-version-completion-rules]], and [[trade-validation-gated-group-processing]] for qualified interpretations.

## Test Matrix

```text
| case | group_major_version | select | expect_result | before | after | |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1：PENDING C2：PENDING ... C294：PENDING | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1：PENDING C2：PENDING ... C291：PENDING ** ** | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1：END C2：END ... C291：END | image-2025-10-31_11-1-7.png; image-2025-10-31_11-4-42.png | image-2025-10-31_11-44-41.png; image-2025-10-31_11-45-1.png | |
| 1.2 | **T1_G1_V1**: **PENDING_TRADE_VALIDATION** c1:PENDING c2:END c3:ERROR **T1_G1_V2**: **PENDING_PRE_GROUP** c1: PENDING c2:END c3:PENDING | **T1_G1_V1**: **PENDING_TRADE_VALIDATION** c1:PENDING c2:END c3:ERROR **T1_G1_V2**: **PENDING_PRE_GROUP** c1: PENDING | **T1_G1_V1**: **COMPLETED** c1:PENDING c2:END c3:ERROR **T1_G1_V2**: **PENDING_PRE_GROUP** c1: PENDING | image-2025-10-31_21-53-21.png; image-2025-10-31_21-53-58.png | image-2025-10-31_22-4-4.png; image-2025-10-31_22-3-9.png; image-2025-10-31_22-4-49.png | |
| 1.3 | **T1_G1_V1**: **PENDING_TRADE_VALIDATION** c1:PENDING c2:PENDING **T1_G1_V2**: **PENDING_PRE_GROUP** c1: PENDING c2:PENDING | **T1_G1_V1**: **PENDING_TRADE_VALIDATION** c1:PENDING c2:PENDING **T1_G1_V2**: **PENDING_PRE_GROUP** c1: PENDING c2:PENDING | **T1_G1_V1**: **COMPLETED** c1:END c3:END **T1_G1_V2**: **COMPLETED** c1:END c3:END | image-2025-10-31_22-8-48.png; image-2025-10-31_22-10-16.png | image-2025-10-31_22-14-40.png | |
| 2.1 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C291:END C292：PENDING C293：PENDING C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING | **N/A** | image-2025-10-31_14-41-41.png; image-2025-10-31_14-41-28.png | image-2025-10-31_14-45-17.png | |
| 2.2 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C291:END C292：PENDING C293：PENDING C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **N/A** | image-2025-10-31_14-47-27.png; image-2025-10-31_14-47-14.png | image-2025-10-31_14-46-56.png | |
| 2.3 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C291:END C292：PENDING C293：PENDING C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G3_V3: **PENDING_TRADE_VALIDATION C1:PENDING | **N/A** | image-2025-10-31_14-47-14.png; image-2025-10-31_14-47-27.png | image-2025-10-31_14-48-45.png | |
| 3.1 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C291:END C292：PENDING C293：PENDING C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING | **T1_G1_V1**: PENDING_TRADE_VALIDATION C292：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING | **T1_G1_V1**: PENDING_TRADE_VALIDATION C292：END | image-2025-10-31_14-47-27.png; image-2025-10-31_14-47-14.png | image-2025-10-31_14-52-44.png; image-2025-10-31_14-52-11.png | |
| 3.2 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C292:END C293：PENDING C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G1_V1**: PENDING_TRADE_VALIDATION C293：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G1_V1: **PENDING_TRADE_VALIDATION C293：END | image-2025-10-31_14-47-14.png; image-2025-10-31_14-47-27.png | image-2025-10-31_14-57-58.png; image-2025-10-31_14-58-21.png; image-2025-10-31_14-58-33.png | |
| 3.3 | **T1_G1_V1**: PENDING_TRADE_VALIDATION C1: END....C293:END C294：PENDING **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING ** ** | **T1_G1_V1: **PENDING_TRADE_VALIDATION C294：PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION C1:PENDING | **T1_G1_V1:** COMPLETED C294：END | image-2025-10-31_14-58-21.png; image-2025-10-31_14-58-33.png | image-2025-10-31_15-0-40.png; image-2025-10-31_15-0-30.png | |
| 4.1 | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION & is_trade_validated=false C1:PENDING ** ** | **T1_G2_V2: **PENDING_TRADE_VALIDATION C1:PENDING | **T1_G2_V2:**COMPLETED C1:END | image-2025-10-31_15-7-30.png; image-2025-10-31_15-8-4.png | image-2025-10-31_15-46-2.png; image-2025-10-31_15-45-32.png | |
| 4.2 | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**: PENDING_TRADE_VALIDATION & is_trade_validated=true C1:PENDING | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING | **T1_G2_V2**:COMPLETED C1:END **T1_G3_V3**:PENDING_TRADE_VALIDATION C1:END | image-2025-10-31_15-52-23.png; image-2025-10-31_15-51-43.png | image-2025-10-31_15-46-2.png; image-2025-10-31_15-45-32.png | |
| 4.3 | **T1_G2_V2**: PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**:PENDING_PRE_GROUP & is_trade_validated=true C1:PENDING ** ** | **T1_G2_V2: **PENDING_TRADE_VALIDATION C1:PENDING | **T1_G2_V2**:COMPLETED C1:END **T1_G3_V3**:COMPLETED C1:END ** ** | image-2025-10-31_15-52-23.png; image-2025-10-31_16-8-55.png | image-2025-10-31_16-11-9.png; image-2025-10-31_16-11-38.png | |
| 4.4 | **T1_G2_V1**:PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V2**:PENDING_PRE_GROUP & is_trade_validated=false C1:PENDING **T1_G3_V3**:PENDING_PRE_GROUP & is_trade_validated=true C1:PENDING ** ** ** ** | ** ** | ** ** | | | |
| | **T1_G2_V1**:PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V2**:COMPLETED & is_trade_validated=false C1:END **T1_G3_V3**:PENDING_PRE_GROUP & is_trade_validated=true C1:PENDING ** ** | **T1_G2_V1**:PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V3**:PENDING_PRE_GROUP & is_trade_validated=true C1:PENDING ** ** | ** ** | | | |
| 5.2 | **T1_G2_V1**:PENDING_TRADE_VALIDATION C1:PENDING **T1_G3_V2**:PENDING_PRE_GROUP& is_trade_validated=false C1:PENDING **T1_G3_V3**:PENDING_PRE_GROUP & is_trade_validated=true C1:PENDING ** ** | ** ** | ** ** | | | |
```

## Evidence Limitations

The matrix records expected results rather than confirmed actual results. The screenshot references may contain execution evidence, but their content is not available in the source text. Cases 4.4 and 5.2 have blank result and evidence fields, and the unlabeled row between them cannot be reliably assigned to a complete test case.
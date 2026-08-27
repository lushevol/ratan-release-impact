---
type: query
title: Are the Reported Murex CN Vostro Counts Reproducible After Data Cleansing?
tags: [cn-settlement, vostro, ssi, murex-2-11, sql, data-quality, open-question]
related: [cn-vostro-ssi-scope-and-extraction, murex-2-11, fmrp, cn-trade-migration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex 2.11 CN Vostro SSI.md"]
---
# Are the Reported Murex CN Vostro Counts Reproducible After Data Cleansing?

## Question

Can the reported populations of 2,744 Global Vostros and 146,988 China-entity Vostros be reproduced from a dated Murex 2.11 snapshot after correcting SQL defects, normalizing entity values, and confirming join semantics?

## Known issues

The China-entity query references `CPM.M_LABEL` but does not include `TRN_CPDF_DBF CPM` in its `FROM` clause. The client query includes an unquoted Atlas legal-entity value and appears to comment out the `M_NAME <> 'DO NOT USE'` filter.

The entity list contains trailing spaces and apparent naming variants, including `HHANGZHOU `, `SHENZHEN `, and `GUANGZHOU `. Source values also contain inconsistent capitalization and a possible typo, `maual`.

The reported Global and entity counts use different extraction conditions. The source does not provide a complete cross-tabulation, deduplication rule, snapshot date, or denominator for the approximate 40% Global proportion.

## Validation plan

Re-run corrected queries against an identified Murex snapshot and record:

- the exact snapshot date and environment;
- join cardinalities and duplicate behavior;
- normalized and raw entity values;
- current-record criteria, including `M_NOVO=1 AND M_NEXT=0`;
- counts before and after normalization;
- overlap between Global and entity-specific populations;
- reconciliation to SSI+ extracts;
- treatment of blank Settlement Account/Means and security values.

The historical counts should remain labelled as reported values until this validation is complete.
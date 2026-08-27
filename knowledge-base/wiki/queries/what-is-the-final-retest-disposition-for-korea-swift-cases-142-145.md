---
type: query
title: What Is the Final Retest Disposition for Korea SWIFT Cases 142–145?
created: 2026-08-23
updated: 2026-08-23
tags: [korea-migration, uat, swift-mx, retest, unresolved]
related: [korea-cash-settlement-migration, ratan-swift-message-generation, swift-message-reconciliation, swift-mx-regression-retest-normalization, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2026-changes--34-cash--7tkpsr]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Swift Generation UAT cases retest.md"]
---
# What Is the Final Retest Disposition for Korea SWIFT Cases 142–145?

## Open question

Was a formal PASS or FAIL outcome recorded for Korea Migration UAT retest cases 142–145 after the supplied evidence document was produced?

## Evidence gap

The document contains UAT and retest `pacs.008.001.08` and `camt.056.001.08` payloads for this group but leaves both its difference classification and retest result blank.

The UAT and retest records use different cashflow IDs and contain changes that exceed creation timestamps:

- settlement date changes from `2026-06-19` to `2026-05-15`;
- `EndToEndId` changes from `NOTPROVIDED` to `DV70M0000W743907`;
- the next-agent instruction loses `/INF/ ABA NO`;
- cancellation content reflects the retest payment identifiers and dates.

## Required resolution

Obtain an authorized test decision that:

1. Classifies each observed delta as expected test-data variation, accepted generator behavior, or defect.
2. Confirms whether the `pacs.008` and paired `camt.056` messages passed together.
3. Records a final PASS/FAIL result for cases 142–145.
4. States whether the `EndToEndId` behavior is limited to these fixtures or is an approved Korea rule.

Until resolved, this group is not evidence of complete SWIFT MX UAT readiness for [[korea-cash-settlement-migration]].
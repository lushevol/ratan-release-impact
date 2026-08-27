---
type: query
title: What Is the Evidenced LMS Verification Status for All Tranche 1 Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [lms, tranche-1, verification, test-evidence, manual-entities]
related: [lms, manual-entity-lms-reference-data-feed, tranche-1-lms-verification-coverage, tranche-1-uat-coverage-status, what-is-the-manual-entity-lms-feed-contract-and-reconciliation-evidence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/05 CPT/01 CPT -Tranche1-LMS verification.md"]
---
# What Is the Evidenced LMS Verification Status for All Tranche 1 Cashflows?

## Current evidence

The CPT tracker contains 14 planned cashflow cases. Ten are marked `Y` in **if send to LMS**, but it does not define that field or provide textual LMS results, tester names, receipt timestamps, reconciliation references, or completion criteria.

The only non-blank LMS-result cell is for Kenya KES, Trade ID `109838348` and Cashflow ID `M00128225482`; it contains an image attachment whose content is unavailable in the supplied source text.

Accordingly, no complete end-to-end LMS verification status can be concluded from this tracker alone.

## Required evidence

For each case marked `Y`, obtain:

1. The defined meaning of `Y` in **if send to LMS**.
2. Source dispatch or feed-publication evidence.
3. LMS receipt or ingestion evidence tied to the trade and cashflow identifiers.
4. An LMS tester, test date, and explicit pass/fail result.
5. Any reconciliation key and the authoritative completion criterion.

The relevant feed-contract question is [[what-is-the-manual-entity-lms-feed-contract-and-reconciliation-evidence]]. The coverage distinction is described in [[tranche-1-lms-verification-coverage]].
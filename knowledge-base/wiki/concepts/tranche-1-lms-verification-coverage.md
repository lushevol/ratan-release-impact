---
type: concept
title: Tranche 1 LMS Verification Coverage
created: 2026-08-23
updated: 2026-08-23
tags: [tranche-1, lms, cpt, uat, manual-entities, test-coverage]
related: [lms, manual-entity-lms-reference-data-feed, tranche-1-uat-coverage-status, what-is-the-evidenced-lms-verification-status-for-all-tranche-1-cashflows, what-blocks-local-currency-lms-verification-for-tanzania-sri-lanka-vietnam-and-bangladesh]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/05 CPT/01 CPT -Tranche1-LMS verification.md"]
---
# Tranche 1 LMS Verification Coverage

Tranche 1 LMS verification coverage is the CPT/UAT assessment of whether selected manual-entity cashflows can be sent to and validated in [[lms]].

The available tracker defines 14 planned cases: one USD and one local-currency scenario for each of seven country-labelled legal entities. Ten cases are marked `Y` for sending to LMS, but the tracker supplies no textual LMS pass/fail result, named tester, receipt confirmation, or reconciliation reference for those cases.

## Evidence boundary

A `Y` routing indication must not be treated as proof that LMS received or validated a cashflow. Its meaning is not defined in the tracker.

One Kenya KES case, Trade ID `109838348` and Cashflow ID `M00128225482`, has image-only attachments. Their contents are unavailable in the source text, so the case has supporting material but no interpretable recorded outcome.

## Incomplete local-currency coverage

Tanzania TZS remains pending downstream feedback. Sri Lanka LKO, Vietnam VNO, and Bangladesh BDO remain dependent on MO trade booking and Operations cashflow release before LMS verification can be requested.

This makes the intended dual-currency scope incomplete as documented. The applicable execution questions are tracked in [[what-is-the-evidenced-lms-verification-status-for-all-tranche-1-cashflows]] and [[what-blocks-local-currency-lms-verification-for-tanzania-sri-lanka-vietnam-and-bangladesh]].

## Relationship to the LMS feed

[[manual-entity-lms-reference-data-feed]] describes the feed concern. This concept is limited to the coverage and evidence status of the Tranche 1 verification tracker; it does not define LMS interfaces, routing rules, or success criteria.
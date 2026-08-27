---
type: query
title: Was Korea Migration Formally Signed Off?
tags: [korea, migration, sign-off, testing, swift, performance]
related: ["ratan-settlement-korea", "cao-geoffrey-ruiheng", "yang-ji-hoon", "swift-message-difference-acceptance", "post-implementation-testing"]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/End to End Testing for Korea Migration.md"]
---
# Was Korea Migration Formally Signed Off?

## Question

Did [[yang-ji-hoon]] and [[cao-geoffrey-ruiheng]] formally approve the Korea migration test after the 2026-07-28 document update, and what scope did that approval cover?

## Evidence

The source records functional pass results and marks two issues as closed. However, its sign-off fields for the Ops leader and Dev leader are blank.

The SWIFT comparison population totals 4,384 messages. The source identifies 4,325 passed or expected outcomes, but the classified excluded categories total 58 whereas total minus passed equals 59. The acceptance threshold and treatment of this discrepancy are not documented.

The stated average of `10 cashflows/minutes` is not accompanied by stage-level RATAN timings, a service-level objective, or a formal performance pass criterion.

## Information needed

- Completed sign-off evidence, including date and approval authority.
- Confirmation whether approval covered functional processing, operational readiness, SWIFT reconciliation, data/static differences, and performance.
- The applicable SWIFT reconciliation acceptance threshold and explanation for the one-message classification discrepancy.
- A documented risk decision for the SSI+/Murex Vostro difference and RATAN symbol limitation.
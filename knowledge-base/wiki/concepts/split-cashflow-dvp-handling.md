---
type: concept
title: Split Cashflow DVP Handling
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-split, DVP, Auto DVP, settlement, Ratan]
related: [auto-dvp-ebbs, dvp-exception-lifecycle, cashflow-lineage-and-amendment-correlation, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS)/AutoDVP UAT testing.md"]
---
# Split Cashflow DVP Handling

Split cashflow DVP handling is the treatment of multiple Pay child cashflows created from an original Pay cashflow linked to one Receive cashflow.

## Specified split behavior

In the split scenario:

1. One Receive cashflow, C1, is linked to an original Pay cashflow, C2.
2. C2 is split into child cashflows S1, S2, and S3.
3. S1 is released through maker/checker and becomes `Settled`.
4. S2 and S3 remain `Waiting` with DVP exceptions before the Receive-side RTA event.
5. A qualifying Receive-side eBBS RTA notification causes the DVP exceptions on S2 and S3 to close automatically.

The source does not specify the final cashflow statuses of S2 and S3 after their exceptions close.

## Contrast with non-split one-to-many linkage

A separate scenario has one Receive cashflow linked to two ordinary, non-split Pay cashflows, C2 and C3. After the Receive-side RTA notification, both Pay cashflows retain their DVP exceptions unless manually closed.

This establishes a behavioral distinction between split children and ordinary one-to-many relationships. The source does not define the data attribute or relationship algorithm that Ratan uses to distinguish them.
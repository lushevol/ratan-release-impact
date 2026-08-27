---
type: entity
title: Sabre Trade Admin Tool
created: 2026-08-23
updated: 2026-08-23
tags: [Sabre, trade replay, BCS, FM re-platforming, testing]
related: [bcs, fmrp, mock-settlement-test-data-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Mock testing data userguide.md"]
---

# Sabre Trade Admin Tool

The Sabre Trade Admin Tool is used to replay trade-message samples in a selected testing environment.

## BCS replay workflow

The guide instructs testers to:

1. Select a testing environment.
2. Choose **Replay**.
3. Select `BCS` as the source system.
4. Paste a trade-message sample.
5. Change `tradeId` and `trackingId` to new values.
6. Select **SUBMIT**.
7. Inspect the transformed result.
8. Search for the resulting cashflow in the FMO Post Trade Portal.

The guide treats the transformed result as evidence that the trade booked successfully, but it does not provide an independent booking confirmation contract.

## Reference

https://confluence.global.standardchartered.com/display/FMRP/Sabre+Trade+Admin+Tool+Overview

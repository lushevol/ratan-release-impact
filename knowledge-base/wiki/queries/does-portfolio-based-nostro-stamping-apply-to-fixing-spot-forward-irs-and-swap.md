---
type: query
title: Does Portfolio-Based Nostro Stamping Apply to Fixing, Spot, Forward, IRS, and Swap?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, portfolio, regression-testing, cdu, fixing, spot, forward, irs, swap]
related: [portfolio-based-nostro-stamping, nostro-stamping, cdu]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
---
# Does Portfolio-Based Nostro Stamping Apply to Fixing, Spot, Forward, IRS, and Swap?

## Open Question

Does the portfolio-based RFI/non-RFI nostro selection rule apply to fixing, spot, forward, IRS, and swap trade messages, or do these products retain the existing behavior of selecting the nostro matched with the vostro SI?

## Current Evidence

Test 13 states that these standard trade types should follow the existing SI-matched nostro process. The UAT document records no test data or outcome and requests regression testing from [[cdu]].

This limits the demonstrated scope of [[portfolio-based-nostro-stamping]] to the completed KRW/KRO scenarios.

## Required Evidence

Obtain CDU regression-test results for each named product type, including portfolio classification, selected nostro, selected vostro, SI mismatch behavior, generated SWIFT output, and accounting outcome.
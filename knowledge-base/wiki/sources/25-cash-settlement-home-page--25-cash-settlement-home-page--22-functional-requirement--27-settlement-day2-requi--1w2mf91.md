---
type: source
title: RFI Nostro Trade Stamping Regression
authors: []
year: 2026
url: ""
venue: UAT regression-test evidence
created: 2026-08-23
updated: 2026-08-23
tags: [uat, regression-testing, rfi-nostro, portfolio, nostro-stamping]
related: [portfolio-based-rfi-nostro-stamping, nostro-stamping, rfi-nostro-account, cash-settlement-home-page, rfi-nostro-stamping-based-on-portfolio, what-is-the-authoritative-rfi-nostro-lookup-and-duplicate-rule, rfi-nostro-trade-stamping-regression-coverage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT/RFI Nostro Trade Stamping Regression.md"]
---
# RFI Nostro Trade Stamping Regression

This UAT regression-evidence document records screenshot attachments for portfolio-based RFI Nostro stamping scenarios across IRS, fixing, forward, and swap products.

## Coverage

The matrix contains 12 substantive scenarios: each product is tested under missing Nostro, best-match Nostro, and multi-match Nostro conditions.

| Product | Missing Nostro | Best-Match Nostro | Multi-Match Nostro |
| --- | --- | --- | --- |
| IRS | Covered | Covered | Covered |
| fixing | Covered | Covered | Covered |
| forward | Covered | Covered | Covered |
| swap | Covered | Covered | Covered |

The repeated matrix suggests that [[portfolio-based-rfi-nostro-stamping]] is expected to be exercised consistently across the four product types.

## Test Evidence

| Product | Scenario | Screenshot evidence |
| --- | --- | --- |
| IRS | missing nostro | `image-2026-3-27_11-16-0.png`; `image-2026-3-27_11-18-35.png` |
| IRS | best match nostro | `image-2026-3-27_11-17-42.png`; `image-2026-3-27_11-18-5.png` |
| IRS | multi match nostro | `image-2026-3-27_11-19-57.png`; `image-2026-3-27_11-20-8.png`; `image-2026-3-27_11-21-1.png`; `image-2026-3-27_11-21-19.png` |
| fixing | missing nostro | `image-2026-3-27_11-23-56.png`; `image-2026-3-27_11-24-30.png` |
| fixing | best match nostro | `image-2026-3-27_11-24-54.png`; `image-2026-3-27_11-23-29.png` |
| fixing | multi match nostro | `image-2026-3-27_11-25-50.png`; `image-2026-3-27_11-25-40.png`; `image-2026-3-27_11-26-15.png`; `image-2026-3-27_11-26-28.png` |
| forward | missing nostro | `image-2026-3-27_11-29-43.png`; `image-2026-3-27_11-31-37.png` |
| forward | best match nostro | `image-2026-3-27_11-28-24.png`; `image-2026-3-27_11-30-1.png` |
| forward | multi match nostro | `image-2026-3-27_11-32-52.png`; `image-2026-3-27_11-32-42.png`; `image-2026-3-27_11-33-41.png` |
| swap | missing nostro | `image-2026-3-27_11-37-44.png`; `image-2026-3-27_11-38-28.png` |
| swap | best match nostro | `image-2026-3-27_11-38-50.png`; `image-2026-3-27_11-39-28.png` |
| swap | multi match nostro | `image-2026-3-27_11-40-17.png`; `image-2026-3-27_11-40-9.png`; `image-2026-3-27_11-40-44.png` |

## Evidence Limits

The attached screenshots establish that evidence was captured for every substantive scenario. They do not, from the textual document alone, establish expected results, actual outcomes, pass/fail status, or product-specific exceptions.

In particular, this source does not define the portfolio attributes used to select an [[rfi-nostro-account]], the ranking rule for a best match, the resolution of multi-match conditions, or the result of a missing-Nostro condition. These gaps are tracked in [[what-is-the-authoritative-rfi-nostro-lookup-and-duplicate-rule]].

Rows 4, 8, and 12 in the original matrix are blank separators rather than additional test scenarios.
---
type: concept
title: UK CNH eBBS Currency Preservation
created: 2026-08-22
updated: 2026-08-22
tags: [UK, CNH, CNY, eBBS, cash-settlement, currency-normalization]
related: [uk-strategic-cash-settlements-rollout, ratan, lms]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features/Settlements BRP/Settlements BRP Prioritization.md"]
---
# UK CNH eBBS Currency Preservation

UK CNH eBBS currency preservation is the requirement to send `CNH` as `CNH` in the eBBS feed when the UK cashflow currency is CNH, rather than converting it to `CNY`.

The source records this item as released on November 9, 2024. It is a specific downstream-feed representation rule and should not be generalized to all currency processing or all entities.

## Control objective

Preserving the original `CNH` code avoids an unintended currency-code transformation between cash-settlement processing and the eBBS feed. The source does not provide message examples, interface specifications, or evidence beyond the reported release comment.
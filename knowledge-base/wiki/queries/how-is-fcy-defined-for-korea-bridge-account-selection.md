---
type: query
title: How Is FCY Defined for Korea Bridge-Account Selection?
tags: [currency, bridge-account, static-data, korea, open-question]
related: [currency-dependent-bridge-account-selection, scfb-seoul, ratan-static-data-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# How Is FCY Defined for Korea Bridge-Account Selection?

The documented mapping for `SCFB_SEOUL` assigns `000287` to `KRW` and `040446` to `FCY`. The source does not state whether `FCY` means every non-KRW currency, a controlled currency group, or another classification.

The authoritative rule must specify input currency normalization, fallback behavior, static-data ownership, and validation for unsupported currencies.
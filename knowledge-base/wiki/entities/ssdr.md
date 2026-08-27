---
type: entity
title: SSDR
created: 2026-08-24
updated: 2026-08-24
tags: ["ssdr", "eod", "extract", "cashflow-splitting", "downstream-system", "dashboard", "osv", "dqsl", "api", "ratan", "indonesia", "cash-settlement", "consumer-system", "data-exposure", "downstream-application", "reporting", "entitlement"]
related: ["cashflow-splitting", "split-cashflow-downstream-integration", "dqsl", "cash-settlement-platform", "ratan-indonesia-onshoring-2026", "query-service", "cash-settlement-query-cn-cashflow-data", "wide-cashflow-read-projection-performance", "does-ssdr-cashflow-exposure-meet-its-required-latency-and-pagination-sla", "ces", "cash-settlement-data-entitlement", "ces-data-entitlement-integration"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Technical Design/Indonesia Upstream Downstream Details.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution.md"]
---
# SSDR

SSDR is a downstream reporting application that relies on RATAN data-entitlement controls when querying Cash Settlement data.

The source records that RATAN-owned entitlement was enabled for SSDR as of 10 December 2025. It separately identifies `v2/data/provider/query/cashflows` in [[query-service]] as an interface that should switch to [[ces]].

This reported current state must not be interpreted as evidence that SSDR is already integrated with CES or that its access controls meet the intended final policy.
---
type: concept
title: RatanOne UI Performance
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, ui-performance, lighthouse, cash-settlement]
related: [ratanone, ui-performance-metrics, frontend-configuration-loading, iframe-micro-frontend-loading-priority, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# RatanOne UI Performance

## Scope

This concept captures the loading and interactivity behavior of [[ratanone]] when multiple blotter applications are composed in a workspace. The evidence comes from a December 2022 UAT Office Network benchmark.

## Baseline findings

| Case | Workspace composition | TTI | TBT | Performance score |
| --- | --- | ---: | ---: | ---: |
| I | Cashflow Blotter only | 8.8 sec | 2,000 ms | 27 |
| II | Cashflow Blotter, Suppression Rules, and Validation Exception | 9.2 sec | 4,350 ms | 27 |
| III | Cashflow Blotter and Trade Blotter in the first screen; Validation Exception and Settlement Exceptions in the second | 13.7 sec | 5,340 ms | 17 |
| IV | Cashflow Blotter and Trade Blotter in the first screen; Validation Exception and Settlement Exceptions behind | 19.8 sec | 14,100 ms | 13 |

TTI and TBT worsen substantially as more applications are loaded. FCP and LCP remain comparatively moderate, showing that initial paint does not necessarily mean the workspace is ready for user interaction.

## Principal bottlenecks

- Serial configuration JSON loading delays `main.js` execution.
- iFrame composition does not guarantee that first-screen applications load first.
- Additional blotters increase JavaScript execution and resource contention.
- The reported Lighthouse scores are affected by poorly performing notebook hardware.

The most directly measured optimization is consolidated or zipped configuration loading, which reduced the reported cashflow-grid FMP from 2.89–4.46 seconds to 1.03 seconds in the supplied tests.

## Recommended measurement

RatanOne should track workflow-specific milestones in addition to browser metrics:

- Cashflow Loaded: under 3 seconds.
- Cashflow Table Loaded: under 300 milliseconds.
- Cashflow Quick Search Interaction: under 500 milliseconds.
- Cashflow Custom Search Interaction: under 1,000 milliseconds.

These targets are proposed by the source and are not identified as approved production SLAs.

## Architectural direction

Potential improvements include configuration aggregation, skeleton loading, shell-level loading priority, on-demand application loading, `ratan-message` loading-state propagation, custom performance tracking, and continuous monitoring. Migration from iFrame composition to [[single-spa]] is presented as a possibility rather than an approved decision.

## Evidence boundary

Absolute Lighthouse scores should not be treated as production-grade measurements. Relative differences across workspace cases are directionally useful, but repeatable tests with controlled hardware, browser, network, cache, and dataset conditions are required.
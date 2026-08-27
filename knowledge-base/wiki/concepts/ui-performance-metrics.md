---
type: concept
title: UI Performance Metrics
created: 2026-08-24
updated: 2026-08-24
tags: [ui-performance, browser-metrics, lighthouse, observability]
related: [ratanone-ui-performance, lighthouse]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Performance Analysis (2022 Dec).md"]
---
# UI Performance Metrics

## Browser metrics

| Metric | Meaning |
| --- | --- |
| FCP | First Contentful Paint: when the first text or image is painted |
| FMP | First Meaningful Paint: when meaningful application content has finished rendering |
| TTI | Time to Interactive: when the application can reliably respond to user interaction |
| TBT | Total Blocking Time: the sum of blocking time from long tasks between FCP and interactivity |
| LCP | Largest Contentful Paint: when the largest visible text or image is painted |
| FID | First Input Delay: the delay from the first user interaction to the browser response |

The source references web.dev guidance for FCP, LCP, FID, TTI, and TBT. FMP and TTI are retained in the source’s benchmark vocabulary, although metric definitions and Lighthouse treatment can vary by tool version.

## Reference thresholds

| Metric | Good | Needs improvement | Poor |
| --- | --- | --- | --- |
| FCP | < 1.8 sec | 1.8–3.0 sec | > 3 sec |
| LCP | < 2.5 sec | 2.5–4.0 sec | > 4 sec |
| FID | < 100 ms | 100–300 ms | > 300 ms |
| TTI | Reduce the gap between FCP and TTI | — | — |
| TBT | Reduce TBT | — | — |

## Application-specific metrics

Generic paint metrics do not establish whether a cash-settlement operator can work with a blotter. The source therefore proposes:

| Metric | Description | Target |
| --- | --- | --- |
| Cashflow Loaded | Initialization to first data table | < 3 sec |
| Cashflow Table Loaded | Table initialization to first data table | < 300 ms |
| Cashflow Quick Search Interaction | Search click to result display | < 500 ms |
| Cashflow Custom Search Interaction | Custom search or view change to result display | < 1,000 ms |

These are proposed targets, not confirmed acceptance criteria.
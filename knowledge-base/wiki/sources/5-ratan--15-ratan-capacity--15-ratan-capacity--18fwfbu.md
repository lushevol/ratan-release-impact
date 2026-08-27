---
type: source
title: RATAN Capacity Management Plan Index
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, ratanone, capacity-management, performance, sla, testing]
related: [ratan-capacity-factors, ratan-sla-capacity-baseline, ratan-performance-capacity-multipliers, what-is-the-authoritative-ratan-capacity-baseline, what-is-the-ratan-capacity-peak-measurement-interval, why-is-ratan-trade-eod-capacity-targeted-at-2x, are-ratan-capacity-factors-tested-or-only-sla-assumptions]
sources: ["RATAN/RATAN -Capacity/RATAN -Capacity.md"]
authors: []
year: 0
url: "https://onepoint.global.standardchartered.com/ui/form/mid=102767&pid=75441175&iid=526477139"
venue: "OnePoint and Confluence"
---
# RATAN Capacity Management Plan Index

This index points to the finalized **RATAN (51358) Capacity Management Plan [PLAN-16312]** and related capacity-testing materials. It states SLA-agreed capacity figures and testing targets, but does not itself provide observed test measurements, test environments, pass/fail outcomes, or evidence that targets were achieved.

## Primary plan

[RATAN (51358) Capacity Management Plan [PLAN-16312]](https://onepoint.global.standardchartered.com/ui/form/mid=102767&pid=75441175&iid=526477139)

## Capacity agreed in SLA

| Service Measurements (i.e Name of Products, Name of Components, Concurrent users, etc.) | Volumes |
|---|---:|
| Capacity Factor-1 (Daily Max volume) | 335,771 as current daily volume |
| Trade daily volume | 158,263 |
| Settlemet GDC daily volume | 173,610 |
| ISO Korea daily volume | 3,898 |
| Sum | 335,771 |
| Capacity Factor-2 (Peak volume per hour or minutes) assumption — Settlement | 19,396 |
| Capacity Factor-2 (Peak volume per hour or minutes) assumption — Trade (intraday) | 10,927 |
| Capacity Factor-2 (Peak volume per hour or minutes) assumption — Trade (EOD) | 58,713 |
| Capacity Factor-3 (Concurrent users) — Max concurrent per min | 89->103 |
| Capacity Factor-3 (Concurrent users) — Total users | 386->545 |
| Capacity Factor-4 — 4X STP(Settlement) | 19,396 * 4 = 77,584 per hour |
| Capacity Factor-4 — 4X STP(Trade intraday) | 10,927 * 4 = 43,708 per hour |
| Capacity Factor-4 — 2X STP(Trade EOD) | 58,713 * 2 = 117,426 per hour |
| Capacity Factor-4 — 4X concurrent users | 103 * 4 = 412 |
| User action turn around time — Cashflow blotter loading, maximum | 5 seconds |
| User action turn around time — Cashflow blotter loading, average | 2 seconds |

The daily-volume components sum to the stated total: `158,263 + 173,610 + 3,898 = 335,771`.

The source label `Settlemet GDC` is retained as written. It appears likely to refer to Settlement GDC, but this is not confirmed by the source.

## Linked testing materials

### Post Portal baseline

- [PTP Test Result - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/PTP+Test+Result)
- [Test Result - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Test+Result)

### Application performance

- [RATAN One - Backend Performance Test Result Feb 2025 - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RATAN+One+-+Backend+Performance+Test+Result+Feb+2025)
- [Trade Control Line Performance Testing Metric Collection - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Trade+Control+Line+Performance+Testing+Metric+Collection)

### Non-functional testing

- [RATAN One Non-Functional Testing - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RATAN+One+Non-Functional+Testing)

## Interpretation boundaries

The four stated factors are documented in [[ratan-capacity-factors]]. The daily baseline is recorded in [[ratan-sla-capacity-baseline]], and multiplier requirements are detailed in [[ratan-performance-capacity-multipliers]].

The statement that RATAN can process “up to 4 times” hourly volume has a stated Trade EOD exception: its calculation is 2X, not 4X. The source also leaves the Capacity Factor-2 time interval ambiguous by saying “per hour or minutes.”

The 5-second maximum and 2-second average Cashflow blotter loading figures are requirements or targets from this source, not recorded measured results. They provide capacity context for [[cashflow-blotter]], [[ratanone-ui-performance]], and [[ui-performance-metrics]].
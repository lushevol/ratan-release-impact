---
type: source
title: Production Performance Monitoring
authors: []
year: 2023
url: ""
venue: Internal operational monitoring record
created: 2026-08-24
updated: 2026-08-24
tags: [production-monitoring, murex-211, fmrp, cashflow-integration, throughput, post-go-live]
related: [ratan-murex-211-cashflow-integration, fmrp, fmrp-outbound-mq, fmrp-inbound-mq, production-performance-monitoring, fmrp-cashflow-publication-lifecycle, fmrp-murex-cashflow-status-synchronization, fmrp-payment-insertion-eligibility, what-are-the-authoritative-production-performance-counters-for-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Production Performance Monitoring.md"]
---
# Production Performance Monitoring

This operational record documents batch and real-time volumes around the stated Biz GO LIVE date of 13 November 2023 for the Murex 2.11 cashflow integration.

## Summary of reported evidence

For the real-time outbound snapshot dated `20231113`, `docPayment` received 10,012 records and routed 4,071 to `extSettle`. `extSettleRouter` sent 4,057 records to FMRP and 14 to `mls`.

The source reports that all 4,057 FMRP-bound records passed through `FmrpFilter`, `FmrpSettleEnrichment`, `FmrpSettleFilter`, and `FmrpOutboundMQ`. The reported peak rate for these stages was 252 records per hour, or 4.20 records per minute.

The inbound snapshot reports 4,092 records from `FmrpInoundMQ`—a source spelling that is likely intended to mean [[fmrp-inbound-mq]]. `FmrpInboundRouter` splits the volume into 4,057 `acked` records and 35 `released` records. The acknowledgement branch reports 4,057 successes through `FmrpAckProcessor`.

This is throughput and routing evidence, not an SLA assessment. The record does not provide latency distributions, queue depth, resource utilization, alert thresholds, failure percentages, or target performance criteria.

## Reconciliation cautions

The source does not define whether the counters are interval, cumulative, retry-inclusive, or sampled. Consequently, the following figures must not be interpreted as failure rates or loss rates without corroboration:

- `FlowEntrySpliter` reports 162 records from node `82193`, whereas `FmrpInboundRouter` reports 35 records on its `released` branch.
- `PayInsertionFilter` lists 220 discarded, 57 retried, and 2,020 processed records against an input volume of 2,240; the outputs total 2,297.
- `INIT2SNTR1` lists 2,020 input records, 2,018 triggered records, and 439 error records.
- Batch entries begin on 7 November 2023, before the stated 13 November 2023 go-live date.
- Several timestamps use `12:00AM` alongside `12:00PM`, including apparently overlapping entries. Time-zone and AM/PM semantics are not stated.

See [[what-are-the-authoritative-production-performance-counters-for-murex-211-cashflow-integration]] for the unresolved counter semantics and reconciliation questions.

## Source tables

### Static on RT - Outbound Vol

| **Key Task** | **In Node** | **Out Node** | **Out Name** | **Date** | **In Vol** | **Out Vol** | **Peak Hours** | **Peak Hours Vol** | **Peak Hours Vol/min** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| docPayment | 44520 | 6172 | OUT | 20231113 | 10012 | 2658 | 2：00-3：00am | | |
| | | 6174 | DISCARD | | | 839 | | | |
| | | 61992 | C6 | | | 202 | | | |
| | | 64216 | CCIL | | | 2 | | | |
| | | 82224 | insert | | | 2240 | 97 | 1.62 | |
| | | 82225 | extSettle | | | 4071 | 252 | 4.20 | |
| extSettleRouter | 82225 | 82218 | mls | | 4071 | 14 | | | |
| | | 82197 | fmrp | | 4071 | 4057 | 252 | 4.20 | |
| FmrpFilter | 82197 | 82192 | out | | 4057 | 4057 | 252 | 4.20 | |
| | | 82222 | discard | | | 0 | 252 | 4.20 | |
| FmrpSettleEnrichment | 82192 | 82215 | | | 4057 | 4057 | 252 | 4.20 | |
| FmrpSettleFilter | 82215 | 82216 | | | 4057 | 4057 | 252 | 4.20 | |
| FmrpOutboundMQ | 82216 | 82204 | | | 4057 | 4057 | 252 | 4.20 | |

### Static on RT - Inbound Vol

| **Key Task** | **In Node** | **Out Node** | **Out Name** | **Date** | **In Vol** | **Out Vol** | **Peak Hours** | **Peak Hours Vol** | **Peak Hours Vol/min** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FmrpInoundMQ | | 82296 | Output | | | 4092 | 2：00-3：00am | 252 | 4.20 |
| FmrpInboundRouter | 82296 | 82211 | discard | | | | | |
| | | 82205 | acked | | | 4057 | 252 | 4.20 |
| | | 82193 | released | | | 35 | | |
| FmrpAckProcessor | 82205 | 82221 | success | | | 4057 | 252 | 4.20 |
| FlowEntrySpliter | 82193 | 82198 | out | | | 162 | | |
| PayInsertionFilter | 82224 | 82212 | discard | | 2240 | 220 | 5 | 0.08 |
| | | 82207 | retry | | 57 | 6 | 0.10 |
| | | 82208 | process | | 2020 | 92 | 1.53 |
| INIT2SNTR1 | 82208 | 82294 | Triggered | | 2020 | 2018 | 92 | 1.53 |
| | 82209 | 82295 | Error | | 439 | 441 | 14 | 0.23 |
| SNTR2RLSR | 82198 | 82200 | Triggered | | | 161 | | |
| | | 82201 | Error | | | 6 | | |

### Static on Batch Job Vol

| Date | Starting Time | EndTime | Vol |
| --- | --- | --- | --- |
| Nov 7 2023 | 12:00AM | 12:01AM | 1 |
| Nov 8 2023 | 6:15AM | 6:15AM | 1 |
| Nov 8 2023 | 6:30AM | 6:31AM | 1 |
| Nov 9 2023 | 1:45AM | 1:46AM | 2 |
| Nov 9 2023 | 2:30AM | 2:31AM | 4 |
| Nov 9 2023 | 2:45AM | 2:46AM | 2 |
| Nov 9 2023 | 3:00AM | 3:01AM | 2 |
| Nov 9 2023 | 3:30AM | 3:31AM | 2 |
| Nov 9 2023 | 6:15AM | 6:16AM | 2 |
| Nov 9 2023 | 6:30AM | 6:31AM | 2 |
| Nov 10 2023 | 2:15AM | 2:16AM | 10 |
| Nov 10 2023 | 2:30AM | 2:31AM | 2 |
| Nov 10 2023 | 2:45AM | 2:45AM | 1 |
| Nov 10 2023 | 2:45AM | 2:46AM | 3 |
| Nov 10 2023 | 3:00AM | 3:01AM | 8 |
| Nov 10 2023 | 3:15AM | 3:16AM | 14 |
| Nov 10 2023 | 3:30AM | 3:34AM | 227 |
| Nov 10 2023 | 6:15AM | 6:15AM | 3 |
| Nov 10 2023 | 7:00AM | 7:01AM | 1 |
| Nov 10 2023 | 7:15AM | 7:16AM | 2 |
| Nov 10 2023 | 7:30AM | 7:31AM | 4 |
| Nov 10 2023 | 8:00AM | 8:01AM | 5 |
| Nov 10 2023 | 8:45AM | 8:45AM | 1 |
| Nov 10 2023 | 8:45AM | 8:46AM | 2 |
| Nov 10 2023 | 9:00AM | 9:01AM | 1 |
| Nov 10 2023 | 10:15AM | 10:16AM | 6 |
| Nov 10 2023 | 10:45AM | 10:46AM | 3 |
| Nov 10 2023 | 11:00AM | 11:01AM | 3 |
| Nov 10 2023 | 11:30AM | 11:31AM | 4 |
| Nov 10 2023 | 11:45AM | 11:46AM | 2 |
| Nov 10 2023 | 12:00AM | 12:03AM | 4 |
| Nov 11 2023 | 2:00AM | 2:03AM | 100 |
| Nov 13 2023 | 1:15AM | 1:17AM | 80 |
| Nov 13 2023 | 1:30AM | 1:31AM | 4 |
| Nov 13 2023 | 1:30AM | 1:32AM | 36 |
| Nov 13 2023 | 1:45AM | 1:48AM | 40 |
| Nov 13 2023 | 2:00AM | 2:01AM | 40 |
| Nov 13 2023 | 2:15AM | 2:16AM | 40 |
| Nov 13 2023 | 2:30AM | 2:31AM | 40 |
| Nov 13 2023 | 2:45AM | 2:46AM | 40 |
| Nov 13 2023 | 3:00AM | 3:02AM | 40 |
| Nov 13 2023 | 3:15AM | 3:17AM | 40 |
| Nov 13 2023 | 3:30AM | 3:31AM | 40 |
| Nov 13 2023 | 3:45AM | 3:46AM | 40 |
| Nov 13 2023 | 4:00AM | 4:02AM | 40 |
| Nov 13 2023 | 4:15AM | 4:16AM | 40 |
| Nov 13 2023 | 4:30AM | 4:31AM | 40 |
| Nov 13 2023 | 4:45AM | 4:46AM | 40 |
| Nov 13 2023 | 5:00AM | 5:02AM | 40 |
| Nov 13 2023 | 5:15AM | 5:16AM | 40 |
| Nov 13 2023 | 5:30AM | 5:31AM | 40 |
| Nov 13 2023 | 5:45AM | 5:46AM | 40 |
| Nov 13 2023 | 6:00AM | 6:01AM | 40 |
| Nov 13 2023 | 6:15AM | 6:17AM | 40 |
| Nov 13 2023 | 6:30AM | 6:31AM | 40 |
| Nov 13 2023 | 6:45AM | 6:47AM | 40 |
| Nov 13 2023 | 7:00AM | 7:01AM | 16 |
| Nov 13 2023 | 7:15AM | 7:16AM | 64 |
| Nov 13 2023 | 7:30AM | 7:31AM | 40 |
| Nov 13 2023 | 7:45AM | 7:46AM | 40 |
| Nov 13 2023 | 8:00AM | 8:01AM | 40 |
| Nov 13 2023 | 8:15AM | 8:16AM | 40 |
| Nov 13 2023 | 8:30AM | 8:31AM | 40 |
| Nov 13 2023 | 8:45AM | 8:46AM | 40 |
| Nov 13 2023 | 9:00AM | 9:01AM | 40 |
| Nov 13 2023 | 9:15AM | 9:16AM | 40 |
| Nov 13 2023 | 9:30AM | 9:32AM | 40 |
| Nov 13 2023 | 9:45AM | 9:46AM | 40 |
| Nov 13 2023 | 10:00AM | 10:02AM | 40 |
| Nov 13 2023 | 10:15AM | 10:16AM | 40 |
| Nov 13 2023 | 10:30AM | 10:32AM | 40 |
| Nov 13 2023 | 10:45AM | 10:46AM | 40 |
| Nov 13 2023 | 11:00AM | 11:01AM | 40 |
| Nov 13 2023 | 11:15AM | 11:17AM | 40 |
| Nov 13 2023 | 11:30AM | 11:31AM | 40 |
| Nov 13 2023 | 11:45AM | 11:47AM | 40 |
| Nov 13 2023 | 12:00AM | 12:01AM | 40 |
| Nov 13 2023 | 12:00PM | 12:02PM | 40 |
| Nov 13 2023 | 12:15AM | 12:16AM | 40 |
| Nov 13 2023 | 12:15PM | 12:16PM | 40 |
| Nov 13 2023 | 12:30AM | 12:31AM | 40 |
| Nov 13 2023 | 12:30PM | 12:31PM | 39 |
| Nov 13 2023 | 12:45AM | 12:46AM | 40 |
| Nov 14 2023 | 1:00AM | 1:02AM | 40 |
| Nov 14 2023 | 1:15AM | 1:16AM | 40 |
| Nov 14 2023 | 1:30AM | 1:31AM | 20 |
| Nov 14 2023 | 2:00AM | 2:02AM | 32 |
| Nov 14 2023 | 2:15AM | 2:16AM | 7 |
| Nov 14 2023 | 2:30AM | 2:32AM | 8 |
| Nov 14 2023 | 3:00AM | 3:01AM | 4 |
| Nov 14 2023 | 3:15AM | 3:16AM | 5 |
| Nov 14 2023 | 3:45AM | 3:46AM | 5 |
| Nov 14 2023 | 4:00AM | 4:01AM | 1 |
| Nov 14 2023 | 5:45AM | 5:46AM | 2 |
| Nov 14 2023 | 6:00AM | 6:01AM | 2 |
| Nov 14 2023 | 6:45AM | 6:46AM | 2 |
| Nov 14 2023 | 7:15AM | 7:16AM | 3 |
| Nov 14 2023 | 7:45AM | 7:46AM | 2 |
| Nov 14 2023 | 8:00AM | 8:01AM | 2 |
| Nov 14 2023 | 8:30AM | 8:31AM | 2 |
| Nov 14 2023 | 8:45AM | 8:46AM | 5 |
| Nov 14 2023 | 9:45AM | 9:46AM | 4 |
| Nov 14 2023 | 10:45AM | 10:46AM | 2 |
| Nov 14 2023 | 12:00AM | 12:02AM | 40 |
| Nov 14 2023 | 12:15AM | 12:17AM | 40 |
| Nov 14 2023 | 12:30AM | 12:32AM | 40 |
| Nov 14 2023 | 12:45AM | 12:46AM | 5 |
| Nov 15 2023 | 1:00AM | 1:02AM | 40 |
| Nov 15 2023 | 1:15AM | 1:16AM | 23 |
| Nov 15 2023 | 1:30AM | 1:31AM | 2 |
| Nov 15 2023 | 1:45AM | 1:48AM | 95 |
| Nov 15 2023 | 2:00AM | 2:01AM | 8 |
| Nov 15 2023 | 2:15AM | 2:16AM | 9 |
| Nov 15 2023 | 2:45AM | 2:46AM | 2 |
| Nov 15 2023 | 3:00AM | 3:01AM | 11 |
| Nov 15 2023 | 3:15AM | 3:16AM | 4 |
| Nov 15 2023 | 3:30AM | 3:31AM | 5 |
| Nov 15 2023 | 3:45AM | 3:46AM | 10 |
| Nov 15 2023 | 4:00AM | 4:01AM | 5 |
| Nov 15 2023 | 6:00AM | 6:01AM | 1 |
| Nov 15 2023 | 6:15AM | 6:16AM | 5 |
| Nov 15 2023 | 6:30AM | 6:31AM | 3 |
| Nov 15 2023 | 6:45AM | 6:46AM | 2 |
| Nov 15 2023 | 7:00AM | 7:01AM | 5 |
| Nov 15 2023 | 7:15AM | 7:16AM | 4 |
| Nov 15 2023 | 7:30AM | 7:32AM | 6 |
| Nov 15 2023 | 7:45AM | 7:46AM | 5 |
| Nov 15 2023 | 8:00AM | 8:02AM | 4 |
| Nov 15 2023 | 8:15AM | 8:16AM | 1 |
| Nov 15 2023 | 8:45AM | 8:46AM | 2 |
| Nov 15 2023 | 9:00AM | 9:01AM | 2 |
| Nov 15 2023 | 9:15AM | 9:16AM | 3 |
| Nov 15 2023 | 9:45AM | 9:46AM | 2 |
| Nov 15 2023 | 10:00AM | 10:01AM | 2 |
| Nov 15 2023 | 10:15AM | 10:16AM | 2 |
| Nov 15 2023 | 12:00AM | 12:03AM | 40 |
| Nov 15 2023 | 12:15AM | 12:17AM | 40 |
| Nov 15 2023 | 12:30AM | 12:32AM | 40 |
| Nov 15 2023 | 12:45AM | 12:47AM | 40 |
| Nov 16 2023 | 1:00AM | 1:02AM | 28 |
| Nov 16 2023 | 1:15AM | 1:16AM | 31 |
| Nov 16 2023 | 2:30AM | 2:31AM | 4 |
| Nov 16 2023 | 2:45AM | 2:46AM | 4 |
| Nov 16 2023 | 3:15AM | 3:16AM | 2 |
| Nov 16 2023 | 3:30AM | 3:31AM | 2 |
| Nov 16 2023 | 3:45AM | 3:46AM | 4 |
| Nov 16 2023 | 6:00AM | 6:02AM | 4 |
| Nov 16 2023 | 6:30AM | 6:31AM | 2 |
| Nov 16 2023 | 7:00AM | 7:01AM | 4 |
| Nov 16 2023 | 7:17AM | 7:17AM | 8 |
| Nov 16 2023 | 7:30AM | 7:31AM | 7 |
| Nov 16 2023 | 8:00AM | 8:02AM | 2 |
| Nov 16 2023 | 8:30AM | 8:31AM | 2 |
| Nov 16 2023 | 9:00AM | 9:01AM | 2 |
| Nov 16 2023 | 9:30AM | 9:31AM | 2 |
| Nov 16 2023 | 10:15AM | 10:16AM | 1 |
| Nov 16 2023 | 12:30AM | 12:32AM | 40 |
| Nov 16 2023 | 12:45AM | 12:46AM | 40 |
| Nov 16 2023 | 1:00AM | 1:02AM | 24 |
| Nov 17 2023 | 1:15AM | 1:16AM | 30 |
| Nov 17 2023 | 2:15AM | 2:17AM | 4 |
| Nov 17 2023 | 2:30AM | 2:32AM | 1 |
| Nov 17 2023 | 3:00AM | 3:02AM | 7 |
| Nov 17 2023 | 3:15AM | 3:16AM | 6 |
| Nov 17 2023 | 3:30AM | 3:31AM | 4 |
| Nov 17 2023 | 4:00AM | 4:01AM | 1 |
| Nov 17 2023 | 5:15AM | 5:16AM | 8 |
| Nov 17 2023 | 5:45AM | 5:46AM | 1 |
| Nov 17 2023 | 6:00AM | 6:01AM | 2 |
| Nov 17 2023 | 6:15AM | 6:16AM | 8 |
| Nov 17 2023 | 6:30AM | 6:31AM | 4 |
| Nov 17 2023 | 6:45AM | 6:46AM | 4 |
| Nov 17 2023 | 7:00AM | 7:01AM | 8 |
| Nov 17 2023 | 7:15AM | 7:16AM | 2 |
| Nov 17 2023 | 7:30AM | 7:31AM | 6 |
| Nov 17 2023 | 7:45AM | 7:46AM | 8 |
| Nov 17 2023 | 8:00AM | 8:01AM | 1 |
| Nov 17 2023 | 8:15AM | 8:16AM | 2 |
| Nov 17 2023 | 8:30AM | 8:31AM | 10 |
| Nov 17 2023 | 8:45AM | 8:46AM | 9 |
| Nov 17 2023 | 9:00AM | 9:01AM | 4 |
| Nov 17 2023 | 9:30AM | 9:31AM | 2 |
| Nov 17 2023 | 12:30AM | 12:32AM | 18 |
| Nov 17 2023 | 12:45AM | 12:46AM | 40 |
| Nov 20 2023 | 1:00AM | 1:02AM | 40 |
| Nov 20 2023 | 1:15AM | 1:16AM | 40 |
| Nov 20 2023 | 1:30AM | 1:32AM | 19 |
| Nov 20 2023 | 1:45AM | 1:46AM | 40 |
| Nov 20 2023 | 2:00AM | 2:02AM | 57 |
| Nov 20 2023 | 2:15AM | 2:16AM | 40 |
| Nov 20 2023 | 2:30AM | 2:32AM | 40 |
| Nov 20 2023 | 2:45AM | 2:46AM | 43 |
| Nov 20 2023 | 3:00AM | 3:02AM | 40 |
| Nov 20 2023 | 3:15AM | 3:16AM | 40 |
| Nov 20 2023 | 3:30AM | 3:32AM | 40 |
| Nov 20 2023 | 3:45AM | 3:47AM | 40 |
| Nov 20 2023 | 4:00AM | 4:02AM | 40 |
| Nov 20 2023 | 4:15AM | 4:17AM | 40 |
| Nov 20 2023 | 4:30AM | 4:32AM | 40 |
| Nov 20 2023 | 4:45AM | 4:47AM | 40 |
| Nov 20 2023 | 5:00AM | 5:02AM | 40 |
| Nov 20 2023 | 5:15AM | 5:17AM | 40 |
| Nov 20 2023 | 5:30AM | 5:32AM | 40 |
| Nov 20 2023 | 5:45AM | 5:47AM | 40 |
| Nov 20 2023 | 6:00AM | 6:02AM | 40 |
| Nov 20 2023 | 6:15AM | 6:17AM | 40 |
| Nov 20 2023 | 6:30AM | 6:32AM | 40 |
| Nov 20 2023 | 6:45AM | 6:47AM | 40 |
| Nov 20 2023 | 7:00AM | 7:02AM | 20 |
| Nov 20 2023 | 7:45AM | 7:46AM | 2 |
| Nov 20 2023 | 8:15AM | 8:16AM | 4 |
| Nov 20 2023 | 8:30AM | 8:32AM | 7 |
| Nov 20 2023 | 9:30AM | 9:31AM | 2 |
| Nov 20 2023 | 9:45AM | 9:46AM | 2 |
| Nov 20 2023 | 12:00AM | 12:01AM | 40 |
| Nov 20 2023 | 12:15AM | 12:16AM | 40 |
| Nov 20 2023 | 12:30AM | 12:32AM | 40 |
| Nov 20 2023 | 12:45AM | 12:46AM | 40 |
| Nov 21 2023 | 1:00AM | 1:02AM | 27 |
| Nov 21 2023 | 1:15AM | 1:17AM | 53 |
| Nov 21 2023 | 1:30AM | 1:32AM | 40 |
| Nov 21 2023 | 1:45AM | 1:47AM | 37 |
| Nov 21 2023 | 2:00AM | 2:02AM | 40 |
| Nov 21 2023 | 2:15AM | 2:17AM | 28 |
| Nov 21 2023 | 2:45AM | 2:46AM | 3 |
| Nov 21 2023 | 3:00AM | 3:02AM | 4 |
| Nov 21 2023 | 3:15AM | 3:16AM | 1 |
| Nov 21 2023 | 3:45AM | 3:46AM | 6 |
| Nov 21 2023 | 4:00AM | 4:02AM | 10 |
| Nov 21 2023 | 4:15AM | 4:16AM | 6 |
| Nov 21 2023 | 4:30AM | 4:31AM | 2 |
| Nov 21 2023 | 6:00AM | 6:02AM | 6 |
| Nov 21 2023 | 6:15AM | 6:16AM | 3 |
| Nov 21 2023 | 6:30AM | 6:31AM | 2 |
| Nov 21 2023 | 7:00AM | 7:02AM | 8 |
| Nov 21 2023 | 7:15AM | 7:16AM | 5 |
| Nov 21 2023 | 7:45AM | 7:46AM | 4 |
| Nov 21 2023 | 8:15AM | 8:16AM | 6 |
| Nov 21 2023 | 8:30AM | 8:32AM | 4 |
| Nov 21 2023 | 8:45AM | 8:46AM | 3 |
| Nov 21 2023 | 9:00AM | 9:01AM | 1 |
| Nov 21 2023 | 12:00AM | 12:03AM | 40 |
| Nov 21 2023 | 12:15AM | 12:17AM | 40 |
| Nov 21 2023 | 12:30AM | 12:32AM | 40 |
| Nov 21 2023 | 12:45AM | 12:47AM | 40 |
| Nov 21 2023 | 1:00AM | 1:02AM | 32 |
| Nov 22 2023 | 1:15AM | 1:17AM | 48 |
| Nov 22 2023 | 1:30AM | 1:32AM | 40 |
| Nov 22 2023 | 1:45AM | 1:46AM | 2 |
| Nov 22 2023 | 3:00AM | 3:02AM | 2 |
| Nov 22 2023 | 3:30AM | 3:32AM | 12 |
| Nov 22 2023 | 3:45AM | 3:46AM | 2 |
| Nov 22 2023 | 5:00AM | 5:01AM | 3 |
| Nov 22 2023 | 6:15AM | 6:17AM | 4 |
| Nov 22 2023 | 7:00AM | 7:02AM | 6 |
| Nov 22 2023 | 7:15AM | 7:16AM | 4 |
| Nov 22 2023 | 7:45AM | 7:47AM | 4 |
| Nov 22 2023 | 8:00AM | 8:02AM | 16 |
| Nov 22 2023 | 8:15AM | 8:16AM | 1 |
| Nov 22 2023 | 8:30AM | 8:31AM | 2 |
| Nov 22 2023 | 8:45AM | 8:47AM | 3 |
| Nov 22 2023 | 12:00AM | 12:02AM | 40 |
| Nov 22 2023 | 12:15AM | 12:17AM | 40 |
| Nov 22 2023 | 12:30AM | 12:32AM | 40 |
| Nov 22 2023 | 12:45AM | 12:46AM | 40 |
---
type: concept
title: ITRS-to-Control-M File-Monitor Mapping
created: 2026-08-22
updated: 2026-08-22
tags: [itrs, control-m, file-monitoring, eod, aspire, ratan]
related: [itrs, controlm, ratan, aspire, what-are-the-complete-itrs-monitoring-parameters-for-ratan-eod-files, why-does-rat-cn-acc-hk-identify-two-different-accounting-jobs]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md"]
---
# ITRS-to-Control-M File-Monitor Mapping

ITRS-to-Control-M file-monitor mapping provides traceability from an expected EOD output filename to the scheduled job that produces it. The source documents four RATAN-to-Aspire accounting mappings, all hosted on `uklvasapp590` within `RATAN_Settlement_Aspire_P`.

| ITRS filename | Control-M producer job | Accounting scope |
| --- | --- | --- |
| `RATAN_PAYMENT_TRANSACTION_HK` | `RAT_CN_ACC_HK` | Aspire accounting for HK |
| `RATAN_PAYMENT_TRANSACTION_TH` | `RAT_CN_ACC_TH` | Aspire accounting for TH |
| `RATAN_PAYMENT_TRANSACTION_TW` | `RAT_CN_ACC_TW` | Aspire accounting for TW |
| `RATAN_PAYMENT_TRANSACTION_JE` | `RAT_CN_ACC_JE` | Aspire accounting for JE |

This is not a complete monitor specification. It identifies filenames and corresponding producer jobs, but not monitor configuration or operational response requirements. The `RAT_CN_ACC_HK` producer must be distinguished from a same-named eBBS-accounting entry under `RATAN_CN_AUTO_JOB_P`; see [[why-does-rat-cn-acc-hk-identify-two-different-accounting-jobs]].

Related systems are [[itrs]], [[controlm]], [[ratan]], and [[aspire]].
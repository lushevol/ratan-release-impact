---
type: concept
title: Murex-RATAN Hybrid Batch and Real-Time Processing
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, control-m, batch-processing, real-time-processing, cashflows]
related: [murex-ratan-bidirectional-cashflow-integration, china-cashflow-payment-stp-exclusion, scb-fmrp-dbf, control-m, cn-settlement-murex-211-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Murex-RATAN Hybrid Batch and Real-Time Processing

The CN integration combines two routes that converge on the same Murex workflow and RATAN publication mechanism.

## Regular processing

For `VD -7`, [[control-m]] runs every two hours to populate `SCB_FMRP_DBF`, move cashflows from `INIT` to `SNTR`, trigger a RATAN validation publication, and synchronize workflow status back to staging.

## Real-time processing

The real-time path begins when an eligible cashflow is inserted in `INIT` status. The insertion event is not a RATAN publication. A subsequent real-time `INIT → SNTR` workflow invokes the same validation-message publication and status synchronization used by the regular path.

The source reports that trade booking, amendment, and fixing-generated `INIT` cashflows were expected to be sent to RATAN. A generic payment-queue movement from `XXX → INIT` was expected not to be sent.

## Performance observations

| Object | Pre-runtime | Post-runtime | Difference | Delay |
|---|---:|---:|---:|---:|
| PAY FIX Procedure | 16H 58mins | 17H 7mins | 9min | 0.8% |
| Data Publisher | 47min 58s | 50min 47s | 2min 49s | 5.87% |

These are reported test observations, not formal service-level acceptance criteria. The document provides no environment details, repetitions, percentile data, or thresholds.
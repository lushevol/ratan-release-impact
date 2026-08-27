---
type: query
title: How Does Auto DVP Prevent Closure After Receive Cashflow Withdrawal?
created: 2026-08-23
updated: 2026-08-23
tags: [withdrawal, cashflow-status, safety-control, dvp]
related: [auto-dvp, ebbs-rta-notification, ratan, dvp-nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# How Does Auto DVP Prevent Closure After Receive Cashflow Withdrawal?

The process says RATAN must ignore withdrawal events. Withdrawal scenarios also require that an RTA for an original receive cashflow must not close the linked pay exception after the receive cashflow has returned to `Waiting`.

The source does not define the event marker or runtime receive-cashflow status check needed to enforce this safety condition. Specify the authoritative withdrawal state, ordering rule, and audit evidence required before Auto DVP can close a pay exception.
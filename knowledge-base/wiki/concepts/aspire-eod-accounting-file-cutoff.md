---
type: concept
title: Aspire EOD Accounting File Cutoff
created: 2026-08-23
updated: 2026-08-23
tags: [eod, cutoff, payment-accounting, file-delivery]
related: [aspire-payment-accounting, ratan, aspire, tlm, when-does-the-3-am-ratan-aspire-file-deferral-exception-override-late-file-delivery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# Aspire EOD Accounting File Cutoff

RATAN EOD Aspire accounting files include cashflows with value dates through the current day that reached an eligible status before 10 PM local time. Inclusion is determined by qualifying event time, not by the time a failed job is rerun.

A late rerun may send an original-date file containing pre-cutoff items, preserving its filename date and `AsOfDate`. Items that become eligible after cutoff belong in the following business-day file.

Business-day files are mandatory Monday to Friday, except 25 December and 1 January. If delayed delivery causes out-of-order files, Aspire must hold the newer PSGL file until the prior file has been processed to [[tlm]]. The reported 3 AM deferral exception conflicts with the general late-delivery rule and requires clarification.
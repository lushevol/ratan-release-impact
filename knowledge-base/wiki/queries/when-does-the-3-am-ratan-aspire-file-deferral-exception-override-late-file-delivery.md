---
type: query
title: When Does the 3 AM RATAN Aspire File Deferral Exception Override Late File Delivery?
created: 2026-08-23
updated: 2026-08-23
tags: [eod, file-delivery, exception-handling, psgl]
related: [aspire-eod-accounting-file-cutoff, aspire-payment-accounting, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Aspire Accounting.md"]
---
# When Does the 3 AM RATAN Aspire File Deferral Exception Override Late File Delivery?

The general requirement says a delayed post-cutoff file must be sent when ready using its original filename date and `AsOfDate`. The production-support procedure says that after 3 AM, missing data is included in the next-day file with next-day filename and `AsOfDate`.

Define the governing authority, the exact decision boundary, required reconciliation, approval authority, and customer or Aspire notification requirements for this accounting-completeness exception.
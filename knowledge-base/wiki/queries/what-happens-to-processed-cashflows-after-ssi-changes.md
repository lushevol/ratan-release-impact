---
type: query
title: What Happens to Processed Cashflows After SSI Changes?
created: 2026-08-25
updated: 2026-08-25
tags: [cashflow, ssi, settlement, re-evaluation, data-consistency]
related: [ssi-change-notification, ssi-plus, ratan-ssi-stamping, ratan-settlement, 5-ratan--17-ratan-interfaces--19-ratan-and-ssi-50509--zpvcrt]
sources: ["RATAN/RATAN -Interfaces/Ratan and SSI+ 50509.md"]
---
# What Happens to Processed Cashflows After SSI Changes?

The source warns that SSI updates, additions, and deletions may affect previously processed cashflows and may require re-evaluation or adjustment for consistency and accuracy. It does not establish whether this occurs automatically or manually.

## Questions

- Which cashflows are considered impacted by a changed SSI record?
- Does RATAN automatically re-evaluate or restamp affected cashflows?
- Are only unsettled cashflows eligible for adjustment?
- Who owns approval and execution of any corrective action?
- How are downstream settlement and accounting consumers notified?
- What audit trail records the original and changed SSI data?

Until corroborating documentation is available, automatic retrospective adjustment must not be assumed.
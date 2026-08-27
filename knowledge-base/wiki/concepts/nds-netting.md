---
type: concept
title: NDS Netting
created: 2026-08-22
updated: 2026-08-22
tags: [nds, auto-netting, interest-rate-swap, ratan]
related: [ratan-netting-rule-check, ratan, nid-authoritative-nds-grouping-key]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# NDS Netting

NDS Netting is the stated RATAN auto-netting path for Non-Deliverable Interest Rate Swap cashflows of NDS. The source says that these cashflows must be auto-netted by the system based on `NID`.

The source does not define `NID`, its format, its authority as a grouping key, or the treatment of amendments, reversals, unmatched cashflows, and resultants. It also does not establish that the NDS rule applies to other IRS cashflows.

The meaning and operational authority of `NID` are tracked in [[nid-authoritative-nds-grouping-key]].
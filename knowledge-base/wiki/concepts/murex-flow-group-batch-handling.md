---
type: concept
title: Murex Flow-Group Batch Handling
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, mxml, cashflow, batching, reconciliation]
related: [murex, ratan, murex-to-ratan-cashflow-interface, auto-netting-datetime-calculation, what-is-the-authoritative-murex-cashflow-publication-window]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# Murex Flow-Group Batch Handling

Murex can generate multiple payments from a single market event, including new booking, Cancel & Reissue, and restructure events. Although it publishes one MxML message per payment, each message contains a `Flows` block that lists related flow IDs, statuses, and value dates.

Ratan is expected to use this block to infer the payments expected for a market-event group and raise an exception when the group is incomplete.

## Documented selection logic

Payments in `INIT` status are included in the current event group when their value date is within the configured Murex system-date window:

```java
if mxSystemDate <= Payment VD <= mxSystemDate + 9Day
    Murex would send the MxML in the current trade event
else
    the payment would be sent in future
```

Previously sent `SNTR` flows are treated as belonging to earlier batches and should not be counted as new messages in the current batch.

## Control objective

The group check is intended to identify message loss. For example, if Murex creates three expected payments but Ratan receives only two, Ratan should raise an interface exception.

## Undefined controls

The requirement does not define:

- a canonical group key;
- the wait period before declaring a missing message;
- whether a `Flows` snapshot is immutable or can become stale;
- deduplication and retry behavior;
- treatment of messages arriving after an exception;
- operational ownership of exception remediation.

The nine-day selection rule also conflicts with the seven-business-day publication statement elsewhere in the source.
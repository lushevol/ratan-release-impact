---
type: source
title: Ratan and Aspire 51282
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, aspire, interface, payment-accounting, batch, fileit]
related: [ratan, aspire, ratan-aspire-payment-accounting-interface, fileit-file-arrival-notification, operational-level-agreement]
sources: ["RATAN/RATAN -Interfaces/Ratan and Aspire 51282.md"]
authors: [Junying Jiang, Yunzhe Ta, Daiqi Wang]
year: 2026
url: "https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA"
venue: Confluence
---
# Ratan and Aspire 51282

This sparse interface record documents one stated flow: a Payment Accounting message is sent from [[ratan]] to [[aspire]] in batch mode through FileIT.

## Stated flow

```text
Ratan --(FileIT)-->Aspire
```

The source describes the payload only as a “Payment Accounting message.” It does not define its accounting semantics, data layout, format, version, or validation rules.

## Documentation review record

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| @Junying Jiang @Yunzhe Ta | 2026-01-02 | @Yunzhe Ta @Daiqi Wang | 2026-01-09 | |

The template says that the status should be updated to Published after review, but the recorded Status field is blank. The update and review activity is evidenced; publication status is not confirmed.

## OLA reference

The page directs readers to the RATAN FM Settlement OLA location:

<https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA>

This reference establishes a potentially relevant operational documentation location, but this source does not state any Aspire-specific OLA terms. See [[operational-level-agreement]] and [[sources/5-ratan--11-ratan-ola--11-ratan-ola--13lq67q]].

## Missing interface contract details

The following template sections are unpopulated: connection details, interface specification, interface-team contact, known issues, and troubleshooting steps. Consequently, the source provides no evidence for endpoints, FileIT route or job identifiers, transport security, file schema, schedule, acknowledgements, reconciliation, duplicate handling, retry or replay behavior, support ownership, or escalation procedures.

The heading’s references to “BPMS APP and Interface APP” and the example “RATAN and TDS3” do not explain their relationship to Aspire or the meaning of identifier `51282`.
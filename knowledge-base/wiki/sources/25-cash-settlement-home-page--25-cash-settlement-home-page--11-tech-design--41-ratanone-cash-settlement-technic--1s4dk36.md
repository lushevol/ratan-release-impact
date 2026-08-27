---
type: source
title: Source: Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, swift, accounting, ebbs, ratanone, technical-design]
related: [ratanone, ebbs, value-date-accounting-feed-cutoff, accounting-feed-withdrawal-as-reversal, swift-reinstatement-and-unsuppression, what-is-the-authoritative-ebbs-accounting-feed-state-machine, what-are-the-accounting-feed-validation-retry-error-codes-and-limits, does-the-negative-balance-filter-apply-to-swift-unsuppression, are-aspire-and-ebbs-distinct-accounting-targets-or-names-for-one-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md"]
authors: []
year: 2026
url: ""
venue: "Internal technical design"
---
# Swift Generation and Settlement Accounting Tech Design

This technical design describes Swift generation and settlement-accounting feed behaviour in the [[ratanone]] Cash Settlement context, with [[ebbs]] named as the accounting-feed destination or integration context.

## Referenced documentation

- [Cash Settlement - Accounting - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Cash+Settlement+-+Accounting)
- [RATANONE Cash Settlement Technical Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2560471970)

## Design principles

1. EBBS feed generation is event driven.
2. Value date is the cutoff for feed publishing:
   - Hold the feed if its value date has not arrived.
   - Publish directly if its value date has already arrived.
   - Retry up to three times on validation error codes.
3. A withdrawal is generated in the reversal direction of the New transaction, rather than as a wholly new feed.

The value-date rule contributes source-specific evidence for [[value-date-accounting-feed-cutoff]]. The withdrawal treatment supports [[accounting-feed-withdrawal-as-reversal]]. The source does not define event names, idempotency keys, applicable time zones, retryable validation error codes, retry intervals, or exhausted-retry handling.

## Reinstatement and unsuppression

The source records the following reversal-related conditions verbatim:

```text
Status changed from FAILED
→ reinstate action
→ reversal flag = reinstate

Status changed from SWIFT_SUPPRESSED
→ approve action on unsuppressed item
→ reversal flag = SwiftUnSuppressed

Filter:
reversal flag = reinstate
AND last published balance < 0
```

The stated filter explicitly applies to `reinstate`. The document does not establish whether `last published balance < 0` also applies to the `SwiftUnSuppressed` path. See [[swift-reinstatement-and-unsuppression]] and [[does-the-negative-balance-filter-apply-to-swift-unsuppression]].

## Status machine gap

Although the document has a “Status Machine” heading, it provides no state diagram, transition table, terminal-state treatment, or relationship between publication and accounting-task status. This leaves the EBBS accounting-feed lifecycle unresolved; see [[what-is-the-authoritative-ebbs-accounting-feed-state-machine]].

## SOD job statistics

| Condition | Task Sum | Cost | Evidence attachments |
|---|---:|---:|---|
| Just publish | 4002 | 40.2s | `publish start.jpg`; `publish end.jpg` |
| Generate JSON and publish | 4000 | 40.7s | `gen start.jpg`; `gen end.jpg` |

These two observations show similar elapsed times for the reported runs, but do not provide enough context to establish comparative scalability or a general JSON-generation performance conclusion.

## Scope note

The document ends with “new version for UK” but gives no UK-specific design, deployment, scheduling, or timezone detail. The relationship between EBBS and [[aspire]] is also not clarified here; see [[are-aspire-and-ebbs-distinct-accounting-targets-or-names-for-one-feed]].
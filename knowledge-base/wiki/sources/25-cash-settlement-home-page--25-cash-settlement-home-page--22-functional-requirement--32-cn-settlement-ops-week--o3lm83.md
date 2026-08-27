---
type: source
title: CN Settlement Ops Weekly Session Open Items
tags: [cn-settlement, operations, open-items, fmrp, swift, historical-tracker]
related: [cn-settlement, fmswg-swift-message-validation, ssi-data-quality-for-swift-generation, what-is-the-approved-cn-settlement-field-20-format, is-auto-split-in-or-out-of-scope-for-fmrp-cn-settlement, what-does-the-murex-2-11-payment-queue-reasons-field-mean-and-who-consumes-it, what-was-the-30-november-decision-on-agency-booking-for-cn-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/Open Items.md"]
created: 2026-08-23
updated: 2026-08-23
authors: []
year: 2022
url: "https://confluence.global.standardchartered.com/display/DSP/FMRP+Open+Items"
venue: Confluence
---
# CN Settlement Ops Weekly Session Open Items

This historical operational tracker records unresolved CN Settlement follow-ups and two agency-booking tasks closed as not required. It states that the tracker content was moved to the Confluence page *FMRP Open Items - Derivative Strategy Projects*.

The tracker is evidence of task status, not an authoritative functional specification. In particular, it does not resolve the general Field 20 format, auto-split scope, or the meaning of the Murex payment-queue `Reasons` field.

## Source context

Moved to page [FMRP Open Items - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/FMRP+Open+Items)

| Workshop Date | Description | Task Owner | Status | Comment |
| --- | --- | --- | --- | --- |
| # [2022-11-16](https://confluence.global.standardchartered.com/display/DSP/2022-11-16) | Check with CMO for the Field 20 format: The 'MX' prefix and the ending 'A'/'B'/'C'. | @Arockia Dinesh | Open | |
| To check with Cang, Yuanyuan <Yuanyuan.Cang@[sc.com](http://sc.com/)> for the booking model of agency booking model | @Arockia Dinesh | Closed | Email from Wu,Wen on 30 Nov advised not required |
| To check with Srinivas/Asther if implement the field 20 logic related to agency booking | @Arockia Dinesh | Closed | Email from Wu,Wen on 30 Nov advised not required |
| To check with Srinivas/Asther if auto split is out of scope for FMRP CN Settlement | @Arockia Dinesh | Open | |
| Check the 'Reasons' field from Murex 2.11 payment queues | @Yi Li | Open | |
| | | | | |

## Recorded status

Three items remain open in this tracker:

- Required CN Settlement Field 20 construction, including the `MX` prefix and terminal `A`, `B`, or `C`.
- Whether auto split is excluded from FMRP CN Settlement scope.
- The meaning and processing relevance of the `Reasons` field in Murex 2.11 payment queues.

Two agency-booking-specific tasks are marked closed because an email from Wu, Wen on 30 November reportedly advised that they were not required. The referenced email, its year, decision owner, rationale, and precise scope are absent from this source.

## Interpretation boundary

The agency-booking closure does not establish that general Field 20 formatting is unnecessary. The general Field 20 question remains open in the same tracker. Nor does the tracker establish that auto split is either in or out of scope.

This source provides historical operational context for [[cn-settlement]] and related SWIFT work such as [[fmswg-swift-message-validation]] and [[ssi-data-quality-for-swift-generation]]. It should not supersede later technical specifications or implementation evidence.
---
type: query
title: What Is the Authoritative Murex Reversal NSTP and Suppression Rule for CN Migration?
tags: [murex-2-11, reversal, nstp, suppression, cn, migration]
related: [cn-trade-migration, murex-2-11, ratan, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Is the Authoritative Murex Reversal NSTP and Suppression Rule for CN Migration?

The source says that Murex 2.11 reversal cashflows caused by migration-weekend trade cancellation should be suppressed when the original payment was settled early. Its final business-rule section instead specifies an NSTP rule to hold those reversal cashflows.

Clarification is needed on the authoritative lifecycle state, downstream messaging behaviour, release or removal criteria, control owner, and whether the treatment varies by original settlement status.
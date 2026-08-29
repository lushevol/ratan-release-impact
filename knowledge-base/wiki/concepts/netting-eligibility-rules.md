---
type: concept
title: Netting Eligibility Rules
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, netting, eligibility, static-data, nstp, ratan]
related: [ratan, manual-cashflow-netting, dvp-nstp, cashflow-logical-model, configuration-driven-onboarding, what-are-the-ratan-netting-rule-match-and-precedence-semantics, what-is-the-ratan-nstp-hold-and-release-lifecycle-for-netting-eligible-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Rules Static Data.md"]
---
# Netting Eligibility Rules

Netting eligibility rules are [[ratan]] static-data rules that determine whether a cashflow is eligible for netting. In the documented CN Day 1 scope, an eligible cashflow is held as NSTP for subsequent manual processing by settlement ops.

## CN Day 1 Matching Attributes

The documented active rule uses:

- Booking Entity FM Code: `Entity.Booking_Entity_SCI_FMCODE`, with operator `IS`.
- Client FM Code: `Entity.Counterparty_SCI_FMCODE`, with operator `IS`.
- Product Type: `Instrument_Common.ISDA_Taxonomy`, with operator `IS/IN`; this attribute may be blank.

The source does not define matching semantics, including the behavior of `IS` and `IN`, missing values, multiple matching rules, precedence, or duplicate matches. These issues are tracked in what are the ratan netting rule match and precedence semantics.

## Scope Boundary

This concept describes the manual CN Day 1 eligibility flow only. The same source marks auto netting and potential netting as removed from CN Day 1 scope. It does not establish their status in other releases or product areas.

NSTP holding is documented here as a netting consequence, but it must not be assumed equivalent to every use of NSTP described by dvp nstp. The lifecycle and release mechanism remain unresolved in what is the ratan nstp hold and release lifecycle for netting eligible cashflows.
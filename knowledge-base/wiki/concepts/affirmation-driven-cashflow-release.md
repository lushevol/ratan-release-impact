---
type: concept
title: Affirmation-Driven Cashflow Release
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, affirmation, waiting, nstp, exception-management, stp]
related: [email-based-cashflow-affirmation, ratan, ai-factory-layer, held-cashflow-reinstatement, release-cutoff-risk-for-unhold, dvp-nstp-exception-handling, what-is-the-pending-affirmation-exception-lifecycle-and-stp-release-contract, what-controls-validate-ai-mediated-email-affirmation-before-cashflow-release, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--vhh9uf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
---
# Affirmation-Driven Cashflow Release

Affirmation-driven cashflow release is the proposed process of moving a cashflow held in `WAITING` out of the NSTP queue after acceptance of an external client affirmation.

The intended chain is:

`WAITING` with “Pending Affirmation” → scheduled email → client response → response processing → closure of the pending-affirmation exception → NSTP release → STP.

The source does not establish whether “Pending Affirmation” is an exception code, exception status, workflow status, or UI label. It also does not define whether exception closure and queue release are atomic, idempotent, or mediated through an existing [[ratan]] release workflow.

This process is related to [[held-cashflow-reinstatement]] and [[release-cutoff-risk-for-unhold]], but should not be treated as equivalent to generic reinstatement without authoritative lifecycle evidence. Its mention of NSTP does not establish that the capability is DVP-specific; [[dvp-nstp-exception-handling]] is only a related exception-handling context.
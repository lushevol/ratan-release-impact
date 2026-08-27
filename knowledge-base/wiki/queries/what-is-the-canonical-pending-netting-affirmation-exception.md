---
type: query
title: What Is the Canonical Pending Netting Affirmation Exception?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, auto-netting, exceptions, affirmation, terminology]
related: [auto-netting-affirmation-removal, pending-confirmation-affirmation, cashflow-auto-netting, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Remove Auto Affirmation from Auto Netting.md"]
---
# What Is the Canonical Pending Netting Affirmation Exception?

## Question

Should the exception introduced or used by the auto-netting affirmation change be named `"Pending Affirmation"` or `"Pending Netting Affirmation"`?

## Evidence

The functional requirement consistently describes the expected exception as `"Pending Affirmation"`. A comment proposes `"Pending Netting Affirmation"` as a possible new exception name. The source does not identify a canonical exception code, data-model value, migration plan, or approval decision.

## Why this matters

The name affects exception creation, operations workflows, reporting, user-interface labels, test cases, and lifecycle transition rules. The decision should also clarify whether the existing [[concepts/pending-confirmation-affirmation]] exception is reused or whether a netting-specific exception type is introduced.

## Current position

Treat `"Pending Affirmation"` as the source-stated requirement wording, not as a confirmed canonical implementation value. Do not treat `"Pending Netting Affirmation"` as approved until the owning team confirms the exception taxonomy and downstream consumers.
---
type: query
title: What Is the NAMS Nostro Account Reuse and Duplicate-Prevention Rule?
tags: [nams, nostro, duplicate-prevention, account-reuse, static-data, open-question]
related: [nams-nostro-account-opening-workflow, nostro-record-composite-uniqueness, nostro-records]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Nostro SSI/How to create a Nostro Account in NAMS.md"]
---

# What Is the NAMS Nostro Account Reuse and Duplicate-Prevention Rule?

## Question

What search key and business rules determine whether an existing NAMS Nostro account can be reused, and what prevents duplicate account creation?

## Evidence

During account creation, NAMS displays available Nostro accounts for the selected SCB Entity and currency in the relevant country. The requestor may select an existing account or choose **CREATE NEW**.

The source does not state whether provider, account type, business purpose, agent bank, account number, LEID, or other attributes participate in the lookup or uniqueness rule. The availability screen is not sufficient evidence of a technical composite uniqueness constraint.

## Required investigation

Confirm:

- The complete existing-account search key.
- Reuse eligibility and account status requirements.
- The canonical uniqueness key.
- Whether duplicate creation is blocked or only flagged.
- Permitted exceptions and approval requirements.
- Behavior when two requests are submitted concurrently.
- Whether closed, pending, or amended accounts appear in search results.
- The relationship to [[concepts/nostro-record-composite-uniqueness]].

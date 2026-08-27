---
type: query
title: Does Ratan Enforce Profile USD Limits Server-Side for Submit and Approve Actions?
created: 2026-08-23
updated: 2026-08-23
tags: [query, ratan, authorization, backend-enforcement, maker-checker, ui-gating]
related: [ratan, profile-based-usd-authorization-limits, profile-limit-static-data-governance, settle-as-gross-maker-checker-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# Does Ratan Enforce Profile USD Limits Server-Side for Submit and Approve Actions?

## Question

Does Ratan perform authoritative backend or API authorization validation, or does it only hide the Submit/Approve button in the UI?

## Evidence

The source says that Ratan should check whether the user has sufficient authority and show the Submit/Approve button only when authorized. It does not explicitly require server-side enforcement, nor does it distinguish maker submission from checker approval.

## Required clarification

Confirm that every relevant backend operation validates:

- The acting user's current profile.
- The applicable profile limit.
- The cashflow's USD-equivalent amount.
- The current maker/checker state.
- Concurrent changes to payment, rate, or authorization data.

UI suppression should be treated as a usability control, not the sole security boundary.

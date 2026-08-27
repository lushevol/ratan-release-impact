---
type: query
title: What Are the Details, Status, and Ownership of RATAN Issues 9 and 24?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, issue-tracking, reverse-and-rebook, inter-entity, evidence-gap]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tech--6o5vl6, ratan, issue-tracking-and-technical-debt-governance, murex-ratan-reversal-and-replacement-lifecycle, post-settlement-amendment-and-cancellation-handling, inter-entity-auto-netting, inter-entity-cashflow-pre-match]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/RATAN Issue Tracking.md"]
---
# What Are the Details, Status, and Ownership of RATAN Issues 9 and 24?

## Question

What are the scope, business impact, affected systems, owner, priority, status, root cause, remediation, and validation evidence for RATAN Issue 9 and Issue 24?

## Known Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--28-02-issue-tracking-tech--6o5vl6]] provides only two index entries:

- Issue 9 is labelled “Reverse and rebook” and references an email from Shobi.
- Issue 24 is labelled “Internal Intra/Inter entity deals” and references a Structure Deposit sample email from SF.

The document contains none of the underlying emails, attachments, issue records, or resolution evidence.

## Retrieval Required

1. Retrieve the complete Issue 9 email, attachments, and tracker record.
2. Retrieve the complete Issue 24 Structure Deposit email, attachments, and tracker record.
3. Confirm whether the issue identifiers are RATAN-specific, globally unique, and still active.
4. Record the owner, status, priority, impact, reproduction conditions, root cause, remediation, and validation evidence.
5. Map confirmed impacts to specific workflows or services only where the retrieved evidence establishes that connection.

## Boundary

Issue 9 must not be assumed to describe the implementation documented in [[murex-ratan-reversal-and-replacement-lifecycle]] or [[post-settlement-amendment-and-cancellation-handling]]. Likewise, Issue 24 must not be assumed to affect [[inter-entity-auto-netting]] or [[inter-entity-cashflow-pre-match]] without direct evidence.
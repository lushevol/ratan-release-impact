---
type: query
title: What Are the Authorization and Terminal Outcome Rules for FMSGW Manual Queues?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, manual-queues, authorization, approval, auditability, payment-controls]
related: [fmsgw, fmsgw-manual-payment-validation-queues, qatar-scb-doha]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# What Are the Authorization and Terminal Outcome Rules for FMSGW Manual Queues?

The UAT confirms that users can access selected [[fmsgw]] validation queues, view Data and Action audit tabs, add comments, process entries, approve high-value payments, and terminate cancellation-queue transactions. The governing control rules are unspecified.

## Questions to resolve

- Which user roles may view, process, approve, reject, or terminate each queue type?
- Is maker-checker approval required for high-value payments or other actions?
- What are the terminal states and downstream effects of rejection or termination?
- Can a processed queue item be returned, re-opened, or re-queued?
- What audit events, comments, identities, timestamps, and retention periods are mandatory?
- Who receives notifications, and how are notification failures handled?

Formal operating procedures, entitlement specifications, and negative-path UAT evidence are needed.
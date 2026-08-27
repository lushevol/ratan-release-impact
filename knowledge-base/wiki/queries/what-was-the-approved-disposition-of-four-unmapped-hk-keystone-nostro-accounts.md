---
type: query
title: What Was the Approved Disposition of the Four Unmapped HK KeyStone Nostro Accounts?
created: 2026-08-23
updated: 2026-08-23
tags: [keystone, hong-kong, nostro, account-mapping, exception-management, uat]
related: [keystone, keystone-nostro-account-mapping, razor, production-data-refresh-for-uat]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md"]
---
# What Was the Approved Disposition of the Four Unmapped HK KeyStone Nostro Accounts?

## Question

What did the November 2023 instruction to “ignore” four unmapped HK KeyStone BCS Nostro accounts mean operationally, and was it formally approved and implemented with adequate reconciliation controls?

## Known evidence

The source records that four accounts could not be mapped and that Naresh and operations users confirmed that they could be ignored. The referenced email and screenshot attachments are unavailable.

## Evidence required

- The four account identifiers and their account status.
- The reason each account could not be mapped.
- The precise operational disposition: exclusion, suppression, inactivity confirmation, remediation deferral, or another treatment.
- The accountable approver and formal approval record.
- Assessment of payment, liquidity, accounting, regulatory, and customer impact.
- The implemented KeyStone and Razor handling.
- Reconciliation evidence demonstrating that the exception did not omit applicable settlement activity.
- Confirmation of whether the exception remained valid after the 2023 UAT activity.

## Why it matters

Treating an unmapped Nostro account as ignorable can be a valid scoped-data decision, but it can also create an untracked gap in settlement routing or reconciliation. The available status record does not distinguish these cases.
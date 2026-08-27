---
type: source
title: Keystone Supporting
authors: []
year: 2023
url: ""
venue: Internal project status record
created: 2026-08-23
updated: 2026-08-23
tags: ["keystone", "bcs", "nostro-account", "uat", "razor", "account-mapping", "cash-settlement", "nostro", "hong-kong"]
related: ["keystone", "bcs", "razor", "nostro-account-mapping", "account-mapping-exception", "production-data-refresh-for-uat", "what-are-the-four-unmapped-keystone-accounts-and-why-can-they-be-ignored", "keystone-nostro-account-mapping", "what-was-the-approved-disposition-of-four-unmapped-hk-keystone-nostro-accounts", "static-data-readiness", "settlement-integration-static-data-readiness", "2023-q4-cash-settlement-delivery-planning"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2023-Q4 Analysis/Keystone Supporting.md"]
---
# Keystone Supporting — November 2023 UAT and Nostro Mapping Status

This short status record documents HK KeyStone BCS preparation work between 8 and 14 November 2023. It records a test-plan share, testing of a production-data load and Nostro-update script intended to send data to [[razor]], unresolved mapping questions, and an instruction to ignore four unmapped accounts.

## Timeline

### 8 November 2023

Alice shared a test plan.

Referenced evidence:

- `attachments/image2023-11-10_15-59-27.png`
- `attachments/RE_ Data refresh - Preparation and UAT environment.msg`

The supplied source establishes that the plan was shared, but not its scope, completeness, approval status, test cases, or acceptance criteria.

### 10 November 2023

The status note states:

> Script is in testing, (to load prod data and update nostro to send to Razor)

It also states that account-mapping logic had been received, while some items remained to be confirmed and an email had been sent.

Referenced evidence:

- `attachments/RE_ HK KeyStone BCS - Nostro account mapping.msg`

This is evidence of work in progress only. It does not demonstrate successful script execution, completed UAT, deployment, or confirmed receipt of updated data by Razor.

### 14 November 2023

The status note states:

> 4 account not be able to find mapping, Naresh confirmed as attached, ops user also confirmed we can ignore them.

Referenced evidence:

- `attachments/RE_ HK KeyStone BCS - Nostro account mapping.msg`
- `attachments/image2023-11-29_10-17-1.png`

The four account identifiers, their status, the meaning of “ignore,” approval authority, implementation method, and reconciliation evidence are not available in the supplied material.

## Evidence limitations

The referenced screenshots and `.msg` attachments were not supplied for review. Consequently, this record cannot substantiate detailed mapping rules, technical design, test results, formal approvals, or operational-control adequacy.

The source uses both “KeyStone” and “Keystone.” This page uses **KeyStone** as the visible spelling in the HK KeyStone BCS reference. It does not establish that [[keystone]] is the same system as [[keystore]].

## Related topics

- [[keystone]] is the stated source context for the data refresh and account-mapping activity.
- [[keystone-nostro-account-mapping]] describes the mapping dependency and necessary exception controls.
- [[production-data-refresh-for-uat]] captures the reported testing activity without inferring completion.
- [[what-was-the-approved-disposition-of-four-unmapped-hk-keystone-nostro-accounts]] tracks the unresolved account-exception evidence.
- [[static-data-readiness]] and [[settlement-integration-static-data-readiness]] provide related readiness context.
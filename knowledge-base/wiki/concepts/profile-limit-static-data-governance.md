---
type: concept
title: Profile Limit Static Data Governance
created: 2026-08-23
updated: 2026-08-23
tags: [static-data, maker-checker, business-rules, authorization, ratan, segregation-of-duties]
related: [ratan, fmo-ops, profile-based-usd-authorization-limits, netting-client-configuration, settle-as-gross-maker-checker-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Profile USD Limit.md"]
---

# Profile Limit Static Data Governance

## Definition

Profile limit static data governance is the controlled administration of Ratan profile limits and related settlement rules. The requirement moves authorization limits from on-the-fly calculation into Ratan-specific static data.

## Required controls

The Profile & Limit Static Data GUI requires maker/checker control for:

- Record creation.
- Record update.
- Record deletion.

The source also separates profile responsibilities:

- `FMO_STA_MKR`: maintains static data such as the Client Level Netting Flag.
- `FMO_STA_CKR`: checker role for static data.
- `FMO_BR_MKR`: maintains profile USD limits, Suppression Rules Table, NSTP Rules Table, and Netting Rules Table.
- `FMO_BR_APR`: approves business-rule changes.

## Proposed data fields

The source identifies four important fields:

```text
1 Profile
2 Currency
3 USDConverted
4 Limit
```

No physical schema is provided. The source does not define field types, keys, uniqueness, effective dates, audit columns, approval states, versioning, rollback, or self-approval restrictions.

`USDConverted` is ambiguous: it may represent a converted amount, a conversion indicator, or another business attribute. Its meaning must be confirmed before implementation.

## Governance implication

The configuration workflow should preserve segregation of duties and an audit trail. Profile-limit changes should not become effective without the required approval, and the authorization decision should identify the applicable profile-limit version.

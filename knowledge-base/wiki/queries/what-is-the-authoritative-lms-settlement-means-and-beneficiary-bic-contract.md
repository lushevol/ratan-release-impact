---
type: query
title: What Is the Authoritative LMS Settlement Means and Beneficiary BIC Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, settlement-means, beneficiary-bic, nostro, scbml, integration-contract]
related: [lms, lms-cashflow-feed-eligibility, nostro-stamping, vostro-data-sourcing-from-ssi-plus, nostro-centralization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/LMS Feed.md"]
---
# What Is the Authoritative LMS Settlement Means and Beneficiary BIC Contract?

The source defines LMS filtering with the logical model fields:

```text
Settlement_Instruction.Account.SCB_Nostro_Account_Type
Settlement_Instruction.Account.Beneficiary_BIC_code
```

It permits only settlement means `Nos` and rejects beneficiary BIC `REJECTXXALL`.

The XML template instead exposes:

```xml
<scb:settlementMeans>
    <scb:settlementAccountNo>${settlementAccountNo!}</scb:settlementAccountNo>
</scb:settlementMeans>
```

The requirement does not establish:

- whether `SCB_Nostro_Account_Type` is used only inside Ratan;
- whether the settlement-means type must be serialized for LMS;
- which of the two settlement instructions owns the beneficiary BIC used for filtering;
- whether “Vostro Beneficiary BIC” is a specific field or a generic settlement-instruction field.

A canonical validation and serialization contract is required before the XML mapping is treated as complete.
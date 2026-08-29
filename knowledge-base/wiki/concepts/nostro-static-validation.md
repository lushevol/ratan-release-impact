---
type: concept
title: Nostro Static Validation
created: 2026-08-22
updated: 2026-08-22
tags: [Nostro, validation, static-data, settlement, Korea]
related: [nostro-static, maker-checker-settlement-control, korea-static-settlement-configuration, cashflow-logical-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Netting and Nostro Static.md"]
---
# Nostro Static Validation

## Purpose

Nostro Static validation protects the integrity of settlement-instruction data used for SSI stamping. Validation occurs when a maker submits a creation or update and includes mandatory-field checks, conditional settlement-means checks, duplicate prevention, and primary-record uniqueness.

## Mandatory fields

The following fields are mandatory for Nostro creation and update:

```text
Legal Entity FMCode
Legal Entity FMID
CCY
Settlement Means
Settlement Account
EBBS account
```

When `Settlement Means = 'NOS'`, these additional fields are mandatory:

```text
Correspondent Swift
Nostro Account
```

## Korea-specific validation

The source defines a Korea-specific case with the following requirements:

```text
Settlement Means = 'NOX'
Settlement Account in ('KRO UIBOK', 'KRO BOKSEO')
Correspondent Swift is mandatory and must contain 11 characters
Account in 'eBBS information' must contain 6 digits
```

The phrase `account in 'eBBS information'` is retained from the source because the exact underlying field name is not specified. These rules should be reconciled with korea static settlement configuration.

## Duplicate-key validation

A submitted change is rejected when an existing record has the same combination of:

```text
Legal entity FMID
Currency
Settlement means
Settlement account
CCY pair
```

This check prevents duplicate Nostro records for the same settlement-instruction key.

## Primary-record validation

A creation or update is rejected when the maker selects the primary flag and an existing primary Nostro already exists for the same:

```text
Legal entity FMID
Currency
```

Duplicate-key validation and primary-record validation are separate controls: the former prevents equivalent records, while the latter prevents multiple primary settlement instructions for an entity and currency.

## Approval and effectiveness

Nostro makers and checkers must be different people. A checker can approve or reject the submitted Nostro change, and newly added, updated, or deleted records become effective only after approval. The source does not specify whether validation is repeated at approval time or whether the record is rechecked for conflicts after submission.

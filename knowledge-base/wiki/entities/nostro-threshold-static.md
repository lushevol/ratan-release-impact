---
type: entity
title: Nostro Threshold Static
created: 2026-08-22
updated: 2026-08-23
tags: [static-data, nostro, cashflow-splitting, ratan, settlement, reference-data, threshold]
related: [nostro-threshold-auto-splitting, nostro-static, nostro-static-validation, data-ops, cash-settlement-home-page, business-rule-maintenance, threshold-based-cashflow-auto-distribution, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Nostro Threshold Static

Nostro Threshold Static is a reference-data configuration managed through a dedicated RATAN blotter for threshold-based automatic cashflow distribution. It is related to, but distinct from, [[nostro-static]]: it defines payment-splitting parameters rather than core settlement-static configuration.

According to the Split Demo Cases source, this configuration determines whether [[threshold-based-cashflow-auto-distribution]] is triggered at release cut-off.

## Record scope and fields

Both sources identify Currency as mandatory and Booking Entity and Nostro Agent/BIC as optional scope attributes. The Cashflow Splitting requirements provide the following detailed field specification:

| Field | Requirement |
| --- | --- |
| Booking Entity FMID | Optional; backend matching attribute. |
| Booking Entity FM CODE | Optional; user reference attribute only. |
| Nostro Agent | Optional; 53 correspondent SWIFT from Nostro static; 8 or 11 characters. |
| Currency | Mandatory. |
| Threshold | Mandatory integer. |
| Amount | Mandatory integer; described as less than Threshold and limitation. |
| Limitation | Mandatory integer; less than Threshold. |

The Split Demo Cases source refers to the optional Nostro scope field as **Nostro agent BIC** and to the optional booking scope field as **Booking entity**.

## Duplicate validation

The Cashflow Splitting requirements define the duplicate key as:

```text
Booking Entity + Nostro Agent + Currency
```

Duplicate validation returns:

```text
Duplicate record exists with the same Booking Entity + Nostro Agent + Currency
```

## Access control and governance

The Cashflow Splitting requirements state that [[data-ops]] can create, update, and disable records, while other users have read-only access. They also require maker/checker control and specify that the interface follows the existing BIC Netting Static pattern.

The Split Demo Cases source states that [[settlement-ops]] Data Ops users may create, update, and delete threshold-static records, while other users have read-only access.

## Open implementation points

The Cashflow Splitting requirements do not define:

- Whether “Booking Entity” in the duplicate key means FMID, FM CODE, or both.
- The unambiguous `Amount`-to-`Limitation` validation relationship.
- Deterministic matching when several records apply.

Separately, the Split Demo Cases source does not provide:

- The threshold amount field name.
- The threshold amount data type.
- An effective-date model.
- Matching precedence when multiple records apply.

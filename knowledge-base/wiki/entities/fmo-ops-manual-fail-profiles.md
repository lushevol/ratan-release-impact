---
type: entity
title: FMO Ops Manual Fail Profiles
created: 2026-08-23
updated: 2026-08-23
tags: [authorization, cash-settlement, manual-fail, operations]
related: [cash-settlement-home-page, bulk-cashflow-manual-fail, cashflow-manual-fail-maker-checker, settlement-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# FMO Ops Manual Fail Profiles

## Role

This profile set is authorized to use Bulk Fail in the Cash Settlement Home Page. The requirement states that the profiles are the same as those currently allowed to perform single-cashflow manual fail.

## Authorized profiles

- `FMO_OPS_BOL`
- `FMO_OPS_BOC`
- `FMO_OPS_BO`
- `FMO_OPS_INV`
- `FMO_OPS_MKR`
- `FMO_OPS_BOS`
- `FMO_OPS_BOM`

## Control boundary

The source does not distinguish maker-only and checker-only permissions among these profiles. It also does not explicitly state whether every listed profile may approve requests created by every other listed profile. The authorization granularity remains an implementation question for [[concepts/cashflow-manual-fail-maker-checker]].

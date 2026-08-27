---
type: project
title: RFI Dedicated Nostro Stamping
status: planned
owner: ""
start_date: 2026-08-23
target_date: ""
created: 2026-08-23
updated: 2026-08-23
tags: [rfi, nostro, cash-settlement, static-data]
related: [001-implement-rfi-selection-in-ssi-stamping-service, dedicated-nostro-stamping, portfolio-currency-nostro-selection, nostro-selection-economic-change-detection, dedicated-nostro-static-data-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# RFI Dedicated Nostro Stamping

## Objective

Enable RFI portfolio cashflows to select dedicated Nostro static data for the KOR currency leg while preserving standard selection for all other cashflows.

## Scope

Affected deployment components are [[ratanone-static-data-service]], [[ratan-cash-settlement-ssi-stamping-service]], [[ratan-cash-settlement-group-management-service]], [[ratanone-swift-service]], [[ratan-cash-settlement-query-service]], and [[ratanone-db-repository]].

## Delivery controls

- Confirm canonical KOR/KRO currency value.
- Approve the final static-data schema and uniqueness rule.
- Migrate static Nostro data without migrating historical cashflows.
- Test missing and multiple-match behavior.
- Test amendment economic-change classification using changed `nostroId`.
- Confirm supported SSI stamping entry points, including ad hoc and split flows.
- Define monitoring, rollback, ownership, and deployment approval criteria.
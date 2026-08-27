---
type: query
title: What Is the Approved Korea Settlement-Account Inventory for TIS Routing?
created: 2026-08-23
updated: 2026-08-23
tags: [korea, settlement-account, static-data, nostro, ssi-plus, tis]
related: [korea-settlement-account-routing, settlement-integration-static-data-readiness, nostro-static-data-governance, ssi-plus, tis, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# What Is the Approved Korea Settlement-Account Inventory for TIS Routing?

## Question

Which settlement accounts are approved and deployed for Korean TIS routing, including `KRO UISUS`, `KRO UIBOK`, and `CNH UISUS`, and what is the completion status of the Vostro migration to SSI+?

## Evidence

The document identifies the settlement-account inventory as in progress and separately records Vostro-account migration to [[ssi-plus]] as in progress. These account values determine whether a cashflow is selected and how TIS derives its UINO.

## Why it matters

Missing, stale, or inconsistently populated routing-account data can misclassify a cashflow, omit it from the API response, or route it to TIS instead of [[enisis]].

## Needed decision

Publish an approved account inventory with currency, account marker, effective date, owner, SSI+ migration status, RATAN deployment evidence, and TIS test evidence.
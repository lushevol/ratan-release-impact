---
type: concept
title: Korea Accounting Reconciliation
created: 2026-08-23
updated: 2026-08-23
tags: [korea, accounting, reconciliation, cash-settlement, migration]
related: [ratan, tlm, aspire, oltp, ratan-accounting-reconciliation-api, accounting-posting-statuses, ebbs-accounting-message-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# Korea Accounting Reconciliation

Korea accounting reconciliation is the comparison performed by [[tlm]] using accounting records retrieved from [[ratan]] and the corresponding posting outcomes from [[oltp]].

## Interim integration

The requirement limits the interim feed to the Korea booking entity `SCFB_SEOUL` with FMID `10036645`. TLM queries records through the [[ratan-accounting-reconciliation-api]], subject to a maximum three-day interval and an accounting-task-history filter.

The feed is intended to cover postings that were acknowledged successfully, rejected, or sent without a response. The broader [[accounting-posting-statuses]] model also includes entries held, missing mandatory information, or disabled from delivery.

## Migration context

The direct RATAN-to-TLM path is motivated by Aspire's inability to meet the Korea release timeline. The intended future architecture is described as `OLTP > ASPIRE > TLM`, with eventual decommissioning of the direct RATAN-to-TLM route. Migration criteria, ownership, and acceptance evidence are not specified.

## Reconciliation dependencies

Accuracy depends on:

- correct FMID and time-window filtering;
- the relationship between task status and accounting response status;
- RATAN static data for branch, currency, bridge account, and transaction code;
- versioned cashflow external-system keys;
- correct Nostro and bridge-leg debit/credit directions; and
- complete narrative and extended-narrative mappings.

This source is a requirement and should not be treated as evidence of deployment or production behavior.
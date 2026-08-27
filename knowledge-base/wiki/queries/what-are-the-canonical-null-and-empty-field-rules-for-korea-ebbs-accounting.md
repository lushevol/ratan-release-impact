---
type: query
title: What Are the Canonical Null and Empty Field Rules for Korea EBBS Accounting?
created: 2026-08-24
updated: 2026-08-24
tags: [ebbs, korea, schema, nullability, accounting]
related: [ebbs, query-recon-records, korea-tlm-accounting-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# What Are the Canonical Null and Empty Field Rules for Korea EBBS Accounting?

The Korea field logic states that `posting-branch` is empty and `transaction-code` is `NULL`. Yet sample records use both `null` and `""` for `transaction-code`. Several fields labelled mandatory may also be blank under valid conditions, including utilization-related narratives and counterparty details for non-split activity.

Define whether each conditional field must be present, `null`, an empty string, or omitted. TLM reconciliation and strict JSON validation require these conventions to be stable.
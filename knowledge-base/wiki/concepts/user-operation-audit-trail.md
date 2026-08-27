---
type: concept
title: User-Operation Audit Trail
tags: [audit, maker-checker, cash-settlement, persistence]
related: [cashflow-user-operation-record, nstp-maker-checker-processing, maker-checker-segregation-of-duties-and-authorization, cashflow-user-operation-record-schema-and-audit-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# User-Operation Audit Trail

A user-operation audit trail records activity performed through maker-checker workflows so that manual process actions can be persisted and reviewed.

The NSTP proposal introduces [[cashflow-user-operation-record]] as the planned persistence mechanism and calls for save and CRUD APIs. The intended record content and audit policy are not defined in the source.

An authoritative audit design should establish event identity, workflow and cashflow correlation, actor identity, role and authorization evidence, timestamps, immutable history requirements, access control, retention, and treatment of retries or duplicate requests.
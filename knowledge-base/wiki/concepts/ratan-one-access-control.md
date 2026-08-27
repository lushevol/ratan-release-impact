---
type: concept
title: RATAN ONE Access Control
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, ratan-one, access-control, rbac, data-entitlement, segregation-of-duties]
related: [ratan, fmo, myit-service-catalogue-servicenow, maker-checker-settlement-control, ratan-subject-to-tile-authorization, what-is-the-current-ratan-one-entitlement-provisioning-and-approval-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/How to apply for RATAN ONE access.md"]
---
# RATAN ONE Access Control

The documented RATAN ONE access model has three distinct layers:

1. **Functional access role** — a profile associated with a request group and sub-group, such as `FMO_OPS`, `FMO_STA_MKR`, or `FMO_BR_APR`.
2. **Data entitlement** — a data-access scope selected as `Global`, `GBS`, or `Onshore`.
3. **Request subject** — an application-function identifier that maps to one or more RATAN ONE tiles.

This separation means that a request is not documented as a single undifferentiated RATAN permission. The guide does not specify whether the listed data scopes are mutually exclusive, combinable, or hierarchical, nor does it define the precise actions granted by a functional role or subject.

## Segregation-of-duties indication

The role inventory distinguishes maker, checker, approver, operations, back-office, investigator, super-user, and read-only profiles, primarily for [[fmo]]. This supports a segregation-of-duties intent and provides access-model evidence relevant to [[maker-checker-settlement-control]].

It does not prove that every RATAN workflow applies maker-checker controls or that named roles correspond to specific create, amend, approve, or delete permissions.

## Provisioning constraint

The source states that `X_RATANONE` and `RATAN_DATA_ENTITLEMENT` can currently be granted only through bulk request because an E-Form upgrade is still in progress. As the source is undated, this statement must be verified before it is used as an operating instruction.

## Approval-routing limitation

The documented routing table has blank approver-group and/or approver entries for several functional profiles and for the `Global` and `Onshore` data-entitlement scopes. This is an ambiguity in the guide, not evidence that production routing is absent. See [[what-is-the-current-ratan-one-entitlement-provisioning-and-approval-routing]].
---
type: query
title: What Is the Current RATAN ONE Entitlement Provisioning and Approval Routing?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, ratan-one, entitlements, access-provisioning, approval-routing, servicenow]
related: [ratan, fmo, myit-service-catalogue-servicenow, ratan-one-access-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/How to apply for RATAN ONE access.md"]
---
# What Is the Current RATAN ONE Entitlement Provisioning and Approval Routing?

## Question

What is the authoritative current process for provisioning `X_RATANONE` and `RATAN_DATA_ENTITLEMENT`, and which approver groups own all RATAN ONE functional roles and data-entitlement scopes?

## Evidence

The guide states that `X_RATANONE` and `RATAN_DATA_ENTITLEMENT` can only be granted by bulk request while an E-Form upgrade is in progress. It also leaves approver-group and/or approver fields blank for multiple functional roles, and has incomplete entries for `GBS`, `Global`, and `Onshore` data-entitlement scopes.

Because the document has no effective date or revision history, these statements are not sufficient evidence of current operating practice.

## Resolution needed

Confirm with the IAM, ServiceNow catalog, and RATAN application owners:

- whether the E-Form upgrade is complete and the current request path;
- whether bulk provisioning remains mandatory for the two named entitlements;
- approval groups for profiles with blank routing entries;
- accountable routing for `Global`, `GBS`, and `Onshore`; and
- whether the three data scopes are exclusive, combinable, or hierarchical.

Do not infer current authorization from the historical guide until this is resolved.
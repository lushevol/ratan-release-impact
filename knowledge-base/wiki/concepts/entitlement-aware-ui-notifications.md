---
type: concept
title: Entitlement-Aware UI Notifications
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, notifications, authorization, entitlements, data-security]
related: [cashflow-notification-and-auto-refresh, cashflow-blotter, query-service, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/cashflow notification.md"]
---

# Entitlement-Aware UI Notifications

Entitlement-aware UI notifications ensure that a cashflow notification is delivered or exposed only to a user entitled to view the corresponding cashflow data.

## Requirement

The cashflow notification design explicitly requires entitlement checks to apply to notifications. This requirement is particularly important because the proposed event contains full cashflow data, including settlement instructions, account fields, party identifiers, payment information, and workflow state.

## Authorization Versus Filtering

The design proposes that the UI, rather than the backend, apply the user’s current search filter. That is a presentation decision and must not be treated as authorization.

Entitlement enforcement must occur before sensitive data reaches an unauthorized user. Possible enforcement points include:

- Notification publication;
- Broker topic or subscription access;
- A server-side entitlement-aware delivery service;
- A combination of these controls.

The source does not select one enforcement point.

## Design Risk

Publishing a full-data notification broadly and relying on the UI to hide records would expose data to clients that may not be authorized to inspect it. The final contract should define entitlement scope, enforcement location, revocation behavior, and audit evidence.
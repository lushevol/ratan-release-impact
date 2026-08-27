---
type: query
title: How Are Maker-Checker Segregation of Duties and Authorization Enforced?
tags: [maker-checker, authorization, segregation-of-duties, camunda, audit]
related: [camunda, nstp-maker-checker-processing, user-operation-audit-trail, cashflow-user-operation-record]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# How Are Maker-Checker Segregation of Duties and Authorization Enforced?

The proposal moves maker-checker activity into Camunda but does not specify the identity, authorization, or segregation-of-duties model.

Required clarification includes whether a maker can approve their own request, how user identity is passed to services, which roles can create or complete tasks, task claiming and delegation rules, authorization checks for APIs, and the audit evidence required to demonstrate dual control.

These controls are essential to the proposed workflow but are not defined by the source.
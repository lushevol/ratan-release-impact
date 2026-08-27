---
type: query
title: Does Message Bridge Enforce the Uber FMID Filter in Production?
tags: [query, message-bridge, uber, fmid, integration-testing, production]
related: [message-bridge, uber, ratanone, tdsx, uber-cashflow-validation-filtering, what-is-the-authoritative-uber-fmid-validation-scope]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Upstream Integration.md"]
---
# Does Message Bridge Enforce the Uber FMID Filter in Production?

## Question

Does `Message Bridge` reject or route `Uber` messages whose `Entity.Booking_Entity_SCI_FMID` is outside the March 28 target list?

## Evidence limitation

The non-target-FMID integration test used FMID `400899993` and was marked `Pass`, but the test environment was open for all entities. The message was therefore not filtered by Message Bridge. Its accepted status was attributed to payments already being `SUSPENDED` and processed by RATAN.

That result does not prove that the intended filter works in production.

## Required evidence

A controlled test or production-readiness check should demonstrate:

- A target-FMID message reaches the validation path.
- A non-target-FMID message follows the intended routing behavior.
- The result can be attributed to Message Bridge rather than to prior processing state.
- The behavior is observable and operationally recoverable.

The source assigns proof of the Message Bridge filter to [[yonghua-li]].
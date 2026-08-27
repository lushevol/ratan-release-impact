---
type: concept
title: Cashflow Amendment Supersession
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, amendment, supersession, message-processing]
related: [stella, ratan, cashflow-blotter, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# Cashflow Amendment Supersession

Cashflow amendment supersession is the specified handling of a Stella `Amendment` following a `New` message for the same cashflow.

The [[Cashflow Blotter]] is expected to display only the amendment cashflow and discard the original `New` cashflow.

The source does not specify the identifier used to determine that messages concern the same cashflow, whether the original record is physically deleted or logically superseded, or how multiple and out-of-order amendments are handled.
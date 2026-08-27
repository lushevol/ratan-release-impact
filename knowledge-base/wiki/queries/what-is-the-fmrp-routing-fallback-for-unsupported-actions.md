---
type: query
title: What Is the FMRP Routing Fallback for Unsupported Actions?
created: 2026-08-24
updated: 2026-08-24
tags: [query, fmrp, murex-211, routing, error-handling]
related: [fmrp-murex-211-settlement-workflow, fmrp, murex-211]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# What Is the FMRP Routing Fallback for Unsupported Actions?

## Question

What should happen when `client.scb.fmrp.ExtSettleRouter` receives an action outside the documented MLS and FMRP action sets?

## Evidence

The XSL formula contains branches for `RI2C`, `MCXI`, `MIXC`, `FAIS`, `FMIS`, `FMSI`, and `I2SR`, but no `<xsl:otherwise>` branch.

## Verification needed

Confirm whether an empty formula result is discarded by the workflow, whether it causes an error, or whether an explicit discard or alert route is required for observability.
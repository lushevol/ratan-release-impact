---
type: query
title: What Failure Policy Applies to SCI, RDM, and FX Conversion Lookups?
tags: [cash-settlement, integration, resiliency, static-data]
related: [sci, rdm, fx-conversion-service, cashflow-multi-exception-generation]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions.md"]
---
# What Failure Policy Applies to SCI, RDM, and FX Conversion Lookups?

SCI supports GSAM Client and Corporate Client classification, RDM supports Bad Business Day checks, and the FX Conversion Service supports High Value Payment classification.

The requirement does not define timeout behavior, retries, stale-data acceptance, malformed-response handling, fallback values, or whether a dependency failure should block workflow, create an exception, or defer evaluation. Establish an operational policy for each dependency.
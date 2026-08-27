---
type: decision
title: Implement RFI Selection in SSI Stamping Service
status: proposed
deciders: []
date: 2026-08-23
supersedes: ""
created: 2026-08-23
updated: 2026-08-23
tags: [rfi, nostro, ssi, architecture]
related: [rfi-dedicated-nostro-stamping, ratan-cash-settlement-ssi-stamping-service, dedicated-nostro-stamping, ratan-rule-service, ratanone-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md"]
---
# Implement RFI Selection in SSI Stamping Service

## Context

RFI requires a portfolio-and-currency dedicated-Nostro path and its resulting `nostroId` affects amendment economic classification.

## Proposed decision

Implement RFI eligibility and dedicated-Nostro selection in [[ratan-cash-settlement-ssi-stamping-service]], rather than using [[ratan-rule-service]] or [[ratanone-rule-service]].

## Consequences

This minimizes dependencies and avoids altering rule-engine default behavior. It also makes the RFI condition backend-maintained rather than user-configurable.

The design remains only partly configurable: future dedicated types require code and mapping changes. Approval is contingent on resolving the canonical currency code, static-data schema, uniqueness rule, fallback behavior, and entry-point scope.
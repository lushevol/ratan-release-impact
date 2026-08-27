---
type: query
title: How Are Historical SCBML Cashflows Handled in Uber Scope?
created: 2026-08-22
updated: 2026-08-22
tags: [query, historical-data, scbml, uber, json, migration]
related: [uber, scbml, ratan-strategic-json-data-model, uber-legacy-workflow-isolation, murex-ratan-migration-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# How Are Historical SCBML Cashflows Handled in Uber Scope?

## Question

What is the authoritative processing and conversion rule for historical SCBML cashflows whose booking entities are within Uber scope?

## Evidence

The source explicitly distinguishes Uber entity scope from message format. It states that historical Uber-scope cashflows may remain SCBML, while some UI and netting proposals suggest real-time conversion so that resultants become JSON.

## Resolution needed

Confirm whether historical cashflows remain on the legacy workflow, are converted at read or operation time, or undergo a one-time migration. Define the treatment of source cashflows, resultants, netting, exception handling, SSI refresh, and reconciliation.
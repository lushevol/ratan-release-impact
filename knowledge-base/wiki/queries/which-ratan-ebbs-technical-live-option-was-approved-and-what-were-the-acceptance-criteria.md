---
type: query
title: Which Ratan-EBBS Technical Live Option Was Approved and What Were the Acceptance Criteria?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, technical-live, ratanone, ebbs, cpt, acceptance-criteria]
related: [ratanone, accounting-service, ebbs, full-accounting-tech-live-vs-mocked-solace-integration, technical-live-versus-business-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Which Ratan-EBBS Technical Live Option Was Approved and What Were the Acceptance Criteria?

## Question

Was Option 1 or Option 2 formally approved, and what acceptance criteria and results determined completion of the Ratan-EBBS technical live?

## Evidence

Option 1 records UAT deployment on 2024-05-24 and regression in progress on 2024-05-27. Option 2 has no recorded progress. The source does not state that either option was selected, completed, or signed off.

Option 1 also contains unresolved test conditions: `Amount < 0.001`, confirmation with Karthick that the amount was acceptable, and an unspecified entity FMID for IN.

## Questions to Resolve

- Was Option 1 formally selected over Option 2?
- Did the Option 1 regression pass, and where is the execution evidence?
- Was the accounting feed received and acknowledged by EBBS?
- Was the ACK consumed by Ratan and followed by an accounting update on the originating cashflow?
- Was the IN entity FMID configured correctly?
- Is `Amount < 0.001` a valid test value, a threshold, or a system constraint?
- Was Option 2 executed as a fallback, separate test, or not pursued?
- Who provided technical-live approval and business sign-off?

## Current Assessment

The available evidence describes planned coverage and interim progress only. UAT deployment and regression-in-progress status must not be interpreted as successful completion or business go-live.
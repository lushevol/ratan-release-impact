---
type: query
title: What Is the Swift Payment Date Rule After Failed Cashflow Reprocessing?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, swift-generation, payment-date, failed-cashflow, reprocessing]
related: [failed-cashflow-accounting, swift-suppression, payment-date-override, value-date-based-cashflow-materialization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# What Is the Swift Payment Date Rule After Failed Cashflow Reprocessing?

## Question

When is Swift Payment Date mandatory after a failed cashflow is re-processed, and does the rule differ between a simple retry and an amendment?

## Evidence

In the normal re-processing case, the Swift Value Date changes to 9th May, or VD+1, before Swift generation. In the repeated-failure case, it changes to 10th May, or VD+2. In the amendment-after-accounting case, Swift generation is marked `Y` but the Swift Value Date is blank.

## Why It Matters

A missing or inconsistent Swift payment date could cause an invalid payment instruction, incorrect settlement timing, or divergent behavior between retry and amendment flows.

## Current Position

Unresolved. The requirement demonstrates revised dates for retry flows but does not define whether every `READY` cashflow sent to Razor must carry an explicit Swift Payment Date.
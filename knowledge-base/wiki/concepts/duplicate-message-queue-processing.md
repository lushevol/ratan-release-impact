---
type: concept
title: Duplicate Message Queue Processing
tags: [fmsgw, duplicate-detection, validation-queue, manual-processing, scb]
related: [fmsgw, fmsgw-inbound-message-routing]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/001 BAHRAIN-SCB BAHRAI MAN(GBS).md"]
---
# Duplicate Message Queue Processing

Duplicate Message Queue Processing is the manual workflow for settlement messages identified as duplicates.

## UAT behavior

For duplicate `MT103`, `MT202`, or `MT202COV` messages, the user navigates to Validation → Duplicate Message Queue and searches for the trade. Selecting **Process** is expected to move the transaction to the next validation stage, **SCB Specific Validations**.

The scenario is marked **Pass**.

## Evidence boundary

The source does not define the duplicate-detection criteria, linkage to the original message, disposition semantics, audit-retention requirements, or the result of SCB Specific Validations.
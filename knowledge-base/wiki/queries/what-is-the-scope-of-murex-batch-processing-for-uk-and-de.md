---
type: query
title: What Is the Scope of Murex Batch Processing for UK and DE?
created: 2026-08-24
updated: 2026-08-24
tags: [murex, ratan, uk, de, batch-processing, scope]
related: [murex, ratan, murex-batch-cashflow-ingestion, what-is-the-authoritative-murex-batch-file-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Murex batch processing.md"]
---
# What Is the Scope of Murex Batch Processing for UK and DE?

The referenced requirement is *UK - Murex -> RATAN cashflow feeding*, while an otherwise empty detailed-design heading refers to “Realtime Processing for UK & DE.”

## Questions to Resolve

- Is the batch cashflow feed limited to the UK?
- Is DE intended to use real-time processing, batch processing, both, or neither?
- Are UK and DE separate feeds with distinct schedules, files, validation rules, and recovery states?
- Does the stated batch schedule apply to both regions?
- Which teams own the regional scope decision and deployment plan?

The empty UK-and-DE section does not establish a real-time design or expand the batch-feed scope beyond the UK requirement.
---
type: query
title: What Is the Canonical RATAN SSI Best-Match and Tie-Break Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, ssi, matching, cfi-code, uk]
related: [ratan-ssi-stamping, vostro-nostro-ssi-selection, ssi-effective-date-selection, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow.md"]
---
# What Is the Canonical RATAN SSI Best-Match and Tie-Break Rule?

The source specifies different selection hierarchies for UK and non-UK entities but does not fully reconcile them.

For non-UK entities, the summary says `CFI Code -> Is_Default_SSI -> Branch`, while the priority table ranks country-specific versus global scope before primary versus secondary. UK entities use branch, then CFI specificity, then primary status, but no final tie-breaker is defined.

A canonical deterministic algorithm is required, including effective-date filtering order, duplicate handling, and behavior when multiple equally ranked records remain.
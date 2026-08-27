---
type: query
title: Are Non-RFI Cashflows in Scenarios 7 and 8 Meant to Stamp to RFI Nostro?
tags: [RFI, non-RFI, Nostro, test-scenarios, contradiction]
related: [rfi-nostro-account, portfolio-based-rfi-nostro-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# Are Non-RFI Cashflows in Scenarios 7 and 8 Meant to Stamp to RFI Nostro?

The expected results for scenarios 7 and 8 state that non-RFI cashflows are stamped to the RFI Nostro. This conflicts with their non-RFI scenario descriptions, scenario 6, the stated routing objective, and the separate RFI/non-RFI EBBS-account distinction.

The authoritative expected Nostro for scenarios 7 and 8 should be confirmed before implementation or UAT. The scenarios may contain a documentation error, or they may represent an intentional exception that is not otherwise defined.

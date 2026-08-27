---
type: query
title: Is CashPlatform an Alias or Component of RATAN?
created: 2026-08-22
updated: 2026-08-22
tags: [cashplatform, ratan, architecture, interface]
related: [murex-to-ratan-cashflow-integration, murex-cashflow-status-lifecycle, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Is CashPlatform an Alias or Component of RATAN?

The source uses “RATAN” as the Murex cashflow destination but describes lifecycle examples in which Murex sends `SNTR` flows to “CashPlatform” and transitions to `RLSR` after release from RATAN.

It is unclear whether CashPlatform is an alternate name for RATAN, a RATAN ONE component, or a separate interface layer. The answer affects interface ownership, acknowledgement responsibilities, incident routing, and system architecture documentation.
---
type: query
title: How Is NDS Deliverable-Currency Routing Enforced Between Murex and RATAN?
created: 2026-08-22
updated: 2026-08-22
tags: [nds, murex, ratan, routing, currency, netting]
related: [murex-to-ratan-cashflow-integration, murex-cashflow-migration-to-ratan, rebook-cashflow-netting-exclusion]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# How Is NDS Deliverable-Currency Routing Enforced Between Murex and RATAN?

The documented target behavior is that the NDS non-deliverable currency leg remains netted in Murex while RATAN receives only the deliverable-currency cashflow.

The source explicitly says that Murex must make a change to achieve this outcome and asks how the split will be guaranteed. It also records a need for Murex/RATAN testing. This is therefore an unresolved implementation dependency rather than a confirmed routing behavior.

Needed evidence includes the Murex filter or transformation rule, the corresponding RATAN inbound validation, UAT scenarios, and production monitoring for incorrectly routed non-deliverable legs.
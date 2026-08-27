---
type: stakeholder
title: Murex PSS
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, production-support, workflow, incident-management]
related: [murex-211, murex-ratan-cashflow-reconciliation, cn-settlement-murex-211-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Murex PSS

Murex PSS is the support owner for Murex workflow crashes in the CN Settlement Murex 2.11 integration.

The technical design assigns Murex workflow failures to the workflow error queue for immediate capture. Murex PSS then follows the BAU production-workflow support process. This responsibility applies to both outbound publication failures and inbound RATAN-response synchronization failures caused by Murex workflow crashes.
---
type: concept
title: DQSL Cashflow Query Limit
created: 2026-08-22
updated: 2026-08-22
tags: [DQSL, cashflow, query, pagination, cashflow-blotter]
related: [cashflow-blotter-netting-workflow, ratan-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md"]
---
# DQSL Cashflow Query Limit

The source identifies a current limitation in DQSL: a single batch query captures only hundreds of cashflows. Settlement operations require the cashflow blotter to retrieve larger result sets without an arbitrary practical ceiling.

The target requirement is described as “no limitation” on the number of cashflows returned from DQSL. For implementation, this should be expressed as a scalable retrieval contract, most likely bounded pages with a continuation mechanism rather than an unbounded response.

The requirement is connected to the [[cashflow-blotter-netting-workflow]] because users must be able to load all relevant cashflows for an ad-hoc request while the system continues to reflect changes automatically. Query consistency, pagination, sorting, filtering, and behavior when a cashflow changes state during retrieval are not specified.

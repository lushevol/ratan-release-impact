---
type: concept
title: Latest Cashflow SSI Result
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, ssi-stamping, cdups, restamping, versioning]
related: [cdups, ssi-stamping-service, ssi-stamping, ratan-ssi-stamping, ssi-effective-date-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Latest Cashflow SSI Result

The latest cashflow SSI result is the current Vostro and Nostro stamping outcome associated with a materialized cashflow. It is distinct from an earlier general or trade-level SSI result because later cashflow processing may select a different SSI.

The source requires CDUPS to retrieve the latest cashflow-level outcome when needed. It also states that fixing-notice responses should provide the latest cashflow stamping result before the general SSI stamping result.

The term “latest” is not formally defined. Candidate ordering dimensions include trade version, cashflow materialization, SSI effective date, static-data refresh, and stamping completion time. The sample SSI IDs `123`, `456`, and `789` are illustrative and do not establish precedence.
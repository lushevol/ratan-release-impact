---
type: query
title: What Is the Authoritative Murex Receive-to-Pay Linkage Key for Amended Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [murex, amendment, cashflow-linkage, dvp]
related: [murex, auto-dvp, receive-to-pay-cashflow-linkage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# What Is the Authoritative Murex Receive-to-Pay Linkage Key for Amended Cashflows?

The confirmed Murex rule uses trade ID plus payment date. A later example states that an amended replacement pay cashflow can have a changed trade ID while retaining its original trade relationship, suggesting trade version or original trade ID plus payment date.

A single approved key and replacement-cashflow selection rule is needed to prevent missed eligible closures and unsafe linkage to unrelated cashflows.
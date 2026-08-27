---
type: query
title: What Is the Authoritative MT103 ACK-Dependent MT202COV Release Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [mt103, mt202cov, acknowledgement, release-ordering, fmsgw]
related: [ratan, fmsgw, ratan-fmsgw-amh-settlement-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# What Is the Authoritative MT103 ACK-Dependent MT202COV Release Contract?

The Qatar SCB Doha UAT source states that MT202COV should be released when MT103 receives a successful ACK. It does not define the formal dependency contract.

## Questions to resolve

- Which MT103 identifier correlates to an MT202COV message?
- What does “successful ACK” mean: technical receipt, FMSGW acceptance, AMH acceptance, or another event?
- Which component emits the controlling ACK?
- What happens when the ACK is rejected, delayed, duplicated, or never received?
- What timeout, retry, recovery, and audit behavior governs the held MT202COV message?

A technical design, interface specification, or negative-path test evidence is required before treating this as an authoritative release rule.
---
type: concept
title: ACK-Dependent MT202COV Release
created: 2026-08-23
updated: 2026-08-23
tags: [settlement, fmsgw, ratan, mt103, mt202cov, acknowledgement, uat]
related: [settlement-acknowledgement-flow, fmsgw-inbound-message-routing, ghana-scb-ghana-acc-gbs, what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/008 GHANA SCB GHANA ACC(GBS).md"]
---
# ACK-Dependent MT202COV Release

## Definition

ACK-dependent `MT202COV` release is the sequencing behavior in which an associated `MT202COV` is released only after the related `MT103` receives a successful acknowledgement.

## Evidence from Ghana UAT

The UAT record for [[entities/ghana-scb-ghana-acc-gbs]] states:

> MT202 Cov should be released upon MT103 getting ACK successfully.

The same test case confirms the broader successful path: `MT103/202COV` is received from [[entities/ratan]], sent through [[entities/fmsgw]] to [[entities/amh]], and an ACK is sent back to `RATAN`.

## Scope

This source establishes the rule as tested for **GHANA SCB GHANA ACC(GBS)**. It does not establish whether the behavior is universal across all manual entities, whether a particular ACK type or status is required, or how delayed, rejected, duplicated, or missing ACKs are handled.

The authoritative cross-entity contract remains open in [[queries/what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract]].

---
type: concept
title: Pending Trade Validation Cashflow Control
created: 2026-08-24
updated: 2026-08-24
tags: [trade-validation, cashflow, middle-office, trade-confirmation]
related: [uber-message, fo-hard-block-mo-soft-block, trade-confirmation-driven-cashflow-stp, cashflow-business-and-message-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Pending Trade Validation Cashflow Control

## Definition

`PENDING_TRADE_VALIDATION` is a proposed cashflow-level status used while Middle Office trade validation remains incomplete.

The source depicts all cashflows for a trade carrying `PENDING_TRADE_VALIDATION = Yes` and requires trade confirmation in which the trade and cashflow business version/event are matched.

## What is not established

The source does not state whether this status is a hard settlement block, a soft warning, or informational metadata. It does not define the transition owner, matching fields, partial-failure behavior, release rule, or relationship to [[fo-hard-block-mo-soft-block]].

The status should therefore not be interpreted as an approved settlement-control policy.
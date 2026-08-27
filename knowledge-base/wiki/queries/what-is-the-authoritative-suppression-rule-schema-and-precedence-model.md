---
type: query
title: What Is the Authoritative Suppression Rule Schema and Precedence Model?
created: 2026-08-23
updated: 2026-08-23
tags: [suppression, static-data, rules, precedence, nstp]
related: [suppression-rule-management, cashflow-suppression, swift-suppression, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# What Is the Authoritative Suppression Rule Schema and Precedence Model?

The requirement says that suppression rules use pre-defined fields and are Maker/Checker controlled for creation and deletion. It does not specify the rule schema or execution semantics.

The authoritative design should define permitted fields and operators, rule precedence, conflict resolution, effective dates, versioning, audit retention, and the relationship between Cashflow, Payment, and Swift suppression rule types.
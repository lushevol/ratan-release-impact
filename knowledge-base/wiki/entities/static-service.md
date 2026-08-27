---
type: entity
title: Static Service
created: 2026-08-22
updated: 2026-08-22
tags: [static-data, cash-settlement, auto-netting, scheduling]
related: [auto-netting-job-time, auto-netting-rule-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Auto Netting TechDesign.md"]
---
# Static Service

Static Service is the named static-data dependency in the auto-netting technical design.

It is intended to provide an API for calculating auto-netting datetime and to support a new booking-entity/home-currency lookup table. The source provides only example rows and does not define API signatures, table DDL, ownership, uniqueness rules, effective dating, or whether home currency governs auto-netting rule currency.

Its distinct architectural identity should be confirmed if “Static service” is a generic label rather than a deployed service name.
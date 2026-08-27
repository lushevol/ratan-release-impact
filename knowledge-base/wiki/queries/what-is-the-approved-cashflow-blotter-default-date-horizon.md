---
type: query
title: What Is the Approved Cashflow Blotter Default Date Horizon?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, frontend, default-filter, date-horizon]
related: [static-code-in-ui, mfe-cashflow-blotter, static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft)/Static Code In UI.md"]
---
# What Is the Approved Cashflow Blotter Default Date Horizon?

`UIconfig.ts` comments that the default `WAITING` Cashflow Blotter filter spans today through today plus 15 days. Its implementation instead uses `dayjs().add(6, "day")`.

Confirm the intended horizon before this filter is treated as an authoritative configuration value or migrated to a static configuration service.
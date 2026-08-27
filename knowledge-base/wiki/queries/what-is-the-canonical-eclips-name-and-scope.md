---
type: query
title: What Is the Canonical ECLIPS Name and Scope?
created: 2026-08-22
updated: 2026-08-22
tags: [ECLIPS, ECLIP, ECLIPSE, naming, cash-settlement]
related: [ratan, cashflow-auto-netting, irs-net-over-net, how-will-eclips-400452428-cashflow-suppression-be-resolved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md"]
---
# What Is the Canonical ECLIPS Name and Scope?

## Question

Which identifier—ECLIPS, ECLIP, or ECLIPSE—is the canonical business and operational name for the scope using counterparty FMID `400883001`?

## Evidence

The requirement agreement calls the scope `ECLIPS`. The new auto-netting rule reason is `ECLIP SCB HK LCH*LDN`. The SWIFT-suppression rule reason uses `ECLIPSE`.

All references appear to concern counterparty `400883001`, with intended booking entities `2` and `400452428`, but the source does not identify the governing legal entity, clearing arrangement, or canonical naming authority.

## Why this matters

A confirmed identifier is needed before creating a durable entity page, consolidating rule documentation, assigning operational ownership, or determining whether the `400452428` suppression dependency affects the complete scope or only one entity path.
---
type: stakeholder
title: Clearing Ops
created: 2026-08-22
updated: 2026-08-23
tags: [operations, clearing, uat, auto-netting, settlements, ratan]
related: [cashflow-auto-netting, clearing-resultant-swift-suppression, ratan-settlement-contact-routing, pss, gbs-settlements-east, gbs-settlements-west, in-country-ops]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Settlements Ops Contacts.md"]
---
# Clearing Ops

Clearing Ops has two documented contexts: a clearing-focused UAT tester group and a conditional settlement-contact routing category in the RATAN directory.

## UAT participation

According to the **Cashflow Auto Netting UAT** source, Clearing Ops is the tester group named for clearing-focused cashflow auto-netting UAT scenarios. These include:

- CITIC
- HKEX
- LCH
- TAIFEX
- SCH net-over-net
- CME
- JSCC
- ICE

The source identifies the following members of this group:

- Yew Fuong Hii
- Reena Mary Anthony
- Hamsaveni Thanabal
- Hui Chien Khoo

The UAT source does not establish a formal ownership model beyond UAT participation.

## RATAN settlement-contact routing

According to the **Settlements Ops Contacts** source, Clearing Ops is a conditional settlement-contact routing category in the RATAN directory.

The source assigns the following contacts only to specified profiles:

- `otc.clearingoperations@sc.com`
- `OTCHouseClearing_KL@exchange.standardchartered.com`

Examples of applicable profiles include Germany, selected Hong Kong, India, Singapore, Taiwan, and the United Kingdom. For China, the routing is explicitly limited to `SCB CN CHO*CHO` / FMID `400899993`.

The source does not establish Clearing Ops as a default destination for all settlement cases.
---
type: concept
title: Net-Over-Net
created: 2026-08-22
updated: 2026-08-22
tags: [netting, auto-netting, IRS, clearing, resultant-cashflow]
related: [cashflow-auto-netting, netting-resultant-cashflow, clearing-swift-suppression, taifex, citic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Net-Over-Net

Net-over-net is the application of auto-netting logic to IRS netting cashflows or other eligible cashflows that may already have a netting relationship.

## Source application

The 2025-11-18 and 2025-11-20 requirements add separate rules for TAIFEX and CITIC. Both match IRS taxonomy values or patterns and allow either `Cashflow__Payment_Type == "IRS Netting"` or an empty `Cashflow__Netting_Id`.

TAIFEX uses booking entity `10038345` and counterparty `401040938`. CITIC uses booking entity `2` and counterparty `401014221`.

The rules are classified as `Clearing_Swift_Suppress` and use NSTP for Maker+Checker. Suppression must distinguish auto-netted IRS netting cashflows from non-auto-netted IRS netting cashflows.
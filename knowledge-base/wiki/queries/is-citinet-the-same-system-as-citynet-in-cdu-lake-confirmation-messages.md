---
type: query
title: Is CitiNet the Same System as Citynet in CDU Lake Confirmation Messages?
created: 2026-08-23
updated: 2026-08-23
tags: [citinet, citynet, cdu-lake, murex-2-11, integration, open-question]
related: [cdu-lake, murex-2-11, ratan, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--53-c--1d13ogn]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Copy of Trade Confirmation & Cashflow STP - Deprecated.md"]
---
# Is CitiNet the Same System as Citynet in CDU Lake Confirmation Messages?

The deprecated requirement identifies `CitiNet` as the confirmation-status source for Murex 2.11 SWIFT trades. Its preserved JSON sample instead uses `"Confirmation_System_Name": "Citynet"` and a `Data_Publication_Id` containing `citynet`.

Determine whether these names denote one system, a renamed system, a formatting variation, or different integration components before creating a canonical entity or binding a current interface contract.
---
type: source
title: Strategic Cash Settlements Features
authors: []
year: 2025
url: ""
venue: "Internal strategic overview"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, RATAN, FMRP, Murex, migration, strategic-settlements]
related: [ratan, ratan-one, murex, fmrp, settlement-first-migration, strategic-settlements-platform, live-versus-full-cashflow-volume-reporting, dual-blind-input, murex-cashflow-migration-to-ratan, murex-to-ratan-cashflow-integration, fmmis, razor, ssdr, ebbs-settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Strategic Cash Settlements Features.md"]
---

# Strategic Cash Settlements Features

## Summary

As part of FMRP (FM Re-Platforming), RATAN is being built as a Strategic Settlements Platform intended to replace Murex 2.11 for settlement processing. The migration strategy moves settlement processing ahead of trade migration by feeding cashflows from both the Murex trade population and FMRP trades into RATAN.

This mixed-population approach is intended to centralise downstream payment processing in RATAN, remove the settlement-payment dependency on Murex, and allow each country to settle from one system regardless of whether its cashflows originate from Murex 2.11 or the strategic stack.

The source presents a capability catalogue and roadmap rather than verified production evidence. The `Live` feature column is not populated with unambiguous status values, so listed capabilities should be treated as source-reported capabilities unless independently validated.

## Strategic migration approach

The source describes [[settlement-first-migration]] as the central migration approach:

1. Cashflows from Murex trade populations are fed into RATAN.
2. Cashflows from FMRP strategic trades are also fed into RATAN.
3. Downstream payments are centralised in RATAN.
4. Settlement migration occurs for each country ahead of trade migration.
5. RATAN becomes the single settlement system for cashflows from both legacy and strategic trade stacks.

This separates trade origination from settlement and payment ownership. Murex can remain a transitional source of trades or cashflows while RATAN assumes settlement-processing responsibility.

## Reported benefits

The source reports the following expected or stated benefits:

- Fewer manual payment scenarios through Serial MT103 support, Third-Party Payments, automatic removal of special characters, and value-date selection during payment release.
- Improved STP, with the exact percentage marked as to be confirmed.
- A real-time exceptions dashboard.
- Self-service maintenance of business rules by Data Ops without dependency on a change release.
- Risk reduction through Dual Blind Input, with an associated increase in checker processing time.
- Acknowledgement and negative-acknowledgement notifications intended to reduce dependency on email from FMSRE or FMSGW.
- Swift Suppression support.
- A single queue across markets to support a follow-the-sun operating model.

These are capability or expected-benefit statements. The source does not provide validated outcome measurements for manual-payment reduction, STP improvement, or operational-efficiency gains.

## Cashflow volume reporting

The source states:

> Full Volume includes Cancelled Cashflows. Going forward, only Live Volumes will be reported from FMMIS

This changes the definition of reported volume. Historical full-volume data and future live-volume data may not be directly comparable unless cancelled cashflows are removed from historical data or the reporting series is restated. The source does not specify the effective date or reconciliation method.

## 2026 high-level plan

| Deliverable | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Indonesia - Local Instance |  |  |  |  |  |  |  |  |  |  |  |  | Commitment to OJK (Central Bank) to setup RATAN local instance by end 2026 |
| MX2.11 Non Payment module entities |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

The Indonesia local-instance item records a commitment to OJK by the end of 2026. No milestones, owner, dependencies, acceptance criteria, or delivery-confidence assessment are provided.

## Feature catalogue

| Description | Live |
|---|---|
| Countries & Products | Legacy: Equity Derivatives (BCS) — UK, SINGAPORE, HONGKONG, JERSEY. Via RAZOR: LOANIQ, FX — EGYPT, NEPAL, SAUDI. Strategic: All via Murex — CHINA, INDIA, MALAYSIA, SINGAPORE, GERMANY, UK. Strategic: Via FMRP — CHINA (IRS, CCS, NDF, SCF), UK (Prime Precious Metals). |
| Netting | Bilateral Netting; BIC Netting; CCIL Netting; NDS Auto Netting; IRS Auto Netting |
| Settlement Method | DVP (manual) |
| External Integration | SSDR; FMMIS; RATAN EOD; SCI; SSI+; RDM; CDUPS; EBBS; ASPIRE; FMSGW |
| STP / NSTP | STP based on Confirmation (TDS3) status; NSTP based on exceptions defined |
| SI Stamping / Input | Dual Blind Input; Block special characters; Auto populate SCI info; TPP Supported |
| Dashboard | Realtime Exceptions Dashboard |
| Payment Generation | Via RAZOR for BCS, LOANIQ, EG, NP, SA. Strategic: MT103, MT202, MT210, Flip MT202, MT192, MT292, MT604, MT605, MT692. Serial MT103 supported; Rounding Logic; Swift Customization (Field 20, 53). |
| Settlement Accounting Generation | Via RAZOR for BCS, LOANIQ, EG, NP, SA. Strategic Settlement Accounting Generation via EBBS / ASPIRE. Display Accounting Entries Generated. |
| Exceptions Handling | NSTP as per requirement; Trigger Reversal & Rebook exceptions for Maker & Checker |
| Business Rules | Low code Self Service Maintenance of Rules; NSTP Rules; Cashflow Suppression; Swift Suppression; Authorization Limits |
| Static | Bilateral Netting; BIC Netting; Nostro Static |
| Cashflow Events | New; Withdrawal |
| Trade Events | New Booking; Amendment; Cancellation; Early Termination (Partial / Full); Portfolio Re-Assignment; Novation |
| Profiles | Source includes an image profile reference: `attachments/image-2025-3-10_8-16-42.png` |
| Cashflow Status | Multiple as per requirement; Sub Status; FM Swift Gateway / AMH / SCPAY Status |
| Settlement Affirmation | Single / Bulk Cashflow Affirmation; Netting Affirmation |
| Auto Refresh | Cashflow Blotter Refresh; Vostro SI Refresh on Cashflows; Nostro Refresh |
| Data Extraction & MIS | Cashflow data available in SSDR (real time query); Volume & Touchpoint data available in FMMIS (VD+2 basis) |

## Backlog references

- [RATAN Settlements FMRP Backlog - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/RATAN+Settlements+FMRP+Backlog)
- [RATAN Settlements Day 2 Backlog - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/RATAN+Settlements+Day+2+Backlog)

## Evidence limitations and open points

- The source does not identify which catalogue entries are live in production.
- Country and product descriptions do not clearly distinguish trade origination, cashflow generation, settlement routing, and payment ownership.
- The source does not quantify the claimed STP improvement.
- Manual DVP is listed without scope or rationale.
- The source does not define the boundaries between RATAN, RAZOR, EBBS, ASPIRE, FMMIS, and other integrations.
- The 2025 plan is represented by an unavailable image, and the 2026 schedule contains almost no milestone detail.
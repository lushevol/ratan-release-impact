---
type: entity
title: SCFB_SEOUL
created: 2026-08-23
updated: 2026-08-24
tags: [korea, booking-entity, cash-settlement, fmid-10036645, fmid, static-data]
related: [korea-migration, korea-cash-settlement-migration, ratan, tis, oltp, ratan-tis-payment-query-integration, korea-cashflow-migration, currency-dependent-bridge-account-selection, oltp-accounting, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - OLTP.md"]
---
# SCFB_SEOUL

SCFB_SEOUL is the active Korea Seoul booking entity in the RATAN-to-TIS integration scope and is configured for the OLTP Accounting migration.

## Identifiers

- FMID: `10036645`
- Country code: `KR`
- Configured branch code: `70`

The payment and receipt query filters restrict returned cashflows to `Entity.Booking_Entity_SCI_FMID='10036645'`.

## Bridge accounts

SCFB_SEOUL has distinct bridge accounts by currency:

| Currency | Bridge account |
|---|---|
| `KRW` | `000287` |
| `FCY` | `040446` |

These accounts require currency-aware account resolution rather than an entity-only bridge-account lookup.

## Scope

The Functional Requirement source explicitly identifies `SCFB_SEOUL` as active while striking through `SCSK_SEOUL` and `SEOUL`; those names are not in the documented active scope.
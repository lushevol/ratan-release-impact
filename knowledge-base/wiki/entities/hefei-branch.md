---
type: entity
title: Hefei Branch
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, branch, china, cash-settlement, onboarding]
related: [2025-hefei-branch-onboarding, hefei-strategic-settlement-routing, fmrp, murex-2-11, ebbs, cashflow-blotter, what-is-the-authoritative-hefei-entity-name]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
---
# Hefei Branch

The Hefei branch is the China branch/entity being onboarded in the 2025 cash-settlement checklist.

## Identifiers

- Murex 2.11 entity name: `HEFEI`
- Murex label: `HEIFEI`
- FMID: `401053411`
- Branch code: `73`
- Legal entity: `SCB CHINA*HFI`
- Country: `CN`
- GUI country code: `CHINA`

## SWIFT mappings specified

- Sender BIC: `SCBLCNSXHFI`
- CNY Field 53 BIC (Rule1): `SCBLCNSXGMO`
- CNY Field 58 BIC (Rule2): `SCBLCNSXGMO`

Receiver BIC values for MT604/605, Field 20 configuration, and complete branch-specific SWIFT mappings are not supplied by the checklist.

## Settlement-accounting mapping

The required [[ebbs]] configuration specifies posting branch `10000`, transaction type `RTN`, debit transaction code `100`, credit transaction code `200`, and bridge account `560100000001910205`.

## Naming caution

The source uses the variants `Hefie`, `Heifei`, and `HEFEI`, while `SCB CHINA*HFI` is the legal-entity identifier. These values may represent distinct system fields, but the preferred human-readable branch name requires confirmation in [[what-is-the-authoritative-hefei-entity-name]].
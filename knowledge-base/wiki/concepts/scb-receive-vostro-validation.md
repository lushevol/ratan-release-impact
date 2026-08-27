---
type: concept
title: SCB Receive Vostro Validation
tags: [cash-settlement, scb, ssi-stamping, vostro, nostro, validation]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1ki16y7, precious-metal-cashflow-vostro-requirement, concepts/nostro-stamping, what-is-the-authoritative-scb-receive-vostro-validation-rule]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping.md"]
---
# SCB Receive Vostro Validation

## Definition

SCB receive vostro validation is the conditional SSI-stamping and manual-update policy that determines when `vostro` settlement data is mandatory and how it must correspond to `nostro` data.

The policy is limited to SCB cashflows. It supplements the broader [[concepts/nostro-stamping]] process and should not be applied to other entities without separate requirements evidence.

## Validation matrix

| Cashflow condition | Vostro requirement | Settlement-data rule |
|---|---|---|
| SCB pay | Mandatory | Required vostro and nostro fields must be present; settlement means and settlement account must match |
| SCB receive with `XAU`, `XAG`, `XPD`, or `XPT` | Mandatory | Required vostro and nostro fields must be present; settlement means and settlement account must match |
| SCB receive with settlement means `"Over-Account"` | Mandatory | Required vostro and nostro fields must be present; settlement means and settlement account must match |
| Other SCB receive cashflows | Existing mandatory validation bypassed | If `vostro SSI Type` is null, copy settlement means and settlement account from nostro |

## Manual-update behavior

The mandatory cases apply when a user adds adhoc SSI through the Cashflow Details UI and submits the change. The source does not specify the complete set of mandatory fields beyond the settlement means and settlement account consistency requirements.

For exempt SCB receive cashflows, a null `vostro SSI Type` triggers conditional auto-population from the corresponding nostro values. The source does not clarify whether the populated values are persisted, used only for stamping, or subsequently revalidated.

## Precedence

The requirement lists precious-metal currency and `"Over-Account"` as separate mandatory conditions. Therefore, an SCB receive cashflow meeting either condition must be treated as subject to mandatory validation. The source does not explicitly define precedence if both conditions apply, but the outcome is the same under the stated rules.

The phrase “other SCB receive cashflow” should consequently exclude both mandatory categories.

## Scope limitation

The requirement does not identify whether “SCB” means SCB London, SCB Korea, or another SCB legal entity or branch. Claims about [[entities/scb-london]] or [[entities/scb-korea]] require confirmation before being added to those entity pages.
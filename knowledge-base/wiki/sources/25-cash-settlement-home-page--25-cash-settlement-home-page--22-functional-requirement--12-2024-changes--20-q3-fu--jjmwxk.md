---
type: source
title: Swap Agent Payment
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, swap-agent, murex-2-11, ratan, functional-requirement, q3-2024]
related: [swap-agent-clear-service, swap-agent-strategy, swap-agent-payment-hybrid-settlement, murex-three-trade-swap-agent-booking-model, swap-agent-cashflow-swift-suppression, how-are-swap-agent-settle-and-non-settle-flags-defined-and-prioritized, how-does-ratan-prevent-netting-and-swift-generation-for-swap-agent-non-settle-cashflows, does-suppressxxx-apply-to-all-of-trade-2-or-only-swap-agent-non-settle-cashflows, how-does-trade-3-offset-trade-1-dummy-principal-payments]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Swap Agent Payment.md"]
---
# Swap Agent Payment

## Status and scope

This Q3 2024 document records a functional requirement and proposed solution for onboarding Swap Agent Payment processing in [[murex-211]] and [[ratan]]. It is not evidence of design approval, implementation, deployment, testing, or production validation.

The intended model is hybrid:

- Only Trade 2 initial and final principal payments settle bilaterally with the client.
- Interim coupons, interim principal payments, and dummy principal payments bypass settlement while still generating accounting.
- All scoped payments generate accounting on the Main Nostro account.
- No netting is required.

Payments not settled bilaterally are expected to be cleared through the [[swap-agent-clear-service]].

## Booking constraint and three-trade package

The document states that [[murex-211]] cannot book one trade that produces both the required bilateral principal flows and interim Swap Agent-cleared flows. The proposed workaround is a three-trade package sharing the `SWAP_AGENT` strategy and illustrative LTI ID `123456`.

### Trade 1

Trade 1 primarily generates interim coupons, with dummy principal flows generated because of the stated Murex limitation. Every listed flow is accounting-only.

| Flow Type | Value Date | Amount | LTI ID | Strategy | Typology | Settlement Requirement |
| --- | --- | --- | --- | --- | --- | --- |
| Initial Principal (**dummy**) | T+2(Start date +2) | 100mio | 123456 | SWAP_AGENT | Vanilla X-ccy swap | No Settlement, Accounting only |
| Interim Coupon 1 | 3M+2 | 2mio | 123456 | SWAP_AGENT | Vanilla X-ccy swap | No Settlement, Accounting only |
| Interim Coupon 1 | 6M+2 | 2mio | 123456 | SWAP_AGENT | Vanilla X-ccy swap | No Settlement, Accounting only |
| Interim Coupon 1 | 9M+2 | 2mio | 123456 | SWAP_AGENT | Vanilla X-ccy swap | No Settlement, Accounting only |
| Final Principal ( **dummy**) | 12M+2(Maturity +2) | (-1) 100mio | 123456 | SWAP_AGENT | Vanilla X-ccy swap | No Settlement, Accounting only |

### Trade 2

Trade 2 generates the required initial and final principal payments for bilateral settlement. Its interim principal payments remain accounting-only.

| Flow Type | Value Date | Amount | LTI ID | Strategy | Typology | Settlement Requirement |
| --- | --- | --- | --- | --- | --- | --- |
| Initial Principal (Bilateral Settlement) | T(Start date) | 100mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | Bilateral Settlement |
| Interim Principal 1 | 3M | 10 mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | No Settlement, Accounting only |
| Interim Principal 1 | 6M | 10 mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | No Settlement, Accounting only |
| Final Principal (Bilateral Settlement) | 12M(Maturity) | (-1) 100mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | Bilateral Settlement |

### Trade 3

Trade 3 is described as resolving Trade 1 dummy payments by booking “opiate payments” to knock off those flows. The source wording is retained. The displayed amounts and signs do not, on their own, demonstrate the claimed offset.

| Flow Type | Value Date | Amount | LTI ID | Strategy | Typology | Settlement Requirement |
| --- | --- | --- | --- | --- | --- | --- |
| Initial Principal (**Dummy**) | T+2(Start Date+2) | 100mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | No Settlement, Accounting only |
| Final Principal (**Dummy**) | 12M+2(Maturity+2) | (-1) 100mio | 123456 | SWAP_AGENT | RFR CCS MTM Fixing | No Settlement, Accounting only |

## Proposed control model

[[murex-211]] proposes sending all flows to [[ratan]]. RATAN would consume upstream “Swap Agent settle” and “Swap Agent non settle” classifications, suppress SWIFT settlement output for non-settle cashflows, and preserve accounting generation.

The proposal also states that Murex cannot assign different Vostro configurations for payments sharing the same entity, counterparty, and currency. It proposes assigning `SUPPRESSXXX` on Trade 1 and Trade 2, while assigning a normal Vostro on Trade 2. The scope and precedence of these controls are not defined.

## Unresolved matters

- Exact Murex field names, values, lifecycle timing, and interface contract for settlement classifications are absent.
- `SUPPRESSXXX` scope is ambiguous and could inadvertently suppress Trade 2 bilateral principal payments.
- No control mechanism establishes how `SWAP_AGENT` cashflows are excluded from normal RATAN netting.
- The Main Nostro account has no account identifier or entity-, currency-, or ledger-level mapping.
- The source does not specify accounting events, posting outcomes, exception handling, replay controls, idempotency, or reconciliation for intentionally suppressed cashflows.
- Trade 3 offset mechanics require currency, direction, leg, payer/receiver, and accounting-sign details.

See [[swap-agent-payment-hybrid-settlement]] for the intended processing model and [[swap-agent-cashflow-swift-suppression]] for the proposed RATAN control requirement.
---
type: source
title: Manual Rounding
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11137292"
venue: "Azure DevOps"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, manual-rounding, functional-requirement, settlement-day2]
related: [manual-cashflow-rounding, usd-equivalent-cashflow-adjustment-limit, cashflow-amendment-maker-checker-control, azure-devops, story-11137292-manual-rounding, settlement-accounting, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# Manual Rounding

## Source context

This requirement proposes a controlled Manual Rounding capability for payment cashflows. It is tracked in Azure DevOps Story 11137292 — Manual Rounding.

## Requirement details

- User must be able to add/decrease few cents to the cashflow amount for payment.
- Control must be there to ensure the increase/decrease is less than USD 1, use the exchange rate from upstream (refer to existing authorization limit process).
- Settlement Accounting will ~~follow original cashflow amount~~ - follow the existing process: swift /accounting use the same updated amount.
- [must align with Recon team] TLM? to check the possible break between trade/cashflow.
- Cashflow state for the action? WAITING.
- UI popup: design to be added, only the amount and ccy usd amount in the popup.
- maker/checker required.

## Intended control model

The user-entered increase or decrease is expected to be validated against a USD-equivalent threshold using an exchange rate from an unspecified upstream source. The requirement refers to the existing authorization-limit process but does not identify its implementation or detailed rate contract.

Maker/checker approval is explicitly required. The source does not define the roles, approval sequence, rejection behavior, audit fields, or whether the limit is revalidated at checker approval.

## Downstream amount propagation

The final wording indicates that SWIFT and Settlement Accounting should use the same updated amount rather than retaining the original cashflow amount. This should be validated against the relevant downstream interfaces and accounting process. The requirement does not establish whether EBBS or other settlement platforms are involved.

## Reconciliation dependency

The requirement calls for alignment with the Recon team and asks whether TLM should be used to check for possible breaks between the originating trade and the amended cashflow. TLM involvement and the resulting reconciliation behavior remain unresolved.

## Lifecycle and user-interface questions

`WAITING` is proposed or queried as the cashflow state in which the action may be available, but the source does not confirm whether it is the only eligible state.

The popup is intended to show the amount and currency/USD amount. The referenced design attachment was not included in the supplied source text, so it is not possible to determine whether the popup should show the original amount, adjustment delta, revised amount, FX rate, or approval status.

## Open implementation questions

- Is the USD threshold strictly less than USD 1.00 or inclusive of USD 1.00?
- Is the threshold applied to the absolute adjustment, the cumulative adjustment, or another amount?
- Which upstream system and FX-rate type are authoritative?
- Does “few cents” impose a separate native-currency limit?
- Is `WAITING` the sole eligible cashflow state?
- What exact values must be displayed and audited?
- How will trade/cashflow reconciliation differences be represented and resolved?

## Related knowledge

The requirement extends existing settlement knowledge concerning [[entities/swift]] and [[concepts/outbound-property-propagation-to-swift-mt-mx]]. Its accounting implications should be checked against [[concepts/ebbs-accounting-configuration]] and [[concepts/ebbs-settlement-posting-configuration]] only after the actual Settlement Accounting implementation is identified.

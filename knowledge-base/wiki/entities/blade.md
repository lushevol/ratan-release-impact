---
type: entity
title: Blade
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Source Stack Flow Name in LMS Feed.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
tags: ["upstream-system", "trade-booking", "cash-settlement", "blade", "booking", "strategy", "global-rates", "fmrp", "trading-system", "booking-system", "structured-products", "SCBML", "RFQID", "cashflow", "Stella", "RATAN", "trade-query", "desktop-application"]
related: ["fmrp-china-cash-settlement", "stella", "ratan", "fmo-post-trade-portal", "fmrp", "settlement-method-stamping", "global-rates-settlement-strategy", "cdu", "structured-product-package-trade-model", "package-identifier-lineage", "trade-event-id-lineage", "source-stack-flow-name-propagation", "netting-resultant-stack-derivation", "openfin", "trade-to-cashflow-navigation"]
updated: 2026-08-23
---

# Blade

## Role in the documented workflow

Blade is the originating application in the documented trade-to-cashflow workflow. In the Q2 2023 cash-settlement scenarios, Blade is described as the system in which a user books trades before downstream cashflow processing. The scenarios repeatedly begin with a user booking a trade in Blade.

The Q2 2023 delivery-plan source documents Blade's role as upstream trade booking in the test setup. It does not describe Blade's interfaces, validation rules, ownership, or the exact mapping between a booked trade and the cashflows later displayed in [[fmo-post-trade-portal]].

## Trade search and navigation to Ratan

The FXU technical-design source describes the following user-facing workflow:

1. A user opens Blade through [[openfin]].
2. The user enters the **Trade Query** workspace.
3. The user searches for a trade using its **Trade ID**.
4. From a trade result, the user selects the context-menu action:

   ```text
   Show Cashflow in Ratan
   ```

5. The action opens [[ratan]] for the selected trade's cashflows.

That source documents Blade's user-facing search and navigation behavior. It does not specify the integration protocol, deep-link format, message payload, or authorization behavior behind the Ratan launch.

## Role in LMS feed source-stack flow

The *Source Stack Flow Name in LMS Feed* requirement identifies Blade as the original trade source system for `FMRPSTELLA` cashflows routed through [[stella]].

Under the confirmed Proposal 1 in that requirement:

- The stack-flow value is `FMRPSTELLA`.
- The settlement process is FMRP.
- Swift/accounting is handled by [[ratan]].
- The LMS source value is `FMRPSTELLA`.
- The Tag20 prefix is `DV`.
- A same-stack netting resultant is expected to retain `FMRPSTELLA`.

The mixed-stack netting fallback is not fully specified; see [[netting-resultant-stack-derivation]].

This LMS-feed requirement describes source-stack-flow treatment for Blade-originated cashflows. It does not establish Blade's trade-booking interfaces, structured-product behavior, or the detailed responsibility split between Blade and [[stella]].

## Role in Global Rates migration

The Global Rates settlement-strategy requirement identifies Blade as a booking and strategy application involved in the migration to [[ratan]]. That requirement expects Blade, together with [[stella]], to:

- Stamp settlement methods on trades and cashflows.
- Participate in product, trade, identifier, currency, and settlement-strategy design.

The Global Rates settlement-strategy requirement does not define Blade-specific interfaces or distinguish which responsibilities belong to Blade versus [[stella]]. That division of responsibility requires confirmation before the migration design is finalized.

## Structured-product behavior

The deprecated [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--18-st--tn9c1x|Structure Products]] requirement describes Blade as a trading or booking system.

According to that source, Blade books the trades in a structured-product package as one contract while generating an individual trade `SCBML` document for every trade in the package. This creates a distinction between:

- The package-level economic or booking representation.
- The individual trade-level message representation.

Blade populates the structure-booking link ID, identified in the source as `RFQID`, in each individual trade `SCBML`. The identifier is intended to preserve the relationship between the package and its component trades.

## Evidence boundaries and limitations

The structured-product behavior comes from a deprecated source. That source directly states Blade's package booking, trade-level `SCBML` generation, and `RFQID` propagation, but it does not establish the current production contract, identifier authority, amendment behavior, or version-transition rules.

The deprecated source example also contains inconsistent table alignment. Its values should not be interpreted as a complete Blade interface schema without validating the original document or a newer requirement.

The Q2 2023 delivery-plan source does not establish the structured-product behavior described above; it documents Blade only as the upstream booking system in the cash-settlement scenarios. Conversely, the deprecated structured-product source does not establish Blade's cash-settlement flow, Global Rates migration responsibilities, LMS source-stack-flow treatment, or the division of responsibilities between Blade and [[stella]].

The FXU technical-design source establishes the documented user-facing Trade Query and Ratan-navigation workflow, but does not establish the underlying integration protocol, deep-link format, message payload, or authorization behavior.
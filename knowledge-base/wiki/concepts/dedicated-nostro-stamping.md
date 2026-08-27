---
type: concept
title: Dedicated Nostro Stamping
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, ssi, stamping, rfi, settlement, static-data]
related: [portfolio-currency-nostro-selection, dedicated-nostro-static-data-model, ssi-stamping-behavior-differences, ratan-cash-settlement-ssi-stamping-service, nostro-stamping, nostro-centralization, nostro-record-composite-uniqueness, dedicated-nostro-match-conditions, ratanone-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Cashflow Dedicated Nostro Stamping Design(like RFI STRATEGY etc.).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# Dedicated Nostro Stamping

Dedicated Nostro stamping selects a specific Nostro configuration for qualifying cashflows rather than using the standard lookup factors:

```text
entity + ccy + settlementMeans + settlementAccount
```

It is described as a proposed extension to [[nostro-stamping]] in which a cashflow or trade can select a specialised Nostro configuration using requirement-specific conditions before ordinary Nostro lookup.

## RFI Qualification

The current-source requirement states that, for RFI, qualification selects a dedicated portfolio-and-currency path:

```text
portfolio + ccy
```

The intended paths are exclusive: eligible RFI cashflows use dedicated configuration, while all other cashflows use normal selection. Under this requirement, missing dedicated configuration should fail rather than fall back.

The deprecated design also identifies the RFI dedicated condition as `portfolio + ccy`, but proposes a different behavior when a dedicated Nostro is absent: fall back to the default lookup. This fallback proposal is historical and is not confirmed current behavior.

## Proposed Selection Behavior in the Deprecated Design

The deprecated source proposes the following sequence:

1. Evaluate whether a dedicated condition applies.
2. Retrieve the dedicated Nostro when the condition matches.
3. Fall back to default lookup when no dedicated Nostro is found.

Priority between multiple dedicated types, including RFI and STRATEGY, remains unresolved in that deprecated design.

## Stamping Scope and Context

This requirement affects Nostro stamping only; Vostro stamping remains separate.

The current source lists workflow, ad hoc, trade, accounting, and split stamping as potential entry points, but does not confirm support for all of them.

The deprecated design distinguishes cashflow and trade stamping:

- A cashflow normally requires one stamp action.
- A trade may require up to four actions, with separate currency-related contexts.

For the deprecated design, the proposed dedicated-condition context is:

```text
messageType (cashflow | trade)
+ nostroType (RFI | STRATEGY)
+ currencyTag (UUID)
```

That source notes that a generic condition without this context may be insufficient for trade stamping.

## Observable Outcome

The deprecated design intends `Dedicated_Nostro_Id` to expose the dedicated-match result through the cashflow query service. Its null behavior and availability for both cashflow and trade stamping require confirmation.

## Static-Data and Refresh Concerns

Dedicated configuration may alter the effective uniqueness dimensions of [[nostro-records]], potentially adding dedicated-type, portfolio, or condition-data dimensions beyond the normal composite key.

The deprecated design also identifies unresolved refresh-scope implications discussed in [[nostro-notification-and-refresh]].
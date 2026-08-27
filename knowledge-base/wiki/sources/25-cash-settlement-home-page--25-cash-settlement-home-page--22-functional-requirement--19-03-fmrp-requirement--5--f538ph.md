---
type: source
title: "Global Rates — Settlement Strategy Process and Dependency"
authors: []
year: 2024
url: ""
venue: "Functional Requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [global-rates, settlement, strategy, fmrp, rat an, functional-requirement]
related: [ratan, stella, fmrp, settlement-method-stamping, global-rates-settlement-strategy, strategy-golden-source, dvp-receipt-before-payment-release]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Global Rates — Settlement Strategy Process and Dependency

## Summary

This functional-requirement document describes the strategy and surrounding-system dependencies for migrating Global Rates trades to the strategic settlement platform [[entities/ratan]]. The scope covers G10 and emerging-market desks, with the main entities identified as DE, HK, IN, SG, and TW.

The document treats the migration as a cross-system design problem rather than a settlement-platform-only change. Upstream booking and strategy capabilities in Blade and [[entities/stella]] must provide settlement methods, product classifications, identifiers, currencies, and trade attributes. RATAN must then coordinate settlement processing with Credence, TLM, HORIZON, SSI+, Cortex, and other systems.

The strongest target operating model concerns DVP. Stella is expected to identify DVP trades, RATAN is expected to hold the relevant cashflow as NSTP, TLM is expected to provide the Nostro statement subscription, and RATAN is expected to release the SCB payment after receipt settlement is confirmed.

Several requirements remain unresolved. These include settlement-method amendment, CLS eligibility configuration, rounding ownership, the authority of PCT2 for FMID mappings, lien amount handling, FX utilization, CPN, rollover handling, and detailed interface contracts.

## Scope and migration context

Global Rates refers to the planned migration of trades from G10 and EM desks, primarily involving DE, HK, IN, SG, and TW. The migration requires coordination across:

- Pre-trade and booking applications
- Strategy and product classification
- Settlement-method stamping and amendment
- Cashflow and trade identifiers
- Currency and ISO-code mappings
- Clearing and settlement events
- Nostro static data
- Account-statement subscriptions
- Downstream settlement and suppression integrations

The document is a dependency inventory and planning artifact. It does not provide completed ADO tickets, plan dates, interface schemas, or final ownership decisions.

## Strategy functions and dependencies

| Feature | Requirement | Dependency | ADO ticket | Plan Date |
| --- | --- | --- | --- | --- |
| Settlement Method | 1. Blade/Stella stamp the settlement method on trade & cashflow 2. Subsequent amendment on settlement method is valid requirement, but solution is TBC( **how & where ops users perform the settlement method change**) 3. Settlement activities like Cashflow Suppression, do we need to sync back to HORIZON | 1. Blade/Stella design to drive the settlement method generation 2. Integration between RATAN & Credence | | |
| Settlement method CLS | 1. What's the strategy design of CLS trade confirmation & clearing and how's this impact the settlement? 2. To stamp the settlement method as 'CLS Netting' on the trade & cashflow from Blade/Stella? 3. How & where the CLS eligibility rule config? 1. Entity 2. Counterparty 3. Product 4. Value date 5. Currency | | | |
| Settlement method NET | 1. How Blade/Stella stamp the settlement method NET, will Blade/Stella source the netting agreement from strategy golden source which define netting rule with the key attributes like product/currency/client id | **Sebastien Heuguet**: If any API is exposed, defaulting can be introduced as part of the booking UI. | | |
| Settlement method DVP | 1. Stella populate the settlement method as 'DVP' when book trade, How Blade/Stella support flag the client type as DVP( Non FI clients) or by specific clients 2. RATAN to hold the 'DVP' cashflow as NSTP 3. RATAN to subscribe the Nostro account statement from Nostro agent of the SCB receipt cashflow 4. Once the receipt cashflow had been settled, RATAN auto release the SCB pay cashflow | 1. DVP settlement method by Blade/Stella 2. Nostro account statement subscription from downstream(TLM) **Sebastien Heuguet**: If an API is exposed, defaulting could be introduced as part of the booking UI. ![image2024-12-6_19-55-58.png](attachments/image2024-12-6_19-55-58.png) | | |
| Settlement method PVP | 1. How Blade/Stella stamp the settlement method 'PVP' | **Sebastien Heuguet**: If an API is exposed, defaulting can be introduced as part of the booking UI. ![image2024-12-6_19-55-48.png](attachments/image2024-12-6_19-55-48.png) | | |
| Strategy Rounding | 1. There should be generic universal rounding logic in Stella 2. The rounding logic should be common between trade & cashflow & Fixing(confirmation, fixing notice, settlement) | 1. Golden source of rounding rule 2. Stella building on rounding process on trade & cashflow **Peter Arnold: **This has been discussed at TA before, if you want rounding for settlements, this needs to be done by settlements. | | |
| Booking Entity/Counterparty unique identifier | 1. How Blade/Stella define the strategy identifier of booking entity & counterparty( for single FMID there're multi labels defined in Murex 2.11) 2. This identifier should be used by all the business process including trade booking/Settlement process/Vostro static data/Nostro static data/any other static data | 1. Golden source of strategy identifier 2. New building for different applications to apply the strategy identifier **Peter Arnold:** FMID mappings are setup in PCT2. | | |
| Booking Currency & ISO currency | 1. How Blade/Stella maintain the supported booking currency list 2. There should be golden source of the Booking currency to ISO currency mapping, which settlement process would refer to this mapping for the accounting/swift generation | 1. Golden source of booking currency & design agreement with TP system 2. Golden source of booking currency to currency ISO code mapping & design agreement with relevant systems | | |
| Strategy product catalog | 1. How Blade/Stella define the strategy product catalog & align the business rules with settlement ops. (Right now there're quite lot of settlement business rule defined with Murex 2.11 Strategy/Typology/Family/Group/Type, need to understand how these would be designed in FMRP stack) | 1. Stella strategy product catalog design **Peter Arnold:** Stella (already rolled out for China) has adopted the PRDS (bank standard) product definition. This is currently a tactical implementation with Stella performing the enrichment and this will be migrated to STAMP. For RATAN/downstream there is no impact, the product mapping is already standardized and shared with settlement teams. | | |
| Clearing Status Handling | 1. How Blade/Stella the strategy clearing process ? 2. How the clearing status maintained on trade & cashflow level? | **Peter Arnold: **Clearing is a trade event currently handled as "Remaining Party Full" with reason "Clearing". This is handled at Trade level not RPF event and RATAN has already this in production for China. | | |
| Lien Amount Handling | 1. How Blade/Stella the strategy Lien amount handling process? 2. How is the Lien amount captured in trade & cashflow? | **Sebastien Heuguet** No FMRP design/solution work started at that time | | |
| ND Rates Product Booking Model | 1. How Blade/Stella design the ND product booking model. How the ND currency cashflow be converted to deliverable currency cashflow, within same trade or book separate convert trade? 1. ND CCS 2. ND convert | **Peter Arnold: **Delivery events from Cortex will be sent in delivery currency and subsequent cashflows will be created. | | |
| RFR package trade booking model | 1. How Blade/Stella design the RFR booking model 2. TBC if applicable for DE, HK, IN, SG, TW | **Peter Arnold: **Not in scope for first roll-outs, however package models have already been defined and shared with RATAN. (Package Id) | | |
| CPN | 1. Define the strategy CPN approach for the cashflow sourcing from different TP system | **Peter Arnold: **What is CPN? All cashflow handling will be standerdized. Either they come as delivery events from Cortex or as Fees/payments on the TP messages. | | |
| FX Utilization | 1. How Blade/Stella design the strategy FX trade utilization process | **Sebastien Heuguet** Not sure what that is. So I guess it does not exist in the FMRP stack. | | |
| Nostro Golden source | 1. How SSI+ design the Nostro static data maintenance as strategy golden source | **Peter Arnold:** Not a question for Blade/Stella | | |
| Rollover handling | 1. How's the Blade/Stella design on trade rollover & how's the impact on cashflow | **Sebastien Heuguet** No specific rollover design for now in the FMRP stack. | | |

## Key findings

### Upstream settlement-method stamping

The intended direction is for Blade and Stella to stamp the settlement method on both the trade and its cashflows. The listed methods are CLS Netting, NET, DVP, and PVP. The document does not establish RATAN as the owner of settlement-method generation.

Operational amendment is explicitly a valid requirement, but the mechanism and user interface for changing a settlement method remain to be defined. Integration between RATAN and Credence is also identified as a dependency.

### DVP conditional release

The DVP flow is described as follows:

1. Stella identifies the trade as DVP during booking.
2. RATAN holds the DVP cashflow as NSTP.
3. RATAN receives or subscribes to Nostro account statements through TLM.
4. RATAN confirms settlement of the SCB receipt cashflow.
5. RATAN automatically releases the corresponding SCB payment cashflow.

The source does not define the message format, matching key, timeout, exception path, reversal handling, or operational override for this flow.

### Ownership clarifications

The source comments distinguish several responsibilities:

- Settlement rounding may belong to Settlements rather than Stella.
- FMID mappings currently exist in PCT2.
- Stella uses PRDS for China product definition and enrichment, with a planned migration to STAMP.
- Clearing is represented in RATAN as a trade event with `"Remaining Party Full"` and reason `"Clearing"`; this is already in production for China.
- SSI+ is the relevant Nostro static-data ownership area.
- Cortex delivery events are expected to be sent in delivery currency.
- RFR package trade models are excluded from first roll-outs.

### Unresolved scope

The following items require further clarification before the inventory can become a complete functional baseline:

- CLS eligibility-rule configuration
- Settlement-method amendment and governance
- Rounding ownership and golden source
- Authority of PCT2 for FMID mappings
- Lien amount capture and processing
- FX utilization support
- Definition of CPN
- Rollover design and cashflow impact
- Detailed booking, event, and downstream interface contracts

## Evidence and limitations

This document contains requirements, dependencies, and stakeholder comments rather than approved architecture decisions. No ADO ticket or plan date is populated in the matrix. The referenced DVP and PVP images were not available in the supplied source text. Stakeholder comments should therefore be treated as design input, not as final ownership decisions.

## Related wiki topics

- [[entities/ratan]]
- [[entities/stella]]
- [[entities/fmrp]]
- [[entities/ssi-plus]]
- [[entities/tlm]]
- [[concepts/settlement-method-stamping]]
- [[concepts/dvp-receipt-before-payment-release]]
- [[concepts/strategy-golden-source]]
- [[concepts/strategy-rounding-ownership]]
- [[concepts/nd-delivery-currency-cashflow-model]]
- [[projects/cashflow-migration]]